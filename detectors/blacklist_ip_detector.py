import sqlite3
import pandas as pd

from services.alert_manager import create_alert

def run():
    print("Blacklisted IP Detector Started")

    # Load blacklist
    with open("blacklist.txt", "r") as file:
        blacklist = [
            line.strip()
            for line in file
            if line.strip()
        ]

    conn = sqlite3.connect("traffic.db")

    df = pd.read_sql_query(
        "SELECT * FROM traffic_logs",
        conn
    )

    conn.close()

    for ip in blacklist:

        matches = df[
            (df["source_ip"] == ip)
            |
            (df["destination_ip"] == ip)
        ]

        if len(matches) > 0:

            print(
                f"[HIGH] Blacklisted IP Detected: "
                f"{ip}"
            )

            create_alert(
                ip,
                "BLACKLISTED_IP",
                "HIGH",
                f"Traffic observed involving blacklisted IP {ip}"
            )

    print("\nBlacklisted IP Detection Completed")
if __name__ == "__main__":
    run()
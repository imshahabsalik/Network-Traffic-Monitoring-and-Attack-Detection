import sqlite3
import pandas as pd

from services.alert_manager import create_alert

def run():
    print("ICMP Flood Detector Started")

    THRESHOLD = 10

    conn = sqlite3.connect("traffic.db")

    df = pd.read_sql_query(
        """
        SELECT *
        FROM traffic_logs
        WHERE protocol IN ('ICMP', '1')
        """,
        conn
    )

    conn.close()

    if len(df) == 0:
        print("No ICMP traffic found.")
        exit()

    icmp_counts = (
        df.groupby("source_ip")
        .size()
        .reset_index(name="icmp_count")
    )

    for _, row in icmp_counts.iterrows():

        ip = row["source_ip"]
        count = row["icmp_count"]

        print(f"{ip} -> {count} ICMP packets")

        if count > THRESHOLD:

            print(
                f"[HIGH] ICMP Flood Detected: "
                f"{ip} ({count} packets)"
            )

            create_alert(
                ip,
                "ICMP_FLOOD",
                "HIGH",
                f"Generated {count} ICMP packets"
            )

    print("\nICMP Flood Detection Completed")
if __name__ == "__main__":
    run()
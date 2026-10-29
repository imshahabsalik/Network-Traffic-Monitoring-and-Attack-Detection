import sqlite3
import pandas as pd
from services.alert_manager import create_alert


def run():

    print("DoS Detector Started")

    THRESHOLD = 50

    conn = sqlite3.connect("traffic.db")

    df = pd.read_sql_query("""
    SELECT *
    FROM traffic_logs
    """, conn)

    conn.close()

    packet_counts = (
        df.groupby("source_ip")
          .size()
          .reset_index(name="packet_count")
    )

    for _, row in packet_counts.iterrows():

        ip = row["source_ip"]
        count = row["packet_count"]

        print(f"{ip} -> {count} packets")

        if count > THRESHOLD:

            print(
                f"[CRITICAL] DoS Activity Detected: "
                f"{ip} ({count} packets)"
            )

            create_alert(
                ip,
                "DOS_ATTACK",
                "CRITICAL",
                f"Generated {count} packets"
            )

    print("\nDoS Detection Completed")


if __name__ == "__main__":
    run()
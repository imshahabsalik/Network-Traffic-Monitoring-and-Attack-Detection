import sqlite3
import pandas as pd

from services.alert_manager import create_alert

def run():
    print("Traffic Spike Detector Started")

    THRESHOLD = 30

    conn = sqlite3.connect("traffic.db")

    df = pd.read_sql_query(
        """
        SELECT *
        FROM traffic_logs
        """,
        conn
    )

    conn.close()

    if len(df) == 0:
        print("No traffic data found.")
        exit()

    packet_counts = (
        df.groupby("source_ip")
        .size()
        .reset_index(name="packet_count")
    )

    average_packets = packet_counts["packet_count"].mean()

    print(f"Average packets per IP: {average_packets:.2f}\n")

    for _, row in packet_counts.iterrows():

        ip = row["source_ip"]
        count = row["packet_count"]

        print(f"{ip} -> {count} packets")

        if count > average_packets + THRESHOLD:

            print(
                f"[MEDIUM] Traffic Spike Detected: "
                f"{ip} ({count} packets)"
            )

            create_alert(
                ip,
                "TRAFFIC_SPIKE",
                "MEDIUM",
                f"Generated {count} packets (above normal baseline)"
            )

    print("\nTraffic Spike Detection Completed")
if __name__ == "__main__":
    run()
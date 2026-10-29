import sqlite3
import pandas as pd
from services.alert_manager import create_alert

def run():
    print("Port Scan Detector Started")

    THRESHOLD = 20

    conn = sqlite3.connect("traffic.db")

    df = pd.read_sql_query("""
    SELECT *
    FROM traffic_logs
    WHERE protocol = 'TCP'
    """, conn)

    print(f"Rows Loaded: {len(df)}")
    print()

    for ip in df["source_ip"].unique():

        ip_data = df[df["source_ip"] == ip]

        unique_ports = ip_data["destination_port"].nunique()

        print(f"{ip} -> {unique_ports} unique ports")

        if unique_ports > THRESHOLD:

            print(
                f"[ALERT] Port Scan Detected: "
                f"{ip} ({unique_ports} ports)"
            )

            create_alert(
                ip,
                "PORT_SCAN",
                "HIGH",
                f"Contacted {unique_ports} unique ports"
            )

    conn.close()

    print("\nPort Scan Detection Completed")
if __name__ == "__main__":
    run()
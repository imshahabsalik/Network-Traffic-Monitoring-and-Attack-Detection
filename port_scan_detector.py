import sqlite3
import pandas as pd
from datetime import datetime

conn = sqlite3.connect("traffic.db")

df = pd.read_sql_query("""
SELECT *
FROM traffic_logs
WHERE protocol='TCP'
""", conn)

conn.close()

print("\n===== PORT SCAN DETECTION =====\n")

THRESHOLD = 20

for ip in df["source_ip"].unique():

    ip_data = df[df["source_ip"] == ip]

    unique_ports = ip_data["destination_port"].nunique()

    if unique_ports > THRESHOLD:

        print(
            f"[ALERT] Possible Port Scan "
            f"from {ip} "
            f"({unique_ports} ports)"
        )
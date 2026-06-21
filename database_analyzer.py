import sqlite3
import pandas as pd

conn = sqlite3.connect("traffic.db")

df = pd.read_sql_query(
    "SELECT * FROM traffic_logs",
    conn
)

conn.close()

print("\n===== DATABASE TRAFFIC SUMMARY =====\n")

print(f"Total Packets: {len(df)}")

print("\nProtocol Distribution:")
print(df["protocol"].value_counts())

print("\nTop Source IPs:")
print(df["source_ip"].value_counts().head())
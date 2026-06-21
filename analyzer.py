import pandas as pd

df = pd.read_csv("traffic_logs.csv")

print("\n===== NETWORK TRAFFIC SUMMARY =====\n")

print(f"Total Packets Captured: {len(df)}")

print("\nTop Source IPs:")
print(df["Source IP"].value_counts().head(5))

print("\nTop Destination IPs:")
print(df["Destination IP"].value_counts().head(5))

print("\nProtocol Distribution:")
print(df["Protocol"].value_counts())

print("\nMost Accessed Destination Ports:")
print(df["Destination Port"].value_counts().head(10))
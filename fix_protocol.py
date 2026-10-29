import sqlite3

conn = sqlite3.connect("traffic.db")

cursor = conn.cursor()

cursor.execute("""
UPDATE traffic_logs
SET protocol = 'IGMP'
WHERE protocol = '2'
""")

conn.commit()

print("Protocol mapping updated.")

conn.close()
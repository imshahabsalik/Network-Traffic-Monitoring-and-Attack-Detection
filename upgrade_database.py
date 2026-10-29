import sqlite3

conn = sqlite3.connect("traffic.db")

cursor = conn.cursor()

try:
    cursor.execute("""
    ALTER TABLE alerts
    ADD COLUMN severity TEXT
    """)

    print("Severity column added.")

except Exception as e:
    print(e)

conn.commit()
conn.close()
import sqlite3
import pandas as pd

conn = sqlite3.connect("traffic.db")

alerts = pd.read_sql_query(
    """
    SELECT *
    FROM alerts
    ORDER BY id DESC
    """,
    conn
)

conn.close()

print(alerts)
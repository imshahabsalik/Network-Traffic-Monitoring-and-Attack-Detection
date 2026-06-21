import sqlite3

DB_NAME = "traffic.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS traffic_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        source_ip TEXT,
        destination_ip TEXT,
        protocol TEXT,
        source_port INTEGER,
        destination_port INTEGER,
        packet_size INTEGER
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        source_ip TEXT,
        alert_type TEXT,
        description TEXT
    )
""")

    conn.commit()
    conn.close()

    print("Database initialized successfully.")

if __name__ == "__main__":
    create_database()
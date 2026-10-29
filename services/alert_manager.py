import sqlite3
from datetime import datetime

DB_NAME = "traffic.db"


def create_alert(
    source_ip,
    alert_type,
    severity,
    description
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    # Check if similar alert already exists
    cursor.execute("""
    SELECT COUNT(*)
    FROM alerts
    WHERE source_ip = ?
    AND alert_type = ?
    """, (
        source_ip,
        alert_type
    ))

    existing_alerts = cursor.fetchone()[0]

    if existing_alerts > 0:

        print(
            f"[SKIPPED] Duplicate alert: "
            f"{alert_type} for {source_ip}"
        )

        conn.close()
        return

    cursor.execute("""
    INSERT INTO alerts(
        timestamp,
        source_ip,
        alert_type,
        severity,
        description
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        source_ip,
        alert_type,
        severity,
        description
    ))

    conn.commit()
    conn.close()

    print(
        f"[ALERT CREATED] "
        f"{alert_type} -> {source_ip}"
    )
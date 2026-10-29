from flask import Flask, render_template
import sqlite3
import pandas as pd

from services.stats_service import (
    get_total_packets,
    get_total_alerts,
    get_protocol_distribution,
    get_top_source_ips,
    get_top_destination_ports,
    get_alert_distribution,
    get_critical_alert_count,
    get_high_alert_count,
    get_medium_alert_count,
    get_recent_alerts,
    get_recent_logs
)

app = Flask(__name__)

DB_NAME = "traffic.db"


@app.route("/")
def dashboard():

    protocol_distribution = get_protocol_distribution()
    alert_distribution = get_alert_distribution()

    protocol_labels = list(protocol_distribution.keys())
    protocol_values = list(protocol_distribution.values())

    alert_labels = list(alert_distribution.keys())
    alert_values = list(alert_distribution.values())

    recent_alerts = get_recent_alerts()
    recent_logs = get_recent_logs()

    return render_template(
        "dashboard.html",
        total_packets=get_total_packets(),
        total_alerts=get_total_alerts(),
        critical_alerts=get_critical_alert_count(),
        high_alerts=get_high_alert_count(),
        medium_alerts=get_medium_alert_count(),
        top_ips=get_top_source_ips(),
        top_ports=get_top_destination_ports(),
        protocol_labels=protocol_labels,
        protocol_values=protocol_values,
        alert_labels=alert_labels,
        alert_values=alert_values,
        recent_alerts=recent_alerts,
        recent_logs=recent_logs
    )


@app.route("/alerts")
def alerts():

    conn = sqlite3.connect(DB_NAME)

    alerts_df = pd.read_sql_query(
        """
        SELECT *
        FROM alerts
        ORDER BY id DESC
        """,
        conn
    )

    conn.close()

    return render_template(
        "alerts.html",
        alerts=alerts_df.to_dict("records")
    )


@app.route("/logs")
def logs():

    conn = sqlite3.connect(DB_NAME)

    logs_df = pd.read_sql_query(
        """
        SELECT *
        FROM traffic_logs
        ORDER BY id DESC
        LIMIT 100
        """,
        conn
    )

    conn.close()

    return render_template(
        "logs.html",
        logs=logs_df.to_dict("records")
    )


if __name__ == "__main__":
    app.run(debug=True)
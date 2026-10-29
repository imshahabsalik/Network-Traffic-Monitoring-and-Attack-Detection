import sqlite3
import pandas as pd

DB_NAME = "traffic.db"


def load_traffic_data():
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(
        "SELECT * FROM traffic_logs",
        conn
    )

    conn.close()

    return df


def load_alert_data():
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(
        "SELECT * FROM alerts",
        conn
    )

    conn.close()

    return df


def get_total_packets():

    df = load_traffic_data()

    return len(df)


def get_protocol_distribution():

    df = load_traffic_data()

    return df["protocol"].value_counts().to_dict()


def get_top_source_ips(limit=5):

    df = load_traffic_data()

    return (
        df["source_ip"]
        .value_counts()
        .head(limit)
        .to_dict()
    )


def get_top_destination_ports(limit=10):

    df = load_traffic_data()

    return (
        df["destination_port"]
        .value_counts()
        .head(limit)
        .to_dict()
    )


def get_total_alerts():

    df = load_alert_data()

    return len(df)


def get_alert_distribution():

    df = load_alert_data()

    if len(df) == 0:
        return {}

    return (
        df["alert_type"]
        .value_counts()
        .to_dict()
    )
def get_critical_alert_count():

    df = load_alert_data()

    if len(df) == 0:
        return 0

    return len(
        df[df["severity"] == "CRITICAL"]
    )


def get_high_alert_count():

    df = load_alert_data()

    if len(df) == 0:
        return 0

    return len(
        df[df["severity"] == "HIGH"]
    )


def get_medium_alert_count():

    df = load_alert_data()

    if len(df) == 0:
        return 0

    return len(
        df[df["severity"] == "MEDIUM"]
    )
def get_recent_alerts(limit=10):

    df = load_alert_data()

    if len(df) == 0:
        return []

    return (
        df.sort_values("id", ascending=False)
        .head(limit)
        .to_dict("records")
    )


def get_recent_logs(limit=20):

    df = load_traffic_data()

    if len(df) == 0:
        return []

    return (
        df.sort_values("id", ascending=False)
        .head(limit)
        .to_dict("records")
    )
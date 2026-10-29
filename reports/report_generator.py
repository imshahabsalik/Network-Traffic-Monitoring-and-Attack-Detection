from datetime import datetime
from services.stats_service import (
    get_total_packets,
    get_protocol_distribution,
    get_top_source_ips,
    get_top_destination_ports,
    get_total_alerts,
    get_alert_distribution
)

report_name = (
    f"reports/security_report_"
    f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
)

with open(report_name, "w") as report:

    report.write("=" * 50 + "\n")
    report.write("NETWORK SECURITY REPORT\n")
    report.write("=" * 50 + "\n\n")

    report.write(
        f"Generated: "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    )

    report.write(
        f"Total Packets: "
        f"{get_total_packets()}\n\n"
    )

    report.write("PROTOCOL DISTRIBUTION\n")
    report.write("-" * 30 + "\n")

    for protocol, count in (
        get_protocol_distribution().items()
    ):
        report.write(
            f"{protocol}: {count}\n"
        )

    report.write("\n")

    report.write("TOP SOURCE IPS\n")
    report.write("-" * 30 + "\n")

    for ip, count in (
        get_top_source_ips().items()
    ):
        report.write(
            f"{ip}: {count}\n"
        )

    report.write("\n")

    report.write("TOP DESTINATION PORTS\n")
    report.write("-" * 30 + "\n")

    for port, count in (
        get_top_destination_ports().items()
    ):
        report.write(
            f"{port}: {count}\n"
        )

    report.write("\n")

    report.write(
        f"TOTAL ALERTS: "
        f"{get_total_alerts()}\n\n"
    )

    report.write("ALERT DISTRIBUTION\n")
    report.write("-" * 30 + "\n")

    for alert, count in (
        get_alert_distribution().items()
    ):
        report.write(
            f"{alert}: {count}\n"
        )

print(f"\nReport generated successfully:")
print(report_name)
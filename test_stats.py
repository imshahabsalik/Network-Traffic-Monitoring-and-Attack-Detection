from services.stats_service import *

print("\n===== SYSTEM STATISTICS =====\n")

print("Total Packets:")
print(get_total_packets())

print("\nProtocol Distribution:")
print(get_protocol_distribution())

print("\nTop Source IPs:")
print(get_top_source_ips())

print("\nTop Destination Ports:")
print(get_top_destination_ports())

print("\nTotal Alerts:")
print(get_total_alerts())

print("\nAlert Distribution:")
print(get_alert_distribution())
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
from datetime import datetime
import csv
import os
import sqlite3
from services.detector_runner import run_all_detectors

DB_NAME = "traffic.db"

def save_to_database(
    timestamp,
    src_ip,
    dst_ip,
    protocol,
    src_port,
    dst_port,
    packet_size
):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO traffic_logs(
        timestamp,
        source_ip,
        destination_ip,
        protocol,
        source_port,
        destination_port,
        packet_size
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        src_ip,
        dst_ip,
        protocol,
        src_port,
        dst_port,
        packet_size
    ))

    conn.commit()
    conn.close()

CSV_FILE = "traffic_logs.csv"

# Create CSV file with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp",
            "Source IP",
            "Destination IP",
            "Protocol",
            "Source Port",
            "Destination Port",
            "Packet Size"
        ])

def packet_callback(packet):

    if not packet.haslayer(IP):
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    protocol_number = packet[IP].proto

    protocol_map = {
        1: "ICMP",
        2: "IGMP",
        6: "TCP",
        17: "UDP"
    }

    protocol = protocol_map.get(
        protocol_number,
        f"OTHER_{protocol_number}"
    )

    src_port = None
    dst_port = None

    if packet.haslayer(TCP):
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

    elif packet.haslayer(UDP):
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    packet_size = len(packet)

    print(
        f"[{timestamp}] "
        f"{src_ip}:{src_port} -> "
        f"{dst_ip}:{dst_port} | "
        f"{protocol} | "
        f"{packet_size} bytes"
    )

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            src_ip,
            dst_ip,
            protocol,
            src_port,
            dst_port,
            packet_size
        ])

    save_to_database(
        timestamp,
        src_ip,
        dst_ip,
        protocol,
        src_port,
        dst_port,
        packet_size
    )

print("Network Traffic Monitoring Started...")
print("Capturing packets...\n")

sniff(
    prn=packet_callback,
    store=False,
    timeout=30
)

print("\nCapture Completed.")
print("\nRunning Detection Engine...\n")

run_all_detectors()

print("\nDetection Engine Completed.")
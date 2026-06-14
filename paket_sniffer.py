from scapy.all import sniff
from datetime import datetime

def packet_callback(packet):
    if packet.haslayer("IP"):
        print(
            f"{datetime.now()} | "
            f"Source: {packet['IP'].src} | "
            f"Destination: {packet['IP'].dst}"
        )

print("Capturing packets...")
sniff(prn=packet_callback, count=20)
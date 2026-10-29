from detectors.dos_detector import run as run_dos
from detectors.port_scan_detector import run as run_port_scan
from detectors.icmp_flood_detector import run as run_icmp
from detectors.blacklist_ip_detector import run as run_blacklist
from detectors.traffic_spike_detector import run as run_spike


def run_all_detectors():

    print("\n===== RUNNING DETECTORS =====\n")

    run_dos()
    run_port_scan()
    run_icmp()
    run_blacklist()
    run_spike()

    print("\n===== DETECTION COMPLETE =====\n")
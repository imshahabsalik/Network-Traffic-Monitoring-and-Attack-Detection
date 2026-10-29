# Network Traffic Monitoring and Attack Detection System

A Python-based, SIEM-inspired cybersecurity project that monitors network traffic, detects suspicious patterns, generates security alerts, and displays results through a web dashboard.

## Features

- Real-time network packet capture using Scapy
- Traffic logging with source IP, destination IP, protocol, ports, timestamp, and packet size
- SQLite database storage and CSV logging
- Automated execution of multiple detection modules
- Centralized alert management with severity levels
- Interactive dashboard with traffic and alert statistics
- Protocol distribution and alert distribution charts
- Recent alerts, traffic logs, and top source IPs
- Text-based security report generation

## Technology Stack

- **Python** — Core application and detection logic
- **Scapy** — Network packet capture
- **Pandas** — Traffic analysis
- **Flask** — Web dashboard
- **SQLite** — Database
- **Bootstrap** — Dashboard layout
- **Chart.js** — Data visualization
- **CSV** — Traffic log export

## Detection Modules

| Module | Purpose |
|---|---|
| DoS Detection | Identifies unusually high packet counts from a source IP |
| Port Scan Detection | Detects sources contacting many unique TCP destination ports |
| ICMP Flood Detection | Flags unusually high ICMP packet counts |
| Blacklist Detection | Checks traffic against IP addresses in `blacklist.txt` |
| Traffic Spike Detection | Identifies source IP traffic counts exceeding a configured threshold |

The detectors use rule-based thresholds. An alert indicates suspicious activity for investigation and does not independently confirm an attack.

## System Workflow

1. Scapy captures network packets.
2. Packet metadata is stored in SQLite and CSV.
3. The Detector Runner executes the detection modules sequentially after packet capture finishes.
4. The Alert Manager stores generated alerts.
5. The Statistics Service prepares data for the dashboard.
6. Flask displays traffic statistics, charts, alerts, and logs.

**Note:** Detection runs after the capture window completes, rather than immediately after every packet. The dashboard refreshes every 30 seconds.

## Dashboard

The dashboard provides:

- Total packets and alerts
- Critical, high, and medium alert counts
- Protocol and alert distribution charts
- Top source IP addresses and destination ports
- Recent security alerts
- Recent traffic logs

Pages:
- `/` — Main dashboard
- `/alerts` — Stored alerts
- `/logs` — Latest traffic records

## Project Structure

```text
network_monitoring/
├── app.py
├── packet_sniffer.py
├── database.py
├── analyzer.py
├── database_analyzer.py
├── requirements.txt
├── blacklist.txt
├── detectors/
│   ├── dos_detector.py
│   ├── port_scan_detector.py
│   ├── icmp_flood_detector.py
│   ├── blacklist_ip_detector.py
│   └── traffic_spike_detector.py
├── services/
│   ├── alert_manager.py
│   ├── detector_runner.py
│   └── stats_service.py
├── reports/
│   └── report_generator.py
├── templates/
│   ├── dashboard.html
│   ├── alerts.html
│   └── logs.html
└── static/
    └── style.css
```

## Installation

**Requirements:** Python 3.10 or later is recommended.

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Create a virtual environment and install dependencies.

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the Project

**1. Start packet capture and detection**

```bash
python packet_sniffer.py
```

**2. Start the dashboard in a second terminal**

```bash
python app.py
```

**3. Open the dashboard**

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000).

Packet capture may require administrator or root permissions, depending on the operating system.

Run commands from the project root so the application uses the intended database and log files. The application expects an SQLite database containing the required `traffic_logs` and `alerts` tables. Check the database schema when setting up a fresh database.

Flask debug mode is enabled in the current code and should only be used for local development.

## Data Files

- `traffic.db` — Stores packet records and security alerts
- `traffic_logs.csv` — Stores packet log records
- `blacklist.txt` — Contains IP addresses used by the blacklist detector
- `reports/report_generator.py` — Generates a text-based security report

## Limitations

- Detection relies on rule-based thresholds.
- Detectors analyze accumulated records rather than continuous rolling time windows.
- The system is designed for a small-scale local demonstration.
- Detection accuracy and throughput have not been independently benchmarked.

## Future Improvements

- Time-window-based detection
- Configurable network interfaces and database paths
- Unit and integration testing
- Improved alert filtering and notifications
- Evaluation using labeled datasets and measurable performance metrics

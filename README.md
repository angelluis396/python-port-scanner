Port Scanner
A simple multi-threaded TCP port scanner written in Python. This tool scans a specified range of ports on a target host to identify open ports.
Features

Scans a user-defined range of ports on a target IP or hostname.
Uses multi-threading for faster scanning (default: 100 threads).
Provides scan duration and lists open ports.
Includes default inputs for ease of use (localhost, ports 1-1000).
Handles errors for invalid inputs, unresolved hostnames, and interrupted input.

Requirements

Python 3.x
Standard Python libraries: socket, threading, queue, time

Installation

Save the script as port_scanner.py.
Ensure Python 3 is installed on your system.
No additional dependencies are required.

Usage

Open a terminal and navigate to the directory containing port_scanner.py.
Run the script:python port_scanner.py


Enter the following when prompted:
Target IP or hostname: E.g., 127.0.0.1 (localhost) or scanme.nmap.org. Press Enter for default (127.0.0.1).
Start port: E.g., 1. Press Enter for default (1).
End port: E.g., 1000. Press Enter for default (1000).


The script will display the scan progress, duration, and any open ports found.

Example
Enter target IP or hostname (e.g., 127.0.0.1): scanme.nmap.org
Enter start port (e.g., 1): 1
Enter end port (e.g., 1000): 100
Scanning 45.33.32.156 from port 1 to 100...
Scan completed in 3.45 seconds
Open ports found:
Port 80 is open

Testing

Localhost: Scan 127.0.0.1 to check for open ports like 80 (HTTP) or 22 (SSH) if services are running.
Test Server: Use scanme.nmap.org for a public server designed for scanning tests.
Local Service: Start a web server (python -m http.server 8000) and scan port 8000 to verify detection.

Notes

Legal Warning: Port scanning without permission may be illegal in some jurisdictions. Only scan systems you own or have explicit authorization to test (e.g., scanme.nmap.org).
Performance: Adjust num_threads in the scan_ports function if needed, but 100 is generally efficient.
Interruption: Use Ctrl+C to stop the scan, though partial results may not be displayed.

License
This project is provided as-is for educational purposes. Use responsibly.

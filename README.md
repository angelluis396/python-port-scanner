# 🔍 Port Scanner

A simple multi-threaded TCP port scanner written in Python. This tool scans a specified range of ports on a target host to identify open ports.

---

## 🚀 Features

* Scans a user-defined range of ports on a target IP or hostname.
* Utilizes **multi-threading** for faster results (default: 100 threads).
* Displays scan duration and lists open ports.
* Includes sensible **default inputs** for convenience:

  * Target: `localhost`
  * Port range: `1–1000`
* Gracefully handles invalid input, hostname resolution errors, and interruptions.

---

## 🧰 Requirements

* Python **3.x**
* Standard Python libraries:

  * `socket`
  * `threading`
  * `queue`
  * `time`

No external dependencies required.

---

## 📦 Installation

1. Save the script as `port_scanner.py`.
2. Ensure Python 3 is installed (`python3 --version`).
3. You're ready to go! No additional setup is needed.

---

## ⚙️ Usage

In your terminal:

```bash
python port_scanner.py
```

You'll be prompted to enter:

* **Target IP or hostname**
  Example: `127.0.0.1`, `scanme.nmap.org`
  *(Press Enter for default: `127.0.0.1`)*

* **Start port**
  Example: `1`
  *(Press Enter for default: `1`)*

* **End port**
  Example: `1000`
  *(Press Enter for default: `1000`)*

### Example Output

```
Enter target IP or hostname (e.g., 127.0.0.1): scanme.nmap.org
Enter start port (e.g., 1): 1
Enter end port (e.g., 100): 100

Scanning 45.33.32.156 from port 1 to 100...
Scan completed in 3.45 seconds

Open ports found:
Port 80 is open
```

---

## 🧪 Testing

* **Localhost**: Scan `127.0.0.1` to check for open ports like `22` (SSH) or `80` (HTTP), if services are running.
* **Test Server**: Use [`scanme.nmap.org`](https://nmap.org) — a public test server for scanning.
* **Local Service**: Start a quick server:

  ```bash
  python -m http.server 8000
  ```

  Then scan port `8000`.

---

## ⚠️ Notes

* **Legal Warning**: Port scanning unauthorized systems may be illegal. Only scan systems you own or are explicitly permitted to test (e.g., `scanme.nmap.org`).
* **Performance**: You can tweak the `num_threads` value in the script for slower or faster scans.
* **Interrupting**: Use `Ctrl+C` to cancel the scan. Note: partial results may not print.

---

## 📄 License

This project is provided **as-is for educational purposes**. Use responsibly.

---

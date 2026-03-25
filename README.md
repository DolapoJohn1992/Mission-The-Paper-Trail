# Mission: The Paper Trail | Brute-Force Detector

## 🛡️ Project Overview
This Python-based security tool automates the detection of brute-force login attempts within system authentication logs. It targets repeated failed password attempts, a hallmark of automated credential-stuffing attacks.

## 🚀 Key Features
* **Log Parsing:** Extracts timestamps and source IPs from `auth_audit.log`.
* **Threshold Detection:** Identifies any IP exceeding 4+ failed attempts.
* **Automated Alerting:** Generates `CRITICAL ALERT` console messages.
* **Forensic Reporting:** Saves findings to `brute_report.txt`.

## 🛠️ Technical Reference
| Component | Description |
| :--- | :--- |
| **Python File I/O** | Utilizes `open()` to read logs and write forensic reports. |
| **Data Structures** | Uses Python `dictionaries` to map IP addresses to hit counts. |
| **Logic Flow** | Implements conditional loops to filter `Failed password` strings. |

## 🔧 Infrastructure Troubleshooting
Deployment involved advanced Linux systems administration to bypass lab environment failures:
* **DNS Fix:** Manually mapped GitHub IP (`140.82.112.3`) in `/etc/hosts`.
* **Service Recovery:** Restarted `NetworkManager` to restore the SSH tunnel.
* **Path Resolution:** Located the internal submission tool via absolute pathing.

# 🛡️ Autonomous AI SOC Analyst

A real-time security monitoring system built in Python. This project simulates a Security Operations Center (SOC) workflow by generating live server logs and analyzing them instantly for brute-force attacks.

## ⚙️ How It Works

This system uses a **Producer-Consumer** architecture:

1.  **The Generator (`log_generator.py`)**: Simulates a Linux SSH server. It randomly generates "Accepted password" (safe) and "Failed password" (attack) logs to a shared file.
2.  **The Analyst (`analyst.py`)**: Acts as the Intrusion Detection System (IDS). It tails the log file in real-time, using pattern recognition to flag suspicious activity.



## 🛠️ Technical Features

* **Live File Tailing**: Uses non-blocking file I/O to monitor logs as they are written.
* **Pattern Matching**: Implemented logic to distinguish between authorized access and brute-force attempts.
* **Concurrency**: Designed to run as two independent, interacting processes.

## 🚀 Getting Started

1.  **Start the Server Simulator**:
    ```bash
    python log_generator.py
    ```
2.  **Launch the AI Analyst**:
    ```bash
    python analyst.py
    ```

## 📈 Future Roadmap
- [ ] Add **GeoIP** tracking to see where "attacks" are coming from.
- [ ] Implement a **Discord Webhook** to send alerts to a mobile device.
- [ ] Upgrade to a **Random Forest** ML model for anomaly detection.
# Autonomous-AI-SOC-Analyst
An automated security operations lab using Python to generate synthetic server logs and Google Gemini AI to perform autonomous threat analysis.



## Project Overview
This project simulates a modern Security Operations Center (SOC) environment. It uses Python to generate realistic server authentication logs and leverages the **Google Gemini API** to analyze those logs for potential security threats like brute-force attacks.

This project was built to bridge the gap between theoretical knowledge (CompTIA CySA+) and practical security automation.

## Features
* **Log Generator:** A custom Python script that creates `server_logs.txt` containing both authorized logins and failed attempts from various IP addresses.
* **AI Threat Detection:** Uses Generative AI to parse logs, identify anomalies, and explain security risks in plain language.
* **Automated Workflow:** Demonstrates how AI can assist SOC analysts by reducing the time spent on manual log review.

## Tech Stack
* **Language:** Python
* **API:** Google Gemini (Generative AI)
* **Environment:** Linux/Terminal, VS Code
* **Version Control:** Git & GitHub

## How It Works
1.  **Generate Logs:** Run `log_generator.py` to start creating simulated SSH traffic.
2.  **Analyze:** The AI SOC Analyst script reads the logs and sends suspicious patterns to Gemini for an "expert" security opinion.
3.  **Alert:** The system outputs identified threats and recommended remediation steps.

## Future Enhancements
* Integrate real-world SIEM (Splunk/ELK) log ingestion.
* Add automated incident response (e.g., auto-blocking malicious IPs).
* Expand threat detection to include SQL injection and XSS patterns.

  # Aegis Deceptive Intelligence
### AI-Driven Active Defense System & Honeypot

![Project Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Python](https://img.shields.io/badge/Language-Python%203.10%2B-blue)
![Security](https://img.shields.io/badge/Focus-Active%20Defense-red)

## 🛡️ Overview
**Aegis Deceptive Intelligence** is a next-generation "Active Defense" system designed to detect, analyze, and map cyber threats in real-time. Unlike traditional passive honeypots, Aegis uses **Generative AI (Gemini API)** to analyze attacker payloads and classify their intent (e.g., *Botnet Recruitment*, *Credential Harvesting*, *Reconnaissance*).

The system deploys "Ghost Sensors"—low-interaction services that mimic vulnerable ports (SSH, HTTP, Telnet)—to attract and study adversaries without exposing the actual network infrastructure.

## 🚀 Key Features
* **Smart Ghost Sensors:** Multi-port listeners that emulate vulnerable services to capture raw attack data.
* **AI Threat Classification:** detailed intent analysis of every captured command using Large Language Models.
* **Live Threat Map:** Real-time visualization of attacker origins using geolocation APIs.
* **Hardened Architecture:** Strict Linux permission controls to ensure log integrity and sensor security.

## 🔒 Security & Hardening
Security begins at the file system level. This project adheres to the **Principle of Least Privilege**:
* **Log Integrity:** Write access to the `/logs` directory is restricted to the service account only.
* **Config Protection:** API keys and environment variables are locked down (read-only for root).
* **Audit Trail:** File structures are regularly audited using `ls -la` to detect unauthorized modifications.

## 🛠️ Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/aegis-deceptive-intelligence.git](https://github.com/yourusername/aegis-deceptive-intelligence.git)
    cd aegis-deceptive-intelligence
    ```

2.  **Set up the environment:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Ghost Sensor:**
    ```bash
    sudo python3 sensor.py
    ```

## 📊 Roadmap
- [x] Basic TCP Listener (Ghost Sensor)
- [x] Linux File System Hardening
- [ ] Integration with Gemini API for Intent Analysis
- [ ] Dashboard Development (Streamlit)
- [ ] Docker Containerization

---
*Created by ASHITOSH S JOSHI as part of a Cybersecurity & AI Portfolio.*


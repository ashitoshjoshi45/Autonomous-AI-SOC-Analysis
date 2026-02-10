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


import socket
import json
import os
from datetime import datetime
from ai_analyst import analyze_threat 

def log_to_file(data):
    """Helper to ensure the dashboard has data to read."""
    log_file = "sensor_logs.json"
    logs = []
    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    
    logs.append(data)
    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

def start_ghost_sensor(port=8080): # Changed to 8080 to match Docker
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Fix: Allow immediate port reuse after restart
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"[*] Ghost Sensor listening on port {port}...")

    while True:
        try:
            client_socket, addr = server_socket.accept()
            request = client_socket.recv(1024).decode('utf-8', errors='ignore')
            
            if request:
                print(f"[*] Connection from {addr[0]} | Payload: {request.strip()[:20]}...")
                analysis = analyze_threat(addr[0], request, port)
                
                # Prepare data for dashboard
                log_entry = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "source_ip": addr[0],
                    "payload": request.strip(),
                    "verdict": analysis.get("verdict", "UNKNOWN"),
                    "attack_type": analysis.get("attack_type", "N/A"), # Fixed typo
                    "confidence": analysis.get("confidence", 0),
                    "reasoning": analysis.get("reasoning", "No details")
                }
                
                log_to_file(log_entry)
                
                if log_entry["verdict"] == "MALICIOUS":
                    print(f"!!! ALERT: {log_entry['attack_type']} detected from {addr[0]}")
            
            client_socket.close()
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    start_ghost_sensor()
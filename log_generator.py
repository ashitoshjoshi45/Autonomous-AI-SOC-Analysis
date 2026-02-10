import time
import random

# this is the file where all the logs will be saved
LOG_FILE = "server_logs.txt"

# Fake IP addresses
ips = ["192.168.1.5", "10.0.0.2", "45.33.22.11", "203.0.113.5"]
users = ["admin", "root", "user1", "test"]

print(f"[*] Starting Log Generator... Writing to {LOG_FILE}")
print("[*] Press Ctrl+C to stop.\n")

# Clear the file first
with open(LOG_FILE, "w") as f:
    f.write("")

try:
    while True:
        # 1. Randomly pick an event type
        event_type = random.choice(["SAFE", "ATTACK", "SAFE"])
        
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        ip = random.choice(ips)
        user = random.choice(users)
        
        if event_type == "SAFE":
            log_entry = f"{timestamp} INFO sshd[{random.randint(1000,9999)}]: Accepted password for {user} from {ip} port {random.randint(1024,65535)} ssh2"
        else:
            # Simulate a Brute Force Attack
            log_entry = f"{timestamp} Failed password for invalid user {user} from {ip} port {random.randint(1024,65535)} ssh2"
            
        # 2. Write to file
        with open(LOG_FILE, "a") as f:
            f.write(log_entry + "\n")
            
        print(f"New Log: {log_entry}")
        
        # Wait 2 seconds before next log
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[!] Log Generator Stopped.")

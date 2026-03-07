import re
from collections import Counter

def analyze_logs(log_file_path , threshold=5):
    #pattern to find IP addresses in a standard auth log
    ip_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    failed_ips = []

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                #Looking for failed login attempts
                if "Failed password" in line or "authentication failure" in line:
                    match = re.search(ip_pattern, line)
                    if match:
                        failed_ips.append(match.group(1))

        # count occurence of each IP
        counts = Counter(failed_ips)

        print(f"----Security Alert Report ----")
        for ip, count in counts.items():
            if count >= threshold:
                print(f"[ALERT] IP {ip} exceeded threshold with {count} failures.")
    
    except FileNotFoundError:
        print("Error: Log file not found.")
        
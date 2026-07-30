# added on 30-07-2026

# // title: log parser and threat matcher
# class solution:
class solution:
#     def parse_logs:
    def parser_logs(self, log_file_lines, threat_patterns):
        alerts = []      

#         // OUTER LOOP: For each log_line in the log file
        for log_line in log_file_lines:
#             // Extract IP address for IPv4 and event type from log_line
            ip_match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', log_line)
            ip_address = ip_match.group(0) if ip_match else "unknown IP"  
# // INNER LOOP: For each pattern in threat_patterns
            for pattern in threat_patterns:
                if pattern in log_line:
                    alerts.append({"ip": ip_address, "log": log_line, "matched_pattern": pattern})
#                 // If the event type matches the pattern
#                     // Add the matched log_line and IP to alerts list
                    break        
# // Return the alerts list
        return alerts
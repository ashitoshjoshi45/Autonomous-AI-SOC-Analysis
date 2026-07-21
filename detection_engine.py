# // title: SOC Analyst Alert Rules Engine
# function evaluate_traffic(log_entry, threat_signatures)
#   initialize alert_flag as false
#   initialize log_severity as "INFO"
  
#   for each signature in threat_signatures do
#     if signature.pattern matches log_entry.payload then
#       set alert_flag to true
#       set log_severity to signature.severity
#       break loop
#     end if
#   end for
# added on 17-07-2026
class DetectionEngine:
    def __init__(self):
        #Tracking unique source IP's to map brute force or scanning singal
        self.ip_tracker = {}

        #added on 16-07-2026
        def evaluate_traffic(self, log_entry, threat_signatures):
        alert_flag = False
        log_severity = "INFO"
    
        for rule_name, rule_meta in threat_signatures.items():
            if rule_meta["pattern"].search(log_entry.get("payload", "")):
                alert_flag = True
                log_severity = rule_meta["severity"]
                break
            
        return alert_flag, log_severity

    #added on 19-07-2026
    def analyze_payload(self, source_ip, payload):
        #create a localized log entry structure for evaluator
        log_entry = {"payload":payload}

        # 1. Run signature evaluation
        alert_flag, log_severity = self.evaluate_traffic(log_entry, THREAT_SIGNATURES)

        # 2. Track traffic freq for simple threshold alerting
        self.ip_tracker[source_ip] = self.op_tracker.get(source_ip, 0) + 1
        if self.ip_tracker[source_ip] > 100 and log_severity != "CRITICAL":
            alert_flag = True
            log_severity = "MEDIUM"

        # 3. Return enriched telemetry for the dashboard
        return{
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "source_ip": source_ip,
            "alert_triggered": alert_flag,
            "severity": log_severity
        }
        #added on 20-07-2026
        # title: analyze payload pseudocode
class DetectionEngine:
          def analyze_payload(payload_list, signature_db):
            #added on 21-07-2026
              # initialize an empty list to store detected threats
              payload_list = []
              # iterate through payload_list
                  # iterate through signature_db
                      # if signature is found in the payload
                          # log the detection and defang any malicious URLs
                          # flag payload for Ollama context analysis
                          # break to avoid duplicate alerts for the same payload
              #return the list of detected threats
  
   
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
        def analyze_payload(self, payload_list, signature_db):
            #added on 21-07-2026
            # initialize an empty list to store detected threats
            detected_threats = []
            # iterate through payload_list
            for payload in payload_list:
                # iterate through signature_db
                for signature in signature_db:
                    # if signature is found in the payload
                    if signature in payload:
                        # log the detection and defang any malicious URLs
                        # optimized on 24-07-2026
                        # flag payload for Ollama context analysis
                        detected_threats.append(payload)
                        # break to avoid duplicate alerts for the same payload
                        break
            #return the list of detected threats
            return detected_threats
   
           # added on 25-07-2026
        def integrate_ollama_analysis(self, detected_threats):
            # initialize an empty list to store contextually enriched alerts
            enriched_alerts = []
        
            # iterate through the list of detected threats
            for threat in detected_threats:
                # generate the analysis prompt for the local LLM
                llm_prompt = f"Analyze the following suspicious payload for malicious intent and flag potential CVEs: {threat}"
            
                # append the structured alert with pending AI context
                enriched_alerts.append({
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                    "payload": threat,
                    "ollama_prompt": llm_prompt,
                    "status": "Awaiting LLM response"
                })
            
            # return the enriched contextual alerts
            return enriched_alerts
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
    def evaluate_traffic(self, log_entry, threat_signatures):
    alert_flag = False
    log_severity = "INFO"
    
    for rule_name, rule_meta in threat_signatures.items():
        if rule_meta["pattern"].search(log_entry.get("payload", "")):
            alert_flag = True
            log_severity = rule_meta["severity"]
            break
            
    return alert_flag, log_severity
  
#   return alert_flag, log_severity
# end function
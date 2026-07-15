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
  
#   return alert_flag, log_severity
# end function
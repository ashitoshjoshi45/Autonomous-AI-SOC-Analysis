# added on 03-08-2026

# class solution:
class Solution:
#   def deduplicate_alerts(incoming_alerts, recent_cache):
    def deduplicate_alerts(self, incoming_alerts, recent_cache, time_threshold): 
#         // Initialize an empty list for unique_alerts
        unique_alerts = []
#         // OUTER LOOP: For each alert in incoming_alerts
        for alert in incoming_alerts:
#             // Extract the alert signature and timestamp
#             // Set duplicate_flag to false
            alert_signature = alert.get('signature')
            alert_timestamp = alert.get('timestamp')
            duplicate_flag = False
#             // INNER LOOP: For each cached_alert in recent_cache
            for cached in recent_cache:
#                 // If signature matches and time difference is less than threshold
                if cached.get('signature') == alert_signature:
                    time_diff = alert_timestamp - cached.get('timestamp')
                    if time_diff < time_threshold:
#                     // Set duplicate_flag to true
#                     // Break out of the inner loop
                        duplicate_flag = True
                        break
#             // If duplicate_flag is false
                if not duplicate_flag:
#                 // Add alert to unique_alerts
                     unique_alerts.append(alert)
#         // Return unique_alerts
            return unique_alerts
# end function
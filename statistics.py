from detectors import ThreatDetector


def show_statistics(events):
     print()
     print("========== SECURITY STATISTICS ==========")
    
     if len(events) == 0:
                      print("No security events available.")
    
     else:
                total_events = len(events)
                successful_logins = 0
                failed_logins = 0
                threats = 0
                low_risk = 0
                high_risk = 0
    
                detector = ThreatDetector()
    
                for event in events:
                    if event.event_type == "LOGIN_SUCCESS":
                        successful_logins = successful_logins + 1
    
                    if event.event_type == "LOGIN_FAILED":
                        failed_logins = failed_logins + 1
    
                    event_threats = detector.analyze_event(event)    
    
                    if len(event_threats) > 0:
                        threats = threats + 1
    
                    risk = event.get_risk_level()
                        
                    if risk == "LOW":
                        low_risk = low_risk + 1
    
                    elif risk == "HIGH" or risk == "CRITICAL":
                        high_risk = high_risk + 1
    
                print("Total Events:", total_events)
                print("Successful Logins:", successful_logins)
                print("Failed Logins:", failed_logins)
                print("Threats Detected:", threats)
                print("Low Risk Events:", low_risk)
                print("High/Critical Risk Events:", high_risk)
    
     print("=========================================")
    
from detectors import ThreatDetector


def generate_incident_report(events):
     print()
     print("========== INCIDENT REPORT ==========")
    
     if len(events) == 0:
              print("No security events available.")

     else:
                total_events = len(events)
                threats = 0
                high_risk = 0
    
                detector = ThreatDetector()
    
                for event in events:
                    event_threats = detector.analyze_event(event)
    
                    if len(event_threats) > 0:
                        threats = threats + 1
    
                    risk = event.get_risk_level()
    
                    if risk == "HIGH" or risk == "CRITICAL":
                        high_risk = high_risk + 1    
    
                print("Total Events:", total_events)
                print("Threats Detected:", threats)
                print("High/Critical Risk Events:", high_risk)
    
                print()
                print("---------- INCIDENT DETAILS ----------")
    
    
                for event in events:
                    threats_found = detector.analyze_event(event)
                    risk = event.get_risk_level()
    
                    if len(threats_found) > 0:
                        status = "THREAT DETECTED"
                    elif risk == "MEDIUM":
                        status = "REVIEW"
                    else:
                        status = "NORMAL"
    
                    print()
                    print("Username:", event.get_username())
                    print("Event:", event.event_type)
                    print("Risk Level:", risk)
                    print("Status:", status)
    
                    if len(threats_found) > 0:
                        print("Threats:")
                        for threat in threats_found:
                            print("-", threat)
    
     print("=====================================")
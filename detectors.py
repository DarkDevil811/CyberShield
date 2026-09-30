class ThreatDetector:
    def detect_brute_force(self, event):
        if event.get_failed_attempts() >= 5:
            return "Possible Brute Force Attack"
        else:
            return "No Brute Force Threat"
        
    def detect_suspicious_login(self, event):
        if event.event_type == "SUSPICIOUS_LOGIN":
            return "Suspicious Login Activity"
        else:
            return "No Suspicious Login"
        
    def detect_privilege_change(self, event):
            if event.event_type == "PRIVILEGE_CHANGE":
                return "Privilege Change Detected"
            else:
                return "No Privilege Change"
            
    def analyze_event(self, event):
        results = []

        brute_force = self.detect_brute_force(event)
        suspicious_login = self.detect_suspicious_login(event)
        privilege_change = self.detect_privilege_change(event)

        if brute_force != "No Brute Force Threat":
            results.append(brute_force)

        if suspicious_login != "No Suspicious Login":
            results.append(suspicious_login)

        if privilege_change != "No Privilege Change":
            results.append(privilege_change)

        return results
class SecurityEvent:
    def __init__(self, username, event_type, failed_attempts):
        self.username = username
        self.event_type = event_type
        self.__failed_attempts = failed_attempts

    def get_risk_level(self):
        if  self.__failed_attempts >= 8:
            return "CRITICAL"
        elif  self.__failed_attempts >= 5:
            return "HIGH"
        elif  self.__failed_attempts >= 3:
            return "MEDIUM"
        else:
            return "LOW"

    def get_username(self):
        return self.username

    def get_failed_attempts(self):
        return self.__failed_attempts

    def describe(self):
        return "General security event"
    
    
class LoginEvent(SecurityEvent):
    def describe(self):
        return "Login security event"


class FileEvent(SecurityEvent):
    def describe(self):
        return "File access security event"



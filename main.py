from models import SecurityEvent, LoginEvent, FileEvent
from detectors import ThreatDetector
from reports import generate_incident_report
from statistics import show_statistics


            
events = []


def show_menu():
    print()
    print("⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊")
    print("            CyberShield v1.0")
    print("       Cyber Threat Detection System")
    print("⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊⛊")
    print()
    print("[1] Generate Security Event")
    print("[2] View Security Events")
    print("[3] Analyze Threats")
    print("[4] Risk Analysis")
    print("[5] Incident Report")
    print("[6] Statistics")
    print("[7] Exit")
    print()



while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")

        print()
        print("Select event type:")
        print("[1] LOGIN_SUCCESS")
        print("[2] LOGIN_FAILED")
        print("[3] FILE_ACCESS")
        print("[4] PRIVILEGE_CHANGE")
        print("[5] SUSPICIOUS_LOGIN")

        event_choice = input("Enter event type choice: ")

        if event_choice == "1":
            event_type = "LOGIN_SUCCESS"

        elif event_choice == "2":
            event_type = "LOGIN_FAILED"

        elif event_choice == "3":
            event_type = "FILE_ACCESS"

        elif event_choice == "4":
            event_type = "PRIVILEGE_CHANGE"

        elif event_choice == "5":
            event_type = "SUSPICIOUS_LOGIN"

        else:
            print("Invalid event type.")
            continue

        try:
            failed_attempts = int(input("Enter failed login attempts: "))

        except:
            print("Invalid input. Please enter a number.")
            continue

        if event_type == "LOGIN_SUCCESS" or event_type == "LOGIN_FAILED":
            event = LoginEvent(username, event_type, failed_attempts)
            
        elif event_type == "FILE_ACCESS":
            event = FileEvent(username, event_type, failed_attempts)

        else:
            event = SecurityEvent(username, event_type, failed_attempts)
         
        events.append(event)

        print()
        print("Security event created!")

    elif choice == "2":
        print()
        print("========== SECURITY EVENT LOG ==========")

        if len(events) == 0:
            print("No security events recorded.")

        else:
            for event in events:
                print()
                print("Username:", event.get_username())
                print("Event Type:", event.event_type)
                print("Failed Attempts:", event.get_failed_attempts())
                print("Description:", event.describe())

        print("========================================")

    elif choice == "3":
        print()
        print("========== THREAT ANALYSIS ==========")

        detector = ThreatDetector()

        if len(events) == 0:
            print("No security events available.")

        else:
            for event in events:
                print()
                print("Username:", event.username)
                print("Failed Attempts:", event.get_failed_attempts())

                threats = detector.analyze_event(event)

                if len(threats) == 0:
                    print("✓ No threats detected.")
                
                else:
                    for threat in threats:
                        print("⚠ WARNING:", threat)

        print("=====================================")

    elif choice =="4":
        print()
        print("========== RISK ANALYSIS ==========")

        detector = ThreatDetector()


        if len(events) == 0:
            print("No security events available.")

        else:
            for event in events:
                attempts = event.get_failed_attempts()

                print()
                print("Username:", event.username)
                print("Failed Attempts:", attempts)

                risk = event.get_risk_level()
                print("Risk Level:", risk)

                threats = detector.analyze_event(event)

                if len(threats) == 0:
                    print("Detected Threats: None")
                else:
                    print("Detected Threats:")
                    for threat in threats:
                        print("-", threat)    

        print("===================================")

    elif choice =="5":
        generate_incident_report(events)

    elif choice == "6":
       show_statistics(events)


    elif choice == "7":
        print("Exiting CyberShield...")
        break

    else:
        print("Not a valid choice.Try again!")
# CyberShield

CyberShield is a Python-based cybersecurity threat detection and incident analysis simulator. It is a learning project that demonstrates how security events can be generated, analyzed, classified, and summarized using Python.

## Features

- Generate simulated security events
- View recorded security events
- Detect possible brute-force attacks
- Detect suspicious login activity
- Detect privilege changes
- Classify events as LOW, MEDIUM, HIGH, or CRITICAL risk
- Generate an incident report
- Display security statistics
- Handle invalid user input

## Technologies Used

- Python
- Object-Oriented Programming
- Classes and Objects
- Inheritance and Method Overriding
- Functions and Modules
- Lists and Conditional Statements
- Exception Handling

## Project Structure

```text
CyberShield/
├── main.py
├── models.py
├── detectors.py
├── reports.py
├── statistics.py
├── statement.md
└── README.md
## How to Run

Make sure Python is installed on the system.

Open the CyberShield folder in the terminal and run:

```bash
python main.py
```

The main menu will then be displayed.

## How the System Works

The user first creates a simulated security event by entering a username, event type, and number of failed login attempts.

The event is stored and can then be viewed or analyzed using the available options.

The system checks the event for selected threats such as possible brute-force attacks, suspicious login activity, and privilege changes.

Risk levels are calculated based on the number of failed login attempts.

## Testing

The project was tested using different security event scenarios, including:

- Normal login
- Multiple failed login attempts
- Suspicious login
- Privilege change
- Critical-risk event
- Invalid input
- Empty event list
- Statistics generation

The application completed these tests without crashing.

## Project Scope

CyberShield is a simulation intended for educational purposes. It does not perform real attacks, real-time network monitoring, or intrusion prevention.

## Future Improvements

Possible future improvements include:

- Saving events to a database or file
- Adding more threat detection rules
- Adding a graphical user interface
- Adding real-time monitoring
- Adding more detailed security reports
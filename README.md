# Red Team Automation Platform

Red Team Automation Platform is a web-based cybersecurity tool designed to automate basic penetration testing tasks such as domain reconnaissance, port scanning, web security analysis, and password strength evaluation.

This project demonstrates the integration of multiple security analysis techniques into a single automated platform. It is intended for educational purposes and for students learning cybersecurity concepts, ethical hacking, and network security fundamentals.

--------------------------------------------------

Project Overview

The platform allows users to enter a target domain and test password. The system then performs multiple security checks and displays the results through a web interface.

The application automates several reconnaissance and analysis tasks that are typically performed during the initial stages of a security assessment.

--------------------------------------------------

Features

Domain Reconnaissance
- Retrieves domain information using WHOIS
- Identifies domain registrar
- Displays domain creation details
- Resolves the IP address of the target

Port Scanning
- Scans common ports from 1 to 1024
- Detects open and closed ports
- Displays port status information

Web Security Header Analysis
- Checks important HTTP security headers
- Identifies missing security protections
- Helps evaluate web server security configuration

Password Strength Analyzer
- Evaluates password complexity
- Detects weak password patterns
- Provides strength feedback

Automated Security Report
- Generates a structured report of scan results
- Organizes reconnaissance and scanning data
- Displays results in a readable format

--------------------------------------------------

Technologies Used

Programming Language
Python

Framework
Flask

Libraries
requests
python-nmap
python-whois
reportlab

Other Tools
Nmap

Frontend
HTML
CSS

--------------------------------------------------

Project Structure

red-team-automation-platform

app.py
requirements.txt

modules
    recon.py
    port_scanner.py
    web_scanner.py
    password_analyzer.py
    report_generator.py

templates
    index.html
    result.html

README.md

--------------------------------------------------
Open and use at: red-team-automation-platform.onrender.com


Installation

Step 1. Clone the repository

git clone https://github.com/Pranox-Ai/red-team-automation-platform.git

cd red-team-automation-platform


Step 2. Install dependencies

pip install -r requirements.txt


Step 3. Install Nmap

Download and install Nmap from the official website

https://nmap.org/download.html

Ensure Nmap is installed and accessible from your system.

--------------------------------------------------

Running the Application

Start the Flask application using the following command

python app.py

After starting the server, open a web browser and navigate to

http://127.0.0.1:5000

--------------------------------------------------

Usage

1. Open the application in a web browser.
2. Enter a target domain.
NOTE: It is illegal to use on all domains you could only test it on these two Domains Mentioned Below:
      1. scanme.nmap.org
      2. 127.0.0.1
3. Enter a password for strength testing.
4. Click the Start Scan button.
5. The platform will perform automated security analysis and display the results.

--------------------------------------------------

Security Disclaimer

This project is intended strictly for educational and ethical security testing purposes.

Do not use this tool to scan or test systems without proper authorization. Unauthorized scanning or security testing may violate legal and ethical guidelines.

Use Targeted Domians only these two:-
1. scanme.nmap.org
2. 127.0.0.1

--------------------------------------------------

Future Improvements

Possible improvements for this project include:

- SQL Injection detection
- Subdomain enumeration
- Advanced vulnerability scanning
- API integration
- Automated vulnerability reporting
- Interactive security dashboard

--------------------------------------------------

Author

Pranav R C

Cybersecurity Enthusiast 
AI Developer
Engineering Student
Computer Science and Design

GitHub
https://github.com/Pranox-Ai

--------------------------------------------------

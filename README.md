# -Cyber-Security-Intern---Elevate-Labs
This repository showcases the work, tasks, and learning progress during my Cyber Security Internship at Elevate Labs. It includes hands-on labs, vulnerability assessments, network scans, incident response activities, and documentation of tools and techniques used in real-world cybersecurity scenarios.

Task 1: Scan Your Local Network for Open Ports
Objective :-
Learn how to perform basic network reconnaissance by identifying live hosts and discovering open ports on your local network using Nmap. Understand the risks associated with exposed services.

What Was Done :-
-> Installed and used **Nmap** on Windows
-> Identified local IP range: 192.168.43.0/24
-> Ran a **TCP SYN scan** using:
  bash
  -> nmap -sS 192.168.43.107 -T4 -v
  
Takeaways :-
-> Gained hands-on experience with port scanning using Nmap.
-> Learned to identify and interpret common ports/services.
-> Understood potential security risks from exposed services.
-> Practiced documenting scan results for reporting.


Task 2: Analyze a Phishing Email Sample

Objective :-
Develop the skills to identify and analyze phishing emails by inspecting metadata, content, and behavioral tactics used in social engineering. Learn to recognize spoofed senders, malicious links, and emotional triggers to understand how attackers bypass technical defenses.

What Was Done :-
-> Analyzed a realistic phishing email sample claiming to be from "Microsoft Support".
-> Extracted and examined key email header fields:
  - `From`, `Reply-To`, `Return-Path`, `Received`, `SPF`, `DKIM`, `DMARC`
-> Identified red flags such as:
  - Spoofed domain (`micros0ft-securemail.com`)
  - Mismatched reply-to address
  - Failed SPF, DKIM, and DMARC
  - Suspicious IP address in Received headers
-> Inspected the email body and identified :-
  - Urgent/threatening language
  - Mismatched links (hover vs. destination)
  - Typos and lack of branding
-> Used tools like :-
  - [Google Header Analyzer](https://toolbox.googleapps.com/apps/messageheader/)
  - [MXToolbox Header Analyzer](https://mxtoolbox.com/EmailHeaders.aspx)
  - [VirusTotal](https://virustotal.com) / [urlscan.io](https://urlscan.io)

Skills Gained :-
-> Email header analysis
-> Link inspection and URL manipulation detection
-> SPF/DKIM/DMARC interpretation
-> Psychological and linguistic phishing tactics
-> Forensic-level SOC investigation workflow

Task 3: Vulnerability Scanning with Nessus Essentials
Overview :-
This task involved performing a vulnerability scan using **Tenable Nessus Essentials** to identify potential security issues on a target system.  
The goal was to understand the scanning process, analyze results, and extract key findings from the `.nessus` scan report.

Tools & Environment :-
-> Tool: Tenable Nessus Essentials
-> Operating System: Windows
-> Target: Localhost (127.0.0.1)
-> Report Format: `.nessus` (XML-based)

Task Steps
1. **Installation & Setup**
-> Installed **Nessus Essentials** and activated the free license.
-> Accessed the web interface at:
- Waited for **plugins to compile** before running scans.

2. **Creating a New Scan**
-> Navigated to:
-> Chose **Basic Network Scan** for local vulnerability checks.
-> Configured:
-> **Target:** `localhost`
-> **Schedule:** On-Demand
-> **Scan Type:** Vulnerability

3. **Running the Scan**
-> Started the **Localhost Vulnerability Scan**.
-> Nessus performed:
-> Service discovery
-> OS fingerprinting
-> Vulnerability checks
-> Misconfiguration checks

4. **Exporting Results**
-> Exported scan output in `.nessus` format for deeper analysis.
-> `.nessus` file is XML-based and contains:
-> Host information
-> Detected vulnerabilities
-> Plugin metadata
-> Detailed descriptions & solutions

Key Learnings :-
-> Nessus Essentials is powerful for **network vulnerability scanning** and **service enumeration**.
-> Even informational findings (severity 0) can be valuable to attackers if left unmonitored.
-> The `.nessus` file provides **raw structured data** for post-scan analysis and can be parsed for automated reporting.

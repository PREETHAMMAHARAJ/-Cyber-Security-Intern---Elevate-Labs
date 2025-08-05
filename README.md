# -Cyber-Security-Intern---Elevate-Labs
This repository showcases the work, tasks, and learning progress during my Cyber Security Internship at Elevate Labs. It includes hands-on labs, vulnerability assessments, network scans, incident response activities, and documentation of tools and techniques used in real-world cybersecurity scenarios.

Task 1: Scan Your Local Network for Open Ports
Objective
Learn how to perform basic network reconnaissance by identifying live hosts and discovering open ports on your local network using Nmap. Understand the risks associated with exposed services.

What Was Done
-> Installed and used **Nmap** on Windows
-> Identified local IP range: 192.168.43.0/24
-> Ran a **TCP SYN scan** using:
  bash
  -> nmap -sS 192.168.43.107 -T4 -v
  
Takeaways :
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

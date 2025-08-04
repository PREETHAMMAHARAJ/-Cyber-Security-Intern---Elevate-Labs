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

## Overview
This script automates the process of running an Nmap vulnerability scan on a target IP address. It obtains open ports and potential vulnerabilities on a system by using Nmap’s built-in scripts, making it a valuable tool for network audits and vulnerability assessments. The script also allows users to save the scan report in a text file.

## Key Features
- Automates vulnerability scanning on specified target IP
- Utilizes Nmap’s ‘-sV’ option to detect service versions and ‘–script vuln’ to check for known vulnerabilities
- Allows users to save results into a file with time-stamped information

## Installation

### System Requirements
- Python 3.9+ installed on your machine
- Nmap installed and added to the system PATH

### Steps:
1. Clone repository:

    '''git clone https://github.com/szachbagley/Security-Tools.git'''

2. Navigate to directory:

    '''cd Security-Tools/autoscan/'''


3. Run script using python:
   
    '''Without Saving Text File: py autoscan.py <target_ip>'''
   
    '''With Saving Text File: py autoscan.py <target_ip> [--save]'''

## Save Results to File
Use –save flag to save the results to a text file:

'''py autoscan.py 192.168.1.1 --save'''

## Example Usage
Run Nmap vulnerability scan on single IP address and save results as text file:

'''py autoscan.py 192.168.1.1 --save'''
 
## Example Output
Running Nmap Vulnerability scan on 192.168.1.1
Successful Scan! 

Scan Results: 

Starting Nmap 7.91 ( https://nmap.org ) at 2024-09-30 12:41 UTC 

Nmap scan report for 192.168.1.1 

Host is up (0.013s latency).

PORT STATE SERVICE VERSION

22/tcp open     ssh            OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) | vulners: 

| CVE-2018-15473: 5.0 MEDIUM 

|_ CVE-2020-15778: 7.8 HIGH 

Nmap done: 1 IP address (1 host up) scanned in 12.45 seconds

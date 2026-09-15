# LetsDefend Incident Report: SOC168 - Whoami Command Detected in Request Body

**Platform:** LetsDefend  
**Event ID:** 118  
**Date Completed:** September 15, 2026  
**Role:** SOC Analyst  
**Difficulty:** Easy  
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application)  
**Result:** True Positive  

## 📌 Incident Overview
Investigated a High severity alert triggered by a Command Injection attempt against an internal web server. The attacker sent POST requests containing operating system commands in the request body, attempting to execute arbitrary commands on the server.

## 🔍 Investigation Steps

### 1. Alert Analysis & Triage
Extracted the following details from the alert:
- **Attacker IP (Source):** `61.177.172.87` (External)
- **Target Web Server (Destination):** `172.16.17.16` (WebServer1004)
- **HTTP Request Method:** `POST`
- **Requested URL:** `https://172.16.17.16/video/`
- **Alert Trigger Reason:** Request Body Contains `whoami` string
- **Device Action:** `Allowed`

### 2. Threat Intelligence Verification
Verified the attacker's IP reputation using external threat intelligence tools. The IP originates from an external network and exhibits characteristics of a malicious actor attempting automated web exploitation.

### 3. Log Management & HTTP Analysis (Critical Evidence)
Queried Log Management for traffic between `61.177.172.87` and `172.16.17.16`. Found 5 POST requests, each attempting to execute a different command via the `c` parameter:

| Time | Payload (`?c=`) | HTTP Status | Response Size |
| :--- | :--- | :--- | :--- |
| 03:11:06 | `ls` | 200 OK | 1021 bytes |
| 03:12:00 | `whoami` | 200 OK | 912 bytes |
| 03:13:37 | `uname` | 200 OK | 910 bytes |
| 03:14:09 | `cat /etc/passwd` | 200 OK | 1321 bytes |
| 03:15:39 | `cat /etc/shadow` | 200 OK | 1501 bytes |

## 🧠 Attack Success Analysis
The attack was **Successful**. 

The key indicator was the **varying HTTP Response Sizes**. If the commands had failed, the server would have returned a generic error page with a consistent size. The fact that each command returned a different response size proves the server executed the commands and returned the output to the attacker.

**Critical Severity Note:** The attacker successfully executed `cat /etc/shadow` (1501 bytes), which contains encrypted password hashes. Access to this file indicates the attacker likely achieved high-privilege access on the server.

## 🛡️ Actions Taken
- **Containment:** Isolated the compromised web server (`WebServer1004`) via Endpoint Security to prevent further lateral movement and data exfiltration.
- **Documentation:** Extracted and documented the following IOCs:
    - Attacker IP: `61.177.172.87`
    - Target IP: `172.16.17.16`
    - Malicious Payloads: `?c=whoami`, `?c=cat /etc/passwd`, `?c=cat /etc/shadow`
- **Escalation:** Escalated the incident to Tier 2 for immediate forensic analysis and remediation, as a critical internal server was compromised and sensitive system files were accessed.

## 🧠 Key Takeaways & Lessons Learned
1. **Varying Response Sizes = Successful Command Injection:** In Command Injection attacks, a consistent response size often indicates a failed command (generic error page). Varying response sizes indicate the server is successfully executing the commands and returning unique output.
2. **Monitor for High-Risk Commands:** Commands like `cat /etc/passwd` and `cat /etc/shadow` should trigger immediate alerts. Access to `/etc/shadow` is a critical security breach indicating potential root-level compromise.
3. **Defense in Depth:** Web applications must sanitize all user input, especially parameters passed to system shells. Input validation and Web Application Firewalls (WAFs) are essential controls to prevent Command Injection.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*
# LetsDefend Incident Report: SOC170 - Passwd Found in Requested URL - Possible LFI Attack

**Platform:** LetsDefend  
**Event ID:** 120  
**Date Completed:** September 15, 2026  
**Role:** SOC Analyst  
**Difficulty:** Easy  
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application)  
**Result:** True Positive (Unsuccessful Attack)

## 📌 Incident Overview
Investigated a High severity alert triggered by a Local File Inclusion (LFI) attempt against an internal web server. The attacker attempted to read the Linux system's password file (`/etc/passwd`) via directory traversal.

## 🔍 Investigation Steps

### 1. Alert Analysis & Triage
Extracted the following details from the alert:
- **Attacker IP (Source):** `106.55.45.162` (External)
- **Target Web Server (Destination):** `172.16.17.13` (WebServer1006)
- **HTTP Request Method:** `GET`
- **Requested URL:** `https://172.16.17.13/?file=../../../../etc/passwd`
- **Alert Trigger Reason:** URL Contains `passwd`

### 2. Log Management & HTTP Analysis
Queried Log Management for traffic between `106.55.45.162` and `172.16.17.13`. Found one event for the malicious request.
- **HTTP Response Status:** `500 (Internal Server Error)`
- **HTTP Response Size:** `0 bytes`
- **Analysis:** The server crashed while processing the directory traversal payload. A `500` status code with a `0`-byte response confirms the server did not return the contents of `/etc/passwd`.

## 🧠 Attack Success Analysis
The attack was **Unsuccessful**. 

A successful LFI attack would have returned an `HTTP 200 OK` with a response body containing the contents of `/etc/passwd` (e.g., `root:x:0:0:...`). Instead, the server returned an error and no data, confirming the directory traversal attempt was blocked by the application's error handling.

## 🛡️ Actions Taken
- **Containment:** No containment required. The attack was unsuccessful, and no sensitive data was disclosed.
- **Documentation:** Extracted and documented the following IOCs:
    - Attacker IP: `106.55.45.162`
    - Target IP: `172.16.17.13`
    - LFI Payload: `../../../../etc/passwd`
- **Escalation:** Tier 2 escalation was **not required** because the attack from the Internet did not succeed.

## 🧠 Key Takeaways & Lessons Learned
1. **LFI Detection:** Directory traversal payloads (`../../../../`) targeting sensitive system files (like `/etc/passwd`) are a strong indicator of an LFI attack.
2. **HTTP Response Analysis:** The success of an LFI attack depends on whether the server returns the requested file's contents. A `500 Internal Server Error` with a `0`-byte response indicates the server blocked or crashed while processing the request.
3. **Input Validation:** Web applications must sanitize user input to prevent directory traversal attacks. Implementing proper file access controls is essential.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*
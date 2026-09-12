# LetsDefend Incident Report: SOC146 - Phishing Mail Detected (Excel 4.0 Macros)

**Platform:** LetsDefend  
**Date Completed:** September 12, 2026  
**Role:** SOC Analyst  
**Difficulty:** Easy  
**MITRE ATT&CK:** T1566 (Phishing)  
**Result:** True Positive  

## 📌 Incident Overview
Investigated a High severity alert triggered by an incoming email containing an Excel 4.0 Macro attachment. The alert was generated from a real phishing attack targeting a user within the organization.

## 🔍 Investigation Steps

### 1. Email Analysis (Initial Triage)
Extracted the following details from the alert:
- **Sender:** `trenton@tritowncomputers.com` (SMTP IP: `24.213.228.54`)
- **Recipient:** `lars@letsdefend.io`
- **Subject:** `RE: Meeting Notes`
- **Attachment Hash:** `11f44531fb088d31307d87b01e0ea6ff`
- **Device Action:** `Allowed` (Email was successfully delivered to the user's inbox)

### 2. Attachment Analysis
Analyzed the Excel attachment using a third-party sandbox. The sandbox confirmed the file was **Malicious**, utilizing Excel 4.0 Macros to execute a payload. The sandbox report yielded the Command & Control (C2) IP addresses the malware attempted to contact: `188.213.19.81` and `192.232.219.67`.

### 3. Execution Verification (The Critical Pivot)
Initially, I searched Log Management for the SMTP IP (`24.213.228.54`) and found no outbound connections, which could lead to a false conclusion that the file was "Not Opened." 

**Corrective Analysis:** The SMTP IP is the sender's mail server, not the C2 server. I pivoted my investigation:
1. **Log Management (Network Evidence):** Searched for the extracted **C2 IP (`188.213.19.81`)** and found a Proxy event showing the victim's device (`172.16.17.57` / `LarsPRD`) connecting to the C2 on **Port 443**. Crucially, the initiating process was **`excel.exe`**, confirming the malicious macro was executed and reached out to the C2 server.
2. **Endpoint Management (Host Evidence):** Inspected the `LarsPRD` device's Terminal History. The logs revealed the execution of `regsvr32`, a classic technique used by Excel 4.0 Macros to download and execute malicious payloads while bypassing security controls.

## 🛡️ Actions Taken
- **Containment:** Contained the compromised user machine (`LarsPRD`) via EDR to isolate it from the network and prevent lateral movement. Also deleted the malicious phishing email from the recipient's mailbox.
- **Documentation:** Extracted and documented IOCs (Sender Email, SMTP IP, C2 IPs, Victim IP, Attachment Hash).
- **Escalation:** Escalated the incident to Tier 2 for deeper forensic analysis and remediation, as an internal asset successfully executed malware and communicated with a C2 server.

## 🧠 Key Takeaways & Lessons Learned
1. **SMTP IP ≠ C2 IP:** The SMTP address is only used for the initial email delivery. When analyzing malware execution, you must pivot to the C2 address provided by the sandbox to search network logs effectively.
2. **Process Analysis is King:** A network connection to a suspicious IP is a red flag, but observing the *process* initiating that connection (e.g., `excel.exe` reaching out to a C2) is the definitive proof of execution.
3. **Verify Delivery vs. Execution:** An email being "Allowed" (delivered) does not mean the payload executed. However, it requires immediate investigation. If execution is confirmed, the host must be contained, not just the email deleted.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*

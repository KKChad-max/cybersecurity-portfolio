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
- **Device Action:** `Allowed` (Email was successfully delivered to the user's inbox)

### 2. Attachment Analysis
Analyzed the Excel attachment using a third-party sandbox. The sandbox confirmed the file was **Malicious**, utilizing Excel 4.0 Macros to execute a payload. The sandbox report yielded the Command & Control (C2) IP address the malware attempted to contact.

### 3. Execution Verification (The Critical Pivot)
Initially, I searched Log Management for the SMTP IP (`24.213.228.54`) and found no outbound connections, which could lead to a false conclusion that the file was "Not Opened." 

**Corrective Analysis:** The SMTP IP is the sender's mail server, not the C2 server. I pivoted my investigation:
1. **Log Management:** Searched for the extracted **C2 IP address** instead of the SMTP IP. Found evidence that the victim's device (`LarsPRD`) successfully communicated with the malicious C2 address.
2. **Endpoint Management:** Inspected the `LarsPRD` device's Browser History, Network Connections, and CMD History.
3. **Execution Confirmed:** The CMD History revealed the execution of `regsvr32`, a classic technique used by Excel 4.0 Macros to download and execute malicious payloads while bypassing security controls.

## 🛡️ Actions Taken
- **Containment:** Deleted the malicious phishing email from the recipient's mailbox.
- **Documentation:** Extracted and documented IOCs (Sender Email, SMTP IP, Recipient Email, C2 IP).
- **Analysis:** Confirmed endpoint compromise and identified the specific execution technique.

## 🧠 Key Takeaways & Lessons Learned
1. **SMTP IP ≠ C2 IP:** The SMTP address is only used for the initial email delivery. When analyzing malware execution, you must pivot to the C2 address provided by the sandbox to search network logs effectively.
2. **Pivot from Network to Endpoint:** Network logs (Log Management) confirm if traffic left the network, but Endpoint logs (Endpoint Management) confirm *how* the malware executed. Checking CMD history for suspicious child processes like `regsvr32.exe` or `powershell.exe` spawning from `excel.exe` is crucial.
3. **Verify Delivery vs. Execution:** An email being "Allowed" (delivered) does not mean the payload executed. However, it requires immediate investigation to determine if the user interacted with the malicious attachment.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*
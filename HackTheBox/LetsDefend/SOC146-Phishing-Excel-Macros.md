# LetsDefend Incident Report: SOC146 - Phishing Mail Detected (Excel 4.0 Macros)

**Platform:** LetsDefend  
**Event ID:** 93  
**Date Completed:** September 12, 2026  
**Role:** SOC Analyst  
**Severity:** High  
**Difficulty:** Easy  
**MITRE ATT&CK:** T1566 (Phishing), T1204.002 (Malicious File), T1059 (Command and Scripting Interpreter)  
**Result:** True Positive  

## 📌 Incident Overview
Investigated a High severity alert triggered by an incoming phishing email containing an Excel 4.0 Macro attachment. The investigation confirmed the malicious file was executed on the user's endpoint, established Command & Control (C2) communication, and performed system execution via `regsvr32`.

## 🔍 Investigation Steps

### 1. Email Analysis
Extracted the following details from the email:
- **Sender:** `trenton@tritowncomputers.com` (SMTP IP: `24.213.228.54`)
- **Recipient:** `lars@letsdefend.io`
- **Subject:** `RE: Meeting Notes`
- **Attachment Hash:** `11f44531fb088d31307d87b01e0ea6ff`
- **Device Action:** `Allowed` (Email was successfully delivered to the user's inbox)

### 2. Attachment Analysis (Sandbox)
Analyzed the Excel attachment using a third-party sandbox. The sandbox confirmed the file was **Malicious**, utilizing Excel 4.0 Macros to execute a payload. The sandbox report yielded the following C2 IP addresses:
- **Primary C2:** `188.213.19.81`
- **Secondary C2:** `192.232.219.67`

### 3. Execution Verification (Critical Pivot)
Initially, searching Log Management for the SMTP IP (`24.213.228.54`) yielded no outbound connections. This is a common trap—the SMTP IP is only used for email delivery.

**Corrective Analysis:**
1. **Log Management (Network Evidence):** Searched for the extracted **C2 IP (`188.213.19.81`)** and found a Proxy event showing the victim's device (`172.16.17.57` / `LarsPRD`) connecting to the C2 on **Port 443**. Crucially, the initiating process was **`excel.exe`**, confirming the malicious macro was executed and reached out to the C2 server.
2. **Endpoint Management (Host Evidence):** Inspected the `LarsPRD` device's Terminal History. The logs revealed the execution of `regsvr32`, a classic technique used by Excel 4.0 Macros to download and execute malicious payloads while bypassing security controls.
3. **Timeline Correlation:**
   - **13:11:18** – Phishing email sent.
   - **13:20:10** – `excel.exe` connected to C2 (`188.213.19.81`).
   - **13:47:53** – User last login.
   - **Confirmed Execution:** The macro executed and established C2 communication within 9 minutes of the email being delivered.

## 🧠 Attack Success Analysis
The attack was **Successful**. 

The endpoint logs proved that the malicious Excel file was opened and executed. The `excel.exe` process initiated a connection to the C2 server (`188.213.19.81`), and `regsvr32` was executed—a known technique for downloading and running secondary payloads. This confirms full endpoint compromise.

## 🛡️ Actions Taken
- **Containment:** Isolated the compromised endpoint (`LarsPRD` / `172.16.17.57`) via Endpoint Security. Deleted the malicious phishing email from the recipient's mailbox.
- **Documentation:** Extracted and documented the following IOCs:
    - Sender Email: `trenton@tritowncomputers.com`
    - SMTP IP: `24.213.228.54`
    - Attachment Hash: `11f44531fb088d31307d87b01e0ea6ff`
    - C2 IPs: `188.213.19.81`, `192.232.219.67`
    - Malicious Process: `excel.exe` → `regsvr32.exe`
    - Compromised Host: `172.16.17.57` (`LarsPRD`)
- **Escalation:** Escalated the incident to Tier 2 for malware analysis, forensic investigation, and remediation.

## 🧠 Key Takeaways & Lessons Learned
1. **SMTP IP ≠ C2 IP:** The SMTP address is only used for initial email delivery. When analyzing malware execution, you must pivot to the C2 address provided by the sandbox to search network logs effectively.
2. **Process Analysis is King:** A network connection to a suspicious IP is a red flag, but observing the *process* initiating that connection (e.g., `excel.exe` reaching out to a C2) is the definitive proof of execution.
3. **Regsvr32 Abuse:** `regsvr32.exe` is a legitimate Windows binary frequently abused by attackers to bypass application whitelisting and execute malicious scripts. Its execution from `excel.exe` is a strong indicator of Excel 4.0 macro exploitation.
4. **Verify Delivery vs. Execution:** An email being "Allowed" (delivered) does not mean the payload executed. However, if execution is confirmed, the host must be contained, not just the email deleted.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*

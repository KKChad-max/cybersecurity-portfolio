# LetsDefend Incident Report: SOC282 - Phishing Alert - Deceptive Mail Detected

**Platform:** LetsDefend  
**Event ID:** 257  
**Date Completed:** September 15, 2026  
**Role:** SOC Analyst  
**Severity:** Medium  
**MITRE ATT&CK:** T1566 (Phishing), T1566.002 (Spearphishing Link), T1059 (Command and Scripting Interpreter), T1204 (User Execution)  
**Result:** True Positive  

## 📌 Incident Overview
Investigated a Medium severity alert triggered by a deceptive phishing email containing a malicious ZIP attachment. The investigation confirmed the attachment was executed on the user's endpoint, established Command & Control (C2) communication, and performed system reconnaissance.

## 🔍 Investigation Steps

### 1. Email Analysis
Extracted the following details from the email:
- **Sender:** `free@coffeeshooop.com` (Spoofed domain)
- **Recipient:** `Felix@letsdefend.io`
- **Subject:** `Free Coffee Voucher`
- **SMTP IP:** `103.80.134.63`
- **Attachment:** `free-coffee.zip` (Password: `infected`)
- **Device Action:** `Allowed`

### 2. Endpoint Security Analysis (Deep Dive)
Navigated to Endpoint Security and analyzed the victim's machine (`Felix` / `172.16.20.151`):
- **Malicious Process:** `coffee.exe` 
- **Process ID (PID):** `6697`
- **Image Hash (SHA-256):** `CD903AD2211CF7D166646D75E57FB866000F4A3B870B5EC759929BE2FD81D334`
- **Child Processes:** `cmd.exe` spawned **7 child processes**, which executed the following reconnaissance commands:
  - `systeminfo`
  - `hostname`
  - `wmic logicaldisk get caption,description,providername`
  - `net user`
  - `tasklist /svc`
  - `ipconfig /all`
  - `route print`
- **Network Action:** Showed numerous outbound connections to external IPs, including the confirmed C2 server (`37.120.233.226`).

### 3. Log Management Analysis
Queried Log Management for the attacker's IP (`103.80.134.63`). Found the Exchange event confirming the email was delivered from `free@coffeeshooop.com` to `Felix@letsdefend.io`.

## 🧠 Attack Success Analysis
The attack was **Successful**. 

The endpoint logs proved that the malicious attachment (`coffee.exe`, PID 6697) was executed. The malware spawned `cmd.exe`, which then executed 7 reconnaissance commands. The process `coffee.exe` successfully established C2 communication with `37.120.233.226`.

## 🛡️ Actions Taken
- **Containment:** Isolated the compromised endpoint (`Felix` / `172.16.20.151`) via Endpoint Security to prevent lateral movement.
- **Documentation:** Extracted and documented the following IOCs:
    - Sender Email: `free@coffeeshooop.com`
    - SMTP IP: `103.80.134.63`
    - Malicious Attachment: `free-coffee.zip`
    - Malicious Process: `coffee.exe` (PID: `6697`)
    - Malware Hash (SHA-256): `CD903AD2211CF7D166646D75E57FB866000F4A3B870B5EC759929BE2FD81D334`
    - C2 IP: `37.120.233.226`
    - Compromised Host: `172.16.20.151`
- **Escalation:** Escalated the incident to Tier 2 for malware analysis, forensic investigation, and remediation.

## 🧠 Key Takeaways & Lessons Learned
1. **Phishing Can Lead to Full Compromise:** A deceptive email with a malicious attachment can result in full endpoint compromise and C2 communication.
2. **Process Lineage is Key:** Identifying the PID and Image Hash of the malicious process (`coffee.exe`) is essential for threat intelligence and endpoint blocking.
3. **Child Process Analysis Reveals Intent:** The 7 child processes spawned by `cmd.exe` revealed the attacker's goal: system reconnaissance. This is a classic post-exploitation tactic.
4. **C2 Communication Identification:** Identifying the specific process (`coffee.exe`) that communicates with a C2 server is crucial for understanding the malware's behavior and for future threat hunting.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*
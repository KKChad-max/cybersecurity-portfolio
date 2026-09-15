# LetsDefend Incident Report: SOC282 - Phishing Alert - Deceptive Mail Detected

**Platform:** LetsDefend  
**Event ID:** 257  
**Date Completed:** September 15, 2026  
**Role:** SOC Analyst  
**Severity:** Medium
**MITRE ATT&CK:** T1566 (Phishing), T1566.002 (Spearphishing Link), T1059 (Command and Scripting Interpreter), T1204 (User Execution)  
**Result:** True Positive  

## 📌 Incident Overview
Investigated a Medium severity alert triggered by a deceptive phishing email containing a malicious ZIP attachment. The investigation confirmed the attachment was executed on the user's endpoint, leading to system reconnaissance.

## 🔍 Investigation Steps

### 1. Email Analysis
Extracted the following details from the email:
- **Sender:** `free@coffeeshooop.com` (Spoofed domain)
- **Recipient:** `Felix@letsdefend.io`
- **Subject:** `Free Coffee Voucher`
- **SMTP IP:** `103.80.134.63`
- **Attachment:** `free-coffee.zip` (Password: `infected`)
- **Device Action:** `Allowed`

### 2. Endpoint Security Analysis (Critical Evidence)
Navigated to Endpoint Security and analyzed the victim's machine (`Felix` / `172.16.20.151`):
- **Terminal History:** Showed the execution of `cmd.exe` followed by a series of reconnaissance commands:
  - `systeminfo`
  - `hostname`
  - `wmic logicaldisk get caption,description,providername`
  - `net user`
  - `tasklist /svc`
  - `ipconfig /all`
  - `route print`
- **Network Action:** Showed numerous outbound connections to external IPs (e.g., `52.111.x.x`, `34.104.x.x`), indicating likely Command & Control (C2) communication.

### 3. Log Management Analysis
Queried Log Management for the attacker's IP (`103.80.134.63`). Found the Exchange event confirming the email was delivered from `free@coffeeshooop.com` to `Felix@letsdefend.io`.

## 🧠 Attack Success Analysis
The attack was **Successful**. 

The endpoint logs proved that the malicious attachment was executed. The attacker gained a foothold on the system and performed system discovery using native Windows commands. The network logs further suggest the malware was communicating with external C2 infrastructure.

## 🛡️ Actions Taken
- **Containment:** Isolated the compromised endpoint (`Felix` / `172.16.20.151`) via Endpoint Security to prevent lateral movement.
- **Documentation:** Extracted and documented the following IOCs:
    - Sender Email: `free@coffeeshooop.com`
    - SMTP IP: `103.80.134.63`
    - Malicious Attachment: `free-coffee.zip`
    - Compromised Host: `172.16.20.151`
- **Escalation:** Escalated the incident to Tier 2 for malware analysis, forensic investigation, and remediation.

## 🧠 Key Takeaways & Lessons Learned
1. **Phishing Can Lead to Compromise:** A deceptive email with a malicious attachment can result in full endpoint compromise if executed.
2. **Reconnaissance Commands are a Red Flag:** The execution of system discovery commands (`systeminfo`, `net user`, etc.) from a `cmd.exe` process is a strong indicator of post-exploitation activity.
3. **Network Connections Matter:** A large number of outbound connections to unknown public IPs from a user endpoint is a critical indicator of malware C2 communication.
4. **Endpoint Containment is Critical:** Isolating the compromised machine is the first and most important step to prevent the attacker from moving laterally or exfiltrating data.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*

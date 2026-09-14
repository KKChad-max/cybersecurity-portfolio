# 🛡️ LetsDefend — SOC Analyst Incident Reports

Welcome to my LetsDefend portfolio section. 

LetsDefend (now part of Hack The Box) is a hands-on blue team training platform that simulates real-world Security Operations Center (SOC) environments. This folder contains my incident reports and write-ups from various alerts, demonstrating my ability to triage, investigate, contain, and document security events.

## 📂 Completed Investigations

| Alert Name | Severity | Type | MITRE ATT&CK | Status | Report Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SOC146 - Phishing Mail Detected (Excel 4.0 Macros)** | High | Exchange | T1566 | ✅ True Positive | [View Report](./SOC146-Phishing-Excel-Macros.md) |
| **SOC165 - Possible SQL Injection Payload Detected** | High | Web Attack | T1190 | ✅ True Positive | [View Report](./SOC165-SQL-Injection.md) |
| **SOC166 - Javascript Code Detected in Requested URL** | Medium | Web Attack | T1190 | ✅ True Positive | [View Report](./SOC166-JavaScript-XSS.md) |

*(More reports will be added as I progress through the platform.)*

## 🛠️ Skills Demonstrated
Through these investigations, I have practiced and applied the following SOC Analyst skills:

- **Alert Triage:** Assessing severity and determining the validity of security alerts.
- **Phishing Analysis:** Investigating email headers, sender/recipient addresses, SMTP IPs, and malicious attachments.
- **Web Attack Analysis:** Detecting and analyzing SQL Injection and Cross-Site Scripting (XSS) attempts, decoding URL payloads, and understanding HTTP status codes (e.g., differentiating between successful attacks and blocked attempts via `200 OK`, `302 Redirect`, and `500 Internal Server Error` responses).
- **Threat Intelligence:** Utilizing third-party tools like VirusTotal and AbuseIPDB to validate the reputation of external IP addresses.
- **Sandbox Analysis:** Using third-party sandboxes to safely detonate malware and extract Indicators of Compromise (IOCs), including Command & Control (C2) addresses.
- **Log Management & Network Analysis:** Searching network and web logs for malicious traffic, analyzing HTTP response sizes, and confirming attack success or failure.
- **Endpoint Security & Investigation:** Analyzing endpoint logs, CMD history, and process creation to identify execution techniques (e.g., `regsvr32` spawned by Excel). Performing endpoint containment to isolate compromised devices.
- **Incident Response:** Performing containment actions (deleting malicious emails, isolating compromised servers) and documenting findings.
- **MITRE ATT&CK Framework:** Mapping alert activity to specific tactics and techniques (e.g., T1566 for Phishing, T1190 for Exploit Public-Facing Application).
- **Escalation Procedures:** Understanding when to escalate to Tier 2 (e.g., when an attack from the internet is successful and compromises an internal asset).

## 📝 Report Structure
Each report in this folder follows a standardized incident response format:
1. **Incident Overview:** The who, what, when, and where.
2. **Investigation Steps:** The methodology used to analyze the alert (Alert Analysis, Threat Intel, Log Management, HTTP Analysis).
3. **Actions Taken:** Containment, documentation, and escalation steps.
4. **Key Takeaways:** Lessons learned and corrective pivots made during the investigation (e.g., avoiding the "200 OK" trap).

---
*These write-ups are generated from simulated environments for educational and portfolio purposes.*
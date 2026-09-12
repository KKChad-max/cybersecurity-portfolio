# 🛡️ LetsDefend — SOC Analyst Incident Reports

Welcome to my LetsDefend portfolio section. 

LetsDefend (now part of Hack The Box) is a hands-on blue team training platform that simulates real-world Security Operations Center (SOC) environments. This folder contains my incident reports and write-ups from various alerts, demonstrating my ability to triage, investigate, contain, and document security events.

## 📂 Completed Investigations

| Alert Name | Severity | Type | MITRE ATT&CK | Status | Report Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SOC146 - Phishing Mail Detected (Excel 4.0 Macros)** | High | Exchange | T1566 | ✅ True Positive | [View Report](./SOC146-Phishing-Excel-Macros.md) |

*(More reports will be added as I progress through the platform.)*

## 🛠️ Skills Demonstrated
Through these investigations, I have practiced and applied the following SOC Analyst skills:

- **Alert Triage:** Assessing severity and determining the validity of security alerts.
- **Phishing Analysis:** Investigating email headers, sender/recipient addresses, SMTP IPs, and malicious attachments.
- **Sandbox Analysis:** Using third-party sandboxes to safely detonate malware and extract Indicators of Compromise (IOCs), including Command & Control (C2) addresses.
- **Log Management & Network Analysis:** Searching network logs for outbound C2 traffic to confirm execution.
- **Endpoint Security & Investigation:** Analyzing endpoint logs, CMD history, and process creation to identify execution techniques (e.g., `regsvr32` spawned by Excel).
- **Incident Response:** Performing containment actions (like deleting malicious emails) and documenting findings.
- **MITRE ATT&CK Framework:** Mapping alert activity to specific tactics and techniques (e.g., T1566 for Phishing).

## 📝 Report Structure
Each report in this folder follows a standardized incident response format:
1. **Incident Overview:** The who, what, when, and where.
2. **Investigation Steps:** The methodology used to analyze the alert.
3. **Actions Taken:** Containment and remediation steps.
4. **Key Takeaways:** Lessons learned and corrective pivots made during the investigation.

---
*These write-ups are generated from simulated environments for educational and portfolio purposes.*
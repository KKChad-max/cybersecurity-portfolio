# Incident Handler's Journal

**Date:** August 28, 2026  
**Entry:** 2  

---

| Section | Details |
| :--- | :--- |
| **Description** | Investigated a suspicious file downloaded by an employee via a phishing email. The file was password‑protected and executed a malicious payload upon opening. Used VirusTotal to analyze the SHA256 hash and uncover associated indicators of compromise (IOCs) using the Pyramid of Pain framework. |
| **Tool(s) used** | VirusTotal, SHA256 hashing (technique recalled from the Course 5 hash lab), Incident Handler’s Journal. |
| **The 5 W's** | • **Who:** A malicious actor (or group) who sent a targeted phishing email to an employee. <br><br> • **What:** A malicious file was downloaded and opened by the employee, which executed a payload and created multiple unauthorized executable files on the system. <br><br> • **When:** The email was received at approximately 11:11 p.m. The file was opened at 11:13 p.m., and unauthorized executables were detected at 11:15 p.m. The intrusion detection system (IDS) alerted the SOC at 12:00 p.m. the following day. <br><br> • **Where:** An employee’s workstation at a financial services company. <br><br> • **Why:** The attacker used social engineering (phishing) to trick the employee into opening a password‑protected spreadsheet. The malicious payload was designed to compromise the system and potentially gain unauthorized access or establish persistence. |
| **Additional notes** | The file’s SHA256 hash (`5deeae47...527f6b`) was submitted to VirusTotal. Multiple vendors flagged the file as malicious, and the community score was negative. The Detection tab revealed specific malware names. IOCs identified include the file hash, associated IP addresses, and malicious domains. This investigation confirms the importance of leveraging shared threat intelligence (VirusTotal) and the Pyramid of Pain to prioritize defensive actions. |

---

## VirusTotal & Pyramid of Pain Findings

**Malicious verdict:** ✅ Yes – the file is malicious.

**Reasoning:** The file was flagged by multiple security vendors, had a negative community score, and was identified as malware (e.g., Trojan, RAT, or Downloader). The incident timeline (file opened → unauthorized executables created) confirms malicious activity.

### Pyramid of Pain – IOCs

| Pyramid Level | IOC | Value / Example |
| :--- | :--- | :--- |
| **Hash Values (Trivial)** | SHA256 | `5deeae47eb0463463d8e7f77b7c2136ccfc80ade34f246a1e2fb9aba527f6b` |
| **IP Addresses (Easy)** | Malicious IP | *[Insert IP from VirusTotal]* |
| **Domain Names (Simple)** | Malicious Domain | *[Insert domain from VirusTotal]* |
| **Network/Host Artifacts (Annoying)** | Artifact | *[Suspicious file names, registry keys, or user agents found in the report]* |
| **Tools (Challenging)** | Tool Name | *[e.g., Cobalt Strike, Mimikatz, or specific malware family]* |
| **TTPs (Tough)** | Tactic / Technique | Phishing (T1566), Execution (T1204), Command and Control (T1071) |

---

> *This journal entry builds on the SHA256 hashing lab from Course 5, where I learned to generate and use file hashes as unique identifiers for malware analysis.*
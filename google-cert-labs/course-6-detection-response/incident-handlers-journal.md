# Incident Handler's Journal

**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 6  

---

## Instructions

This journal documents my hands-on experience with incident detection, analysis, and response throughout Course 6: Sound the Alarm. Each entry captures a specific security scenario, the tools used, and the 5 W's of the incident.

---

## Entry 1: Ransomware Incident at Healthcare Clinic

| Section | Details |
| :--- | :--- |
| **Date** | August 25, 2026 |
| **Entry** | 1 |
| **Description** | Ransomware incident at a small U.S. healthcare clinic. Employees were locked out of files, a ransom note was displayed, and business operations were disrupted. This incident involved the Detection and Analysis and Containment phases of the NIST Incident Response Lifecycle. |
| **Tool(s) used** | None specifically used in this scenario, but relevant tools include: SIEM, IDS/IPS, email filtering, antivirus, and endpoint detection and response (EDR). |
| **Who?** | An organized group of unethical hackers known to target healthcare and transportation organizations. |
| **What?** | Ransomware attack that encrypted critical patient files and demanded payment for the decryption key. |
| **When?** | Tuesday at approximately 9:00 a.m. |
| **Where?** | A small U.S. healthcare clinic specializing in primary-care services. |
| **Why?** | The attackers used targeted phishing emails with malicious attachments. An employee downloaded the attachment, which installed malware and allowed the attackers to deploy ransomware. |
| **Additional notes** | The clinic was forced to shut down all computer systems and contact external organizations for assistance. This incident highlights the importance of security awareness training to prevent phishing attacks, regular data backups, and having an incident response plan in place. |

---

## Entry 2: VirusTotal Investigation & Pyramid of Pain

| Section | Details |
| :--- | :--- |
| **Date** | August 28, 2026 |
| **Entry** | 2 |
| **Description** | Investigated a suspicious file downloaded by an employee via a phishing email. The file was password-protected and executed a malicious payload upon opening. Used VirusTotal to analyze the SHA256 hash and uncover associated IOCs using the Pyramid of Pain framework. This activity focused on the Detection and Analysis phase. |
| **Tool(s) used** | VirusTotal, SHA256 hashing, Pyramid of Pain framework. |
| **Who?** | A malicious actor (or group) who sent a targeted phishing email to an employee. |
| **What?** | A malicious file (`bfsvc.exe`) was downloaded and opened by the employee, executing a payload and creating multiple unauthorized executable files on the system. |
| **When?** | Email received at 11:11 p.m. File opened at 11:13 p.m. Unauthorized executables detected at 11:15 p.m. IDS alerted the SOC at 12:00 p.m. the following day. |
| **Where?** | An employee’s workstation at a financial services company. |
| **Why?** | The attacker used social engineering (phishing) to trick the employee into opening a password-protected spreadsheet. The malicious payload was designed to compromise the system and potentially establish persistence. |
| **Additional notes** | The file’s SHA256 hash (`54e6ea47...527f6b`) was submitted to VirusTotal. 53 out of 70 security vendors flagged the file as malicious. The file was identified as Trojan.Flagpro / Fragtor. IOCs identified include the file hash, associated IP addresses (`108.177.126.100`), and a malicious domain (`a.sinkhole.yourtrap.com`). The Pyramid of Pain framework helped prioritize defensive actions. |

---

## Entry 3: Phishing Incident Response – Playbook Escalation

| Section | Details |
| :--- | :--- |
| **Date** | August 28, 2026 |
| **Entry** | 3 |
| **Description** | Responded to a phishing alert (Ticket A‑2703) using the organization's Phishing Playbook. Investigated a malicious email containing a password-protected attachment (`bfsvc.exe`). Verified the file hash as malicious via VirusTotal and escalated the ticket to a Level‑2 SOC analyst for containment and further investigation. This activity involved the Containment, Eradication, and Recovery phase. |
| **Tool(s) used** | Phishing Playbook (Version 1.0), VirusTotal, Alert Ticket System. |
| **Who?** | A malicious actor posing as "Clyde West" from "Def Communications" (sender IP: `114.114.114.114`). |
| **What?** | A phishing email with a password-protected malicious attachment (`bfsvc.exe`). The attachment executed a payload when the employee opened it, generating unauthorized executable files on the system. |
| **When?** | The email was sent on Wednesday, July 20, 2022, at 09:30 AM. The employee downloaded and opened the file shortly after. |
| **Where?** | The incident occurred at an employee’s workstation at the financial services company. |
| **Why?** | The attacker used social engineering (phishing) and a password-protected file to bypass email filters and trick the employee into executing malware. The goal was likely unauthorized access, data exfiltration, or establishing persistence. |
| **Additional notes** | The malicious file hash was flagged by 53/70 VirusTotal vendors. Red flags included: suspicious sender domain (`76tgyuhh6tgftrt7tg.su`), generic subject line, and password-protected attachment. The ticket was escalated to Level‑2 for quarantine, IP/domain blocking, and malware removal. |

---

## Entry 4: Final Report Review – Data Breach Analysis

| Section | Details |
| :--- | :--- |
| **Date** | August 28, 2026 |
| **Entry** | 4 |
| **Description** | Reviewed a final incident report for a data breach that occurred at a mid‑sized retail company. The breach affected over 50,000 customer records and involved the theft of PII and financial data. The root cause was a vulnerability in the e‑commerce web application that allowed forced browsing. This activity focused on the Post‑Incident Activity phase. |
| **Tool(s) used** | Final Incident Report, Incident Handler’s Journal. |
| **Who?** | A malicious attacker who exploited a web application vulnerability. |
| **What?** | Unauthorized access to customer PII and financial information via forced browsing. Approximately 50,000 records were affected. |
| **When?** | The incident was discovered on December 28, 2022, at 7:20 p.m. PT. The initial threat email was received on December 22, 2022. |
| **Where?** | The company’s e‑commerce web application, specifically the purchase confirmation page URL structure. |
| **Why?** | The attacker modified order numbers in the URL to access unauthorized customer transaction data. The web application lacked proper access controls and input validation. |
| **Additional notes** | The attacker initially demanded $25,000, then increased the demand to $50,000. The company offered free identity protection services to affected customers. Recommendations included routine vulnerability scans, penetration testing, and implementing access control mechanisms (allow‑listing URLs, restricting access to authenticated users). |

---

## Reflections / Notes

**1. Were there any specific activities that were challenging for you? Why or why not?**

The most challenging activity was the Pyramid of Pain and VirusTotal investigation. Mapping the IOCs to the different levels of the pyramid required careful analysis and a solid understanding of how attackers operate. It also required interpreting the VirusTotal report correctly and extracting the right pieces of information (IPs, domains, file hashes) to build a complete picture of the threat.

**2. Has your understanding of incident detection and response changed since taking this course?**

Yes, significantly. I now understand that incident response is not just about reacting to alerts but involves a structured lifecycle – from preparation and detection to containment, eradication, and post‑incident review. I also learned the importance of documentation and how tools like playbooks, SIEMs, and threat intelligence platforms (like VirusTotal) work together to support a coordinated response.

**3. Was there a specific tool or concept that you enjoyed the most?**

I enjoyed working with Suricata and the `jq` command the most. Writing custom rules and then seeing them trigger alerts on network traffic made the detection process feel tangible and rewarding. Using `jq` to parse the `eve.json` logs was also a highlight because it showed how to efficiently extract meaningful data from large log files – a critical skill for any SOC analyst.
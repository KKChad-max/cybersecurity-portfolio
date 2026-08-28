# Phishing Incident Response – Alert Ticket Investigation

**Date:** August 28, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 6  

---

## Scenario

A level‑one SOC analyst at a financial services company received a phishing alert about a suspicious file being downloaded on an employee's computer. The file's SHA256 hash was previously verified as malicious using VirusTotal (53/70 vendors flagged it). Following the organization's Phishing Playbook, I investigated the alert, documented my findings, and determined the appropriate next steps.

---

## Phishing Playbook – Steps Followed

| Step | Action | Outcome |
| :--- | :--- | :--- |
| **Step 1** | Received phishing alert. | Alert ticket A-2703 opened. |
| **Step 2** | Evaluated the alert details. | Identified suspicious sender, subject line, and attachment. |
| **Step 3.0** | Does the email contain links or attachments? | ✅ Yes – the email contains an attachment (`bfsvc.exe`). |
| **Step 3.1** | Are the links or attachments malicious? | ✅ Yes – the file hash was flagged as malicious by 53/70 VirusTotal vendors. |
| **Step 3.2** | Update ticket and escalate. | Ticket escalated to Level‑2 SOC analyst. |

---

## Alert Ticket Summary

| Field | Details |
| :--- | :--- |
| **Ticket ID** | A-2703 |
| **Alert Message** | SERVER-MAIL Phishing attempt – possible download of malware |
| **Severity** | Medium |
| **Details** | The user may have opened a malicious email and opened attachments or clicked links. |
| **Ticket Status** | **Escalated** |

---

## Ticket Comments

> **Investigation Summary:**  
> The email originated from `Def Communications` (sender IP: `114.114.114.114`) and was sent to `hr@inergy.com`. The subject line, *"Re: Infrastructure Engineer role"*, was designed to appear legitimate. The email contained an attachment named `bfsvc.exe`, which was password‑protected (password provided in the email).

> **Malicious Verification:**  
> The SHA256 hash of the attachment (`54e6ea47eb04634d3e87fd7787e2136ccfbc80ade34f246a12cf93bab527f6b`) was submitted to VirusTotal and flagged as malicious by **53 out of 70 security vendors**. It was identified as **Trojan.Flagpro / Fragtor** and exhibited behaviors such as `detect-debug-environment`, `long-sleeps`, `service-scan`, and `spreader`.

> **Decision:**  
> Based on the playbook (Step 3.2), this ticket is **escalated** to a Level‑2 SOC analyst for further investigation and containment. The employee's workstation should be quarantined, and the malicious file should be removed.

---

## 5 W's of the Incident

| W | Details |
| :--- | :--- |
| **Who** | A malicious actor (or group) posing as `Clyde West` from `Def Communications`. |
| **What** | A phishing email containing a password‑protected malicious attachment (`bfsvc.exe`). The attachment executed a payload when opened. |
| **When** | The email was sent on **Wednesday, July 20, 2022, at 09:30 AM**. The employee opened the file shortly after. |
| **Where** | The incident occurred at the employee's workstation at the financial services company. |
| **Why** | The attacker used social engineering (phishing) and a password‑protected file to trick the employee into downloading and executing malware. The goal was likely unauthorized access, data exfiltration, or establishing persistence. |

---

## Why This Alert Was Escalated (2–3 Reasons)

1. **The attachment was confirmed malicious** – The SHA256 hash was flagged by 53/70 VirusTotal vendors and identified as Trojan.Flagpro / Fragtor, indicating a high‑confidence malicious verdict.

2. **The email exhibited phishing red flags** – The sender's domain was suspicious (`76tgyuhh6tgftrt7tg.su`), the subject line was generic, and the password‑protected attachment is a common phishing tactic.

3. **Potential impact** – The employee opened the file, which may have already executed malicious code on their workstation, posing a risk of data compromise, lateral movement, or further infection.

---

## Next Steps

- Quarantine the affected workstation.
- Block the malicious IP (`114.114.114.114`) and domain at the firewall.
- Remove the malicious file (`bfsvc.exe`) from the system.
- Conduct a security awareness briefing on phishing and password‑protected attachments.
- Escalate to the Level‑2 SOC team for further incident response and containment.



## References

- VirusTotal Report: `54e6ea47eb04634d3e87fd7787e2136ccfbc80ade34f246a12cf93bab527f6b`
- Phishing Playbook – Version 1.0
- MITRE ATT&CK: T1566 (Phishing), T1204 (User Execution), T1071 (Application Layer Protocol)

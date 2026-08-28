# Incident Handler's Journal

**Date:** August 28, 2026  
**Entry:** 3  

---

| Section | Details |
| :--- | :--- |
| **Description** | Responded to a phishing alert (Ticket A‑2703) using the organization's Phishing Playbook. Investigated a malicious email containing a password‑protected attachment (`bfsvc.exe`). Verified the file hash as malicious via VirusTotal and escalated the ticket to a Level‑2 SOC analyst for containment and further investigation. |
| **Tool(s) used** | Phishing Playbook (Version 1.0), VirusTotal, Alert Ticket System, Incident Handler’s Journal. |
| **The 5 W's** | • **Who:** A malicious actor posing as "Clyde West" from "Def Communications" (sender IP: `114.114.114.114`). <br><br> • **What:** A phishing email with a password‑protected malicious attachment (`bfsvc.exe`). The attachment executed a payload when the employee opened it, generating unauthorized executable files on the system. <br><br> • **When:** The email was sent on **Wednesday, July 20, 2022, at 09:30 AM**. The employee downloaded and opened the file shortly after. <br><br> • **Where:** The incident occurred at an employee’s workstation at the financial services company. <br><br> • **Why:** The attacker used social engineering (phishing) and a password‑protected file to bypass email filters and trick the employee into executing malware. The goal was likely unauthorized access, data exfiltration, or establishing persistence. |
| **Additional notes** | The malicious file hash (`54e6ea47eb04634d3e87fd7787e2136ccfbc80ade34f246a12cf93bab527f6b`) was flagged by 53/70 VirusTotal vendors and identified as Trojan.Flagpro / Fragtor. The phishing playbook guided the escalation process. Key red flags included: suspicious sender domain (`76tgyuhh6tgftrt7tg.su`), generic subject line, and the use of a password‑protected attachment – a common phishing tactic. The ticket was escalated to Level‑2 for quarantine, IP/domain blocking, and malware removal. |

---

## Reflection

This incident reinforced the importance of following a structured playbook during incident response. The Phishing Playbook provided clear, step‑by‑step guidance – from evaluating the alert to escalating the ticket – ensuring a consistent and timely response. Key takeaways:

- **Verification is critical:** The VirusTotal hash analysis confirmed the attachment was malicious, removing any ambiguity.
- **Red flags are actionable:** Suspicious sender domains, generic subject lines, and password‑protected attachments are strong indicators of phishing.
- **Escalation is not failure:** Escalating to a Level‑2 analyst ensures that the incident receives the appropriate level of attention and containment.
- **Documentation matters:** Updating the alert ticket with clear findings and rationale supports the investigation and helps other analysts understand the incident.

> The ability to follow a playbook, use threat intelligence tools, and escalate appropriately is essential for any SOC analyst. This investigation demonstrates readiness to handle real‑world phishing incidents.

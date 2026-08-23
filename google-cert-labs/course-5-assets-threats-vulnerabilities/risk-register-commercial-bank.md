# Risk Register: Commercial Bank

**Date:** August 23, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 5  

---

## Operational Environment

The bank is located in a coastal area with low crime rates. Many people and systems handle the bank’s data – 100 on-premise employees and 20 remote employees. The customer base includes 2,000 individual accounts and 200 commercial accounts. The bank’s services are marketed by a professional sports team and ten local businesses in the community. Strict financial regulations require the bank to secure their data and funds, such as having enough cash available each day to meet Federal Reserve requirements.

---

## Risk Register

| Asset | Risk(s) | Description | Likelihood | Severity | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Funds | Business email compromise | An employee is tricked into sharing confidential information. | 3 | 3 | **9** |
| Funds | Compromised user database | Customer data is poorly encrypted. | 3 | 3 | **9** |
| Funds | Financial records leak | A database server of backed up data is publicly accessible. | 2 | 3 | **6** |
| Funds | Theft | The bank’s safe is left unlocked. | 1 | 3 | **3** |
| Funds | Supply chain disruption | Delivery delays due to natural disasters. | 1 | 3 | **3** |

---

## Notes: How Security Events Are Possible

The bank's operating environment presents several vulnerabilities that could lead to security events:

- **High volume of data handlers:** With 100 on-premise and 20 remote employees, there are many potential points of human error, such as falling for phishing emails (Business Email Compromise) or failing to follow encryption protocols.
- **Remote workforce:** Remote employees increase the attack surface, as they may access sensitive systems from less secure home networks, making them more susceptible to credential theft or unauthorized access.
- **Regulatory pressure:** Strict financial regulations mean that any data breach or financial record leak could result in heavy fines, reputational damage, and loss of customer trust.
- **Public visibility:** The bank's association with a professional sports team and local businesses increases its public profile, making it a more attractive target for attackers seeking media attention or financial gain.
- **Geographic location:** The coastal location introduces a moderate risk of natural disasters (e.g., hurricanes), which could disrupt supply chains and affect the bank's ability to maintain required cash reserves.

---

## Risk Scoring Method

**Formula:** Likelihood × Severity = Priority Score

| Risk Score | Priority Level |
| :--- | :--- |
| 1–2 | Low – Monitor but no immediate action required |
| 3–4 | Medium – Plan remediation within 3–6 months |
| 6 | High – Address within 30–60 days |
| 9 | Critical – Address within 7–14 days |

---

## Summary of Findings

| Priority | Risk | Action Timeline |
| :--- | :--- | :--- |
| **9 (Critical)** | Business email compromise | Address within **7–14 days** – implement phishing-resistant MFA and employee security awareness training. |
| **9 (Critical)** | Compromised user database | Address within **7–14 days** – enforce strong encryption for customer data at rest and in transit, and conduct a database security audit. |
| **6 (High)** | Financial records leak | Address within **30–60 days** – review access controls to backup servers, ensure they are not publicly accessible, and implement logging and monitoring. |
| **3 (Medium)** | Theft | Plan remediation within **3–6 months** – review physical security controls, ensure the safe is locked, and implement dual‑custody procedures for cash handling. |
| **3 (Medium)** | Supply chain disruption | Plan remediation within **3–6 months** – develop a business continuity plan and establish alternate supply chain routes to mitigate natural disaster risks. |

---

## Reflection

This risk assessment highlights the importance of prioritizing resources based on the potential impact of each risk. Business Email Compromise and a Compromised User Database both received critical scores because they directly threaten the bank's financial assets, customer trust, and regulatory compliance. The bank's operational environment – with a large workforce, remote employees, and strict regulations – amplifies these risks and reinforces the need for robust security controls, employee training, and proactive risk management.

---

## Next Steps

- **Immediate (7–14 days):**
  - Deploy MFA for all employee accounts.
  - Enforce encryption for all customer data.
  - Conduct a security awareness training session on phishing and social engineering.

- **Short-term (30–60 days):**
  - Review and restrict access to backup servers.
  - Implement logging and monitoring for sensitive database access.

- **Long-term (3–6 months):**
  - Develop and test a business continuity plan for supply chain disruptions.
  - Review physical security controls for cash handling and storage.
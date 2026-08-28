# Incident Final Report: Data Breach – E‑Commerce Web Application

**Date of Report:** August 28, 2026  
**Incident Date:** December 28, 2022  
**Report Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 6  

---

## Executive Summary

On **December 28, 2022, at approximately 7:20 p.m. PT**, the organization experienced a security incident involving unauthorized access to customer personal identifiable information (PII) and financial data. The attacker exploited a vulnerability in the e‑commerce web application to perform a **forced browsing attack**, accessing approximately **50,000 customer records**. The financial impact is estimated at **$100,000** in direct costs and potential revenue loss. The incident has been closed, and a thorough investigation has been conducted.

**Key findings:**
- The root cause was a vulnerable web application that allowed URL manipulation.
- The attacker demanded a ransom of $50,000 after initially requesting $25,000.
- The organization implemented access control mechanisms and routine vulnerability scans to prevent recurrence.

---

## Timeline

| Date / Time | Event |
| :--- | :--- |
| **Dec 22, 2022 – 3:13 p.m. PT** | An employee received an email from an external sender claiming to have stolen customer data. The sender demanded **$25,000** in cryptocurrency. The employee assumed it was spam and deleted it. |
| **Dec 28, 2022** | The same employee received a second email from the same sender, now including **a sample of stolen customer data** and an increased demand of **$50,000**. |
| **Dec 28, 2022 – 7:20 p.m. PT** | The employee notified the security team. The investigation began immediately. |
| **Dec 28 – Dec 31, 2022** | The security team focused on determining how the data was stolen and the extent of the theft. |
| **Jan 2023** | The organization disclosed the breach to affected customers, offered free identity protection services, and implemented remediation measures. |

---

## Investigation

The security team traveled on‑site to investigate the alert. The root cause was identified as a **vulnerability in the e‑commerce web application** that allowed the attacker to perform a **forced browsing attack**.

### How the Attack Worked
- The attacker manipulated the **order number** in the URL string of the purchase confirmation page.
- By sequentially modifying the order number, the attacker accessed **thousands of customer purchase confirmation pages** without authorization.
- The attacker collected and exfiltrated customer PII and financial data.

### Evidence Collected
- **Web server access logs** showed an exceptionally high volume of sequentially listed customer orders from a single log source.
- This pattern confirmed that the attacker systematically accessed customer order pages.

---

## Response and Remediation

The organization took the following actions:

1. **Customer Notification** – Collaborated with the public relations department to disclose the data breach to affected customers.
2. **Identity Protection** – Offered **free identity protection services** to all customers affected by the incident.
3. **Log Analysis** – Reviewed web server logs to confirm the attack vector and identify the source.
4. **Access Control Implementation** – Implemented allow‑listing to restrict access to a specified set of URLs and automatically block requests outside that range.
5. **Authentication Enforcement** – Ensured that only authenticated users are authorized to access content.

---

## Lessons Learned

A **lessons learned meeting** was conducted with all involved parties. Key insights included:

- **Timely reporting matters** – The initial threat email on December 22 was ignored. If it had been reported earlier, the breach might have been contained sooner.
- **Web application vulnerabilities are high‑risk** – URL manipulation vulnerabilities must be addressed during development and testing.
- **Proactive security controls are essential** – Routine vulnerability scans and penetration testing would have identified the vulnerability before exploitation.

---

## Recommendations

To prevent future recurrences, the organization is implementing the following actions:

| Recommendation | Description |
| :--- | :--- |
| **Routine Vulnerability Scans** | Perform regular automated scans to identify and remediate vulnerabilities in web applications. |
| **Penetration Testing** | Conduct annual penetration tests to simulate real‑world attacks and identify weaknesses. |
| **Access Control Mechanisms** | Implement allow‑listing to restrict access to specified URLs. Block all requests outside this range. |
| **Authentication Enforcement** | Ensure that only authenticated users are authorized to access content. |
| **Employee Security Awareness Training** | Train employees to recognize and report suspicious emails (phishing, extortion attempts). |
| **Incident Response Plan Updates** | Review and update the incident response plan to include faster escalation for extortion emails. |

---

## Conclusion

This incident highlights the critical importance of **secure web application development**, **proactive vulnerability scanning**, and **timely incident reporting**. The organization has taken significant steps to remediate the vulnerability and strengthen its security posture. By implementing the recommendations outlined in this report, the organization aims to prevent similar incidents in the future and protect customer data.

---

> *This final report was prepared as part of the Google Cybersecurity Certificate – Course 6: Sound the Alarm – Detection and Response.*
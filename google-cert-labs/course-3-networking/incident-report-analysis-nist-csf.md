# Incident Report Analysis: NIST CSF

**Date:** August 16, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 3  

---

| Section | Details |
| :--- | :--- |
| **Summary** | A Denial of Service (DoS) attack compromised the company's internal network for approximately two hours. The attack was executed by a malicious actor who exploited an unconfigured firewall to send a massive flood of ICMP pings into the network. This overwhelmed the network services, causing them to stop responding and blocking normal internal traffic. The incident management team responded by blocking incoming ICMP packets, taking non-critical services offline, and restoring critical network services. |
| **Identify** | The security event was identified through network monitoring alerts indicating an unusual spike in incoming ICMP traffic. The internal network and firewall were the primary systems affected. The root vulnerability was an unconfigured firewall that lacked rules to filter or rate-limit ICMP packets. Business operations were disrupted for two hours, impacting internal communication and service delivery. |
| **Protect** | To prevent future attacks, the organization has implemented: <br><br> - **Firewall rule updates:** Rate-limiting on incoming ICMP packets and source IP address verification to detect and block spoofed IPs. <br> - **Intrusion Prevention System (IPS):** Deployed to filter suspicious ICMP traffic based on known attack signatures. <br> - **Access controls:** Reviewing and tightening firewall configuration management to ensure only authorized changes are made. <br> - **Employee training:** Ensuring IT staff are trained on proper firewall configuration and hardening standards to prevent misconfigurations. |
| **Detect** | To improve detection capabilities, the organization has deployed: <br><br> - **Network monitoring software:** Provides real-time visibility into traffic patterns and alerts on abnormal spikes. <br> - **Intrusion Detection System (IDS):** Configured to analyze incoming packets and generate alerts for ICMP floods or other suspicious activity. <br> - **SIEM integration:** Aggregating firewall and IDS logs to correlate events and detect potential reconnaissance or flood attacks earlier. |
| **Respond** | In the event of a similar future incident, the response plan will include: <br><br> - **Containment:** Immediately block the offending IP addresses and filter the specific traffic type (e.g., ICMP) at the firewall. <br> - **Neutralization:** Take non-essential services offline to preserve bandwidth and resources for critical operations. <br> - **Communication:** Notify IT management and affected stakeholders about the incident, impact, and estimated resolution time. <br> - **Analysis:** Preserve firewall and IDS logs for post-incident review to identify the attacker's methods and improve future defenses. |
| **Recover** | Recovery procedures include: <br><br> - **Service restoration:** Gradually re-enable non-critical services once the network stabilizes. <br> - **Data verification:** Ensure systems are functioning correctly and no data was lost or corrupted during the incident. <br> - **Post-incident review:** Conduct a lessons-learned session with the IT and security teams to refine the incident response plan and update security controls. <br> - **Backup validation:** Confirm that backups are intact and available in case data recovery is needed. |

---

### Reflections/Notes

- This incident highlights the critical importance of **proper firewall configuration**. An unconfigured firewall is equivalent to leaving the front door open to attackers.
- The combination of **proactive (Protect)** and **reactive (Detect, Respond)** measures creates a robust defense-in-depth strategy against DoS attacks.
- Regular **audits and configuration checks** should be scheduled to ensure no misconfigurations or "drift" occur over time.
- The implemented IDS/IPS and monitoring tools will not only help detect these attacks but also provide valuable forensic data for future investigations.

---

> *This report was completed as part of the Google Cybersecurity Certificate – Course 3*
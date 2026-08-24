# Access Controls Worksheet: Payroll Incident Investigation

**Date:** August 24, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 5  

---

## Scenario

A business recently experienced a payroll incident where a deposit was made to an unknown bank account. The finance manager claimed they didn't make the mistake, and the payment was stopped. As the first cybersecurity professional hired, I was tasked with investigating the incident using access logs and identifying controls to prevent future occurrences.

---

## Event Log Review

**Event Details:**

| Field | Value |
| :--- | :--- |
| **Event Type** | Information |
| **Event Source** | AdsmEmployeeService |
| **Event Category** | None |
| **Event ID** | 1227 |
| **Date** | 10/03/2023 |
| **Time** | 8:29:57 AM |
| **User** | Legal\Administrator |
| **Computer** | Up2-NoGud |
| **IP Address** | 152.207.255.255 |
| **Description** | Payroll event added. FAUX_BANK |

---

## Access Controls Worksheet

| Notes (1–2 pieces of information about the user) | Issues (1–2 authorization issues) | Recommendations (1–2 mitigations) |
| :--- | :--- | :--- |
| 1. The user is a **Legal Administrator**, indicating they have elevated privileges within the organization. <br><br> 2. The event occurred at **8:29 AM**, during normal business hours, which suggests the action may not have been immediately flagged as suspicious. | 1. The **Legal Administrator** account had the ability to add a payroll event without any additional approval or secondary verification. <br><br> 2. The organization uses a **shared cloud drive** with no clear separation of duties or least privilege enforcement, allowing a single user to access and modify sensitive payroll resources. | 1. **Implement separation of duties:** Require that payroll changes require approval from a second authorized user (e.g., a manager or finance lead) before being processed. <br><br> 2. **Enforce least privilege:** Review user permissions and restrict administrative accounts to only the access required for their specific job functions. Remove unnecessary elevated privileges. <br><br> 3. **Enable logging and monitoring:** Implement real‑time alerts for sensitive actions (e.g., payroll changes, new bank account additions) to enable rapid detection and response. |

---

## Reflection

This investigation highlighted critical gaps in the organization's access control practices:

- **Excessive privileges:** A Legal Administrator had the ability to add payroll events to an unknown bank account without oversight.
- **Lack of separation of duties:** No secondary approval was required for sensitive financial actions.
- **Insufficient monitoring:** The event was only detected after the payment was stopped, not in real time.

By implementing least privilege, separation of duties, and enhanced monitoring, the organization can significantly reduce the risk of similar incidents. These controls align with the **NIST CSF Protect** function and strengthen the overall security posture of the business.

---

## Tools Used

| Tool / Concept | Purpose |
| :--- | :--- |
| **Event logs** | Identify suspicious activity and track user actions |
| **Employee directory** | Cross‑reference event details with user roles |
| **Access controls** | Manage authorization, authentication, and accountability |
| **Separation of duties** | Prevent any single user from having unchecked control over sensitive processes |
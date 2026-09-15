# LetsDefend Incident Report: SOC169 - Possible IDOR Attack Detected

**Platform:** LetsDefend  
**Event ID:** 119  
**Date Completed:** September 15, 2026  
**Role:** SOC Analyst  
**Difficulty:** Medium  
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application)  
**Result:** True Positive  

## 📌 Incident Overview
Investigated a Medium severity alert triggered by an IDOR (Insecure Direct Object Reference) attack against an internal web server. The attacker attempted to enumerate user records by manipulating the `user_id` parameter in consecutive requests.

## 🔍 Investigation Steps

### 1. Alert Analysis & Triage
Extracted the following details from the alert:
- **Attacker IP (Source):** `134.209.118.137` (External)
- **Target Web Server (Destination):** `172.16.17.15` (WebServer1005)
- **HTTP Request Method:** `POST`
- **Requested URL:** `https://172.16.17.15/get_user_info/`
- **Alert Trigger Reason:** Consecutive requests to the same page

### 2. Log Management & HTTP Analysis (Critical Evidence)
Queried Log Management for traffic between `134.209.118.137` and `172.16.17.15`. Found 5 POST requests with sequential `user_id` parameters:

| Time | Payload (`?user_id=`) | HTTP Status | Response Size |
| :--- | :--- | :--- | :--- |
| 21:45:00 | `2` | 200 OK | 253 bytes |
| 21:45:43 | `1` | 200 OK | 188 bytes |
| 21:46:14 | `3` | 200 OK | 351 bytes |
| 21:47:37 | `4` | 200 OK | 158 bytes |
| 21:48:01 | `5` | 200 OK | 267 bytes |

## 🧠 Attack Success Analysis
The attack was **Successful**. 

The key indicators were:
1. **Sequential Enumeration:** The attacker incremented the `user_id` parameter (`1, 2, 3, 4, 5`), indicating a systematic attempt to access multiple user records.
2. **HTTP 200 OK Responses:** All requests were processed successfully by the server.
3. **Varying Response Sizes:** Each response had a different size, proving the server returned distinct user records for each request. The attacker successfully extracted sensitive user data.

## 🛡️ Actions Taken
- **Containment:** Isolated the compromised web server (`WebServer1005`) via Endpoint Security to prevent further data exfiltration.
- **Documentation:** Extracted and documented the following IOCs:
    - Attacker IP: `134.209.118.137`
    - Target IP: `172.16.17.15`
    - Target Endpoint: `/get_user_info/`
- **Escalation:** Escalated the incident to Tier 2 for immediate forensic analysis, data breach assessment, and vulnerability remediation.

## 🧠 Key Takeaways & Lessons Learned
1. **IDOR Detection:** Consecutive requests to the same endpoint with sequentially changing parameters (like `user_id`) are a strong indicator of an IDOR attack.
2. **Varying Response Sizes = Successful Data Extraction:** In IDOR attacks, a consistent response size often indicates a failed request. Varying response sizes indicate the server is returning distinct records, meaning the attack succeeded.
3. **Access Control is Critical:** IDOR vulnerabilities occur when applications expose internal object references without proper authorization checks. Implementing proper access control (e.g., verifying the user has permission to access the requested resource) is essential.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*
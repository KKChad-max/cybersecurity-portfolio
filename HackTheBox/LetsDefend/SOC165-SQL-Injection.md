# LetsDefend Incident Report: SOC165 - Possible SQL Injection Payload Detected

**Platform:** LetsDefend  
**Date Completed:** September 12, 2026  
**Role:** SOC Analyst  
**Difficulty:** Medium  
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application)  
**Result:** True Positive  

## 📌 Incident Overview
Investigated a High severity alert triggered by a possible SQL Injection payload targeting a web application. 

## 🔍 Investigation Steps

### 1. Alert Analysis
Extracted the following details from the alert:
- **Source IP (Attacker):** `167.99.169.17`
- **Destination IP (Target):** `172.16.17.18` (WebServer1001)
- **Targeted Parameter:** `q` (Search query)
- **Payload Detected:** `" OR 1 = 1 -- -`
- **Device Action:** `Allowed`

### 2. Log Management & HTTP Analysis
Searched Log Management for traffic between the Source and Destination IPs. Found 6 associated events.
- **HTTP Status Codes:** The actual SQL Injection requests returned `500 Internal Server Error`.
- **Response Size:** The failed SQL Injection attempts all returned a response size of `948 bytes` (a standard database error page). 
- **Analysis:** The `500` status code and the small `948-byte` response size confirm the SQL payload caused a database syntax error and returned no data. The attack was **Unsuccessful**. (A separate `200 OK` response with a size of `3547 bytes` was also observed, but this corresponded to a benign page load, not the malicious payload).
- The application is vulnerable (it did not sanitize input), but the error handling prevented a successful breach.

## 🛡️ Actions Taken
- **Containment (Temporary):** Initiated containment on `WebServer1001` as a precautionary measure to isolate the device while verifying the extent of the SQL Injection attempt.
- **Containment Rollback (Real-World Context):** Because the attack was determined to be **unsuccessful** (all malicious requests returned HTTP 500 with a 948-byte error page, and no data was exfiltrated), the containment would be rolled back in a real-world scenario after verifying the server is clean and patching the SQL vulnerability. Leaving a production web server isolated indefinitely would cause an unnecessary business outage.
- **Documentation:** Extracted and documented IOCs (Attacker IP: `167.99.169.17`, Target IP: `172.16.17.18`, Payload: `" OR 1 = 1 -- -`).
- **Escalation:** Tier 2 escalation was **not required** because the attack from the Internet did not succeed.

## 🧠 Key Takeaways & Lessons Learned
1. **The "200 OK" Trap:** Not all requests from a malicious IP are part of the attack. Always verify that the `200 OK` response is tied to the *specific malicious payload*, not just a generic page load.
2. **500 vs. 200 in SQLi:** A `500 Internal Server Error` with a small response size means the database crashed due to bad syntax, and the attack *failed*. A `200 OK` with a massive, abnormal response size would indicate a *successful* data dump.
3. **Escalation Criteria:** Escalate to Tier 2 only when an internal asset is successfully compromised. An unsuccessful attack from the Internet can be closed at Tier 1.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*

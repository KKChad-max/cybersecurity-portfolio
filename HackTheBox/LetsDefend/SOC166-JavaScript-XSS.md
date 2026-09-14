# LetsDefend Incident Report: SOC166 - Javascript Code Detected in Requested URL

**Platform:** LetsDefend  
**Event ID:** 116  
**Date Completed:** September 14, 2026  
**Role:** SOC Analyst  
**Difficulty:** Medium  
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application)  
**Result:** True Positive (Unsuccessful Attack)

## 📌 Incident Overview
Investigated a Medium severity alert triggered by JavaScript code embedded in a URL request targeting an internal web server. This is a classic signature of a Cross-Site Scripting (XSS) attack attempt.

## 🔍 Investigation Steps

### 1. Alert Analysis & Triage
Extracted the following details from the alert:
- **Attacker IP (Source):** `112.85.42.13` (External, China Unicom)
- **Target Web Server (Destination):** `172.16.17.17` (WebServer1002)
- **HTTP Request Method:** `GET`
- **Requested URL:** `https://172.16.17.17/search/?q=<script>javascript:$alert(1)</script>`
- **Device Action:** `Allowed`

### 2. Threat Intelligence Verification
Submitted the attacker's IP (`112.85.42.13`) to external threat intelligence platforms:
- **VirusTotal:** 1/94 security vendors flagged the IP as malicious.
- **AbuseIPDB:** The IP was reported **45,565 times** from 479 distinct sources, primarily for brute-force SSH attacks. The IP originates from a Chinese ISP.
- **Conclusion:** The source IP has a known malicious reputation, strengthening the case that this was a deliberate attack.

### 3. Log Management & HTTP Analysis
Queried Log Management for traffic between `112.85.42.13` and `172.16.17.17`. Found **8 events**:
- **5 events** returned an **HTTP 302 (Redirect)** with a response size of `0` bytes.
- **3 events** returned an **HTTP 200 (OK)** with response sizes of `885`, `3531`, and `1024` bytes.

## 🧠 Attack Success Analysis (The Critical Pivot)
Although `200 OK` responses were observed, a successful XSS attack requires the server to **reflect the malicious script** back to the client in the HTML body. 

By matching the specific malicious payload to its HTTP response, it was determined that the actual XSS request containing `<script>javascript:$alert(1)</script>` returned an **HTTP 302 (Redirect)** with a `0`-byte response body. The server redirected the request instead of reflecting the script. 

The `200 OK` responses were benign page loads (likely the attacker following the redirect or scanning other pages). 

**Conclusion:** The attack was **Unsuccessful**. The XSS payload was not reflected, and the vulnerability was not exploited.

## 🛡️ Actions Taken
- **Containment:** Isolated the web server `WebServer1002` via Endpoint Security as a precautionary measure to prevent any further exploitation attempts.
- **Documentation:** Extracted and documented the following IOCs:
    - Attacker IP: `112.85.42.13`
    - Target IP: `172.16.17.17`
    - Attacker Domain: `chinaunicom.com`
    - Malicious Payload URL: `https://172.16.17.17/search/?q=<script>javascript:$alert(1)</script>`
- **Escalation:** Tier 2 escalation was **not required** because the attack from the Internet did not succeed.

## 🧠 Key Takeaways & Lessons Learned
1. **The "200 OK" Trap in XSS:** Not every `200 OK` response means the attack succeeded. Always verify that the specific request containing the malicious payload is the one that returned the `200 OK` with a reflected payload. A `302` redirect means the server dropped the request.
2. **Threat Intel Validation:** Checking the attacker's IP reputation (VirusTotal/AbuseIPDB) is a crucial step to confirm the malicious intent of the traffic, even if the attack fails.
3. **Precautionary Containment:** Even when an attack is unsuccessful, containing the targeted asset can be a valid precautionary measure to prevent follow-up attacks, depending on institutional policy.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*
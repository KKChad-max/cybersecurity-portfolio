# LetsDefend Incident Report: SOC166 - Javascript Code Detected in Requested URL

**Platform:** LetsDefend  
**Event ID:** 116  
**Date Completed:** September 15, 2026  
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

### 3. Log Management & HTTP Analysis (Detailed Analysis)
Queried Log Management for traffic between `112.85.42.13` and `172.16.17.17`. Found **8 events**:
- **3 Benign Requests** returned an **HTTP 200 (OK)** with normal response sizes (`1024`, `3531`, `885` bytes). These were normal page loads (`/`, `/about-us/`, `/search/?q=test`).
- **5 Malicious Requests** returned an **HTTP 302 (Redirect)** with a response size of `0` bytes. The attacker attempted multiple different XSS payloads:

| Time | Payload (`?q=`) | HTTP Status | Response Size |
| :--- | :--- | :--- | :--- |
| 17:46:23 | `<img src=q onerror=prompt(8)>` | 302 (Redirect) | 0 bytes |
| 17:46:36 | `prompt(8)/` | 302 (Redirect) | 0 bytes |
| 17:50:09 | `<script>for((i)in(self))eval(i)(1)</script>` | 302 (Redirect) | 0 bytes |
| 17:53:40 | `<svg><script>?$alert(1)` | 302 (Redirect) | 0 bytes |
| 17:56:55 | `<script>javascript:$alert(1)</script>` | 302 (Redirect) | 0 bytes |

## 🧠 Attack Success Analysis (The Critical Pivot)
The attack was **Unsuccessful**. 

A successful XSS attack requires the server to **reflect the malicious script** back to the client in the HTML body. 

*   **The "200 OK" Trap:** The `200 OK` responses observed were benign page loads, not the malicious XSS requests.
*   **The 302 Redirects:** All 5 malicious XSS requests returned an **HTTP 302 (Redirect)** with a `0`-byte response body. The server redirected the requests instead of reflecting the scripts. The XSS payloads were never executed by any browser.

## 🛡️ Actions Taken
- **Containment:** Isolated the web server `WebServer1002` via Endpoint Security as a precautionary measure to prevent any further exploitation attempts.
- **Documentation:** Extracted and documented the following IOCs:
    - Attacker IP: `112.85.42.13`
    - Target IP: `172.16.17.17`
    - Attacker Domain: `chinaunicom.com`
    - Malicious Payload URLs (all 5 variants listed above)
- **Escalation:** Tier 2 escalation was **not required** because the attack from the Internet did not succeed.

## 🧠 Key Takeaways & Lessons Learned
1. **The "200 OK" Trap in XSS:** Not every `200 OK` response means the attack succeeded. Always verify that the specific request containing the malicious payload is the one that returned the `200 OK`. A `302` redirect means the server dropped the request.
2. **Multiple Payloads = Different Traffic:** Attackers often try multiple variations of a payload in quick succession. Even if the attack fails, identifying that *different traffic* (i.e., the multiple payloads) came from the same source is a crucial part of the investigation.
3. **Threat Intel Validation:** Checking the attacker's IP reputation (VirusTotal/AbuseIPDB) is a crucial step to confirm the malicious intent of the traffic, even if the attack fails.
4. **Precautionary Containment:** Even when an attack is unsuccessful, containing the targeted asset can be a valid precautionary measure to prevent follow-up attacks, depending on institutional policy.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*
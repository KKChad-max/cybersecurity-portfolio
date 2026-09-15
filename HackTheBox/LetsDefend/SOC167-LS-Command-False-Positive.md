# LetsDefend Incident Report: SOC167 - LS Command Detected in Requested URL

**Platform:** LetsDefend  
**Event ID:** 117  
**Date Completed:** September 15, 2026  
**Role:** SOC Analyst  
**Difficulty:** Easy  
**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application)  
**Result:** False Positive  

## 📌 Incident Overview
Investigated a High severity alert triggered by the detection of the `ls` command in a requested URL. This alert was determined to be a **False Positive** caused by a detection rule misinterpreting a benign search query.

## 🔍 Investigation Steps

### 1. Alert Analysis & Triage
Extracted the following details from the alert:
- **Source IP (User):** `172.16.17.46` (Internal)
- **Destination IP:** `188.114.96.15` (External - LetsDefend Blog)
- **Hostname:** `EliotPRD`
- **Requested URL:** `https://letsdefend.io/blog/?s=skills`
- **HTTP Request Method:** `GET`
- **Alert Trigger Reason:** URL Contains `LS`

### 2. Threat Intelligence & HTTP Analysis
- **Destination Analysis:** The destination is the legitimate LetsDefend blog. There is no malicious infrastructure involved.
- **Payload Analysis:** The URL parameter `?s=skills` is a search query for the word "skills". The substring "ls" appears at the end of "skills" and inadvertently matched the detection pattern for the Linux `ls` command. 
- **Traffic Verification:** Confirmed that the request was a normal user action (searching a blog) and not a command injection attempt.

### 3. Endpoint Verification
To be thorough and confirm the false positive, the user's device (`EliotPRD`) was checked via the Endpoint Security page. The Browser History confirmed the user was browsing the LetsDefend blog. There was no evidence of malicious command execution or suspicious activity.

## 🧠 Root Cause Analysis
This was a **False Positive** caused by a detection rule that was too broad. The rule flagged any URL containing the letters "ls", which led to an alert when a user searched for the word "skills". This is a common issue in SOC environments and highlights the need for continuous rule tuning.

## 🛡️ Actions Taken
- **No Containment Required:** The traffic was benign, and no malicious activity was found.
- **Documentation:** Logged the false positive and the specific URL that triggered the rule to aid in future rule tuning.
- **No Tier 2 Escalation:** The incident was resolved as a False Positive at the Tier 1 level.

## 🧠 Key Takeaways & Lessons Learned
1. **False Positives from Substrings:** Detection rules based on simple substring matches (like "ls") are prone to false positives when those letters appear within larger, benign words (like "skills").
2. **Always Verify with Context:** Investigating the full URL, destination reputation, and endpoint activity is critical to distinguishing a true attack from a false alarm.
3. **Rule Tuning:** These investigations are valuable for improving detection rules. This incident should be documented to refine the rule to avoid future false positives.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*
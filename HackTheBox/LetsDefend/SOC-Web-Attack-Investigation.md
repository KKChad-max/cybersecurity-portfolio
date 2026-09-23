# LetsDefend Incident Report: Web Attack Investigation (SOC Challenge)

**Platform:** LetsDefend  
**Date Completed:** September 23, 2026  
**Role:** SOC Analyst  
**Difficulty:** Medium  
**MITRE ATT&CK:** T1595 (Active Scanning), T1083 (File and Directory Discovery), T1110 (Brute Force), T1059 (Command and Scripting Interpreter), T1136 (Create Account)  
**Result:** True Positive  

## 📌 Incident Overview
Investigated a Linux `access.log` file containing over 1,000 events to identify a multi-stage web attack. The investigation revealed a systematic attack chain starting from automated web reconnaissance, moving through directory brute-forcing and login brute-forcing, and culminating in command injection and persistence via account creation.

## 🛠️ Tools & Techniques Used for Log Analysis

To extract these answers from the raw `access.log` file, the following Linux command-line tools and techniques were used:

| Tool / Command | Purpose in Investigation | Example Command Used |
| :--- | :--- | :--- |
| **`grep`** | Filtering the log for specific keywords (e.g., `Nikto`, `POST`, `whoami`, `%`) to isolate attack patterns. | `grep -i "whoami" access.log` |
| **`grep -v -E`** | Removing noise (CSS, JS, images) to create a clean log file for analysis. | `grep -v -E "\.(css|js|png|jpg|jpeg|gif|ico|svg)" access.log > clean.log` |
| **`awk`** | Extracting specific fields from the log (like the 6th field for User-Agent strings) for pattern analysis. | `awk -F'"' '{print $6}' clean.log \| sort \| uniq -c` |
| **`sort \| uniq -c`** | Counting and identifying repeated patterns (e.g., repeated 404 errors for brute-force detection). | `grep " 404 " clean.log \| awk '{print $7}' \| sort \| uniq -c \| sort -rn` |
| **`head / tail`** | Examining the beginning or end of the log to identify the start and end of the attack chain. | `head -n 30 clean.log` / `tail -n 30 clean.log` |
| **URL Decoding** | Manually decoding the URL-encoded persistence payload (`%27net%20user...`) to understand the malicious command. | N/A |

## 🔍 Investigation Steps & Findings

### 1. Web Reconnaissance (Question 1)
- **Answer:** `Nikto`
- **Analysis:** Analyzed the User-Agent strings in the log. The presence of `Nikto/2.1.6` in the User-Agent field, combined with a high volume of rapid requests for unusual paths, confirmed the attacker used the Nikto web scanner for initial reconnaissance.

### 2. Directory Listing Discovery (Question 2)
- **Answer:** `Directory brute force`
- **Analysis:** Observed a large volume of sequential 404 (Not Found) responses for various common administrative and backup directories (e.g., `/admin/`, `/backup/`, `/config/`). This pattern is characteristic of directory brute-forcing tools attempting to map the web server's structure.

### 3. Third Attack Type: Login Brute Force (Question 3)
- **Answer:** `Brute force`
- **Analysis:** After discovering the login page, the attacker initiated a high volume of POST requests to the login endpoint. This indicated a brute-force attack aimed at guessing user credentials.

### 4. Attack Success Verification (Question 4)
- **Answer:** `Yes`
- **Analysis:** Examined the HTTP response codes and sizes for the POST requests. Failed login attempts consistently returned a 200 OK with a small response size (~4,086 bytes). However, one specific request returned a **302 Redirect** followed by a **200 OK** with a significantly larger response size (~23,069 bytes), indicating a successful login and access to a protected dashboard.

### 5. Fourth Attack Type: Code Injection (Question 5)
- **Answer:** `Code Injection`
- **Analysis:** Identified the fourth attack phase by examining the URLs. The attacker was attempting to execute system commands by injecting PHP code (e.g., `phpinfo()`) and OS commands (e.g., `whoami`) into the web application parameters.

### 6. First Payload for Code Injection (Question 6)
- **Answer:** `whoami`
- **Analysis:** Located the initial command used by the attacker to test code execution capabilities. The `whoami` command was injected to identify the privilege level of the web server user.

### 7. Persistence Payload (Question 7)
- **Answer:** `%27net%20user%20hacker%20asd123!!%20/add%27`
- **Analysis:** Identified a URL-encoded payload at the end of the attack sequence. After URL-decoding the payload (`%27net%20user%20hacker%20asd123!!%20/add%27`), it translates to `'net user hacker asd123!! /add'`. This is a classic Windows command used by attackers to create a new local user account for persistence, ensuring continued access to the compromised server.


## 🧠 Key Takeaways & Lessons Learned
1. **Log Noise is the Enemy:** Over 80% of the log was benign traffic (images, CSS). Filtering out static file requests is the critical first step in any web log investigation.
2. **Pattern Recognition:** Web attacks leave distinct footprints. A high volume of 404s indicates directory brute force, while a high volume of POSTs indicates login brute-forcing.
3. **Response Size Matters:** In brute-force attacks, the successful request often stands out not just by the HTTP status code (302), but by the response size, as it grants access to a larger dashboard page.
4. **Persistence is Key:** Attackers rarely stop at initial access. Finding the `net user /add` command proved the attacker's intent to maintain long-term access to the victim machine.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*
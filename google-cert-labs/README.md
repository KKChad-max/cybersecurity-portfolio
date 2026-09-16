# 🎓 Google Cybersecurity Professional Certificate — Labs & Reports

**Completed:** August 2026  
**Certificate:** Google Cybersecurity Professional Certificate (9/9 Courses)

This folder contains my complete coursework, hands-on labs, incident reports, and portfolio artifacts from the Google Cybersecurity Professional Certificate. Each course folder holds notes, labs, and deliverables that demonstrate practical application of security concepts — from auditing to incident response to Python automation.

---

## 📚 Course Overview

| # | Course | Focus |
| :--- | :--- | :--- |
| **1** | Foundations of Cybersecurity | CIA Triad, CISSP Domains, NIST CSF, security tools |
| **2** | Play It Safe – Manage Security Risks | Risk frameworks, controls, SIEM basics |
| **3** | Connect and Protect – Networks | TCP/IP, network attacks, packet analysis |
| **4** | Tools of the Trade – Linux & SQL | File permissions, SQL filtering, log analysis |
| **5** | Assets, Threats, and Vulnerabilities | Risk registers, threat modeling, cryptography |
| **6** | Sound the Alarm – Detection and Response | Incident response, IDS, packet analysis, phishing triage |
| **7** | Automate Cybersecurity Tasks with Python | Python for security automation |
| **8** | Put It to Work – Prepare for Cybersecurity Jobs | AI prompting, SOC log analysis, org structures |

---

## 📂 Course Breakdown

### 📁 [Course 1 — Foundations of Cybersecurity](./course-1-foundations)
- 📘 **[Foundations Notes](./course-1-foundations/notes.md)** — CISSP domains, NIST CSF functions, security analyst responsibilities, and the core tools of the trade.

---

### 📁 [Course 2 — Play It Safe: Manage Security Risks](./course-2-play-it-safe)
- 📘 **[Course 2 Notes](./course-2-play-it-safe/notes.md)** — Risk management frameworks (NIST RMF), CIA Triad, administrative/technical/physical controls.
- 🔍 **[Botium Toys Security Audit](./course-2-play-it-safe/Botium_Toys_Security_Audit.md)** — A full internal security audit with controls and compliance checklists (PCI DSS, GDPR, SOC 1/2). *The company had no encryption, no IDS, and no backups. I told them exactly why that mattered.*

---

### 📁 [Course 3 — Connect and Protect: Networks](./course-3-networking)
- 🌐 **[Network Traffic Analysis (DNS Failure)](./course-3-networking/cybersecurity-incident-report-network-traffic.md)** — Used `tcpdump` to trace a "udp port 53 unreachable" error back to a failing DNS server.
- 💥 **[SYN Flood Attack Analysis](./course-3-networking/cybersecurity-incident-report-syn-flood.md)** — Broke down a DoS attack using Wireshark logs, explaining the TCP 3-way handshake and how half-open connections exhaust server resources.
- 🛡️ **[NIST CSF Incident Analysis](./course-3-networking/incident-report-analysis-nist-csf.md)** — Applied all 5 NIST CSF functions to a DoS attack caused by an unconfigured firewall.
- 🎣 **[Malicious Website Redirect Report](./course-3-networking/security-incident-report-malware-redirect.md)** — Traced a browser redirect from `yummyrecipesforme.com` to a fake site after a brute-force admin compromise.

---

### 📁 [Course 4 — Tools of the Trade: Linux & SQL](./course-4-linux)
- 🐧 **[File Permissions in Linux](./course-4-linux/file-permissions-linux.md)** — Audited and corrected file permissions (`chmod u=r,g=r`, `chmod g-x`) to enforce least privilege on a research team's directory.
- 🗄️ **[Apply Filters to SQL Queries](./course-4-sql/apply-filters-to-sql-queries.md)** — Retrieved after-hours failed logins and filtered employees by department using `AND`, `OR`, `NOT`, and `LIKE`.

---

### 📁 [Course 5 — Assets, Threats, and Vulnerabilities](./course-5-assets-threats-vulnerabilities)
- 🔐 **[Access Controls Worksheet](./course-5-assets-threats-vulnerabilities/access-controls-worksheet.md)** — Investigated a payroll incident where a Legal Administrator added a payment to an unknown bank account. *No separation of duties, no oversight.*
- 🔑 **[Create Hash Values Lab](./course-5-assets-threats-vulnerabilities/create-hash-values-lab.md)** — Proved two seemingly identical files were different using SHA-256 hashing.
- 📤 **[Data Leak Worksheet](./course-5-assets-threats-vulnerabilities/data-leak-worksheet.md)** — Mapped an internal document leak to NIST SP 800-53 AC-6 (Least Privilege) and proposed automated revocation.
- 🔓 **[Caesar Cipher & OpenSSL Decryption Lab](./course-5-assets-threats-vulnerabilities/decrypt-caesar-cipher-lab.md)** — Decoded a Caesar cipher, recovered an AES key, and decrypted an OpenSSL-protected file.
- 🏠 **[Home Office Asset Inventory](./course-5-assets-threats-vulnerabilities/home-office-asset-inventory.md)** — Classified 6 devices by sensitivity level (Public → Restricted) and prioritized controls.
- 🔌 **[Parking Lot USB Exercise](./course-5-assets-threats-vulnerabilities/parking-lot-usb-exercise.md)** — Analyzed the risks of a found USB drive containing PII, and recommended technical, operational, and managerial controls against USB bashing.
- 🏗️ **[PASTA Threat Model Worksheet](./course-5-assets-threats-vulnerabilities/pasta-threat-model-worksheet.md)** — Full 7-stage PASTA threat model for a sneaker marketplace app: data flow diagrams, attack trees, and control recommendations. *Security isn't a wall — it's a design decision.*
- 🎣 **[Phishing Analysis — ExecuTalk](./course-5-assets-threats-vulnerabilities/phishing-analysis-executalk.md)** — Identified 5 phishing red flags in an executive-targeted email, including a spoofed Gmail sender and a 48-hour urgency deadline.
- 📊 **[Risk Register — Commercial Bank](./course-5-assets-threats-vulnerabilities/risk-register-commercial-bank.md)** — Scored 5 risks using Likelihood × Severity. Business Email Compromise and a compromised customer database both hit a critical 9.
- 🧠 **[Threat Modeling Reflection](./course-5-assets-threats-vulnerabilities/threat-modeling-reflection.md)** — Why threat modeling is the foundation of proactive defense.
- 🛡️ **[Vulnerability Assessment Report](./course-5-assets-threats-vulnerabilities/vulnerability-assessment-report.md)** — NIST SP 800-30 qualitative risk assessment of a publicly exposed MySQL database server.

---

### 📁 [Course 6 — Sound the Alarm: Detection and Response](./course-6-detection-response)
- 📝 **[Final Report — Data Breach](./course-6-detection-response/final-report-data-breach.md)** — Formal incident report on a forced-browsing attack that exfiltrated **50,000 customer records**. *$100,000 in damages. Writing the executive summary taught me how to speak business, not just tech.*
- 📓 **[Incident Handler's Journal — Entry 1](./course-6-detection-response/incident-handlers-journal-entry-1.md)** — First entry in a running incident response journal.
- 📓 **[Incident Handler's Journal — Entry 2](./course-6-detection-response/incident-handlers-journal-entry-2.md)** — Second entry, documenting escalating investigation.
- 📓 **[Incident Handler's Journal — Entry 3](./course-6-detection-response/incident-handlers-journal-entry-3.md)** — Third entry, closing out the response.
- 📓 **[Incident Handler's Journal (Full)](./course-6-detection-response/incident-handlers-journal.md)** — Complete journal across the investigation.
- 🔍 **[Network Protocol Analyzers Comparison](./course-6-detection-response/network-protocol-analyzers-comparison.md)** — Comparing Wireshark, tcpdump, and other tools to know which one to reach for.
- 🎣 **[Phishing Incident Response](./course-6-detection-response/phishing-incident-response.md)** — Step-by-step triage of a phishing email using an incident response playbook.
- 🔺 **[Pyramid of Pain with VirusTotal](./course-6-detection-response/pyramid-of-pain-virustotal.md)** — Mapping IOCs against David Bianco's Pyramid of Pain using VirusTotal.
- 🛰️ **[Suricata IDS Lab](./course-6-detection-response/suricata-ids-lab.md)** — Configured and triaged IDS alerts on live network traffic. *The hard part isn't detection — it's deciding what to ignore.*
- 📡 **[tcpdump Packet Capture Lab](./course-6-detection-response/tcpdump-packet-capture-lab.md)** — Captured and analyzed network traffic from the command line.
- 🦈 **[Wireshark Packet Analysis Lab](./course-6-detection-response/wireshark-packet-analysis-lab.md)** — Deep packet inspection to investigate suspicious network behavior.

---

### 📁 [Course 7 — Automate Cybersecurity Tasks with Python](./course-7-python)
- 🐍 **[Algorithm for File Updates (Portfolio Project)](./course-7-python/algorithm-for-file-updates-portfolio.md)** — A complete allow-list updater script that reads a file, removes unauthorized entries, and writes the updated list back. *My first portfolio-quality Python project.*
- 📄 **[Python Algorithm — File Parse Lab](./course-7-python/python-algorithm-file-parse-lab.md)** — Parsing files programmatically with algorithms.
- 🧮 **[Python Algorithm Lab](./course-7-python/python-algorithm-lab.md)** — Building algorithms from scratch.
- 🔀 **[Python Conditional Statements Lab](./course-7-python/python-conditional-statements-lab.md)** — `if`, `elif`, `else` for security decision-making.
- 🐞 **[Python Debugging Lab](./course-7-python/python-debugging-lab.md)** — Fixing syntax, logic, and runtime errors.
- 📂 **[Python File I/O Lab](./course-7-python/python-file-io-lab.md)** — Reading and writing files safely with `with open()`.
- 🧩 **[Python Functions Lab 2](./course-7-python/python-functions-lab-2.md)** — Advanced function design.
- 🧩 **[Python Functions Lab](./course-7-python/python-functions-lab.md)** — Building reusable functions for automation.
- 🔁 **[Python Loops Lab](./course-7-python/python-loops-lab.md)** — Iterating through log entries and file lists.
- 🖨️ **[Python Print Lab](./course-7-python/python-print-lab.md)** — Output formatting and debugging.
- 🔤 **[Python Regex Lab](./course-7-python/python-regex-lab.md)** — Extracting IPs and patterns from unstructured logs.
- 🔡 **[Python Strings Lab](./course-7-python/python-strings-lab.md)** — String manipulation for log parsing.
- 📦 **[Python Variables Lab](./course-7-python/python-variables-lab.md)** — Data types and variable handling.

---

### 📁 [Course 8 — Put It to Work: Prepare for Cybersecurity Jobs](./course-8-put-it-to-work)
- 🤖 **[AI Prompting — Phishing Guide](./course-8-put-it-to-work/AI_Prompting_Phishing_Guide.md)** — Using AI to assist with phishing identification (and understanding its limits).
- 🧠 **[AI Reflection](./course-8-put-it-to-work/AI_Reflection.md)** — My thoughts on AI in cybersecurity workflows.
- 📊 **[SOC Log Analysis](./course-8-put-it-to-work/SOC_Log_Analysis_Course8.md)** — Realistic SOC log analysis exercise.
- 🏢 **[Security Organization Worksheet](./course-8-put-it-to-work/Security_Organization_Worksheet.md)** — Org structures and security team roles.

---

## 🎯 What These Labs Demonstrate

- **Practical frameworks:** NIST CSF, NIST SP 800-30/53, CISSP domains, PASTA, PCI DSS, GDPR
- **Incident response:** Full-cycle reporting from detection to remediation
- **Network analysis:** Wireshark, tcpdump, Suricata, protocol comparison
- **Threat modeling:** PASTA methodology, DFDs, attack trees
- **Risk management:** Risk registers, vulnerability assessments, asset inventories
- **Hands-on cryptography:** SHA-256, AES-256-CBC, Caesar cipher
- **Python automation:** 13 labs culminating in a portfolio project

---

## 🧠 Reflection

This certificate gave me the **vocabulary and frameworks** to describe what I already do in my home lab and Python scripts — and the hands-on labs turned theory into muscle memory. The Botium Toys audit, the PASTA threat model, and the data breach final report were particularly valuable, as they forced me to communicate technical findings to a business audience.

Every file in this folder represents a small step from "learning about security" to *doing* security.

---

> *Completed August 2026 — Google Cybersecurity Professional Certificate (9/9 courses).*
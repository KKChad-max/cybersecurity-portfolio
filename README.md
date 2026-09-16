# 👋 Hi, I'm CHADRACK KALONGO KABINDA

I'm an Electrical Engineering Technologist / IT Tech transitioning into **Cybersecurity**. This portfolio documents my hands-on journey through certifications, labs, and wargames.

---

## 🧑‍💻 About Me

I've been around technology since my young age, but for most of those years, I understood it as a *user*, not as an engineer.

Pursuing Electrical Engineering taught me something about myself. I could reason through circuit logic far more naturally than the abstractions of Computer Science and IT. That bothered me enough to ask a question that eventually changed my career:

> *"Why do I understand electrical logic more than Computer Science and IT in general?"*

The answer wasn't that one was easier, it was that rigidity hides complexity, and flexibility hides it too. That question didn't push me away from tech. It pulled me toward it, especially as every sector (energy, healthcare, finance) goes digital.

Cybersecurity is where that convergence matters most. It's where I can use the rigor of engineering, the logic of code, and the responsibility of protecting real systems, all at once.

My goal: land a role as a **Security Analyst** and keep growing on the blue team side.

---

## 🏆 Certifications & Achievements

| Badge | Status |
| :--- | :--- |
| **Google Cybersecurity Professional Certificate** | ✅ **Completed (9/9 Courses)** |
| **Google AI Professional Certificate** | 4 of 8 Courses ✅ Completed |
| **OPSWAT Critical Infrastructure Protection (ICIP)** | ✅ Earned (Expires Aug 2027) |
| **OverTheWire Bandit 0–25** | ✅ Completed & Documented |
| **NCC Level 4 Diploma in Computing** | ✅ **Completed (8 Modules)** |
| **LetsDefend SOC Analyst Learning Path** | 🚧 In Progress |
| **ISC² Certified in Cybersecurity (CC)** | 🎯 Targeting October 2026 |
| **TryHackMe SAL1** | 🎯 Targeting November 2026 |
| **CompTIA Security+ (SY0-701)** | 🎯 Targeting December 2026 |
| **HTB Silver Certifications (5 exams)** | 🎯 Targeting Dec 2026 – Mar 2027 |
| **TryHackMe SAL2** | 🎯 Targeting April 2027 |

---

## 🛠️ Technical Skills

| Category | Skills & Tools |
| :--- | :--- |
| **Operating Systems** | Linux (Ubuntu, Kali), Windows 10, VirtualBox |
| **Networking** | TCP/IP, DNS, HTTP/HTTPS, Wireshark, tcpdump, Nmap, Netcat, OpenSSL |
| **Blue Team Tools** | Splunk (SIEM), Suricata (IDS), VirusTotal, AbuseIPDB, MITRE ATT&CK, LetsDefend |
| **Scripting** | Python, Bash, PowerShell, SQL |
| **Web Security** | SQLi, XSS, IDOR, LFI/RFI, Command Injection, HTTP Analysis |
| **Malware Analysis** | PowerShell Decoding, C2 Identification, IOC Extraction |
| **Incident Response** | Log Analysis, Endpoint Containment, Phishing Triage, Playbook Execution |
| **Frameworks** | NIST CSF, NIST SP 800-30/53, MITRE ATT&CK, CISSP Domains, PASTA, PCI DSS, GDPR |
| **Cryptography** | SHA-256, AES-256-CBC, Caesar Cipher, File Integrity |

---

## 🔬 Lab Highlights

*A small sample of the work behind this portfolio. Each investigation taught me something I couldn't learn from a textbook.*

| Investigation | The Hook | Key Skills |
| :--- | :--- | :--- |
| **[🔍 SOC138 — Suspicious XLS File](./HackTheBox/LetsDefend/SOC138-Suspicious-Xls-Malware.md)** | Decoded a heavily obfuscated PowerShell stager and extracted 7 malicious C2 download URLs from it. | PowerShell Decoding, Malware Analysis |
| **[☕ SOC282 — Deceptive Phishing](./HackTheBox/LetsDefend/SOC282-Phishing-Deceptive-Mail.md)** | Traced a phishing email to a malicious `coffee.exe` process (PID 6697) talking to an external C2 server. | Process Analysis, C2 Detection, Containment |
| **[📊 SOC146 — Excel 4.0 Macros](./HackTheBox/LetsDefend/SOC146-Phishing-Excel-Macros.md)** | Proved malware execution by pivoting from the sender's SMTP IP to the actual C2 IP — then found `regsvr32` in the terminal history. | Log Analysis, Process Lineage, C2 Investigation |
| **[💉 SOC168 — Whoami Command Injection](./HackTheBox/LetsDefend/SOC168-Whoami-Command-Injection.md)** | Used varying HTTP response sizes to prove an attacker successfully read `/etc/shadow` on a web server. | Response Size Analysis, Attack Verification |
| **[📝 Google Cert — Data Breach Final Report](./google-cert-labs/course-6-detection-response/final-report-data-breach.md)** | Authored a formal executive report on a forced-browsing attack that exfiltrated 50,000 customer records. | Incident Reporting, Forced Browsing, Executive Comms |
| **Google Cert – NIST CSF Analysis** | Mapped a DoS attack to the NIST CSF framework, showing how an unconfigured firewall broke all 5 functions. | NIST CSF, Root Cause Analysis |
| **[🏗️ Google Cert — PASTA Threat Model](./google-cert-labs/course-5-assets-threats-vulnerabilities/pasta-threat-model-worksheet.md)** | Built a full threat model for a sneaker marketplace app, including data flow diagrams and attack trees. | Threat Modeling, PASTA, Secure Design |
| **[🐍 Python — Log Analyzer](./python-practice/log_analyzer.py)** | Built a SIEM-style script that parses authentication logs and flags brute-force IPs by threshold. | Python, Regex, SIEM Concepts |
| **[🛰️ Suricata IDS Lab](./google-cert-labs/course-6-detection-response/suricata-ids-lab.md)** | Configured and triaged IDS alerts on live network traffic using Suricata. | Suricata, IDS, Network Detection |
| **[🐧 OverTheWire Bandit — Levels 0–25](./linux-fundamentals/bandit-levels-0-25.md)** | Escaped a restricted shell (`rbash`) using the classic `vi` trick and documented a full SSH key troubleshooting saga. | Linux CLI, SSH, rbash Escape, Privilege Escalation |

*(See individual folders for full write-ups and evidence.)*

---

## 📅 Phase 1 (Completed: July – September 2026)

Linux Fundamentals · Python Automation · Home Lab · Google Cybersecurity (9/9) · Google AI (4/8) · OPSWAT ICIP · Cybersecurity Field Manual · LetsDefend SOC investigations.

---

## 📅 Phase 2 (In Progress: September 2026 – March 2027)

| Period | Focus | Goal |
| :--- | :--- | :--- |
| **Sept – Oct 20** | LetsDefend | Complete the SOC Analyst Learning Path |
| **Beginning Oct** | ISC² CC Exam | Earn the Certified in Cybersecurity credential |
| **Early Nov** | TryHackMe + SAL1 | Complete rooms and earn SAL1 |
| **Early Dec** | CompTIA Security+ | Pass the SY0-701 exam |
| **Late Dec – Mar 2027** | HackTheBox Silver | Complete 5 HTB certification exams (Junior Associate, Pen Testing, Web Exploitation, Defensive Analyst, Offensive AI) |

---

## 📂 Portfolio Contents

- **[NCC Level 4 Diploma](/ncc-diploma-computing/)** — 8 academic modules (Computer Systems, Networks, Databases, OOP, Software Engineering, Front-End, Algorithms)
- **[Linux Fundamentals](/linux-fundamentals)** — OverTheWire Bandit 0–25 writeup
- **[Python Practice](/python-practice)** — 4 automation scripts (log analyzer, integrity checker, file renamer, parsers)
- **[Home Lab](/home-lab)** — VirtualBox + Ubuntu LTS VM setup
- **[Google Cert Labs](/google-cert-labs)** — All 9 courses: audits, incident reports, SQL labs, hashing, cryptography, threat models
- **[HackTheBox (LetsDefend)](/HackTheBox/LetsDefend)** — SOC Analyst incident investigations (phishing, SQLi, XSS, IDOR, LFI, malware analysis)
- **[TryHackMe Writeups](/tryhackme-writeups)** *(In Progress — Nov 2026)*
- **[OT/ICS Case Study](/ot-ics-case-study)** *(In Progress)*

---

## 🧠 Bonus: Cybersecurity Field Manual
A personal **[Field Manual](/My_Cybersecurity_Field_Manual.md)** in the root directory — Linux, SQL, and Python references plus troubleshooting strategies from real struggles (Bandit, Google Cert labs, and beyond).

---

## 🎯 Current Goal
Building a strong foundation in **network security, Linux, SQL, Python, and critical infrastructure protection** to pursue a role as a **Security Analyst**.

---

## 📬 Connect With Me

| Platform | Link |
| :--- | :--- |
| **LinkedIn** | [linkedin.com/in/chadrack-kabinda](https://www.linkedin.com/in/chadrack-kabinda-a4286442b/) |
| **GitHub** | [github.com/KKChad-max](https://github.com/KKChad-max) |
| **Email** | kabindakchadrack@gmail.com |

---

## 🙏 Acknowledgements

[OverTheWire Bandit](https://overthewire.org/wargames/bandit/) · [Python](https://www.python.org/) · [VirtualBox](https://www.virtualbox.org/) · [OPSWAT Academy](https://www.opswat.com/academy) · [Google](https://www.coursera.org/google) · [LetsDefend](https://letsdefend.io/) · [Hack The Box](https://www.hackthebox.com/) · [TryHackMe](https://tryhackme.com/) · [CompTIA](https://www.comptia.org/)

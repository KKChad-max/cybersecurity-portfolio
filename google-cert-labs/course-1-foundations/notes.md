# Course 1: Foundations of Cybersecurity

**Completed:** August 9, 2026  
**Certificate:** Google Cybersecurity Professional Certificate  

---

## Module 1: Welcome to the Exciting World of Cybersecurity

### Key Concepts

#### What is Cybersecurity?
- The practice of protecting **systems, networks, and programs** from digital attacks.
- Goal: Ensure **Confidentiality, Integrity, and Availability** (CIA Triad).

#### Responsibilities of an Entry-Level Security Analyst
- **Monitor** networks for suspicious activity.
- **Investigate** potential threats and vulnerabilities.
- **Report** findings clearly to the team.
- **Proactive mindset:** Identifying risks before they become incidents.
- **Reactive mindset:** Responding to incidents when they occur.

#### Core Skills for Cybersecurity Professionals

| Transferable Skills | Technical Skills |
| :--- | :--- |
| Communication & Writing | Linux (command-line) |
| Problem-solving | Python / Scripting |
| Curiosity & Attention to detail | SQL (databases) |
| Collaboration | Network fundamentals (TCP/IP, ports, protocols) |
| Adaptability | SIEM tools (e.g., Splunk, Chronicle) |

#### Reflection: Connecting to My Hands-On Work
- **Linux & Command-line:** I used `ls`, `cat`, `find`, `grep`, `nmap`, `nc`, and `openssl` during the Bandit wargame – all directly relevant to monitoring and investigation.
- **Python:** I built a log analyzer that parses authentication logs and flags suspicious IPs – exactly what a SIEM alert rule does.
- **Attention to detail:** The `diff` trap (Level 17 → 18) taught me that small details in output matter – a critical skill for threat hunting.

---

## Module 2: The Evolution of Cybersecurity

### Key Concepts

#### The History of Cybersecurity
- The field evolved as threats moved from physical to digital.
- Early attacks: **Morris Worm (1988)**, **LoveLetter (2000)** – highlighted the need for proactive defense.
- Modern attacks: **Ransomware**, **Phishing**, **DDoS**, **Supply Chain Attacks** (e.g., SolarWinds).

#### The 8 CISSP Security Domains (Core framework)

1. **Security and Risk Management** – Defining security goals and risk tolerance.
2. **Asset Security** – Protecting physical and digital assets.
3. **Security Architecture and Engineering** – Designing secure systems.
4. **Communication and Network Security** – Securing data in transit (TCP/IP, firewalls, encryption).
5. **Identity and Access Management (IAM)** – Who has access to what (passwords, MFA, least privilege).
6. **Security Assessment and Testing** – Auditing, vulnerability scanning, penetration testing.
7. **Security Operations (SOC)** – Monitoring, detecting, and responding to incidents.
8. **Software Development Security** – Secure coding practices (OWASP).

#### Reflection: Connecting to My Hands-On Work
- **Network Security:** My `nmap` port scan (Level 16) and `netcat` connections directly relate to the Communication and Network Security domain.
- **IAM:** The SSH key authentication (Levels 13 & 16) connects to Identity and Access Management.
- **Security Operations:** My log analyzer (`log_analyzer.py`) is a mini-SOC tool – it detects brute-force attempts, which is a core SOC function.

---

## Module 3: Protect Against Threats, Risks, and Vulnerabilities

### Key Concepts

#### Frameworks & Controls

- **Framework:** A structured approach to managing security (e.g., NIST CSF).
- **Controls:** Safeguards to reduce risk (e.g., firewalls, MFA, encryption).

#### NIST Cybersecurity Framework (CSF) – 5 Functions:
- **Identify** – Understand your assets, risks, and vulnerabilities.
- **Protect** – Implement safeguards (e.g., access controls, encryption).
- **Detect** – Monitor for anomalies and alerts.
- **Respond** – Take action when an incident occurs.
- **Recover** – Restore systems and learn from the incident.

#### CIS Controls (Critical Security Controls):
- A prioritized list of actions to protect against the most common attacks.
- Example: **Control 3 – Data Protection** (encryption, hashing).
- Example: **Control 4 – Secure Configuration** (hardening VMs, disabling unnecessary services).

#### Ethics in Cybersecurity
- **Confidentiality:** Protecting sensitive information.
- **Privacy:** Respecting user rights.
- **Professional Integrity:** Reporting vulnerabilities responsibly.
- **Laws & Regulations:** GDPR, HIPAA, etc.

#### Reflection: Connecting to My Hands-On Work
- **Identify & Protect:** My home lab (VirtualBox + Ubuntu) is set up with a NAT network – this isolates the VM, which falls under the *Protect* function of NIST CSF.
- **Detect:** My integrity checker (`integrity_checker.py`) detects unauthorized file changes – that's a classic *Detect* and *Respond* control.
- **Ethics:** By documenting my Bandit writeup without posting spoilers (as per OverTheWire rules), I practiced professional integrity.

---

## Module 4: Cybersecurity Tools and Programming Languages

### Key Concepts

#### Common Cybersecurity Tools

| Tool Category | Examples | What it does |
| :--- | :--- | :--- |
| **SIEM** | Splunk, Chronicle | Aggregates logs, correlates events, triggers alerts |
| **Firewall** | iptables, pfSense | Blocks or allows traffic based on rules |
| **Antivirus/EDR** | CrowdStrike, Windows Defender | Detects and blocks malware |
| **Vulnerability Scanner** | Nessus, OpenVAS | Scans for known vulnerabilities |
| **Network Sniffer** | Wireshark, tcpdump | Captures and analyzes network packets |

#### Programming & Query Languages
- **Linux:** The OS for most security tools.
- **SQL:** For querying databases (e.g., searching logs).
- **Python:** For automation, log parsing, and tool development.

#### Reflection: Connecting to My Hands-On Work
- **SIEM:** My `log_analyzer.py` simulates the *Detect* phase – it ingests logs, filters for failures, and alerts on thresholds.
- **Linux:** I used `grep`, `awk`-like tools (`cut`, `sort`, `uniq`), and `cron` – all core Linux skills for a SOC analyst.
- **Python:** Beyond the log analyzer, my `file_renamer.py`, `text_parser.py`, and `integrity_checker.py` demonstrate automation – a key skill for reducing manual work.

---

## Final Reflection: How This Course Connects to My Portfolio

I entered this course with hands-on experience from the Bandit wargame, Python scripting, and a home lab. This course gave me the **vocabulary** to describe what I already do:

| What I Did | What I Learned |
| :--- | :--- |
| `nmap`, `nc`, `openssl` | Network Security (CISSP Domain 4) |
| SSH key authentication (Levels 13, 16) | IAM (Identity and Access Management) |
| `log_analyzer.py` (SIEM-style alert) | Security Operations (SOC) |
| `integrity_checker.py` (file hashing) | Detect & Protect (NIST CSF) |
| VirtualBox + Ubuntu VM | Hardening, Isolation (Protect function) |

**Key Takeaway:** I am not just learning theory – I am building the technical skills that match the frameworks and domains taught in this course. This alignment is what employers want to see.

---

## Glossary (Key Terms)

| Term | Definition |
| :--- | :--- |
| **CIA Triad** | Confidentiality, Integrity, Availability – the core principles of security. |
| **Threat** | A potential danger (e.g., a hacker). |
| **Vulnerability** | A weakness that can be exploited (e.g., weak password). |
| **Risk** | The likelihood of a threat exploiting a vulnerability. |
| **Control** | A safeguard to reduce risk (e.g., firewall, MFA). |
| **SIEM** | Security Information and Event Management – aggregates and analyzes logs. |
| **NIST CSF** | National Institute of Standards and Technology Cybersecurity Framework. |
| **CISSP** | Certified Information Systems Security Professional – 8 domains. |
| **SOC** | Security Operations Center – where analysts monitor and respond. |
| **rbash** | Restricted Bash shell – a limited shell that can be escaped (I did this in Bandit 25). |

---

> *This document is part of my ongoing portfolio. I will revisit and refine these notes as I progress through Courses 2–8.*
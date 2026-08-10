# Course 2: Play It Safe – Manage Security Risks

**Completed:** August 10, 2026  
**Certificate:** Google Cybersecurity Professional Certificate  

---

## Module 1: Security Domains

### Key Concepts

#### The 8 CISSP Security Domains

1. **Security and Risk Management** – Defining security goals, risk tolerance, and compliance.
2. **Asset Security** – Protecting physical and digital assets (data, hardware, intellectual property).
3. **Security Architecture and Engineering** – Designing secure systems and networks.
4. **Communication and Network Security** – Securing data in transit (TCP/IP, firewalls, encryption, VPNs).
5. **Identity and Access Management (IAM)** – Controlling who has access to what (least privilege, MFA, SSO).
6. **Security Assessment and Testing** – Auditing, vulnerability scanning, penetration testing.
7. **Security Operations (SOC)** – Monitoring, detecting, and responding to incidents.
8. **Software Development Security** – Secure coding practices (OWASP, SDLC).

#### Threats, Risks, and Vulnerabilities

| Term | Definition | Example |
| :--- | :--- | :--- |
| **Threat** | A potential danger | A hacker attempting to brute‑force a password |
| **Vulnerability** | A weakness that can be exploited | A weak password policy (e.g., no complexity requirements) |
| **Risk** | The likelihood of a threat exploiting a vulnerability | The chance that a brute‑force attack succeeds |

#### NIST Risk Management Framework (RMF)

1. **Prepare:** Establish the context and stakeholders.
2. **Categorize:** Classify information and systems based on impact.
3. **Select:** Choose appropriate security controls.
4. **Implement:** Deploy the controls.
5. **Assess:** Evaluate if controls are working.
6. **Authorize:** Approve the system to operate.
7. **Monitor:** Continuously track and update controls.

---

## Module 2: Security Frameworks and Controls

### Key Concepts

#### Frameworks
- A structured approach to managing security risks.
- Provides a common language and methodology.

#### Controls
- Safeguards to reduce risk.

| Control Type | Purpose | Examples |
| :--- | :--- | :--- |
| **Administrative** | Policies and procedures | Security awareness training, incident response plans |
| **Technical** | Hardware/software solutions | Firewalls, encryption, MFA, IDS/IPS |
| **Physical** | Physical safeguards | Locks, CCTV, fire suppression |

#### The CIA Triad

| Pillar | Definition | Example |
| :--- | :--- | :--- |
| **Confidentiality** | Ensuring data is accessible only to authorized users | Encryption, access controls |
| **Integrity** | Ensuring data is accurate and unaltered | Hashing (SHA-256), digital signatures |
| **Availability** | Ensuring systems and data are accessible when needed | Backups, disaster recovery, redundancy |

#### NIST Cybersecurity Framework (CSF) – 6 Functions

1. **Govern:** Establish and monitor security strategy.
2. **Identify:** Understand assets, risks, and vulnerabilities.
3. **Protect:** Implement safeguards (firewalls, encryption, access controls).
4. **Detect:** Monitor for anomalies and alerts.
5. **Respond:** Take action during an incident.
6. **Recover:** Restore systems and learn from incidents.

#### OWASP Security Principles
- **Minimize attack surface** – Disable unnecessary services.
- **Least privilege** – Give users only the access they need.
- **Defense in depth** – Multiple layers of security.
- **Fail securely** – Default to deny.
- **Principle of least astonishment** – Make security intuitive.

#### Security Audits
- A systematic evaluation of an organization's security posture.
- **Process:** Scope → Risk Assessment → Review → Testing → Reporting.
- **Outcome:** Identify gaps, ensure compliance, and improve controls.

---

## Module 3: Introduction to Cybersecurity Tools

### Key Concepts

#### Logs
- Records of events that occur on systems, networks, and applications.
- **Types:** Web server logs, authentication logs, firewall logs, database logs, system logs.

#### SIEM (Security Information and Event Management)

| Capability | What it does | Why it matters |
| :--- | :--- | :--- |
| **Centralized Log Management** | Aggregates logs from all systems into one platform | Eliminates the need to manually check each system |
| **Automated Alerting** | Triggers alerts based on predefined rules | Enables real‑time detection |
| **Correlation** | Links events across systems to identify patterns | Helps identify complex attacks (e.g., DDoS + brute‑force) |
| **Visualization** | Provides dashboards with metrics and trends | Gives analysts a quick overview of the security posture |
| **Forensic Investigation** | Stores historical logs for post‑incident review | Supports compliance reporting and root‑cause analysis |

#### Common SIEM Tools
- **Splunk** – Industry leader, widely used in enterprise SOCs.
- **Chronicle** (Google Cloud) – Cloud‑native, integrates with Google Cloud.
- **Elastic Stack (ELK)** – Open‑source, highly customizable.
- **IBM QRadar** – Enterprise‑grade, strong correlation.

#### SOAR (Security Orchestration, Automation, and Response)
- Extends SIEM by automating incident response tasks (e.g., automatically blocking an IP).
- **Example:** A SIEM detects a brute‑force attack, and the SOAR tool automatically updates the firewall to block the offending IP.

---

## Module 4: Use Playbooks to Respond to Incidents

### Key Concepts

#### Incident Response Playbooks
- A documented set of procedures to follow during a security incident.
- **Purpose:** Standardize response, reduce errors, and ensure consistency.

#### NIST 4‑Step Incident Response Process

| Phase | Description | Example |
| :--- | :--- | :--- |
| **1. Preparation** | Train staff, set up tools, create IR plans | Installing `log_analyzer.py` and `integrity_checker.py` as monitoring tools |
| **2. Detection & Analysis** | Identify and investigate potential incidents | My log analyzer detects an IP with 5+ failed logins – that's detection! |
| **3. Containment & Eradication** | Isolate and remove the threat | Blocking the suspicious IP in a firewall |
| **4. Post‑Incident** | Document lessons learned and improve | Writing a report on what happened and how to prevent it |

#### Playbooks vs. SIEM vs. SOAR

| Tool | Purpose |
| :--- | :--- |
| **Playbook** | Documented procedures for responding to incidents |
| **SIEM** | Detects and alerts on incidents by analyzing logs |
| **SOAR** | Automates response tasks (e.g., blocking an IP, isolating a system) |

---

## How This Course Connects to My Hands‑On Work

| Course Concept | My Practical Experience |
| :--- | :--- |
| **CISSP Domains** | Network Security (Domain 4) – I used `nmap`, `nc`, and SSH in Bandit |
| **IAM** | SSH key authentication (Levels 13, 16) – access control in action |
| **NIST CSF** | Home lab VM isolation (Protect), `log_analyzer.py` (Detect) |
| **Security Controls** | `chmod 600` (technical), SSH keys (access control) |
| **CIA Triad** | `integrity_checker.py` (Integrity), backups (Availability) |
| **SIEM** | `log_analyzer.py` – parses logs and flags suspicious IPs (mini‑SIEM) |
| **Playbooks** | My Bandit writeup documents my troubleshooting process – similar to a playbook |

---

## Key Takeaways

1. **Frameworks provide structure** – NIST CSF, CIS Controls, and regulations (GDPR, PCI DSS) guide security programs.
2. **Controls are the building blocks** – administrative, technical, and physical controls work together to reduce risk.
3. **SIEM tools are force multipliers** – they centralize logs, automate alerts, and help SOC teams detect and respond faster.
4. **Playbooks ensure consistency** – a documented incident response plan reduces errors and speeds up recovery.
5. **Security protects the business** – stronger security means less downtime, fewer fines, and better customer trust.

---

> *This course gave me the vocabulary to describe what I already do in my home lab and Python scripts, and the framework to apply it professionally. The Botium Toys audit was a highlight – it let me apply everything I learned to a realistic business scenario.*
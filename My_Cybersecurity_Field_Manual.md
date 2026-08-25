# 🧠 My Cybersecurity Field Manual

> **Author:** Chadrack Kalongo  
> **Last Updated:** August 2026  
> **Context:** OverTheWire Bandit 0–25, Google Cybersecurity Certificate (Linux, SQL, Python) & Security Automation

---

## 📌 Table of Contents
1. [Git & GitHub Foundations](#-git--github-foundations)
2. [Linux Terminal & SSH Basics](#-linux-terminal--ssh-basics)
3. [Linux User & System Administration](#-linux-user--system-administration-google-cert)
4. [Getting Help in Linux](#-getting-help-in-linux-google-cert)
5. [Bandit Commands Reference (0–20)](#-bandit-commands-reference-020)
   - [Finding & Reading Files](#finding--reading-files)
   - [Searching & Parsing Text](#searching--parsing-text)
   - [Network & Ports](#network--ports)
   - [Encoding & Compression](#encoding--compression)
   - [SSH Keys & Privilege Escalation](#ssh-keys--privilege-escalation)
6. [Cron Jobs & Restricted Shells (rbash)](#-cron-jobs--restricted-shells-rbash)  <!-- NEW -->
   - [Cron Jobs](#cron-jobs)
   - [Restricted Shell (rbash)](#restricted-shell-rbash)
7. [SQL (Structured Query Language)](#-sql-structured-query-language)
8. [The Troubleshooting Hall of Fame](#-the-troubleshooting-hall-of-fame-the-struggles)
9. [Python Automation Toolkit](#-python-automation-toolkit)
10. [Assets, Threats, and Vulnerabilities](#-assets-threats-and-vulnerabilities)
   - [Asset Management & Classification](#asset-management--classification)
   - [Risk Assessment](#risk-assessment)
   - [Vulnerability Assessment](#vulnerability-assessment)
   - [Threat Modeling (PASTA)](#threat-modeling-pasta)
   - [Web-Based Exploits](#web-based-exploits)
   - [Social Engineering & Malware](#social-engineering--malware)
   - [Cryptography & Hashing](#cryptography--hashing)
11. [The "Pro" Takeaways](#-the-pro-takeaways-what-actually-changed-in-my-brain)

---

## 🗂️ Git & GitHub Foundations

| Command | What it does |
| :--- | :--- |
| `git config --global user.name "Your Name"` | Set your identity (one-time setup). |
| `git config --global user.email "your@email.com"` | Set your email (one-time setup). |
| `git clone https://github.com/.../repo.git` | Download a remote repo to your machine. |
| `git status` | Check what has changed. |
| `git add .` | Stage all changes in the current folder. |
| `git commit -m "message"` | Save staged changes with a comment. |
| `git push` | Upload commits to GitHub. |
| `git rm filename.txt` | Remove a file from the repo. |

### 🚨 The Token Trap
- **Problem:** GitHub no longer accepts your normal password for `git push`.
- **Solution:** Generate a **Personal Access Token** (Settings → Developer settings → Tokens).  
  Use that token as the password when `git push` asks for it.

---

## 🖥️ Linux Terminal & SSH Basics

| Command | What it does |
| :--- | :--- |
| `cd ~/Desktop` | Navigate to your Desktop. |
| `cd ..` | Move up one folder level. |
| `ls -la` | List all files (including hidden) with details. |
| `cat filename.txt` | Print the file content to the screen. |
| `touch filename.txt` | Create an empty file. |
| `cp source.txt dest.txt` | Copy a file. |
| `mv old.txt new.txt` | Rename or move a file. |
| `chmod 600 filename` | Make a file only readable/writable by you. |

### 🚨 The "Silent Password" Trap
- **Problem:** When SSH asks for a password, **nothing appears** on screen (no dots, no asterisks).
- **Solution:** Type the password blindly and press Enter. Your keystrokes are being registered.

---

## ⚙️ Bandit Commands Reference (0–20)

### Finding & Reading Files
| Command | What it does |
| :--- | :--- |
| `cat ./-` | Read a file literally named `-` (needs `./`). |
| `cat "./--spaces in this filename--"` | Read a file with spaces and double-dashes. |
| `file ./*` | Show the *type* of every file in the current folder. |
| `find . -size 1033c ! -executable` | Find non-executable files of exact size 1033 bytes. |
| `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null` | Global search, hiding permission errors. |

### Searching & Parsing Text
| Command | What it does |
| :--- | :--- |
| `grep "millionth" data.txt` | Find lines containing the word "millionth". |
| `sort data.txt \| uniq -u` | Show only the line that appears exactly once. |
| `strings data.txt \| grep "="` | Extract readable text from binary, filter for `=`. |
| `diff file1 file2` | Show the differences between two files. |

### Network & Ports
| Command | What it does |
| :--- | :--- |
| `ssh banditX@host -p 2220` | Connect to a remote OverTheWire server. |
| `echo "password" \| nc localhost 30000` | Send data to a local port via Netcat. |
| `openssl s_client -connect localhost:30001` | Connect to an SSL/TLS encrypted port. |
| `nmap -sV -p 31000-32000 localhost` | Scan local ports to find running services. |

### Encoding & Compression
| Command | What it does |
| :--- | :--- |
| `cat data.txt \| tr 'A-Za-z' 'N-ZA-Mn-za-m'` | Decode ROT13 (rotate letters by 13). |
| `base64 -d data.txt` | Decode a Base64 file. |
| `xxd -r data.txt > file1` | Reverse a hexdump. |
| `gzip -d file1.gz` | Decompress Gzip. |
| `bzip2 -d file1.bz2` | Decompress Bzip2. |
| `tar xf file1.tar` | Extract a Tar archive. |

### SSH Keys & Privilege Escalation
| Command | What it does |
| :--- | :--- |
| `chmod 600 sshkey.private` | Make a private key secure (SSH demands this). |
| `ssh -i sshkey.private user@host -p 2220` | Log in using a private key. |
| `./bandit20-do cat /etc/bandit_pass/bandit20` | Run a command as another user via SetUID. |
| `ssh bandit18@host -p 2220 "cat readme"` | Run a remote command without loading `.bashrc`. |

---

## 🤖 Cron Jobs & Restricted Shells (rbash)

### Cron Jobs
**What it is:** Cron is a time‑based job scheduler. It runs commands or scripts automatically at specific times (e.g., every minute, every hour, at reboot).

**Why it matters for security:** Attackers often look for misconfigured cron jobs to escalate privileges. If a cron job runs as `root` and executes a script in a world‑writable directory, an attacker can replace that script with malicious code.

**Key Locations (on OverTheWire/Linux):**
- `/etc/cron.d/` – System‑wide cron jobs (often show the user who runs them).
- `/var/spool/cron/` – User‑specific cron files.
- `crontab -l` – View your own cron jobs.

**Syntax to remember:**

command_to_run
│ │ │ │ │
│ │ │ │ └─── Day of week (0-6)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)

Example: `* * * * * bandit22 /usr/bin/cronjob_bandit22.sh` runs every minute as user `bandit22`.

**My key lessons:**
- Always check **who** owns the cron job (the user column). If it runs as a higher‑privileged user, it's a target.
- If a cron job executes **every script** in a directory (like `/var/spool/bandit24/foo/`), you can plant your own script to read a password file and dump it to a location you control.
- Cron scripts often write passwords or output to `/tmp/` – always check there if a script mentions a temp file.

---

### Restricted Shell (rbash)
**What it is:** `rbash` (restricted bash) is a locked‑down shell that limits what you can do. It typically restricts:
- Changing directories (`cd`)
- Setting environment variables (`export`)
- Using absolute paths (`/bin/ls` instead of `ls`)
- Running commands that contain `/` or `..`

**Why you'll see it:** It is often used to trap players in a sandbox (like `bandit26`). Escaping it demonstrates a real‑world penetration testing skill.

**The Classic Escape (The `vi` Trick):**
1. Log in as the user (usually via an SSH key).
2. If the login automatically runs a pager like `more` (e.g., `/usr/bin/showtext`), **shrink your terminal** (`stty rows 1`) to force the pager to pause.
3. When `more` pauses, press **`v`** to open the `vi` editor.
4. Inside `vi`, type:
   ```vim
   :set shell=/bin/sh
   :shell

Alternative Bypass (Direct Command):
If you only need to read one file, you can skip the restricted shell entirely:

`ssh -i key user@host -p 2220 "cat /etc/bandit_pass/nextlevel"`

---

## 🧩 The Troubleshooting Hall of Fame (The Struggles)

### 1. The SSH Key `libcrypto` Error
- **Situation:** `ssh -i key.txt user@host` gave `error in libcrypto: unsupported` on Windows Git Bash.
- **Why:** My local SSH client was too old for the new OpenSSH key format.
- **Solution:** Wrote a Python script using `paramiko` to load the key and fetch the password.

**Python template (memory aid):**
```python
import paramiko
key_path = r"C:\path\to\key.txt"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
private_key = paramiko.RSAKey.from_private_key_file(key_path)
client.connect(hostname="bandit.labs.overthewire.org", port=2220, username="banditX", pkey=private_key)
# Run your command...
```

### 2. The `localhost` Connection Block
- **Situation:** Tried `ssh bandit14@localhost -p 2220` from inside a server. Got "Connecting from localhost is blocked".
- **Why:** OverTheWire blocks password logins from localhost to force SSH key usage.
- **Solution:** Always jump to the next level from my **local machine** (outside SSH), or use the key method without interactive passwords.

---

### 3. The `diff` Mix-up (Level 17 → 18)
- **Situation:** Ran `diff passwords.new passwords.old`. Output showed `< OLD` and `> NEW`.
- **My mistake:** I tried the line with `>` (thinking "greater" = newer). It failed.
- **Rule:** `diff file1 file2` → `file1` is on the left (`<`). Since `passwords.new` is on the left, the password is the line after `<`!
- **Takeaway:** Always read the context of the output carefully.

---

### 4. The `.bashrc` Instant Logout (Level 18)
- **Situation:** Logged into `bandit18` and got kicked out immediately.
- **Why:** The `.bashrc` file was modified to disconnect users.
- **Solution:** Bypass the login shell by running a command remotely:  
  `ssh bandit18@host -p 2220 "cat readme"`.

---

## 🛠️ Linux User & System Administration (Google Cert)

### User & Group Management

| Command | What it does | Example |
| :--- | :--- | :--- |
| `sudo useradd <username>` | Creates a new user account | `sudo useradd researcher9` |
| `sudo usermod -g <group> <user>` | Sets the **primary group** for a user | `sudo usermod -g research_team researcher9` |
| `sudo usermod -a -G <group> <user>` | Adds a user to a **secondary (supplementary) group** | `sudo usermod -a -G sales_team researcher9` |
| `sudo userdel <username>` | Deletes a user account | `sudo userdel researcher9` |
| `sudo groupdel <groupname>` | Deletes a group | `sudo groupdel researcher9` |
| `sudo chown <user> <file>` | Changes the **owner** of a file or directory | `sudo chown researcher9 /home/researcher2/projects/project_r.txt` |
| `sudo chown :<group> <file>` | Changes the **group** ownership of a file | `sudo chown :research_team project_r.txt` |

### File & Directory Permissions (chmod)

| Symbolic | Octal | What it does |
| :--- | :--- | :--- |
| `u=r` | `400` | User has read‑only access |
| `g=r` | `040` | Group has read‑only access |
| `o-w` | `222` | Remove write permission for others |
| `g-x` | `111` | Remove execute permission for group |
| `u=rwx,g=rx,o=` | `750` | User: full, Group: read+execute, Others: none |

**My lab examples:**
```bash
# Remove write access for "others" on project_k.txt
chmod o-w project_k.txt

# Set user and group to read‑only on a hidden file
chmod u=r,g=r .project_x.txt

# Remove execute permission from the group on a directory
chmod g-x drafts
```

---

## 📖 Getting Help in Linux (Google Cert)

| Command | What it does | Example |
| :--- | :--- | :--- |
| `whatis <command>` | Shows a **one‑line description** of a command | `whatis cat` → `"concatenate files and print on standard output"` |
| `man <command>` | Opens the **full manual page** for a command | `man useradd` (press `q` to exit, `space` to page down) |
| `grep <keyword> <file>` | Searches inside a file (or manual page) for a keyword | `man cat \| grep number` (finds options for numbering lines) |
| `apropos <keyword>` | Searches **all** manual pages for a keyword – great when you forget the exact command name | `apropos "create new group"` → returns `groupadd` |

> 💡 **Pro tip:** If you forget the exact command, use `apropos` or `man -k <keyword>`.

**Example:**

```bash
man -k "create new group"
# Outputs: groupadd (8) - create a new group
```

---



## 🗄️ SQL (Structured Query Language)

### What is SQL?
SQL is used to interact with relational databases. For security professionals, it is essential for:
- Investigating login attempts and access logs
- Auditing user permissions and machine assignments
- Identifying suspicious activity (e.g., after‑hours logins, unusual locations)
- Generating reports for compliance and incident response

---

### Core SQL Components

| Component | Description |
| :--- | :--- |
| **SELECT** | Specifies which columns to retrieve |
| **FROM** | Specifies the table to query |
| **WHERE** | Filters rows based on conditions |
| **ORDER BY** | Sorts results (ASC or DESC) |
| **JOIN** | Combines two tables on a common column |

---

### Common SQL Operators (Filters)

| Operator | Purpose | Security Example |
| :--- | :--- | :--- |
| `=` | Equals | `WHERE department = 'Marketing'` |
| `>` / `<` | Greater than / Less than | `WHERE login_time > '18:00'` |
| `>=` / `<=` | Greater than or equal / Less than or equal | `WHERE login_date >= '2023-01-15'` |
| `BETWEEN` | Range of values | `WHERE login_date BETWEEN '2023-02-01' AND '2023-02-07'` |
| `AND` | Both conditions must be true | `WHERE login_time > '18:00' AND success = 0` |
| `OR` | At least one condition is true | `WHERE department = 'Sales' OR department = 'Finance'` |
| `NOT` | Excludes a condition | `WHERE NOT department = 'Information Technology'` |
| `LIKE` | Pattern matching (use `%` wildcard) | `WHERE country NOT LIKE 'MEX%'` |
| `IN` | Matches any value in a list | `WHERE department IN ('Sales', 'Finance', 'Marketing')` |

---

### SQL Joins

| Join Type | What it does |
| :--- | :--- |
| **INNER JOIN** | Returns only rows that have a match in both tables |
| **LEFT JOIN** | Returns all rows from the left table, and matches from the right table |
| **RIGHT JOIN** | Returns all rows from the right table, and matches from the left table |
| **FULL OUTER JOIN** | Returns all records from both tables. It matches rows that share a common value, and for rows without a match |

**Example – INNER JOIN (employees ↔ machines):**
```sql
SELECT *
FROM machines
INNER JOIN employees ON machines.device_id = employees.device_id;
```
---

### Aggregate Functions

| Function | Purpose |
| :--- | :--- |
| `COUNT(*)` | Returns the total number of rows |
| `AVG(column)` | Returns the average of a numeric column |
| `SUM(column)` | Returns the sum of a numeric column |

**Example – Counting all employees:**

```sql
SELECT COUNT(firstname) FROM employees;
```

Example – Counting employees from a specific country:

```sql
SELECT COUNT(firstname) FROM employees WHERE country = 'USA';
```

---

### Pro Tips

LIKE with `%`: Use `%` as a wildcard.
`LIKE 'East-%'` → matches "East-170", "East-320", etc.
`LIKE 'MEX%'` → matches "MEX" and "MEXICO".

Quotes: String values must be in single quotes (e.g., `'Marketing'`). Numbers and Booleans (`TRUE`/`FALSE`) do not need quotes.

Semicolon: Every SQL statement must end with a `; or the shell will wait for more input.

Table.column notation: When joining tables, use `table.column` to avoid ambiguity (e.g., `machines.device_id` vs `employees.device_id`).
``


---



## 🐍 Python Automation Toolkit

| Script | What it does |
| :--- | :--- |
| `file_renamer.py` | Add a prefix (`backup_`) to every file in a folder using `os.listdir()` and `os.rename()`. |
| `text_parser.py` | Count how many lines contain "ERROR" using `open().readlines()` and `if word in line`. |
| `folder_scanner.py` | Walk through folders and count file extensions using `os.walk()` and `os.path.splitext()`. |
| `fetch_banditX_password.py` | Use `paramiko` to authenticate with an SSH key when the local CLI fails. |

---

## 🧠 Assets, Threats, and Vulnerabilities

---

### Asset Management & Classification

#### What is an Asset?
An asset is anything of value to an organization, including:
- **Physical assets:** Hardware, servers, laptops, routers, storage devices.
- **Digital assets:** Data, databases, intellectual property, customer information.
- **Human assets:** Employees, contractors, partners.
- **Intangible assets:** Brand reputation, customer trust.

#### Asset Classification (Sensitivity Levels)

| Level | Definition | Examples |
| :--- | :--- | :--- |
| **Public** | No impact if disclosed. | Marketing materials, public website content. |
| **Internal-Only** | Minor impact if disclosed. | Internal policies, employee directories. |
| **Confidential** | Moderate to severe impact if breached. | Customer PII, financial records, business plans. |
| **Restricted** | Severe to critical impact if breached. | Encryption keys, root credentials, classified data. |

#### Asset Inventory
- A catalog of all assets that need to be protected.
- Includes: Asset name, owner, location, network access, sensitivity level.
- **Why it matters:** You cannot protect what you don't know exists.

**My lab example:**
I created a home office asset inventory with devices like Network Router (Restricted), Work Laptop (Confidential), and Smart TV (Public/Internal-Only). This helped me prioritize security controls for the most sensitive assets.

---

### Risk Assessment

#### What is Risk?
Risk = Likelihood × Impact

| Term | Definition |
| :--- | :--- |
| **Threat** | A potential danger (e.g., a hacker, a natural disaster). |
| **Vulnerability** | A weakness that can be exploited (e.g., a missing patch). |
| **Risk** | The likelihood of a threat exploiting a vulnerability. |
| **Control** | A safeguard to reduce risk (e.g., firewall, MFA). |

#### NIST SP 800-30 Rev. 1 Risk Assessment Process

| Step | Description |
| :--- | :--- |
| 1. Identify Threat Sources | Who or what could cause harm? (e.g., hackers, employees, natural disasters). |
| 2. Identify Threat Events | What could happen? (e.g., data exfiltration, DoS attack). |
| 3. Determine Likelihood | How likely is the event? (Score 1-3: Low, Moderate, High). |
| 4. Determine Severity | What is the impact? (Score 1-3: Low, Moderate, High). |
| 5. Calculate Risk | Likelihood × Severity = Risk Score (1-9). |
| 6. Prioritize | Focus on high-risk items first. |

#### Risk Register Example

| Asset | Risk | Likelihood | Severity | Priority |
| :--- | :--- | :--- | :--- | :--- |
| Funds | Business Email Compromise | 3 | 3 | **9** (Critical) |
| Funds | Financial Records Leak | 2 | 3 | **6** (High) |
| Funds | Theft | 1 | 3 | **3** (Medium) |

**My lab example:** I completed a risk register for a commercial bank, scoring Business Email Compromise as a critical risk (9) because of its high likelihood and severe impact.

---

### Vulnerability Assessment

#### What is a Vulnerability Assessment?
- A systematic review of an organization's security systems to identify weaknesses.
- Uses frameworks like **NIST SP 800-30 Rev. 1** to guide risk analysis.
- Outcome: A report with identified risks, likelihood/severity scores, and remediation recommendations.

#### Threat Sources (NIST SP 800-30)

| Type | Examples |
| :--- | :--- |
| **Human** | Employees, hackers, competitors, nation-states. |
| **Technological** | Hardware failures, software bugs, network issues. |
| **Environmental** | Natural disasters, power outages, temperature failures. |

#### Threat Events (Examples)

| Threat Event | Description |
| :--- | :--- |
| **Reconnaissance** | Attackers scan for vulnerabilities. |
| **Data Exfiltration** | Sensitive data is stolen. |
| **SQL Injection** | Malicious SQL queries are injected into input fields. |
| **Denial of Service (DoS)** | Systems are overwhelmed with requests. |
| **Man-in-the-Middle (MITM)** | Communication is intercepted. |
| **Phishing** | Users are tricked into revealing credentials. |

#### Remediation Strategy

| Control | Purpose |
| :--- | :--- |
| **IP Allow-listing** | Restrict access to trusted sources. |
| **Multi-Factor Authentication (MFA)** | Add an extra layer of authentication. |
| **Encryption (TLS & AES)** | Protect data in transit and at rest. |
| **Role-Based Access Controls (RBAC)** | Enforce least privilege. |
| **SIEM Monitoring** | Detect and alert on suspicious activity. |
| **Regular Audits & Penetration Testing** | Identify vulnerabilities proactively. |

**My lab example:** I conducted a vulnerability assessment for an e‑commerce company with a publicly accessible database server. I identified threats (reconnaissance, data exfiltration), scored them (Likelihood 2-3, Severity 2-3), and proposed a remediation strategy including IP allow-listing, MFA, and SIEM monitoring.

---

### Threat Modeling (PASTA)

#### What is Threat Modeling?
- A structured approach to identifying security requirements and potential risks in a system.
- Helps integrate security into the software development lifecycle.

#### PASTA Framework (7 Stages)

| Stage | Objective |
| :--- | :--- |
| **I. Define Business Objectives** | Understand why the app is built and what it needs to do. |
| **II. Define Technical Scope** | Identify the technology stack (API, PKI, SQL, etc.). |
| **III. Decompose Application** | Create a Data Flow Diagram to show how data moves. |
| **IV. Threat Analysis** | Identify internal and external threats. |
| **V. Vulnerability Analysis** | List vulnerabilities that could be exploited. |
| **VI. Attack Modeling** | Build an Attack Tree to visualize attack paths. |
| **VII. Risk Analysis & Impact** | Recommend security controls to reduce risk. |

#### Data Flow Diagram (DFD)
- Visual representation of how data flows through an application.
- Shows: Users, processes, databases, external services, and communication paths.

#### Attack Tree
- Visual representation of possible attack paths.
- Goal at the root, branches representing different attack vectors.
- Helps stakeholders understand how an attacker could compromise the system.

**My lab example:** I performed a PASTA threat model for a sneaker company app. I identified business objectives (connect buyers/sellers, secure payments), technical scope (API, PKI, SHA-256, SQL), threats (internal/external), vulnerabilities (SQL injection, weak session management), and recommended controls (input validation, MFA, encryption, rate limiting).

---

### Web-Based Exploits

| Exploit | Description | Example |
| :--- | :--- | :--- |
| **SQL Injection** | Malicious SQL queries injected into input fields. | `' OR '1'='1` bypasses authentication. |
| **Cross-Site Scripting (XSS)** | Malicious scripts injected into web pages. | Stealing session cookies via `<script>` tags. |
| **Parameter Tampering / IDOR** | Modifying URL or form parameters to access unauthorized data. | Changing `user_id=123` to `user_id=124`. |
| **Cross-Site Request Forgery (CSRF)** | Tricking a user into performing unwanted actions. | Making a user change their email address. |
| **Session Hijacking** | Stealing a user's session token. | Using stolen cookies to impersonate a user. |

---

### Social Engineering & Malware

#### Social Engineering Techniques

| Technique | Description |
| :--- | :--- |
| **Phishing** | Mass emails impersonating a trusted source. |
| **Spear Phishing** | Targeted phishing for a specific individual. |
| **Whaling** | Phishing targeting high‑profile executives. |
| **Vishing** | Voice phishing (over the phone). |
| **Smishing** | SMS phishing (via text messages). |
| **Baiting** | Leaving malware‑infected physical devices (e.g., USB drives). |
| **Tailgating** | Following an authorized person into a secure area. |
| **Pretexting** | Creating a false scenario to obtain information. |

#### Common Malware Types

| Type | Description |
| :--- | :--- |
| **Worm** | Self‑replicates and spreads across networks. |
| **Virus** | Requires a host file and user action to spread. |
| **Trojan** | Disguised as legitimate software. |
| **Ransomware** | Encrypts files and demands payment. |
| **Spyware** | Secretly monitors user activity. |
| **Adware** | Displays unwanted advertisements. |
| **Rootkit** | Hides its presence and grants privileged access. |
| **Keylogger** | Records keystrokes to steal credentials. |

**My lab example:** I analyzed a phishing email targeting an executive and identified red flags (sender domain, misspelling, urgency). I also identified malware types like worms and ransomware in the dialogue activity.

---

### Cryptography & Hashing

#### Encryption vs. Hashing

| Feature | Encryption | Hashing |
| :--- | :--- | :--- |
| **Reversible?** | Yes (with the correct key) | No (one‑way function) |
| **Purpose** | Protect confidentiality | Verify integrity |
| **Examples** | AES, RSA | SHA-256, MD5 |
| **Output** | Ciphertext | Fixed‑length hash (digest) |

#### Caesar Cipher
- One of the earliest encryption techniques.
- Shifts letters by a fixed number (e.g., shift of 3: A→D, B→E).
- Decoded using `tr` in Linux:
  ```bash
  cat encrypted.txt | tr 'A-Za-z' 'D-ZA-Cd-za-c'
```

**SHA-256 Hashing**
- Produces a 256‑bit hash value.

- Used to verify file integrity:

```bash
sha256sum file.txt
```

- Even a tiny change in a file produces a completely different hash.

My lab example: I decrypted a Caesar cipher in Linux using tr and used `sha256sum` to verify that two files were not identical (they had different hashes).

---


## 💡 The "Pro" Takeaways (What Actually Changed in My Brain)

1. **No Output = Success.**  
   In Linux, silence means "it worked". Don't panic if you don't see a confirmation message.

2. **Verification is King.**  
   Always `ls` before `cat`. Always `file` before decompressing. Never assume filenames.

3. **When to Quit Fighting.**  
   If a CLI tool gives you a weird error after 15 minutes, switch to Python. Don't brute-force the terminal.

4. **Hidden Characters are Real.**  
   Copy-paste can add invisible newlines. If a password fails, try typing it manually.

5. **Python is Your Safety Net.**  
   Tools like `paramiko` work on Windows, Mac, and Linux. Learning Python for automation makes you immune to local CLI inconsistencies.

---

> *This manual was built from real struggles, late-night debugging, and one very persistent student. Keep it close — it will save you hours in the future.* 🔥



# 🧠 My Cybersecurity Field Manual

> **Author:** Chadrack Kalongo  
> **Last Updated:** August 2026  
> **Context:** OverTheWire Bandit 0–25 & Python Automation

---

## 📌 Table of Contents
1. [Git & GitHub Foundations](#-git--github-foundations)
2. [Linux Terminal & SSH Basics](#-linux-terminal--ssh-basics)
3. [Bandit Commands Reference (0–20)](#-bandit-commands-reference-020)
   - [Finding & Reading Files](#finding--reading-files)
   - [Searching & Parsing Text](#searching--parsing-text)
   - [Network & Ports](#network--ports)
   - [Encoding & Compression](#encoding--compression)
   - [SSH Keys & Privilege Escalation](#ssh-keys--privilege-escalation)
4. [Cron Jobs & Restricted Shells (rbash)](#-cron-jobs--restricted-shells-rbash)  <!-- NEW -->
   - [Cron Jobs](#cron-jobs)
   - [Restricted Shell (rbash)](#restricted-shell-rbash)
5. 5. [SQL (Structured Query Language)](#-sql-structured-query-language)
6. [The Troubleshooting Hall of Fame](#-the-troubleshooting-hall-of-fame-the-struggles)
7. [Python Automation Toolkit](#-python-automation-toolkit)
8. [The "Pro" Takeaways](#-the-pro-takeaways-what-actually-changed-in-my-brain)

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

===


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

**Example – INNER JOIN (employees ↔ machines):**
```sql
SELECT *
FROM machines
INNER JOIN employees ON machines.device_id = employees.device_id;
```
===

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


===



## 🐍 Python Automation Toolkit

| Script | What it does |
| :--- | :--- |
| `file_renamer.py` | Add a prefix (`backup_`) to every file in a folder using `os.listdir()` and `os.rename()`. |
| `text_parser.py` | Count how many lines contain "ERROR" using `open().readlines()` and `if word in line`. |
| `folder_scanner.py` | Walk through folders and count file extensions using `os.walk()` and `os.path.splitext()`. |
| `fetch_banditX_password.py` | Use `paramiko` to authenticate with an SSH key when the local CLI fails. |

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



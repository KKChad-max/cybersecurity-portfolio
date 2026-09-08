# 🧠 My Cybersecurity Field Manual

> **Author:** Chadrack Kalongo  
> **Last Updated:** September 2026  
> **Context:** OverTheWire Bandit 0–25, Google Cybersecurity Certificate (Linux, SQL, Python) & Security Automation

---

## 📌 Table of Contents
1. [Git & GitHub Foundations](#-git--github-foundations)
2. [Linux Terminal & SSH Basics](#-linux-terminal--ssh-basics)
3. [Linux User & System Administration](#-linux-user--system-administration-google-cert)
4. [Getting Help in Linux](#-getting-help-in-linux-google-cert)
5. [Bandit Commands Reference (0–25)](#-bandit-commands-reference-025)
   - [Finding & Reading Files](#finding--reading-files)
   - [Searching & Parsing Text](#searching--parsing-text)
   - [Network & Ports](#network--ports)
   - [Encoding & Compression](#encoding--compression)
   - [SSH Keys & Privilege Escalation](#ssh-keys--privilege-escalation)
6. [Cron Jobs & Restricted Shells (rbash)](#-cron-jobs--restricted-shells-rbash)
   - [Cron Jobs](#cron-jobs)
   - [Restricted Shell (rbash)](#restricted-shell-rbash)
7. [SQL (Structured Query Language)](#-sql-structured-query-language)
8. [The Troubleshooting Hall of Fame](#-the-troubleshooting-hall-of-fame-the-struggles)
9. [Python in Cybersecurity](#-python-in-cybersecurity)
   - [Core Python Syntax](#core-python-syntax)
   - [File Handling & Parsing](#file-handling--parsing)
   - [Regular Expressions (RegEx)](#regular-expressions-regex)
   - [Debugging Strategies](#debugging-strategies)
   - [Automation Scripts](#automation-scripts)
10. [Assets, Threats, and Vulnerabilities](#-assets-threats-and-vulnerabilities)
   - [Asset Management & Classification](#asset-management--classification)
   - [Risk Assessment](#risk-assessment)
   - [Vulnerability Assessment](#vulnerability-assessment)
   - [Threat Modeling (PASTA)](#threat-modeling-pasta)
   - [Web-Based Exploits](#web-based-exploits)
   - [Social Engineering & Malware](#social-engineering--malware)
   - [Cryptography & Hashing](#cryptography--hashing)
11. [🎓 Computing Fundamentals (NCC Diploma)](#-computing-fundamentals-ncc-diploma)
    - [Object-Oriented Programming (OOP) Principles](#object-oriented-programming-oop-principles)
    - [Software Development Lifecycle (SDLC)](#software-development-lifecycle-sdlc)
    - [Data Structures & Algorithms](#data-structures--algorithms)
    - [Databases & Normalization](#databases--normalization)
    - [Networking & the OSI Model](#networking--the-osi-model)
12. [The "Pro" Takeaways](#-the-pro-takeaways-what-actually-changed-in-my-brain)

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
| `git pull origin main` | Fetch and merge remote changes (used when `git push` is rejected). |
| `git pull --rebase origin main` | Fetch remote changes and rebase local commits on top (cleaner history). |
| `git sync` | **Alias command** – pulls remote changes with rebase and pushes in one go. |
| `git rm filename.txt` | Remove a file from the repo. |

### 🚨 The Token Trap
- **Problem:** GitHub no longer accepts your normal password for `git push`.
- **Solution:** Generate a **Personal Access Token** (Settings → Developer settings → Tokens).  
  Use that token as the password when `git push` asks for it.

---

## 📁 Portfolio Management Commands

These commands are used daily to manage the files and folders in your repository.

| Command | What it does | Example |
| :--- | :--- | :--- |
| `mkdir <folder>` | Create a new directory. | `mkdir google-cert-labs/course-7-python` |
| `touch <file>` | Create a new empty file. | `touch notes.md` |
| `notepad <file>` | Open a file in Windows Notepad for editing. | `notepad README.md` |
| `code <file>` | Open a file or folder in VS Code. | `code .` |
| `cp <source> <dest>` | Copy a file or folder. | `cp ~/Desktop/screenshot.png images/` |
| `mv <old> <new>` | Move or rename a file. | `mv old.md new.md` |
| `rm <file>` | Delete a file. | `rm test.txt` |
| `rmdir <folder>` | Delete an empty directory. | `rmdir temp/` |
| `rm -rf <folder>` | **⚠️ Force delete** a folder and all its contents (use with caution!). | `rm -rf old-backup/` |
| `ls` | List files in the current directory. | `ls` |
| `pwd` | Show the current working directory path. | `pwd` |
| `cd <path>` | Change directory. | `cd ~/cybersecurity-portfolio` |

### 💡 My Typical Workflow

```bash
# 1. Navigate to the repo
cd ~/cybersecurity-portfolio

# 2. Create a new folder for a module
mkdir -p google-cert-labs/course-7-python

# 3. Create a new file
touch notes.md

# 4. Edit the file
notepad notes.md

# 5. Copy a screenshot into the repo
cp ~/Desktop/screenshot.png google-cert-labs/course-7-python/images/

# 6. Stage, commit, and sync
git add .
git commit -m "Add notes and screenshot"
git sync
```

### 🛠️ My Git Workflow

After setting up the `git sync` alias, my standard workflow is:

```bash
# 1. Make changes to files
# 2. Stage and commit
git add .
git commit -m "Describe your changes"

# 3. Sync with GitHub (pull + push in one command)
git sync
```

If `git sync` fails (e.g., due to a conflict), I use:

```bash
git pull origin main
# Resolve any conflicts, then:
git push
```

**Alias setup (one-time):**

```bash
git config --global alias.sync '!git pull --rebase && git push'
```

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

## ⚙️ Bandit Commands Reference (0–25)

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
| :--- | :--- | :--- |
| `chmod 600 sshkey.private` | Make a private key secure (SSH demands this). |
| `ssh -i sshkey.private user@host -p 2220` | Log in using a private key. |
| `./bandit20-do cat /etc/bandit_pass/bandit20` | Run a command as another user via SetUID. |
| `ssh bandit18@host -p 2220 "cat readme"` | Run a remote command without loading `.bashrc`. |

### Cron Jobs & Advanced Bandit (Levels 21–25)
| Command | What it does |
| :--- | :--- | :--- |
| `cat /etc/cron.d/cronjob_bandit22` | View scheduled cron jobs for bandit22. |
| `cat /usr/bin/cronjob_bandit22.sh` | Read the script executed by the cron job. |
| `echo "I am user bandit23" \| md5sum \| cut -d ' ' -f 1` | Compute MD5 hash to find the temp file name. |
| `cat /tmp/<hash>` | Read the password written by the cron script. |
| `cp grab.sh /var/spool/bandit24/foo/` | Plant a script in the cron spool directory. |
| `for i in {0000..9999}; do echo "$PASS $i" \| nc localhost 30002; done` | Brute-force a 4-digit PIN on port 30002. |
| `ssh -i bandit26.sshkey bandit26@localhost -p 2220` | Connect using an SSH key (Level 25). |
| `stty rows 1` | Shrink terminal to force `more` pager pause (rbash escape). |
| `:set shell=/bin/sh` and `:shell` | Escape `rbash` using the `vi` trick. |

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

```text
command_to_run
│ │ │ │ │
│ │ │ │ └─── Day of week (0-6)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

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
   ```

**Alternative Bypass (Direct Command):**
If you only need to read one file, you can skip the restricted shell entirely:

```bash
ssh -i key user@host -p 2220 "cat /etc/bandit_pass/nextlevel"
```

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

### 3. The `diff` Mix-up (Level 17 → 18)
- **Situation:** Ran `diff passwords.new passwords.old`. Output showed `< OLD` and `> NEW`.
- **My mistake:** I tried the line with `>` (thinking "greater" = newer). It failed.
- **Rule:** `diff file1 file2` → `file1` is on the left (`<`). Since `passwords.new` is on the left, the password is the line after `<`!
- **Takeaway:** Always read the context of the output carefully.

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

**Example – Counting employees from a specific country:**

```sql
SELECT COUNT(firstname) FROM employees WHERE country = 'USA';
```

---

### Pro Tips

- **LIKE with `%`:** Use `%` as a wildcard.  
  `LIKE 'East-%'` → matches "East-170", "East-320", etc.  
  `LIKE 'MEX%'` → matches "MEX" and "MEXICO".
- **Quotes:** String values must be in single quotes (e.g., `'Marketing'`). Numbers and Booleans (`TRUE`/`FALSE`) do not need quotes.
- **Semicolon:** Every SQL statement must end with a `;` or the shell will wait for more input.
- **Table.column notation:** When joining tables, use `table.column` to avoid ambiguity (e.g., `machines.device_id` vs `employees.device_id`).

---

## 🐍 Python in Cybersecurity

Python is the backbone of my security automation workflow. It allows me to parse logs, update access control lists, and detect threats programmatically. Below is a reference for the core concepts, file handling techniques, regex patterns, and debugging strategies I've used throughout Course 7.

---

### Core Python Syntax

| Concept | Syntax / Example | Purpose |
| :--- | :--- | :--- |
| **Variables & Data Types** | `device_id = "72e08x0"` (str), `max_logins = 3` (int), `is_logged_in = False` (bool), `user_list = ["alice", "bob"]` (list) | Store and manage security data (device IDs, thresholds, statuses, allow lists). |
| **Conditionals** | `if system == "OS 2": print("No update needed") elif system == "OS 1": print("Update needed") else: print("Unknown OS")` | Automate decision-making based on security conditions (e.g., OS version, login time, IP checks). |
| **Loops** | `for element in remove_list:` | Iterate through lists of IPs, usernames, or log lines to perform bulk actions (removals, counts, searches). |
| **Functions** | `def update_file(import_file, remove_list):` | Encapsulate reusable logic. I used this to create a modular allow-list updater that can be called with different files. |
| **`in` Operator** | `if element in ip_addresses:` | Check membership in a list (e.g., verify if an IP is currently in the allow list). |
| **`.index()` Method** | `ind = approved_users.index(username)` | Find the position of a specific user in a list to retrieve corresponding data from a synchronized list (e.g., their assigned device ID). |

**Example: Authentication Algorithm (From Bandit Lab)**
```python
def login(username, device_id):
    if username in approved_users:
        ind = approved_users.index(username)
        if device_id == approved_devices[ind]:
            print("Access granted.")
        else:
            print("Incorrect device.")
    else:
        print("User not approved.")
```

---

### File Handling & Parsing

| Concept | Syntax / Example | Security Application |
| :--- | :--- | :--- |
| **Opening Files** | `with open("allow_list.txt", "r") as file:` | Safely open log files or allow lists. The `with` statement automatically closes the file, preventing memory leaks. |
| **Reading Files** | `ip_addresses = file.read()` | Read the entire contents of a file into a single string for processing. |
| **Writing Files** | `with open("allow_list.txt", "w") as file: file.write(ip_addresses)` | Overwrite a file with updated data (e.g., after removing unauthorized IPs). |
| **Appending Files** | `with open("login.txt", "a") as file: file.write(missing_entry)` | Add new entries to a log file without overwriting existing data. |
| **String to List** | `ip_addresses = ip_addresses.split()` | Convert a space or newline-separated string into a list so that elements can be added or removed individually. |
| **List to String** | `ip_addresses = "\n".join(ip_addresses)` | Convert a list back into a string for writing to a file. Using `"\n"` ensures each IP address is on a new line. |

**My Lab Example (Allow List Update):**
```python
with open("allow_list.txt", "r") as file:
    ip_addresses = file.read().split()  # Read and split into a list

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)    # Remove unauthorized IPs

ip_addresses = "\n".join(ip_addresses)  # Convert back to string

with open("allow_list.txt", "w") as file:
    file.write(ip_addresses)            # Write updated list back to file
```

---

### Regular Expressions (RegEx)

| Pattern / Function | Example | Security Application |
| :--- | :--- | :--- |
| **`re.findall()`** | `re.findall(pattern, log_file)` | Extract all occurrences of a pattern from a string (e.g., all IP addresses or device IDs in a log). |
| **`\w+`** | `r"r15\w+"` | Match alphanumeric characters. Used to find device IDs starting with "r15" that require updates. |
| **`\d{1,3}`** | `r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"` | Match valid IPv4 addresses with 1-3 digits per segment. `{1,3}` provides precision without capturing invalid entries like `9999`. |
| **`\.`** | `\.` | Escape the period character to match literal dots in IP addresses. |
| **Case Insensitivity** | `search_word.upper() in line.upper()` | Ensure keyword searches are case-insensitive (e.g., finding `"ERROR"` in logs regardless of case). |
| **Exact Matching** | `if element in remove_list:` | Rely on exact string matching when comparing IP addresses for removal. |

**My Lab Example (IP Extraction):**
```python
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
valid_ip_addresses = re.findall(pattern, log_file)
```

---

### Debugging Strategies (Google Cert — 3 Error Types)

Debugging is a normal part of developing code. Understanding the **three main types of errors** helps you fix issues faster:

1. **Syntax Errors** – invalid usage of the language (code won't run).
2. **Logic Errors** – code runs but produces unintended results (wrong output).
3. **Exceptions** – syntactically correct code that cannot execute at runtime.

---

#### 1. Syntax Errors

A **syntax error** occurs when you break the rules of Python syntax. Common causes:
- Forgetting a colon `:` after a function or loop header.
- Missing closing brackets `]`, parentheses `)`, or quotes `"`.
- Misspelled keywords.

**Example:**
```python
message = "You are debugging a syntax error
print(message)
```
- **Error output:** `SyntaxError: EOL while scanning string literal`
- **Fix:** Add the missing closing quote: `message = "You are debugging a syntax error"`

> 💡 **Note:** `IndentationError` is a subclass of `SyntaxError` — it occurs when indentation is not syntactically correct (e.g., mixing tabs and spaces, or missing indentation after a colon).

---

#### 2. Logic Errors

A **logic error** happens when the code is valid and runs, but the logic produces unintended results. No error message appears — the output is just wrong.

Common causes:
- Using the wrong operator (e.g., `>=` instead of `>`).
- Assigning the wrong value in a condition.
- Incorrect indentation causing a line to execute when you didn't intend it to.

**Example:**
```python
login_attempts = 5
if login_attempts >= 5:   # Should be `login_attempts < 5`
    print("User has not reached maximum number of login attempts.")
else:
    print("User has reached maximum number of login attempts.")
```
- **Output:** `"User has not reached maximum number of login attempts."` (which is *false* — 5 attempts *has* reached the max).
- **Fix:** Change the condition to `login_attempts < 5`.

---

#### 3. Exceptions

An **exception** occurs when code is syntactically correct but cannot be executed at runtime. Python stops and shows an error message with the exception type.

| Exception Type | When does it happen? | Example |
| :--- | :--- | :--- |
| **`NameError`** | A variable or function hasn't been defined. | `print(username)` when `username` was never assigned. |
| **`TypeError`** | An operation is applied to an object of the wrong type. | `"3" + 5` (string + integer) → cannot concatenate. |
| **`IndexError`** | You try to access an index that does not exist in a sequence (list, tuple, string). | `my_list = [1, 2, 3]; print(my_list[5])` → index out of range. |
| **`KeyError`** | You try to access a key that does not exist in a dictionary. | `my_dict = {"a": 1, "b": 2}; print(my_dict["c"])` → key not found. |
| **`AttributeError`** | You try to access an attribute or method that does not exist on an object. | `"hello".splitit()` (no method named `splitit`). |

**Example (NameError):**
```python
username = "Jameson"
month = "March"
print(username + "is " + month)
# If 'month' was never defined, you'd get: NameError: name 'month' is not defined
```

**Example (IndexError):**
```python
devices = ["laptop", "phone", "tablet"]
print(devices[3])   # IndexError: list index out of range (max index is 2)
```

---

#### 🔧 My Debugging Workflow

| Step | Action |
| :--- | :--- |
| 1 | **Run the code frequently** — don't write 50 lines before testing. |
| 2 | **Read the error message** — it tells you the line number and the error type. |
| 3 | **Fix syntax errors first** — they stop everything else from running. |
| 4 | **Reproduce logic errors** — test with different inputs to see where the output breaks. |
| 5 | **Wrap risky code in `try/except`** — to handle exceptions gracefully (e.g., file not found). |
| 6 | **Use `print()` statements** — to check variable values at each step (or use a debugger like `pdb`). |

---

> 💡 **Key takeaway from the Google Cybersecurity Certificate:**  
> - **Syntax errors** = the code is written incorrectly.  
> - **Logic errors** = the code runs, but your *thinking* is wrong.  
> - **Exceptions** = the code is correct, but the *situation* (missing file, wrong key, out-of-range index) breaks it.

---

### Automation Scripts

| Script | What it does | Key Skills Used |
| :--- | :--- | :--- |
| **`file_renamer.py`** | Add a prefix (`backup_`) to every file in a folder. | `os.listdir()`, `os.rename()`, loops. |
| **`text_parser.py`** | Parses logs to count keywords like "ERROR" case-insensitively. | File I/O, `.upper()`, `in` operator, list iteration. |
| **`folder_scanner.py`** | Walks through directories and maps file extensions. | `os.walk()`, `os.path.splitext()`, `defaultdict`. |
| **`log_analyzer.py`** | SIEM‑style parser that flags brute‑force IPs based on a threshold. | `re` module, `defaultdict`, threshold alerting. |
| **`integrity_checker.py`** | Tripwire‑style file integrity monitor using SHA-256 hashing. | `hashlib`, `os.walk`, baseline comparison. |
| **`update_file.py`** | Reads an allow list, removes unauthorized IPs, and writes back the updated list. | `with open()`, `.split()`, `.remove()`, `.join()`. |

---

> *This section was built from hands-on labs in the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*

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

**My lab example:** I decrypted a Caesar cipher in Linux using `tr` and used `sha256sum` to verify that two files were not identical (they had different hashes).

---

## 🎓 Computing Fundamentals (NCC Diploma)

This section bridges the academic theory from my NCC Level 4 Diploma directly to my cybersecurity practice. Understanding these foundational concepts makes me a more effective security analyst.

---

### Object-Oriented Programming (OOP) Principles

| Principle | Definition | Cybersecurity Application |
| :--- | :--- | :--- |
| **Encapsulation** | Bundling data and methods within a class, hiding internal state. | Writing secure Python scripts (e.g., `log_analyzer.py`) where sensitive data is protected from direct manipulation. |
| **Inheritance** | Creating new classes based on existing ones. | Building modular security tools – a base `Activity` class (from the Fitness Tracker lab) extended by `Walking`, `Swimming`, etc. |
| **Polymorphism** | Using a single interface to represent different data types. | Implementing different `CalculateCalories()` methods for different activities, similar to how security tools handle different log formats. |

---

### Software Development Lifecycle (SDLC)

| Phase | Description | Cybersecurity Relevance |
| :--- | :--- | :--- |
| **Requirements** | Gathering what the system must do. | Defining security requirements (e.g., encryption, MFA) before coding begins. |
| **Design** | Architecture and modelling (UML). | Threat modeling (PASTA) and secure design principles (least privilege, defense in depth). |
| **Implementation** | Writing the code. | Secure coding practices (input validation, avoiding SQL injection). |
| **Testing** | Validating the system. | Penetration testing, vulnerability scanning, and security regression testing. |
| **Deployment & Maintenance** | Releasing and updating the system. | Patch management, monitoring for vulnerabilities (CVE), and incident response. |

---

### Data Structures & Algorithms

| Concept | Definition | Cybersecurity Application |
| :--- | :--- | :--- |
| **Hash Tables** | Key-value storage with O(1) lookup. | **`log_analyzer.py`**: Using `defaultdict` to count failed login attempts per IP address in real-time. |
| **Graphs** | Nodes and edges representing relationships. | **Network Mapping**: Representing network topologies to identify attack paths (e.g., using Dijkstra's algorithm to find the shortest route for a worm or lateral movement). |
| **Sorting Algorithms** | Ordering data (e.g., QuickSort, MergeSort). | **Log Analysis**: Prioritizing threats by severity or timestamp. |
| **Searching Algorithms** | Finding data (e.g., Binary Search). | **Threat Intelligence**: Quickly retrieving IOCs (Indicators of Compromise) from large databases. |

---

### Databases & Normalization

| Concept | Definition | Cybersecurity Application |
| :--- | :--- | :--- |
| **Normalization (3NF)** | Organizing data to reduce redundancy and improve integrity. | Designing secure, efficient databases for storing user logs, audit trails, and incident reports. |
| **SQL Joins** | Combining data from multiple tables. | **Forensics**: Joining `log_in_attempts` with `employees` to trace suspicious activity to specific users. |
| **ACID Properties** | Atomicity, Consistency, Isolation, Durability. | Ensuring that security logs cannot be partially written or corrupted during an attack. |

---

### Networking & the OSI Model

| Layer | Function | Cybersecurity Application |
| :--- | :--- | :--- |
| **Application (L7)** | User-facing apps (HTTP, FTP). | Detecting web attacks (XSS, SQLi) and analyzing application-layer logs. |
| **Transport (L4)** | Reliable data transfer (TCP, UDP). | Firewall rules (blocking ports), detecting SYN floods and port scans. |
| **Network (L3)** | Routing and addressing (IP). | IP spoofing detection, network segmentation, and ACLs. |
| **Data Link (L2)** | Error-free frame transfer (Ethernet). | MAC address filtering, ARP spoofing prevention. |

---

> *This section was built from the NCC Level 4 Diploma in Computing, demonstrating how formal academic training provides the theoretical foundation for practical cybersecurity skills.*

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

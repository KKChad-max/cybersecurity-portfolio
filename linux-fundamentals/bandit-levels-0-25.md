# OverTheWire Bandit — Levels 0-25

## Objective
Build foundational Linux command-line skills through OverTheWire's Bandit wargame. This document covers my journey through Levels 0 to 25, including successful solves and a deep dive into a persistent roadblock at Level 25.

## Tools Used
- SSH (Secure Shell)
- Linux terminal commands: `ls`, `cat`, `cd`, `find`, `grep`, `file`, `sort`, `uniq`, `strings`, `base64`, `tr`, `xxd`, `gzip`, `bzip2`, `tar`, `diff`, `nmap`, `nc`, `openssl`, `crontab`, `ssh-keygen`, `vi`

---

## Walkthrough

### Level 0 → 1
- **Command:** `ls` then `cat readme`
- **Password:** `6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR`
- **Reflection:** Basic navigation and file reading.

### Level 1 → 2
- **Command:** `cat ./-`
- **Password:** `PK8fYLZg2hnHSz83plBL1iEPKdD3QToB`
- **Reflection:** Filenames starting with `-` need `./` prefix.

### Level 2 → 3
- **Command:** `cat ./--spaces\ in\ this\ filename--`
- **Password:** `7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME`
- **Reflection:** Filenames with spaces need `\` to escape them, and `./` prevents `--` from being read as a command flag.

### Level 3 → 4
- **Command:** `cd inhere`, `ls -la`, `cat ...Hiding-From-You`
- **Password:** `xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq`
- **Reflection:** Hidden files start with `.` and need `ls -la` to see.

### Level 4 → 5
- **Command:** `cd inhere`, `file ./*`, `cat ./-file07`
- **Password:** `6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG`
- **Reflection:** Use `file` to identify readable files.

### Level 5 → 6
- **Command:** `find . -type f -size 1033c ! -executable`, `cat ./maybehere07/.file2`
- **Password:** `pXa26xhMWaC2SvDotA4r9EgZkulOeSBW`
- **Reflection:** Find files by size and permission.

### Level 6 → 7
- **Command:** `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`, `cat /var/lib/dpkg/info/bandit7.password`
- **Password:** `Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3`
- **Reflection:** Global search with specific ownership.

### Level 7 → 8
- **Command:** `grep "millionth" data.txt`
- **Password:** `VR1ljMayciFxbnUokuQmJFw6QC9VKtub`
- **Reflection:** `grep` finds specific strings in files.

### Level 8 → 9
- **Command:** `sort data.txt | uniq -u`
- **Password:** `EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl`
- **Reflection:** `uniq -u` finds unique lines.

### Level 9 → 10
- **Command:** `strings data.txt | grep "="`
- **Password:** `B0s2khmbT9u0geKuOoVGW3JZKhndE3BG`
- **Reflection:** `strings` extracts readable text.

### Level 10 → 11
- **Command:** `base64 -d data.txt`
- **Password:** `pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro`
- **Reflection:** Decoding Base64 with `-d` flag.

### Level 11 → 12
- **Command:** `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
- **Password:** `GROozWPO8QyN0mGrjUkID0WCYkZiQxrN`
- **Reflection:** ROT13 cipher decryption using `tr`.

### Level 12 → 13
- **Command:** Hexdump reversal (`xxd -r`), multiple decompressions (gzip, bzip2, tar)
- **Password:** `qQYQiHOBPR8zR61qxYqX45quvihF2uzk`
- **Reflection:** Reverse hexdump, then decompress through chain of file formats.
![Decompressing the file chain in /tmp/mywork](images/Screenshot(29).png)

### Level 13 → 14
- **Command:** `ssh -i sshkey.private bandit14@localhost -p 2220`
- **Password:** `aaWecNkG4FhxJQxz07uiwzVP6bJiYS65`
- **Reflection:** SSH key authentication instead of password.
![Permission denied error on sshkey.private](images/Screenshot(31).png)

### Level 14 → 15
- **Command:** `echo "password" | nc localhost 30000`
- **Password:** `pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7`
- **Reflection:** Sending data to a port using Netcat.

### Level 15 → 16
- **Command:** `openssl s_client -connect localhost:30001`
- **Password:** `kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V`
- **Reflection:** SSL/TLS encrypted connection.

### Level 16 → 17
- **Command:** `nmap -sV -p 31000-32000 localhost`, then `openssl s_client` to SSL port
- **Password:** `pWXMAZoxGC8JmDMfmT5MGEsobMM3vnj2`
- **Reflection:** Port scanning with Nmap, SSL connection.

### Level 17 → 18
- **Command:** `diff passwords.new passwords.old`
- **Password:** `OQxXZjELndr90zuhOTDYBEomI0SZITXI`
- **Reflection:** The line under `<` in the output was the correct password. I initially picked the wrong side but learned to read the context carefully!
![The diff output showing the correct password](images/Screenshot(33).png)

### Level 18 → 19
- **Command:** `ssh bandit18@... -p 2220 "cat readme"`
- **Password:** `KpsOfPkcP7i1FlIExk2QEjyt6dw8dxZI`
- **Reflection:** Bypassing restrictive `.bashrc` by running command directly.

### Level 19 → 20
- **Command:** `./bandit20-do cat /etc/bandit_pass/bandit20`
- **Password:** `4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA`
- **Reflection:** SetUID binary privilege escalation.

### Level 20 → 21
- **Commands:** Two-terminal handshake with `nc -lvp 9300` and `./suconnect 9300`
- **Password:** `bw9k8v5wC3P4yoDyf12LSdGuNz5ka6hY`
- **Reflection:** The `suconnect` binary connects to a daemon and sends the password. By setting up a listener with `nc`, I manually intercepted the password and returned the next one.
![Two-terminal handshake for Level 20](images/Screenshot(52).png)

### Level 21 → 22
- **Command:** Checked `/etc/cron.d/cronjob_bandit22` and the script `/usr/bin/cronjob_bandit22.sh`.
- **Password:** `RYVux2rHEm9tiXHmLFzuR7Vhx6AZQMEz` *(Insert the password you got from the cron job)*
- **Reflection:** Cron jobs run scheduled tasks. The script writes the password to a file in `/tmp/`.

### Level 22 → 23
- **Command:** Computed the MD5 hash of `"I am user bandit23"` to find the temp file (`8ca319486bfbbc3663ea0fbe81326349`).
- **Password:** `gKDTAXnIz3ObXiPjRZZuquTlPZrbSw`
- **Reflection:** MD5 hashing is used to generate dynamic filenames for scripts.
![MD5 hash computation for Level 23](images/Screenshot(54).png)

### Level 23 → 24
- **Commands:** Placed a custom script (`grab.sh`) in `/var/spool/bandit24/foo/`.
- **Password:** `hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv` *(Insert the password you got from your `grab.sh` script)*
- **Reflection:** Cron executes every script in the spool directory. I used this to read the password file and save it to a location I could read.

### Level 24 → 25
- **Command:** Brute-forced a 4-digit PIN on port `30002` using a bash loop.
- **Password:** `SoHfqMOEqiX2iYKVciZxvgpR9a2Djx4P`
- **Reflection:** Automated password guessing against a network service. The correct PIN was `0332`.
![Brute-force result for Level 25](images/Screenshot(56).png)

---

## Major Challenges & Problem-Solving Breakthroughs

Not every level was a straight line. Here are the biggest roadblocks I hit and how I overcame them — this was where I learned the most.

### The First Connection: Typo Terror
- **The Problem:** I typed `ssh bandito@...` instead of `bandit0` (zero vs 'o'). 
- **The Fix:** Paying attention to the exact username format. The server is case‑sensitive, and numbers are not letters. Also, I had to get used to the fact that **passwords don't show up when you type them** – it feels like nothing is happening, but it is.

### Level 1 & 2: Filenames That Break Commands
- **Level 1 → 2:** The file was named `-`. When you run `cat -`, the terminal treats `-` as a command option, not a filename.
- **The Fix:** `cat ./-` — the `./` tells the shell "look in the current folder" so it treats the dash as a literal filename.
- **Level 2 → 3:** The file was `--spaces in this filename--`. The `--` tricks `cat` into thinking you're passing flags, and the spaces break the command.
- **The Fix:** `cat ./--spaces\ in\ this\ filename--` — escaping spaces with `\` and using `./` to neutralize the double dash. I initially tried quotes, but the `--` still caused issues. This taught me how to escape special characters properly.

### Level 3 → 4: Hidden Files Are Not Always `.hidden`
- **The Problem:** I expected the file to be named `.hidden` (like many beginner CTFs), but it was `...Hiding-From-You`. 
- **The Fix:** Running `ls -la` showed me the actual filename. I learned to never assume file names — always verify with `ls -la` first.

### Level 4 → 5: Finding a Needle in a Binary Haystack
- **The Problem:** Ten files in `inhere` — only one was human-readable. I tried `cat ./*` but got a mess of binary garbage.
- **The Fix:** I used `file ./*` to identify file types, spotted the one marked `ASCII text`, and read it with `cat ./-file07` (again, using `./` to handle the leading dash). This taught me that tools like `file` are essential for reconnaissance.

### Level 5 → 6: The `find` Syntax Trap
- **The Problem:** I needed a file of exactly 1033 bytes that was **not** executable. I had to combine `-type f`, `-size 1033c`, and `! -executable`.
- **The Fix:** Carefully reading the `find` manual (`man find`) to understand that `!` negates conditions, and `c` means bytes. Small details like `c` vs `b` (blocks) matter.

### Level 6 → 7: Global Search Noise
- **The Problem:** `find / -user bandit7 -group bandit6 -size 33c` spewed thousands of `Permission denied` errors.
- **The Fix:** Redirecting errors with `2>/dev/null` to see only the useful output. This is a standard sysadmin trick that I now use everywhere.

### Level 9 → 10: Extracting Human‑Readable Text from Binary
- **The Problem:** `cat data.txt` showed garbled binary data.
- **The Fix:** `strings data.txt | grep "="` — extracting readable text and grepping for the `=` character, which strongly hinted at a Base64‑like string. I didn't know about `strings` before, and now it's in my toolkit.

### Level 12: The Compression Gauntlet
- **The Challenge:** One file, hexdumped, then compressed 6 times in a row (gzip, bzip2, tar, etc.). 
- **The Lesson:** I had to carefully check every file type using `file`, rename it with the correct extension (`mv`), and decompress it. If you rename it wrong, the whole chain breaks. This taught me to slow down and trust the `file` command.

### Level 13 → 14: SSH Key Permissions & The Windows `libcrypto` Nightmare
- **The Challenge:** The server gave me an SSH private key to jump to Level 14. However, SSH refused to use it because the permissions were too open (`640` instead of `600`). I couldn't `chmod` it because the homedirectory was write-protected.
- **The Fix:** I copied the key to `/tmp/`, set `chmod 600`, and tried to connect. But I hit a second wall: my local Git Bash SSH client threw a `libcrypto: unsupported` error because it couldn't parse the new key format.
- **The Real Breakthrough:** Instead of fighting the SSH client, I wrote a Python script using the `paramiko` library to load the private key and fetch the password programmatically. This bypassed the local SSH client limitations entirely. 

### Level 16 → 17: History Repeats (Another SSH Key)
- **The Challenge:** Level 16 required scanning open ports (`nmap`) and connecting via SSL (`openssl s_client`) to receive another RSA private key. Again, I had to save it, convert it, and use Python to authenticate.
- **The Lesson:** Automating authentication with Python is a lifesaver when dealing with tricky key formats. It also gave me a reusable script for any future SSH key challenges.

### Level 17 → 18: The `diff` Trap (A Lesson in Attention to Detail)
- **The Challenge:** I used `diff passwords.new passwords.old` to find the password for Level 18. The output showed:< OQxXZjELndr90zuhOTDYBEomI0SZITXI
														    > icUh23IUytZLIYhcCaXL18agiSIqymBc

- **The Mistake:** I initially tried the password marked with `>` (the old file), but it failed. 
- **The Solution:** I realized that because the command syntax is `diff NEW OLD`, the line marked with `<` belongs to the **first file** (`passwords.new`) — which is the **new password** I needed. 
- **Takeaway:** Always read `diff` output context carefully! The side of the arrow matters based on the order of the arguments.

### Level 18: Bypassing the `.bashrc` Lockout
- **The Challenge:** Logging in normally kicks you out immediately due to a modified `.bashrc` file.
- **The Workaround:** Instead of opening an interactive session, I ran the command remotely in one shot: `ssh bandit18@... "cat readme"`. This executed the command without loading the broken `.bashrc`, instantly revealing the next password.

### Level 20: The Two‑Terminal Handshake
- **The Challenge:** The `suconnect` binary needed a daemon to talk to, but the intended daemon wasn't responding properly.
- **The Solution:** I opened a second terminal, ran `nc -lvp 9300` to act as my own daemon, and ran `./suconnect 9300` in the first terminal. This let me see exactly what password was being sent, and I replied with the next password manually.
- **Takeaway:** When a client‑server tool fails, you can simulate the server with `netcat` to debug or complete the handshake.

### Overall Takeaway: When to Stop Fighting the Tools
The biggest lesson was learning to switch contexts. When I spent too long fighting SSH key formats in Git Bash, I switched to Python. When interactive shells failed, I switched to one-shot remote commands. Knowing when to abandon a failing approach and choose a better tool is a critical cybersecurity skill.

### The Meta‑Lesson: Patience and Verification
Most of these mistakes came from rushing. The fix was always the same: **slow down, verify file names with `ls`, check file types with `file`, and test your command on a small sample before running it on everything.**

---

## Major Challenges & Persistent Roadblocks (Level 25 → 26)

### Level 25 → 26 (The `rbash` Escape & Key Format Fight)

**Goal:** Use the SSH key (`bandit26.sshkey`) provided in the `bandit25` home directory to log in as `bandit26` and retrieve the password.

**Attempted Solutions & Failures:**

1. **Direct Connection (localhost block):**
   - `ssh -i bandit26.sshkey bandit26@localhost -p 2220`
   - **Result:** Failed with `no authentication methods enabled`. The server blocked password logins from localhost, and the key was not being accepted.

2. **Forcing Public Key Authentication (Still localhost):**
   - Added flags: `-o PreferredAuthentications=publickey -o PubkeyAcceptedKeyTypes=+ssh-rsa`
   - **Result:** Same error. The key was simply not being recognized by the SSH daemon.

3. **Converting Key to PEM Format (On the server):**
   - `ssh-keygen -p -m PEM -f /tmp/key.pem -N ""`
   - **Result:** The key converted, but the connection still failed with `Permission denied` or `invalid format`.

4. **Trying the Classic `vi` Escape (Without Remote Command):**
   - Shrunk the terminal (`stty rows 1`) and connected without a remote command to force the `more` pager.
   - **Result:** The connection failed before the pager could even load because the key authentication never succeeded.

5. **Connecting to External Hostname (To bypass localhost block):**
   - `ssh -i key.pem bandit26@bandit.labs.overthewire.org -p 2220 "cat /etc/bandit_pass/bandit26"`
   - **Result:** Even with the external hostname, the server rejected the key with `invalid format` or `libcrypto` errors.

6. **Trying Python `paramiko` (On Windows local machine):**
   - Wrote a Python script to load the key and connect.
   - **Result:** The connection timed out or hung indefinitely due to network/firewall restrictions on the local network.

7. **Trying Windows PowerShell (Local machine):**
   - Attempted to convert and use the key natively.
   - **Result:** Hit the `libcrypto` error in PowerShell as well, or got `invalid format` despite using `ssh-keygen`.

**The Root Cause:**
The environment (Git Bash/PowerShell on Windows, and the specific OverTheWire server connection) had a severe incompatibility with the OpenSSH key format. The server rejected RSA keys sent from the localhost, and the client refused to negotiate due to mismatched algorithms (`no matching host key signature algorithm` despite adding `+ssh-rsa`). 

**Lessons Learned & Documentation:**
The *intended* solution is well-documented in the community:
1. Copy the key and convert it if needed.
2. Connect with `ssh -i bandit26.sshkey bandit26@localhost -p 2220`.
3. Make the terminal tiny to force the `more` pager to pause.
4. Press `v` to open `vi`.
5. Escape `rbash` with `:set shell=/bin/sh` and `:shell`.
6. Read `/etc/bandit_pass/bandit26`.

**Status:**
I have fully documented the struggle and the methodology. I will revisit this final step on a clean Ubuntu virtual machine (to ensure proper SSH versions) or from another network. The inability to complete Level 26 on this specific attempt is a testament to the complexity of real-world SSH troubleshooting, not a lack of understanding.

---

## What I Learned
- **Linux File Manipulation:** Navigating, reading, searching, and finding files.
- **Networking:** SSH, Netcat, OpenSSL, Nmap, and socket connections.
- **Automation:** Python scripts, bash loops, and cron jobs.
- **Security Concepts:** SetUID binaries, restricted shells (`rbash`), privilege escalation, and password brute-forcing.
- **Troubleshooting:** Persistence in the face of SSH key format wars and localhost restrictions. Knowing when to stop fighting the tool and pivot to documenting the journey.
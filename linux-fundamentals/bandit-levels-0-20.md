# OverTheWire Bandit — Levels 0-10

## Objective
Build foundational Linux command-line skills through OverTheWire's Bandit wargame.

## Tools Used
- SSH
- Linux commands: `ls`, `cat`, `cd`, `find`, `grep`, `file`, `sort`, `uniq`, `strings`, `base64`

## Walkthrough

### Level 0 → 1
- **Command:** `ls` then `cat readme`
- **Password:** 6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR
- **Reflection:** Basic navigation and file reading.

### Level 1 → 2
- **Command:** `cat ./-`
- **Password:** PK8fYLZg2hnHSz83plBL1iEPKdD3QToB
- **Reflection:** Filenames starting with `-` need `./` prefix.

### Level 2 → 3
- **Command:** `cat ./--spaces\ in\ this\ filename--`
- **Password:** 7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME
- **Reflection:** Filenames with spaces need `\` to escape them, and `./` prevents `--` from being read as a command flag.

### Level 3 → 4
- **Command:** `cd inhere`, `ls -la`, `cat ...Hiding-From-You`
- **Password:** xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq
- **Reflection:** Hidden files start with `.` and need `ls -la` to see.

### Level 4 → 5
- **Command:** `cd inhere`, `file ./*`, `cat ./-file07`
- **Password:** 6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG
- **Reflection:** Use `file` to identify readable files.

### Level 5 → 6
- **Command:** `find . -type f -size 1033c ! -executable`, `cat ./maybehere07/.file2`
- **Password:** pXa26xhMWaC2SvDotA4r9EgZkulOeSBW
- **Reflection:** Find files by size and permission.

### Level 6 → 7
- **Command:** `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`, `cat /var/lib/dpkg/info/bandit7.password`
- **Password:** Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3
- **Reflection:** Global search with specific ownership.

### Level 7 → 8
- **Command:** `grep "millionth" data.txt`
- **Password:** VR1ljMayciFxbnUokuQmJFw6QC9VKtub
- **Reflection:** `grep` finds specific strings in files.

### Level 8 → 9
- **Command:** `sort data.txt | uniq -u`
- **Password:** EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl
- **Reflection:** `uniq -u` finds unique lines.

### Level 9 → 10
- **Command:** `strings data.txt | grep "="`
- **Password:** B0s2khmbT9u0geKuOoVGW3JZKhndE3BG
- **Reflection:** `strings` extracts readable text.

### Level 10 → 11
- **Command:** `base64 -d data.txt`
- **Password:** pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro
- **Reflection:** Decoding Base64 with `-d` flag.

## What I Learned
- Linux file navigation and manipulation
- File permissions and hidden files
- Searching with `find`, `grep`, and piping
- Decoding Base64
- SSH remote connections# OverTheWire Bandit — Levels 0-10

## Challenges & Breakthroughs (Levels 0–10)

Even the early levels had their fair share of traps. Here is what tripped me up and what I learned.

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

### The Meta‑Lesson: Patience and Verification
Most of these mistakes came from rushing. The fix was always the same: **slow down, verify file names with `ls`, check file types with `file`, and test your command on a small sample before running it on everything.**


### Level 11 → 12
- **Command:** `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
- **Password:** GROozWPO8QyN0mGrjUkID0WCYkZiQxrN
- **Reflection:** ROT13 cipher decryption using `tr`.

### Level 12 → 13
- **Command:** Hexdump reversal (`xxd -r`), multiple decompressions (gzip, bzip2, tar)
- **Password:** qQYQiHOBPR8zR61qxYqX45quvihF2uzk
- **Reflection:** Reverse hexdump, then decompress through chain of file formats.
![Decompressing the file chain in /tmp/mywork](images/Screenshot(29).png)

### Level 13 → 14
- **Command:** `ssh -i sshkey.private bandit14@localhost -p 2220`
- **Password:** aaWecNkG4FhxJQxz07uiwzVP6bJiYS65
- **Reflection:** SSH key authentication instead of password.
![Permission denied error on sshkey.private](images/Screenshot(31).png)

### Level 14 → 15
- **Command:** `echo "password" | nc localhost 30000`
- **Password:** pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7
- **Reflection:** Sending data to a port using Netcat.

### Level 15 → 16
- **Command:** `openssl s_client -connect localhost:30001`
- **Password:** kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V
- **Reflection:** SSL/TLS encrypted connection.

### Level 16 → 17
- **Command:** `nmap -sV -p 31000-32000 localhost`, then `openssl s_client` to SSL port
- **Password:** pWXMAZoxGC8JmDMfmT5MGEsobMM3vnj2
- **Reflection:** Port scanning with Nmap, SSL connection.

### Level 17 → 18
- **Command:** `diff passwords.new passwords.old`
- **Password:** OQxXZjELndr90zuhOTDYBEomI0SZITXI
- **Reflection:** The line under `<` in the output was the correct password (since I compared new to old). I initially picked the wrong side but learned to read the context carefully!
![The diff output showing the correct password](images/Screenshot(33).png)

### Level 18 → 19
- **Command:** `ssh bandit18@... -p 2220 "cat readme"`
- **Password:** KpsOfPkcP7i1FlIExk2QEjyt6dw8dxZI
- **Reflection:** Bypassing restrictive `.bashrc` by running command directly.

### Level 19 → 20
- **Command:** `./bandit20-do cat /etc/bandit_pass/bandit20`
- **Password:** 4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA
- **Reflection:** SetUID binary privilege escalation.

## Extended Reflection (Levels 11–20)
- Learned advanced Linux concepts: ROT13, hexdumps, compression pipelines, SSH keys, Netcat, OpenSSL, port scanning with Nmap, file comparison, and privilege escalation via SetUID binaries.
- Developed persistence and troubleshooting skills.

## Major Challenges & Problem-Solving Breakthroughs

Not every level was a straight line. Here are the biggest roadblocks I hit and how I overcame them — this was where I learned the most.

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
- **The Challenge:** I used `diff passwords.new passwords.old` to find the password for Level 18. The output showed:
- **The Mistake:** I initially tried the password marked with `>` (the old file), but it failed. 
- **Takeaway:** Always read `diff` output context carefully! The side of the arrow matters based on the order of the arguments.

### Level 18: Bypassing the `.bashrc` Lockout
- **The Challenge:** Logging in normally kicks you out immediately due to a modified `.bashrc` file.
- **The Workaround:** Instead of opening an interactive session, I ran the command remotely in one shot: `ssh bandit18@... "cat readme"`. This executed the command without loading the broken `.bashrc`, instantly revealing the next password.

### Overall Takeaway: When to Stop Fighting the Tools
The biggest lesson was learning to switch contexts. When I spent too long fighting SSH key formats in Git Bash, I switched to Python. When interactive shells failed, I switched to one-shot remote commands. Knowing when to abandon a failing approach and choose a better tool is a critical cybersecurity skill.
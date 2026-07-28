🧠 My Cybersecurity Field Manual: OverTheWire Bandit 0–20
Module 1: Git & GitHub Foundations (The Portfolio Backbone)
Commands Used:
bash
# Configure your identity (one-time setup)
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"

# Clone a remote repository to your local machine
git clone https://github.com/your-username/repo-name.git

# Check the status of changes
git status

# Stage all changes in the current folder
git add .

# Commit staged changes with a message
git commit -m "Describe your changes here"

# Upload local commits to GitHub
git push

# Remove a file from the repo
git rm filename.txt
git commit -m "removed file"
git push
🚨 The Token Trap:
Challenge: GitHub no longer accepts your account password for git push.

Solution: Generate a Personal Access Token (Settings → Developer settings → Tokens). Copy it immediately and use it as the password when git push prompts you. Save it in a secure notepad while working.

Module 2: Linux Terminal & SSH Basics
Commands Used:
bash
# Navigate directories
cd ~/Desktop          # Go to Desktop
cd ..                 # Go up one level
cd /tmp               # Go to root temp directory

# List files
ls                    # List basic
ls -la                # List all (including hidden) with details

# Read files
cat filename.txt      # Print entire file to screen

# Create empty file
touch filename.txt

# Copy a file
cp source.txt destination.txt

# Move or rename a file
mv oldname.txt newname.txt

# Set file permissions (read/write/execute)
chmod 600 filename    # Owner can read/write, nobody else
🚨 The "Silent Password" Trap:
Challenge: When SSH asks for a password, no characters appear as you type (no dots, no asterisks). It looks frozen.

Solution: Type the password blindly and press Enter. It is registering your keystrokes; it's just hidden for security.

Module 3: Bandit Commands Reference (0–20)
Finding & Reading Files
Command	What it does
cat ./-	Read a file named - (needs ./ to avoid command flags).
cat "./--spaces in this filename--"	Read a file with spaces and double-dashes.
cat ...Hiding-From-You	Read a file with three dots (just literal characters).
file ./*	Identifies the type of every file in a folder (ASCII, binary, compressed).
find . -size 1033c ! -executable	Find a non-executable file exactly 1033 bytes in current folder.
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null	Find a specific file on the whole system, hiding permission errors.
Searching & Parsing Text
Command	What it does
grep "millionth" data.txt	Find lines containing the word "millionth".
sort data.txt | uniq -u	Sort lines, then show only the line that appears once.
strings data.txt | grep "="	Extract human-readable text from binary, filter for =.
diff file1 file2	Compare two files and show differences.
Network & Ports
Command	What it does
ssh banditX@host -p 2220	Connect securely to a remote server.
echo "password" | nc localhost 30000	Send a password to a local port using Netcat.
openssl s_client -connect localhost:30001	Connect to an SSL/TLS encrypted port.
nmap -sV -p 31000-32000 localhost	Scan local ports 31000-32000 to find services.
Encoding & Compression
Command	What it does
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'	Decode ROT13 cipher (rotate letters by 13).
base64 -d data.txt	Decode a Base64 encoded file.
xxd -r data.txt > file1	Reverse a hexdump.
gzip -d file1.gz	Decompress a Gzip archive.
bzip2 -d file1.bz2	Decompress a Bzip2 archive.
tar xf file1.tar	Extract a Tar archive.
SSH Keys & Privilege Escalation
Command	What it does
chmod 600 sshkey.private	Make a private key readable only by owner (SSH demands this).
ssh -i sshkey.private user@host -p 2220	Log in using a private key file.
./bandit20-do cat /etc/bandit_pass/bandit20	Run a command as another user using a SetUID binary.
ssh bandit18@host -p 2220 "cat readme"	Run a command on the remote server without loading .bashrc.
Module 4: The Troubleshooting Hall of Fame (The Struggles)
1. The SSH Key libcrypto Error
Situation: Tried ssh -i bandit14_key.txt bandit14@... on my Windows Git Bash. Got error in libcrypto: unsupported.

Why: My local Git Bash SSH client was too old to parse the new OpenSSH key format.

Solution: Wrote a Python script using the paramiko library to load the key and fetch the password programmatically. This bypassed the local SSH client entirely.

Python Template (Memory Aid):

python
import paramiko
key_path = r"C:\path\to\key.txt"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
private_key = paramiko.RSAKey.from_private_key_file(key_path)
client.connect(hostname="bandit.labs.overthewire.org", port=2220, username="banditX", pkey=private_key)
# Run a command...
2. The localhost Connection Block
Situation: Tried ssh bandit14@localhost -p 2220 from inside a bandit server to jump to the next level. Got "Connecting from localhost is blocked".

Why: OverTheWire blocks password logins from localhost to conserve resources and force you to use SSH keys.

Solution: Always jump to the next level from my local machine (outside SSH), or use the -i key method without interactive passwords.

3. The diff Mix-up (Level 17 → 18)
Situation: Ran diff passwords.new passwords.old. Output showed < OLD and > NEW.

Why: I tried the line marked with > (thinking it was "greater/newer"). It failed.

Solution: Critical Rule: diff file1 file2 means file1 is on the left (<). Since passwords.new is on the left, the password is the line after <!

Takeaway: Always read the output context: < belongs to the first file in the command.

4. The .bashrc Instant Logout (Level 18)
Situation: Logged into bandit18 and got kicked out immediately.

Why: The .bashrc file was modified to disconnect users.

Solution: Bypass the login shell by running a command remotely: ssh bandit18@host -p 2220 "cat readme".

Module 5: Python Automation Toolkit
I wrote these scripts to save time and handle tasks too complex for one-liners.

1. file_renamer.py
Use case: Prepend a prefix (e.g., backup_) to every file in a folder.

Core concept: os.listdir() and os.rename().

2. text_parser.py
Use case: Count how many lines in a log file contain "ERROR".

Core concept: open(file).readlines() and if word in line.

3. folder_scanner.py
Use case: Scan a folder (and subfolders) and report how many .txt, .py, etc., exist.

Core concept: os.walk() and os.path.splitext().

4. fetch_banditX_password.py (using paramiko)
Use case: When Git Bash fails to read an SSH key, Python handles it flawlessly.

Core concept: Automating SSH authentication with code.

Module 6: The "Pro" Takeaways (What actually changed in my brain)
No Output = Success: In Linux, if a command runs and prints nothing, it usually worked. Silence is good.

Verification is King: Always run ls to confirm the file exists before catting it. Always run file before decompressing.

When to Quit Fighting: If a CLI tool gives you a weird error after 15 minutes, switch to Python or a different approach. Don't brute-force the terminal.

Hidden Characters are Real: Copy-pasting can add invisible newlines. If a password fails, try typing it manually, even if it's long.

Portability: Tools like paramiko work on Windows, Mac, and Linux. Learning Python for system automation makes you immune to local CLI inconsistencies.


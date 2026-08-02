import re
from collections import defaultdict
import os

# === CONFIGURATION ===
LOG_FILE = "sample_auth.log"   # The log file to analyze
THRESHOLD = 5                  # Alert if an IP fails more than this many times

# === SAMPLE LOG GENERATION (runs if the file doesn't exist) ===
def create_sample_log():
    """Creates a realistic-looking auth.log sample for testing."""
    sample_lines = [
        "Mar 12 08:14:22 server sshd[1234]: Failed password for invalid user admin from 192.168.1.100 port 54321 ssh2",
        "Mar 12 08:15:01 server sshd[1235]: Failed password for user root from 10.0.0.50 port 54322 ssh2",
        "Mar 12 08:15:45 server sshd[1236]: Failed password for invalid user test from 192.168.1.100 port 54323 ssh2",
        "Mar 12 08:16:10 server sshd[1237]: Accepted password for user jane from 10.0.0.10 port 54324 ssh2",
        "Mar 12 08:17:22 server sshd[1238]: Failed password for user root from 10.0.0.50 port 54325 ssh2",
        "Mar 12 08:18:01 server sshd[1239]: Failed password for invalid user admin from 192.168.1.100 port 54326 ssh2",
        "Mar 12 08:19:33 server sshd[1240]: Failed password for user root from 10.0.0.50 port 54327 ssh2",
        "Mar 12 08:20:12 server sshd[1241]: Failed password for user root from 10.0.0.50 port 54328 ssh2",
        "Mar 12 08:21:44 server sshd[1242]: Failed password for invalid user guest from 192.168.1.101 port 54329 ssh2",
        "Mar 12 08:22:55 server sshd[1243]: Failed password for user root from 10.0.0.50 port 54330 ssh2"
    ]
    with open(LOG_FILE, "w") as f:
        f.write("\n".join(sample_lines))
    print(f"📄 Created sample log file: {LOG_FILE}")

if not os.path.exists(LOG_FILE):
    create_sample_log()

# === REGEX PATTERNS ===
# Matches IPv4 addresses (e.g., 192.168.1.100)
IP_PATTERN = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

# === MAIN LOGIC ===
def analyze_log():
    failures = defaultdict(int)
    
    with open(LOG_FILE, "r") as f:
        for line in f:
            # Only count lines that mention "Failed password"
            if "Failed password" in line:
                # Extract the IP address
                ip_match = re.search(IP_PATTERN, line)
                if ip_match:
                    ip = ip_match.group()
                    failures[ip] += 1

    # === OUTPUT RESULTS ===
    print(f"\n📊 Analysis of {LOG_FILE} completed.")
    print(f"🔍 Total unique IPs with failed attempts: {len(failures)}")
    print("-" * 40)

    alerted = False
    for ip, count in sorted(failures.items(), key=lambda x: x[1], reverse=True):
        status = "🚨 ALERT" if count >= THRESHOLD else "✅ Info"
        print(f"{status}: {ip} -> {count} failed attempts")
        if count >= THRESHOLD:
            alerted = True

    if not alerted:
        print("\n✅ No suspicious IPs exceeded the threshold.")
    else:
        print("\n⚠️  Action required: Investigate the flagged IPs above!")

if __name__ == "__main__":
    analyze_log()
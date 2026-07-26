# text_parser.py — Counts how many lines contain a specific word

import os

# === CONFIGURATION ===
file_name = "sample_log.txt"     # The file to analyze
search_word = "ERROR"            # The word to count

# === CREATE A SAMPLE LOG FILE ===
sample_content = """INFO: User logged in
WARNING: Disk space low
ERROR: Connection timeout
INFO: File uploaded
ERROR: Authentication failed
INFO: Logout successful
ERROR: Database unreachable
INFO: Health check passed"""

with open(file_name, "w") as f:
    f.write(sample_content)

print(f"✅ Created '{file_name}' with sample log entries.")

# === COUNT HOW MANY LINES CONTAIN THE SEARCH WORD ===
try:
    with open(file_name, "r") as f:
        lines = f.readlines()
    
    count = 0
    for line in lines:
        if search_word.upper() in line.upper():  # Case‑insensitive
            count += 1
    
    print(f"\n📊 Found '{search_word}' in {count} out of {len(lines)} lines.")
    print(f"🔍 That's { (count / len(lines)) * 100:.1f}% of the log entries.")
    
except FileNotFoundError:
    print(f"❌ Error: File '{file_name}' not found.")
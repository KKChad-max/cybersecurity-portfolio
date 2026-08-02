import os
import hashlib
import json
import sys

BASELINE_FILE = "baseline_hashes.json"

def hash_file(filepath):
    """Compute SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (IOError, OSError):
        # Skip files we can't read (permission issues)
        return None

def scan_folder(folder_path):
    """Walk through a folder and return a dict of {filepath: hash}."""
    results = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            # Skip the baseline file itself if it's in the folder
            if os.path.abspath(full_path) == os.path.abspath(os.path.join(os.getcwd(), BASELINE_FILE)):
                continue
            file_hash = hash_file(full_path)
            if file_hash:
                results[full_path] = file_hash
    return results

def save_baseline(folder_path):
    """Scan folder and save hashes to baseline file."""
    print(f"📂 Scanning folder: {folder_path}")
    data = scan_folder(folder_path)
    with open(BASELINE_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Baseline saved ({len(data)} files) to {BASELINE_FILE}")

def check_integrity(folder_path):
    """Scan folder and compare against existing baseline."""
    if not os.path.exists(BASELINE_FILE):
        print(f"❌ Error: Baseline file '{BASELINE_FILE}' not found.")
        print("💡 Run without the --check flag first to create a baseline.")
        return

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    print(f"📂 Checking folder: {folder_path}")
    current = scan_folder(folder_path)
    changes = []

    # Check for modified or new files
    for path, new_hash in current.items():
        old_hash = baseline.get(path)
        if old_hash is None:
            changes.append(f"➕ NEW FILE: {path}")
        elif old_hash != new_hash:
            changes.append(f"🔄 MODIFIED: {path}")

    # Check for deleted files
    for path in baseline.keys():
        if path not in current:
            changes.append(f"❌ DELETED: {path}")

    if not changes:
        print("✅ No changes detected. Integrity is intact!")
    else:
        print("\n⚠️  CHANGES DETECTED:")
        for change in changes:
            print(change)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python integrity_checker.py <folder_path>         # Create baseline")
        print("  python integrity_checker.py <folder_path> --check # Check integrity")
        sys.exit(1)

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"❌ Error: '{folder}' is not a valid folder.")
        sys.exit(1)

    if "--check" in sys.argv:
        check_integrity(folder)
    else:
        save_baseline(folder)
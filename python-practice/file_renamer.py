import os

# === CONFIGURATION ===
folder_path = "./test_files"           # Folder containing files to rename
prefix = "backup_"                     # What to add to the beginning

# === CREATE A TEST FOLDER (to not accidentally rename real files) ===
os.makedirs(folder_path, exist_ok=True)

# Create 3 dummy files to test with
for i in range(1, 4):
    dummy_path = os.path.join(folder_path, f"file{i}.txt")
    with open(dummy_path, "w") as f:
        f.write(f"This is test file {i}")

print(f"✅ Created test files in '{folder_path}'")

# === RENAME THE FILES ===
for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)
    
    # Only rename files (skip folders)
    if os.path.isfile(old_path):
        new_name = prefix + filename
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

print("✅ All files renamed successfully!")
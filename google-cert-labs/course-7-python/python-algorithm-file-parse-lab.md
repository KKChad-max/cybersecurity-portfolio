# Python Algorithm Lab: Parsing and Updating an Allow List

**Date:** September 8, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I am responsible for controlling access to restricted content. In this lab, I worked with a text file containing IP addresses that are allowed to access specific restricted content at my organization.

I developed an algorithm that:

1. Parses the text file of IP addresses.
2. Removes addresses that no longer have access.
3. Updates the file with the revised list.

---

## Task 1: Display the Variables

I displayed the contents of the `import_file` and `remove_list` variables to explore what they contain.

**Code:**

```python
# Assign `import_file` to the name of the file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Display `import_file`
print(import_file)

# Display `remove_list`
print(remove_list)
```

**Output:**

```text
allow_list.txt
['192.168.97.225', '192.168.158.170', '192.168.201.40', '192.168.58.57']
```

**Observation:** `import_file` stores the filename, and `remove_list` contains the IP addresses that need to be removed from the allow list.

---

## Task 2: Open the File with `with`

I started writing the first line of a `with` statement to open the allow list file in read mode.

**Code:**

```python
# Assign `import_file` to the name of the file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# First line of `with` statement
with open(import_file, "r") as file:
```

**Observation:** The `with` statement opens `allow_list.txt` in read mode (`"r"`). The file object is assigned to the variable `file`.

---

## Task 3: Read the File with `.read()`

I used the `.read()` method to read the contents of the file and stored the result in `ip_addresses`. I then displayed `ip_addresses` to examine its contents.

**Code:**

```python
# Assign `import_file` to the name of the file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()

# Display `ip_addresses`
print(ip_addresses)
```

**Output:**

```text
ip_address
192.168.25.60
192.168.205.12
192.168.97.225
192.168.6.9
192.168.52.90
192.168.158.170
192.168.90.124
192.168.186.176
192.168.133.188
192.168.203.198
192.168.201.40
192.168.218.219
192.168.52.37
192.168.156.224
192.168.60.153
192.168.58.57
192.168.69.116
```

**Observation:** The file contents are displayed as a single string, but because the file contains newline characters (`\n`), each IP address appears on a separate line. The IP `192.168.97.225`, `192.168.158.170`, `192.168.201.40`, and `192.168.58.57` appear in both the allow list and `remove_list`.

---

## Task 4: Convert String to List with `.split()`

I used the `.split()` method to convert the string into a list of individual IP addresses.

**Code:**

```python
# Assign `import_file` to the name of the file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()

# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()

# Display `ip_addresses`
print(ip_addresses)
```

**Output:**

```text
['ip_address', '192.168.25.60', '192.168.205.12', '192.168.97.225', '192.168.6.9', '192.168.52.90', '192.168.158.170', '192.168.90.124', '192.168.186.176', '192.168.133.188', '192.168.203.198', '192.168.201.40', '192.168.218.219', '192.168.52.37', '192.168.156.224', '192.168.60.153', '192.168.58.57', '192.168.69.116']
```

**Observation:** The `ip_addresses` variable is now a list, making it easier to iterate through and modify. Note that `"ip_address"` is the header from the file and is included as the first element of the list.

---

## Task 5: Iterate Through the List

I built an iterative statement to loop through `ip_addresses` and display each element.

**Code:**

```python
# Assign `import_file` to the name of the file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()

# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()

# Build iterative statement
# Name Loop variable `element`
# Loop through `ip_addresses`
for element in ip_addresses:
    # Display `element` in every iteration
    print(element)
```

**Output:**

```text
ip_address
192.168.25.60
192.168.205.12
192.168.97.225
192.168.6.9
192.168.52.90
192.168.158.170
192.168.90.124
192.168.186.176
192.168.133.188
192.168.203.198
192.168.201.40
192.168.218.219
192.168.52.37
192.168.156.224
192.168.60.153
192.168.58.57
192.168.69.116
```

**Observation:** The loop iterates through each IP address in the list and prints it individually, including the `"ip_address"` header.

---

## Task 6: Remove Unwanted IP Addresses

I added a conditional statement inside the loop to remove IP addresses that are in `remove_list`.

**Code:**

```python
# Assign `import_file` to the name of the file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()

# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()

# Build iterative statement
# Name Loop variable `element`
# Loop through `ip_addresses`
for element in ip_addresses:
    # Build conditional statement
    # If current element is in `remove_list`,
    if element in remove_list:
        # then current element should be removed from `ip_addresses`
        ip_addresses.remove(element)

# Display `ip_addresses`
print(ip_addresses)
```

**Output:**

```text
['ip_address', '192.168.25.60', '192.168.205.12', '192.168.6.9', '192.168.52.90', '192.168.90.124', '192.168.186.176', '192.168.133.188', '192.168.203.198', '192.168.218.219', '192.168.52.37', '192.168.156.224', '192.168.60.153', '192.168.69.116']
```

**Observation:** The IP addresses `192.168.97.225`, `192.168.158.170`, `192.168.201.40`, and `192.168.58.57` were successfully removed from the list.

---

## Task 7: Update the Original File

I converted the list back to a string using `.join()` and wrote it back to the original file.

**Code:**

```python
# Assign `import_file` to the name of the file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()

# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()

# Build iterative statement
# Name Loop variable `element`
# Loop through `ip_addresses`
for element in ip_addresses:
    # Build conditional statement
    # If current element is in `remove_list`,
    if element in remove_list:
        # then current element should be removed from `ip_addresses`
        ip_addresses.remove(element)

# Convert `ip_addresses` back to a string so that it can be written into the text file
ip_addresses = " ".join(ip_addresses)

# Build `with` statement to rewrite the original file
with open(import_file, "w") as file:
    # Rewrite the file, replacing its contents with `ip_addresses`
    file.write(ip_addresses)
```

**Observation:** The `" ".join(ip_addresses)` converts the list back to a space-separated string, and the `"w"` mode overwrites the file with the updated contents.

---

## Task 8: Verify the Updated File

I read the updated file and displayed its contents to verify the changes.

**Code:**

```python
# Assign `import_file` to the name of the file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information.
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use `read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()

    # Use `split()` to convert `ip_addresses` from a string to a list
    ip_addresses = ip_addresses.split()

# Build iterative statement
# Name Loop variable `element`
# Loop through `ip_addresses`
for element in ip_addresses:
    # Build conditional statement
    # If current element is in `remove_list`,
    if element in remove_list:
        # then current element should be removed from `ip_addresses`
        ip_addresses.remove(element)

# Convert `ip_addresses` back to a string so that it can be written into the text file
ip_addresses = " ".join(ip_addresses)

# Build `with` statement to rewrite the original file
with open(import_file, "w") as file:
    # Rewrite the file, replacing its contents with `ip_addresses`
    file.write(ip_addresses)

# Build `with` statement to read in the updated file
with open(import_file, "r") as file:
    # Read in the updated file and store the contents in `text`
    text = file.read()

# Display the contents of `text`
print(text)
```

**Output:**

```text
ip_address 192.168.25.60 192.168.205.12 192.168.6.9 192.168.52.90 192.168.90.124 192.168.186.176 192.168.133.188 192.168.203.198 192.168.218.219 192.168.52.37 192.168.156.224 192.168.60.153 192.168.69.116
```

**Observation:** The updated file no longer contains the removed IP addresses. The `"ip_address"` header is preserved at the beginning.

---

## Task 9: Define a Function

I encapsulated the entire algorithm into a function named `update_file()` that takes `import_file` and `remove_list` as parameters.

**Code:**

```python
def update_file(import_file, remove_list):
    # Build `with` statement to read in the initial contents of the file
    with open(import_file, "r") as file:
        # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
        ip_addresses = file.read()

    # Use `.split()` to convert `ip_addresses` from a string to a list
    ip_addresses = ip_addresses.split()

    # Build iterative statement
    # Name Loop variable `element`
    # Loop through `ip_addresses`
    for element in ip_addresses:
        # Build conditional statement
        # If current element is in `remove_list`,
        if element in remove_list:
            # then current element should be removed from `ip_addresses`
            ip_addresses.remove(element)

    # Convert `ip_addresses` back to a string so that it can be written into the text file
    ip_addresses = " ".join(ip_addresses)

    # Build `with` statement to rewrite the original file
    with open(import_file, "w") as file:
        # Rewrite the file, replacing its contents with `ip_addresses`
        file.write(ip_addresses)
```

**Observation:** The function encapsulates all the steps, making the code reusable and modular.

---

## Task 10: Call the Function

I called the `update_file()` function with a new list of IP addresses to remove and verified the updated file.

**Code:**

```python
# Define a function named `update_file` that takes in two parameters: `import_file` and `remove_list`
# and combines the steps you've written in this lab leading up to this
def update_file(import_file, remove_list):
    # Build `with` statement to read in the initial contents of the file
    with open(import_file, "r") as file:
        # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
        ip_addresses = file.read()

    # Use `.split()` to convert `ip_addresses` from a string to a list
    ip_addresses = ip_addresses.split()

    # Build iterative statement
    # Name Loop variable `element`
    # Loop through `ip_addresses`
    for element in ip_addresses:
        # Build conditional statement
        # If current element is in `remove_list`,
        if element in remove_list:
            # then current element should be removed from `ip_addresses`
            ip_addresses.remove(element)

    # Convert `ip_addresses` back to a string so that it can be written into the text file
    ip_addresses = " ".join(ip_addresses)

    # Build `with` statement to rewrite the original file
    with open(import_file, "w") as file:
        # Rewrite the file, replacing its contents with `ip_addresses`
        file.write(ip_addresses)

# Call `update_file()` and pass in `allow_list.txt` and a list of IP addresses to be removed
update_file("allow_list.txt", ["192.168.25.68", "192.168.140.81", "192.168.283.198"])

# Build `with` statement to read in the updated file
with open("allow_list.txt", "r") as file:
    # Read in the updated file and store the contents in `text`
    text = file.read()

# Display the contents of `text`
print(text)
```

**Output:**

```text
ip_address 192.168.25.60 192.168.205.12 192.168.6.9 192.168.52.90 192.168.90.124 192.168.186.176 192.168.133.188 192.168.203.198 192.168.218.219 192.168.52.37 192.168.156.224 192.168.60.153 192.168.69.116
```

**Observation:** The function successfully removed the specified IP addresses and updated the file. The `"ip_address"` header is preserved.

---

## Consolidated Key Takeaways

- **`with` statement** ensures files are properly opened and closed.
- **`.read()`** reads the entire file as a string.
- **`.split()`** converts a string into a list, useful for parsing space-separated data.
- **`.join()`** converts a list back into a string for writing to a file.
- **`for` loops** with `if` statements can remove unwanted elements from a list.
- **Functions** encapsulate reusable logic, making code modular and maintainable.

---

## Conclusion

This lab provided hands-on practice with parsing and updating a text file in Python for security-related tasks. By the end of the exercises, I had successfully:

- Read an allow list from a text file.
- Converted the file contents into a list.
- Removed IP addresses that no longer had access.
- Updated the original file with the revised list.
- Encapsulated the algorithm into a reusable function.

These skills are directly applicable to automating access control list management and other security documentation tasks.

---

## Comparison to `text_parser.py`

Throughout this course, I have built multiple Python scripts that work with text files. This lab and the earlier `text_parser.py` script share similar foundations but serve different purposes. Below is a comparison of the two.

### `text_parser.py` – Log Analysis

```python
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
```

### Comparison Table

| Aspect | `text_parser.py` | `update_file.py` (This Lab) |
| :--- | :--- | :--- |
| **Purpose** | Analyzes log files to count occurrences of a keyword. | Updates an allow list by removing unwanted IP addresses. |
| **File Input** | Reads a log file (`sample_log.txt`). | Reads an allow list file (`allow_list.txt`). |
| **File Output** | Prints analysis results to the console. | Rewrites the allow list file with updated contents. |
| **Data Structure** | Reads lines into a list; treats each line as a string. | Reads contents as a string, splits into a list, modifies, and joins back. |
| **Iteration** | `for` loop over each line. | `for` loop over each IP address. |
| **Conditional Logic** | `if search_word.upper() in line.upper()`. | `if element in remove_list`. |
| **Case Sensitivity** | Uses `.upper()` for case‑insensitive matching. | Relies on exact string matching. |
| **Error Handling** | `try`/`except` to handle missing files. | Assumes the file exists. |
| **Reusability** | Standalone script. | Encapsulated in a reusable function (`update_file()`). |

### Key Differences in Approach

| Difference | `text_parser.py` | `update_file.py` |
| :--- | :--- | :--- |
| **Purpose** | Analysis (read-only). | Modification (read-write). |
| **File Mode** | `"r"` (read only). | `"r"` and `"w"` (read and write). |
| **Data Modification** | Does not modify the original file. | Overwrites the original file with updated data. |
| **Output** | Console output (statistics). | Updated file and console verification. |
| **Flexibility** | Hardcoded filename and search word. | Function parameters allow dynamic input. |

### Overlapping Skills Demonstrated

Both scripts demonstrate the following core Python skills:

1. **File Handling:** Using `with open()` to safely read from and write to files.
2. **String Manipulation:** Using `.split()`, `.join()`, `.upper()`, and the `in` operator.
3. **Iteration:** Using `for` loops to process data line by line or element by element.
4. **Conditional Logic:** Using `if` statements to filter and act on specific conditions.
5. **Error Handling:** Using `try`/`except` to manage missing files.

### Why This Matters for a Security Analyst

- **`text_parser.py`** demonstrates the ability to **analyze logs** – a core SOC function. By parsing logs for keywords like "ERROR", analysts can identify system issues, security incidents, or suspicious activity.
- **`update_file.py`** demonstrates the ability to **manage access control lists** – another essential security task. Automating the removal of unauthorised IP addresses ensures that only approved users retain access to restricted resources.

Together, these scripts show a progression from simple log analysis to active file manipulation and automation. This reflects the real‑world responsibilities of a security analyst: monitoring, investigating, and remediating security issues.

---

## Reflection

This lab reinforced the importance of file parsing and list manipulation in security automation. Being able to efficiently update allow lists programmatically is essential for maintaining access control in a dynamic environment.

The progression from opening a file to defining a reusable function demonstrated how to build modular, production-ready security tools. Encapsulating the algorithm in a function makes it easy to reuse for different files and remove lists.

Mastering these techniques is essential for building robust security automation scripts that manage access control lists, log files, and other security documentation.

---

> *This lab was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*
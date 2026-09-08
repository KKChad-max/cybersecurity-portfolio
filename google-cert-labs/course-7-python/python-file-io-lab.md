# Python File I/O Lab: Importing and Parsing Text Files

**Date:** September 8, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I work with security logs that are often stored in text files. To analyze these logs, I need to import and parse them using Python. In this lab, I practiced:

1. **Importing a security log file** and reading its contents.
2. **Appending missing entries** to a log file.
3. **Creating a new text file** containing a list of IP addresses allowed to access restricted information.

---

## Task 1: Open a File with `with`

I started by writing the first line of a `with` statement to open the security log file. The `with` statement ensures the file is automatically closed after reading.

**Code:**

```python
# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"

# First Line of the `with` statement
# Use `open()` to import security log file and store it as a string
with open(import_file, "r") as file:
```

**Observation:** The `with` statement opens `login.txt` in read mode (`"r"`). The file object is assigned to the variable `file`.

---

## Task 2: Read the File with `.read()`

I used the `.read()` method to read the contents of the imported file and stored the result in a variable named `text`. I then displayed `text` to examine its contents.

**Code:**

```python
# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"

# The `with` statement
# Use `open()` to import security log file and store it as a string
with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store the result in a variable named `text`
    text = file.read()

# Display the contents of `text`
print(text)
```

**Output:**

```text
username,ip_address,time,date
tshah,192.168.92.147,15:26:08,2022-05-10
dtanaka,192.168.98.221,9:45:18,2022-05-09
tmitchel,192.168.110.131,14:13:41,2022-05-11
daquino,192.168.168.144,7:02:35,2022-05-08
eraab,192.168.170.243,1:45:14,2022-05-11
jlansky,192.168.238.42,1:07:11,2022-05-11
acook,192.168.52.90,9:56:48,2022-05-10
asundara,192.168.58.217,23:17:52,2022-05-12
jclark,192.168.214.49,20:49:00,2022-05-10
cjackson,192.168.247.153,19:36:42,2022-05-12
jclark,192.168.197.247,14:11:04,2022-05-12
apatel,192.168.46.207,17:39:42,2022-05-10
mabadi,192.168.96.244,10:24:43,2022-05-12
iuduike,192.168.131.147,17:50:00,2022-05-11
abelimas,192.168.60.111,13:37:05,2022-05-10
gesparza,192.168.148.80,6:30:14,2022-05-11
cgriffin,192.168.4.157,23:04:05,2022-05-09
alevitsk,192.168.210.228,8:10:43,2022-05-08
eraab,192.168.24.12,11:29:27,2022-05-11
jsoto,192.168.25.60,5:09:21,2022-05-09
```

**Observation:** The `text` variable contains the entire log file as a single string, with each line separated by newline characters (`\n`).

---

## Task 3: Split the String into Lines

I used the `.split()` method to split the string into a list of strings, with each line as a separate element.

**Code:**

```python
# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"

# The `with` statement
# Use `open()` to import security log file and store it as a string
with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store the result in a variable named `text`
    text = file.read()

# Display the contents of `text` split into separate lines
print(text.split())
```

**Output:**

```text
['username,ip_address,time,date', 'tshah,192.168.92.147,15:26:08,2022-05-10', 'dtanaka,192.168.98.221,9:45:18,2022-05-09', 'tmitchel,192.168.110.131,14:13:41,2022-05-11', 'daquino,192.168.168.144,7:02:35,2022-05-08', 'eraab,192.168.170.243,1:45:14,2022-05-11', 'jlansky,192.168.238.42,1:07:11,2022-05-11', 'acook,192.168.52.98,9:56:48,2022-05-10', 'asundara,192.168.58.217,23:17:52,2022-05-12', 'jclark,192.168.214.49,20:49:00,2022-05-10', 'cjackson,192.168.247.153,19:36:42,2022-05-12', 'jclark,192.168.197.247,14:11:04,2022-05-12', 'apatel,192.168.46.207,17:39:42,2022-05-10', 'mabadi,192.168.96.244,10:24:43,2022-05-12', 'iuduike,192.168.131.147,17:50:00,2022-05-11', 'abellmas,192.168.60.111,13:37:05,2022-05-10', 'gesparza,192.168.148.80,6:30:14,2022-05-11', 'cgriffin,192.168.4.157,23:04:05,2022-05-09', 'alevitsk,192.168.210.228,8:10:43,2022-05-08', 'eraab,192.168.24.12,11:29:27,2022-05-11', 'jsoto,192.168.25.60,5:09:21,2022-05-29']
```

**Observation:** Before using `.split()`, the output is one continuous string. After using `.split()`, the output is a list where each element is a line from the file. This is useful for iterating through log entries.

---

## Task 4: Append a Missing Entry

There was a missing entry in the log file. I appended it using the `.write()` method with the `"a"` parameter in the `open()` function.

**Code:**

```python
# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"

# Assign `missing_entry` to a log that was not recorded in the log file
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"

# Use `open()` to import security log file and store it as a string
# Pass in "a" as the second parameter to indicate that the file is being opened for appending purposes
with open(import_file, "a") as file:
    # Use `.write()` to append `missing_entry` to the log file
    file.write(missing_entry)

# Use `open()` with the parameter `"r"` to open the security log file for reading purposes
with open(import_file, "r") as file:
    # Use `.read()` to read in the contents of the log file and store in a variable named `text`
    text = file.read()

# Display the contents of `text`
print(text)
```

**Output:**

```text
username,ip_address,time,date
tshah,192.168.92.147,15:26:08,2022-05-10
dtanaka,192.168.98.221,9:45:18,2022-05-09
tmitchel,192.168.110.131,14:13:41,2022-05-11
daquino,192.168.168.144,7:02:35,2022-05-08
eraab,192.168.170.243,1:45:14,2022-05-11
jlansky,192.168.238.42,1:07:11,2022-05-11
acook,192.168.52.98,9:56:48,2022-05-10
asundara,192.168.58.217,23:17:52,2022-05-12
jclark,192.168.214.49,20:49:00,2022-05-10
cjackson,192.168.247.153,19:36:42,2022-05-12
jclark,192.168.197.247,14:11:04,2022-05-12
apatel,192.168.46.207,17:39:42,2022-05-10
mabadi,192.168.96.244,10:24:43,2022-05-12
iuduike,192.168.131.147,17:50:00,2022-05-11
abellmas,192.168.60.111,13:37:05,2022-05-10
gesparza,192.168.148.80,6:30:14,2022-05-11
cgriffin,192.168.4.157,23:04:05,2022-05-09
alevitsk,192.168.210.228,8:10:43,2022-05-08
eraab,192.168.24.12,11:29:27,2022-05-11
jsoto,192.168.25.60,5:09:21,2022-05-29
jrafael,192.168.243.140,4:56:27,2022-05-09
```

**Observation:** The missing entry was appended to the end of the file. This is because the `"a"` parameter opens the file for appending, which adds new content to the end without overwriting existing data.

---

## Task 5: Create a New Text File

I created a new text file named `"allow_list.txt"` to store a list of IP addresses that are allowed to access restricted information.

**Code:**

```python
# Assign `import_file` to the name of the text file that you want to create
import_file = "allow_list.txt"

# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = ["192.168.218.160", "192.168.97.225", "192.168.145.158", "192.168.108.13", "192.168.60.153", "192.168.96.200", "192.168.247.153", "192.168.3.252", "192.168.116.187", "192.168.15.110", "192.168.39.246"]

# Display `import_file`
print(import_file)

# Display `ip_addresses`
print(ip_addresses)
```

**Output:**

```text
allow_list.txt
['192.168.218.160', '192.168.97.225', '192.168.145.158', '192.168.108.13', '192.168.60.153', '192.168.96.200', '192.168.247.153', '192.168.3.252', '192.168.116.187', '192.168.15.110', '192.168.39.246']
```

**Observation:** The `import_file` variable stores the filename, and `ip_addresses` contains a list of IP addresses.

---

## Task 6: Write to the Text File

I created a `with` statement to write the list of IP addresses to the text file using the `"w"` parameter.

**Code:**

```python
# Assign `import_file` to the name of the text file that you want to create
import_file = "allow_list.txt"

# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = ["192.168.218.160", "192.168.97.225", "192.168.145.158", "192.168.108.13", "192.168.60.153", "192.168.96.200", "192.168.247.153", "192.168.3.252"]

# Create a `with` statement to write to the text file
with open(import_file, "w") as file:
    # Write `ip_addresses` to the text file
    file.write(str(ip_addresses))
```

**Observation:** The `"w"` parameter opens the file for writing. If the file already exists, it will be overwritten. The `str()` function converts the list to a string before writing.

---

## Task 7: Read the File

I added code to read the text file and display its contents.

**Code:**

```python
# Assign `import_file` to the name of the text file that you want to create
import_file = "allow_list.txt"

# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = ["192.168.218.160", "192.168.97.225", "192.168.145.158", "192.168.108.13", "192.168.60.153", "192.168.96.200", "192.168.247.153", "192.168.3.252"]

# Create a `with` statement to write to the text file
with open(import_file, "w") as file:
    # Write `ip_addresses` to the text file
    file.write(str(ip_addresses))

# Create a `with` statement to read in the text file
with open(import_file, "r") as file:
    # Read the file and store the result in a variable named `text`
    text = file.read()

# Display the contents of `text`
print(text)
```

**Output:**

```text
['192.168.218.160', '192.168.97.225', '192.168.145.158', '192.168.108.13', '192.168.60.153', '192.168.96.200', '192.168.247.153', '192.168.3.252']
```

**Observation:** The file was successfully written and then read back, displaying the list of IP addresses as a string.

---

## File Contents Reset

To reset the `login.txt` file to its original contents, I used the following code:

```python
# Resets the `"login.txt"` file to its original contents
# Allows learners to complete lab more than once

# Assigns the original contents of the file to the `login_file` variable
login_file = """username,ip_address,time,date
tshah,192.168.92.147,15:26:08,2022-05-10
dtanaka,192.168.98.221,9:45:18,2022-05-09
tmitchel,192.168.110.131,14:13:41,2022-05-11
daquino,192.168.168.144,7:02:35,2022-05-08
eraab,192.168.170.243,1:45:14,2022-05-11
jlansky,192.168.238.42,1:07:11,2022-05-11
acook,192.168.52.90,9:56:48,2022-05-10
asundara,192.168.58.217,23:17:52,2022-05-12
jclark,192.168.214.49,20:49:00,2022-05-10
cjackson,192.168.247.153,19:36:42,2022-05-12
jclark,192.168.197.247,14:11:04,2022-05-12
apatel,192.168.46.207,17:39:42,2022-05-10
mabadi,192.168.96.244,10:24:43,2022-05-12
iuduike,192.168.131.147,17:50:00,2022-05-11
abelimas,192.168.60.111,13:37:05,2022-05-10
gesparza,192.168.148.80,6:30:14,2022-05-11
cgriffin,192.168.4.157,23:04:05,2022-05-09
alevitsk,192.168.210.228,8:10:43,2022-05-08
eraab,192.168.24.12,11:29:27,2022-05-11
jsoto,192.168.25.60,5:09:21,2022-05-09
"""

# Writes `login_file` to the `"login.txt"` file
with open("login.txt", "w") as file:
    file.write(login_file)
```

---

## Consolidated Key Takeaways

- **`with` statement** automatically closes files after reading or writing.
- **`open()` function** requires two parameters: the filename and the mode (`"r"` for read, `"w"` for write, `"a"` for append).
- **`.read()`** reads the entire file as a single string.
- **`.split()`** splits a string into a list, useful for processing line-by-line.
- **`.write()`** writes a string to a file.
- **`"a"` mode** appends to the end of a file without overwriting existing content.
- **`"w"` mode** overwrites the file or creates a new one.

---

## Conclusion

This lab provided hands-on practice with file input/output operations in Python for security-related tasks. By the end of the exercises, I had successfully:

- Imported a security log file using `open()` and `with`.
- Read the file contents using `.read()`.
- Split the text into lines using `.split()`.
- Appended a missing entry to the log file using `"a"` mode.
- Created a new text file and written IP addresses to it using `"w"` mode.
- Read the newly created file to verify its contents.

These skills are directly applicable to automating log analysis, generating allow lists, and managing security documentation.

---

## Reflection

This lab reinforced the importance of file handling in security automation. Being able to import, parse, and modify text files is a foundational skill for any SOC analyst.

The ability to append missing entries to a log file demonstrates how to update security records programmatically. Creating and writing to a new file with IP addresses shows how to generate documentation that can be shared with a security team.

Mastering file I/O is essential for building security tools that read logs, process data, and generate reports.

---

> *This lab was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*

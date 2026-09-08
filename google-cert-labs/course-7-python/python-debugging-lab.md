# Python Debugging Lab

**Date:** September 8, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I need to ensure that automated processes run smoothly. Debugging is an essential practice that helps identify and resolve errors in code so that it achieves the desired outcome.

Throughout this lab, I worked with code similar to what I've written before, but with intentional errors. I ran the code, identified the errors, and adjusted the code to resolve them.

---

## Task 1: Syntax Error – Missing Colon

The following code cell contained a syntax error. I ran the code, identified the error, and fixed it.

**Original Code:**

```python
# For Loop that iterates over a range of numbers
# and displays a message each iteration

for i in range(10)
    print("Connection cannot be established")
```

**Error:** The `for` loop is missing a colon (`:`) at the end of the line.

**Fixed Code:**

```python
# For Loop that iterates over a range of numbers
# and displays a message each iteration

for i in range(10):
    print("Connection cannot be established")
```

**Output:**

```text
Connection cannot be established
Connection cannot be established
Connection cannot be established
Connection cannot be established
Connection cannot be established
Connection cannot be established
Connection cannot be established
Connection cannot be established
Connection cannot be established
Connection cannot be established
```

**Observation:** The `for` loop requires a colon at the end of the line to indicate the start of the loop body. Without it, Python raises a `SyntaxError`.

---

## Task 2: Syntax Error – Missing Comma in List

The following code cell contained a syntax error. I ran the code, identified the error, and fixed it.

**Original Code:**

```python
# Assign `usernames_list` to a list of usernames
usernames_list = ["dnames", "jpark", "tbailey", "zdutchma" "esmith", "srobinso", "dcoleman", "fbautist"]

# Display `usernames_list`
print(usernames_list)
```

**Error:** The list is missing a comma between `"zdutchma"` and `"esmith"`. Without the comma, Python treats them as a single string (`"zdutchmaesmith"`).

**Fixed Code:**

```python
# Assign `usernames_list` to a list of usernames
usernames_list = ["dnames", "jpark", "tbailey", "zdutchma", "esmith", "srobinso", "dcoleman", "fbautist"]

# Display `usernames_list`
print(usernames_list)
```

**Output:**

```text
['dnames', 'jpark', 'tbailey', 'zdutchma', 'esmith', 'srobinso', 'dcoleman', 'fbautist']
```

**Observation:** Python requires commas to separate elements in a list. Missing commas cause unexpected string concatenation.

---

## Task 3: Syntax Error – Missing Closing Parenthesis

The following code cell contained a syntax error. I ran the code, identified the error, and fixed it.

**Original Code:**

```python
# Display a message in upper case
print("update needed".upper()
```

**Error:** The `print()` function is missing a closing parenthesis.

**Fixed Code:**

```python
# Display a message in upper case
print("update needed".upper())
```

**Output:**

```text
UPDATE NEEDED
```

**Observation:** The `print()` function requires a closing parenthesis to complete the function call. Without it, Python raises a `SyntaxError`.

---

## Task 4: Multiple Errors – Variable Name, Comparison Operator, and Indentation

The following code cell contained two syntax errors and one exception. I fixed them one at a time.

**Original Code:**

```python
# Assign `usernames_list` to a list of usernames that represent approved users
usernames_list = ["dnames", "jpark", "tbailey", "zducthma", "esmith", "srobinso", "dcoleman", "fbautist"]

# Assign `username` to a specific username
username = "esmith"

# For Loop that iterates over the elements of `usernames_list` and determines whether each element corresponds to an approved user
for name in username_list:
    # Check if `name` matches `username`
    # If it does match, then display a message accordingly
    if name = username:
    print("The user is an approved user")
```

**Errors:**
1. **Syntax Error 1:** `username_list` is used instead of `usernames_list` – variable name mismatch.
2. **Syntax Error 2:** `if name = username:` uses `=` instead of `==`.
3. **Exception:** The `print()` statement is not indented inside the `if` block.

**Fixed Code:**

```python
# Assign `usernames_list` to a list of usernames that represent approved users
usernames_list = ["dnames", "jpark", "tbailey", "zducthma", "esmith", "srobinso", "dcoleman", "fbautist"]

# Assign `username` to a specific username
username = "esmith"

# For Loop that iterates over the elements of `usernames_list` and determines whether each element corresponds to an approved user
for name in usernames_list:
    # Check if `name` matches `username`
    # If it does match, then display a message accordingly
    if name == username:
        print("The user is an approved user")
```

**Output:**

```text
The user is an approved user
```

**Observation:** 
- Variable names must be consistent.
- Comparison uses `==`, not `=`.
- Code blocks must be properly indented.

---

## Task 5: Index Error – List Index Out of Range

The following code cell contained an index error. I identified the type of error and fixed it.

**Original Code:**

```python
# Assign `usernames_list` to a list of usernames
usernames_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to a specific username
username = "eraab"

# Determine whether `username` is the final username in `usernames_list`
# If it is, then display a message accordingly
if username == usernames_list[5]:
    print("This username is the final one in the list.")
```

**Error:** `usernames_list[5]` is out of range because the list has 5 elements (indices 0–4). Index 5 does not exist.

**Fixed Code:**

```python
# Assign `usernames_list` to a list of usernames
usernames_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to a specific username
username = "eraab"

# Determine whether `username` is the final username in `usernames_list`
# If it is, then display a message accordingly
if username == usernames_list[-1]:
    print("This username is the final one in the list.")
```

**Output:**

```text
This username is the final one in the list.
```

**Observation:** The `-1` index accesses the last element of a list. This is a safer way to check the final element without assuming the list length.

---

## Task 6: Multiple Errors – Method Call Syntax and Logic Error

The following code cell contained a syntax error and an exception related to a string method. I fixed both.

**Original Code:**

```python
# Assign `import_file` to the name of the text file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access the network
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# With statement that reads in the text file and stores its contents as a list in `ip_addresses`
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert `ip_addresses` from a string to a list
ip_addresses = split.ip_addresses()

# For Loop that iterates over the elements in `remove_list`,
# checks if each element is in `ip_addresses`,
# and removes each element that corresponds to an IP address that is no longer allowed
for element in remove_list:
    if element in ip_addresses:
    ip_addresses.remove(element)

# Display `ip_addresses` after the removal process
print(ip_addresses)
```

**Errors:**
1. **Syntax Error:** `split.ip_addresses()` is incorrect. The correct syntax is `ip_addresses.split()`.
2. **Exception:** The `if` statement is missing indentation for the `ip_addresses.remove(element)` line.

**Fixed Code:**

```python
# Assign `import_file` to the name of the text file
import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access the network
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# With statement that reads in the text file and stores its contents as a list in `ip_addresses`
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()

# For Loop that iterates over the elements in `remove_list`,
# checks if each element is in `ip_addresses`,
# and removes each element that corresponds to an IP address that is no longer allowed
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Display `ip_addresses` after the removal process
print(ip_addresses)
```

**Output:**

```text
['ip_address', '192.168.25.60', '192.168.205.12', '192.168.6.9', '192.168.52.90', '192.168.90.124', '192.168.186.176', '192.168.133.188', '192.168.203.198', '192.168.218.219', '192.168.52.37', '192.168.156.224', '192.168.60.153', '192.168.69.116']
```

**Observation:** 
- The `.split()` method is called on the string variable, not the other way around.
- Indentation is critical for defining blocks of code within loops and conditionals.

---

## Task 7: Logic Error – Incorrect Index Mapping

The following code contained logic errors. I assigned the `system` variable to different values, identified the incorrect output, and fixed it.

**Original Code:**

```python
# Assign `system` to a specific operating system as a string
system = "OS 2"

# Assign `patch_schedule` to a list of patch dates in order of operating system
patch_schedule = ["March 1st", "April 1st", "May 1st"]

# Conditional statement that checks which operating system is stored in `system` and displays a message showing the corresponding date
if system == "OS 1":
    print("Patch date:", patch_schedule[2])
elif system == "OS 2":
    print("Patch date:", patch_schedule[0])
elif system == "OS 3":
    print("Patch date:", patch_schedule[2])
```

**Error:** The indices in the `patch_schedule` list do not correctly map to the operating systems:
- `"OS 1"` should map to `"March 1st"` (index 0).
- `"OS 2"` should map to `"April 1st"` (index 1).
- `"OS 3"` should map to `"May 1st"` (index 2).

**Fixed Code:**

```python
# Assign `system` to a specific operating system as a string
system = "OS 2"

# Assign `patch_schedule` to a list of patch dates in order of operating system
patch_schedule = ["March 1st", "April 1st", "May 1st"]

# Conditional statement that checks which operating system is stored in `system` and displays a message showing the corresponding date
if system == "OS 1":
    print("Patch date:", patch_schedule[0])
elif system == "OS 2":
    print("Patch date:", patch_schedule[1])
elif system == "OS 3":
    print("Patch date:", patch_schedule[2])
```

**Output (for `system = "OS 2"`):**

```text
Patch date: April 1st
```

**Observation:** Logic errors occur when the code runs without crashing but produces incorrect results. Careful mapping of indices to values is essential for correct output.

---

## Consolidated Key Takeaways

- **Syntax Errors** occur when the code violates Python's grammar rules (e.g., missing colons, parentheses, or commas).
- **Exceptions** occur when the code runs but encounters an error (e.g., index out of range).
- **Logic Errors** occur when the code runs but produces incorrect results (e.g., wrong index mapping).
- **Debugging Strategy:** Focus on one error at a time. Run the code after fixing each error to verify the fix.
- **Indentation** is critical in Python – it defines code blocks.
- **Method Calls** must be applied to the correct objects (e.g., `string.split()`, not `split.string()`).

---

## Conclusion

This lab provided hands-on practice with debugging Python code in a security context. By the end of the exercises, I had successfully:

- Identified and fixed syntax errors (missing colons, commas, parentheses).
- Fixed exceptions (index out of range, method call errors).
- Corrected logic errors (incorrect index mapping, variable name mismatches).
- Used a systematic approach to debug code by focusing on one error at a time.

These skills are directly applicable to writing and maintaining reliable security automation scripts.

---

## Reflection

This lab reinforced the importance of debugging in security automation. Errors in code can lead to incorrect results, failed automation, or even security vulnerabilities. Being able to systematically identify, diagnose, and fix errors is essential for any security analyst who writes Python scripts.

The progression from simple syntax errors to complex logic errors demonstrated how to apply a structured debugging approach. I also learned that running code frequently and testing after each fix is the most efficient way to debug.

Mastering debugging is essential for building robust security tools that automate log analysis, access control, and threat detection.

---

> *This lab was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*
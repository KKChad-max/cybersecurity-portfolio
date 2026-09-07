# Python Regular Expressions Lab: Extracting Device IDs and IP Addresses

**Date:** September 7, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I work with log files that contain information about login attempts, device IDs, and IP addresses. Using regular expressions in Python helps automate the process of extracting important information from these files.

In this lab, I completed two main tasks:

1. **Extracting device IDs** containing certain characters from a log to identify devices requiring updates.
2. **Extracting all valid IP addresses** from a log and comparing them to a list of flagged addresses.

---

## Task 1: Import the `re` Module

I imported the `re` module, which contains functions for working with regular expressions in Python.

**Code:**

```python
import re
```

**Observation:** The `re` module is now available for use throughout the notebook.

---

## Task 2: Display the Device Log

I examined the contents of a string containing device IDs.

**Code:**

```python
devices = "r262c36 67bv8fy 41jlu2e r151dm4 1270t3o 42dr56i r15xkh9 2j33krk 253be78 ac742a1 r15u9q5 zh86b21 i1286fq 9x482kt 6oa6mc"
print(devices)
```

**Output:**

```text
r262c36 67bv8fy 41jlu2e r151dm4 1270t3o 42dr56i r15xkh9 2j33krk 253be78 ac742a1 r15u9q5 zh86b21 i1286fq 9x482kt 6oa6mc
```

**Observation:** The string displays all device IDs separated by spaces.

---

## Task 3: Build a Pattern for Device IDs

I created a regular expression pattern to find device IDs that start with `"r15"`.

**Code:**

```python
target_pattern = r"r15\w+"
```

**Pattern breakdown:**
- `r15` – matches the literal characters "r15".
- `\w+` – matches one or more alphanumeric characters (letters, digits, or underscores).

**Observation:** The pattern will match any device ID that begins with "r15".

---

## Task 4: Extract Matching Device IDs

I used `re.findall()` to extract all device IDs that match the pattern.

**Code:**

```python
devices = "r262c36 67bv8fy 41jlu2e r151dm4 1270t3o 42dr56i r15xkh9 2j33krk 253be78 ac742a1 r15u9q5 zh86b21 i1286fq 9x482kt 6oa6mc"
target_pattern = r"r15\w+"
print(re.findall(target_pattern, devices))
```

**Output:**

```text
['r151dm4', 'r15xkh9', 'r15u9q5']
```

**Observation:** The pattern successfully extracted all device IDs starting with `"r15"`.

---

## Task 5: Display the Log File

I examined the contents of a network security log file.

**Code:**

```python
log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 1"
print(log_file)
```

**Output:**

```text
eraab 2022-05-10 6:03:41 192.168.152.148
iuduike 2022-05-09 6:46:40 192.168.22.115
smartell 2022-05-09 19:30:32 1
```

**Observation:** The log file contains usernames, dates, times, and IP addresses.

---

## Task 6: Build a Pattern for IP Addresses (Strict)

I created a pattern to match IP addresses with exactly three digits per segment.

**Code:**

```python
pattern = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
```

**Pattern breakdown:**
- `\d` – matches a digit (0-9).
- `\.` – matches a literal period.

**Observation:** This pattern only matches IP addresses with exactly three digits per segment.

---

## Task 7: Extract IP Addresses (Strict)

I used `re.findall()` with the strict pattern.

**Code:**

```python
log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 1"
pattern = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
print(re.findall(pattern, log_file))
```

**Output:**

```text
['192.168.152.148']
```

**Observation:** Only `192.168.152.148` was extracted. `192.168.22.115` was missed because it has only two digits in the third segment.

---

## Task 8: Adjust the Pattern for Variable Digits

I updated the pattern to allow one to three digits per segment using `+`.

**Code:**

```python
log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 1"
pattern = r"\d+\.\d+\.\d+\.\d+"
print(re.findall(pattern, log_file))
```

**Output:**

```text
['192.168.152.148', '192.168.22.115']
```

**Observation:** Both valid IP addresses were extracted, but the pattern is too broad—it would also match invalid IPs like `9999.9999.9999.9999`.

---

## Task 9: Use Curly Brackets for Precise Matching

I refined the pattern using `{1,3}` to match exactly one to three digits per segment.

**Code:**

```python
log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 1"
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
valid_ip_addresses = re.findall(pattern, log_file)
print(valid_ip_addresses)
```

**Output:**

```text
['192.168.152.148', '192.168.22.115']
```

**Observation:** This pattern extracts only valid IP addresses with one to three digits per segment, without matching invalid entries.

---

## Task 10: Display Flagged IP Addresses

I displayed a list of IP addresses that had been previously flagged for unusual activity.

**Code:**

```python
flagged_addresses = ["192.168.190.178", "192.168.96.200", "192.168.174.117", "192.168.168.144"]
print(flagged_addresses)
```

**Output:**

```text
['192.168.190.178', '192.168.96.200', '192.168.174.117', '192.168.168.144']
```

**Observation:** The list contains four IP addresses flagged for further analysis.

---

## Task 11: Check for Flagged IP Addresses

I looped through the extracted IP addresses and checked if each was flagged.

**Code:**

```python
log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 1"
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
valid_ip_addresses = re.findall(pattern, log_file)

flagged_addresses = ["192.168.190.178", "192.168.96.200", "192.168.174.117", "192.168.168.144"]

for address in valid_ip_addresses:
    if address in flagged_addresses:
        print("The IP address", address, "has been flagged for further analysis.")
    else:
        print("The IP address", address, "does not require further analysis.")
```

**Output:**

```text
The IP address 192.168.152.148 does not require further analysis.
The IP address 192.168.22.115 does not require further analysis.
```

**Observation:** None of the extracted IP addresses were flagged, so no alerts were triggered.

---

## Consolidated Key Takeaways

- **`re` module** provides functions like `findall()` for pattern matching.
- **`\w+`** matches one or more alphanumeric characters (useful for device IDs).
- **`\d`** matches digits; **`+`** matches one or more; **`{1,3}`** matches exactly 1 to 3.
- **`\.`** matches a literal period (must be escaped).
- **`re.findall()`** returns a list of all non-overlapping matches.
- **Iterative statements with conditionals** can be used to check extracted data against flagged lists.

---

## Conclusion

This lab provided hands-on practice with regular expressions in Python for security-related tasks. By the end of the exercises, I had successfully:

- Extracted device IDs starting with `"r15"` using `\w+`.
- Built and refined patterns for IP addresses using `\d`, `+`, and `{1,3}`.
- Extracted valid IP addresses from a log file.
- Looped through extracted IP addresses and checked them against a flagged list.

These skills are directly applicable to automating log analysis, threat detection, and security monitoring tasks.

---

## Reflection

This lab reinforced the importance of regular expressions in security automation. Being able to extract specific patterns from unstructured log data—such as device IDs or IP addresses—is a foundational skill for any SOC analyst.

The progression from a strict pattern (`\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d`) to a flexible pattern (`\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`) demonstrated how to balance precision and flexibility in regex design. The final loop showed how to operationalise the extracted data by checking it against a flagged list.

Mastering regular expressions is essential for building efficient security tools that automate threat detection and incident response.

---

> *This lab was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*
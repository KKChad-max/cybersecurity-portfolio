# Python Strings Lab: Working with String Data

**Date:** September 2, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I work with a lot of string data—employee IDs, device IDs, and URLs are all commonly represented as strings. In this lab, I practiced:

- Converting data types to strings.
- Using string methods like `.index()`.
- Extracting substrings using string slicing and indexing.

Throughout this lab, I built foundational skills for automating tasks such as updating ID formats, extracting device information, and parsing URLs.

---

## Task 1: Converting an Integer to a String

I was given a four-digit numeric employee ID (`4186`). I converted it to a string format using the `str()` function and verified the data type before and after the conversion.

**Code:**

```python
# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186

# Display the data type of `employee_id`
print(type(employee_id))

# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)

# Display the data type of `employee_id` now
print(type(employee_id))
```

**Output:**

```text
<class 'int'>
<class 'str'>
```

**Observation:** The first `print()` displays `<class 'int'>`, confirming the variable is an integer. After reassigning with `str()`, the second `print()` displays `<class 'str'>`, confirming it is now a string. This conversion is essential for string operations like concatenation and indexing.

---

## Task 2: Checking String Length with `len()`

I wrote a conditional statement to check if the employee ID has fewer than five digits.

**Code:**

```python
# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)

# Conditional statement that displays a message if the length of `employee_id` is less than five digits
if len(employee_id) < 5:
    print("This employee ID has less than five digits. It does not meet length requirements.")
```

**Output:**

```text
This employee ID has less than five digits. It does not meet length requirements.
```

**Observation:** The `len()` function returns the number of characters in the string. Since `"4186"` has four characters, the condition `len(employee_id) < 5` evaluates to `True`, and the message is displayed.

---

## Task 3: Concatenating Strings to Meet Length Requirements

I used string concatenation (`+`) to add an `"E"` in front of the four-digit ID, creating a five-character ID.

**Code:**

```python
# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)

# Display the `employee_id` as it currently stands
print(employee_id)

# Conditional statement that updates the `employee_id` if its length is less than 5 digits
if len(employee_id) < 5:
    employee_id = "E" + employee_id

# Display the `employee_id` after the update
print(employee_id)
```

**Output:**

```text
4186
E4186
```

**Observation:** The concatenation `"E" + employee_id` merges the string `"E"` with `"4186"`, resulting in `"E4186"`. This is a practical example of standardizing data formats in a security context.

---

## Task 4: Extracting a Specific Character with Indexing

I extracted the fourth character from the device ID `"r262c36"` using bracket notation.

**Code:**

```python
# Assign `device_id` to a string that contains alphanumeric characters
device_id = "r262c36"

# Extract the fourth character in `device_id` and display it
print(device_id[3])
```

**Output:**

```text
2
```

**Observation:** Python uses **zero-based indexing**, so the fourth character is at index `3`. This is useful for extracting specific characters from device IDs, usernames, or log entries.

---

## Task 5: Extracting a Slice (First Three Characters)

I extracted the first through third characters of the device ID using string slicing.

**Code:**

```python
# Assign `device_id` to a string that contains alphanumeric characters
device_id = "r262c36"

# Extract the first through the third characters in `device_id` and display the result
print(device_id[0:3])
```

**Output:**

```text
r26
```

**Observation:** The slice `[0:3]` includes characters at indices `0`, `1`, and `2`. This technique is useful for extracting meaningful segments from longer strings, such as prefixes in device IDs.

---

## Task 6: Extracting the Protocol from a URL

I extracted the protocol (`"https://"`) from a URL using string slicing.

**Code:**

```python
# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Extract the protocol of `url` along with the syntax following it, display the result
print(url[0:8])
```

**Output:**

```text
https://
```

**Observation:** The protocol `"https://"` occupies the first 8 characters of the URL. This is a common task in security analysis when parsing logs or URLs for threat intelligence.

---

## Task 7: Using `.index()` to Find a Substring

I used the `.index()` method to find where the domain extension `.com` begins in the URL.

**Code:**

```python
# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Display the index where the domain extension ".com" is located in `url`
print(url.index(".com"))
```

**Output:**

```text
22
```

**Observation:** The `.index()` method returns the starting index of the specified substring (`.com`). This allows for dynamic extraction of components even when the URL length varies.

---

## Task 8: Storing the Index in a Variable

I stored the output of `.index()` in a variable called `ind` for reuse.

**Code:**

```python
# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url`
ind = url.index(".com")
```

**Observation:** Storing values in variables improves code readability and reusability. The variable `ind` can now be used in multiple operations without recalculating the index.

---

## Task 9: Extracting the Domain Extension Using the Index

I used the `ind` variable to slice and extract the domain extension `.com`.

**Code:**

```python
# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url`
ind = url.index(".com")

# Extract the domain extension in `url` and display it
print(url[ind:ind+4])
```

**Output:**

```text
.com
```

**Observation:** The slice `url[ind:ind+4]` extracts the `.com` extension. This demonstrates how to use a dynamic index to extract a substring of known length.

---

## Task 10: Extracting the Website Name

I extracted the website name (`"exampleURL1"`) by slicing from the end of the protocol to the start of the domain extension.

**Code:**

```python
# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url`
ind = url.index(".com")

# Extract the website name in `url` and display it
print(url[8:ind])
```

**Output:**

```text
exampleURL1
```

**Observation:** The slice `[8:ind]` starts after `"https://"` and ends at the beginning of `.com`. This extracts the core domain name, which is useful for logging or filtering web traffic.

---

## Consolidated Key Takeaways

- **`str()`** converts non‑string data types (like integers) to strings.
- **`len()`** returns the number of characters in a string.
- **String concatenation (`+`)** merges strings together.
- **Zero‑based indexing** accesses specific characters in a string.
- **Slicing (`[start:end]`)** extracts substrings.
- **`.index()`** finds the starting position of a substring.
- **Dynamic slicing** using variables allows for flexible string extraction.

---

## Conclusion

This lab provided hands‑on practice with Python string operations in a security context. By the end of the exercises, I had successfully:

- Converted data types to strings.
- Checked string lengths and applied conditional logic.
- Used concatenation to standardize employee IDs.
- Extracted specific characters, slices, and components from device IDs and URLs.
- Used `.index()` to locate substrings dynamically.

### Bridging the Gap to Real‑World Security Automation

While this lab focused on static strings (IDs and URLs), the **exact same principles** power my `text_parser.py` script—a practical log‑analysis tool I built in my portfolio. 

In `text_parser.py`, I analyze log files to detect critical events (like authentication failures). The bridge between this lab and that script is **string methods**:

| Lab Concept (This Activity) | `text_parser.py` Implementation |
| :--- | :--- |
| **Slicing strings** to extract parts (`[0:3]`, `[8:ind]`) | Extracting timestamps, IPs, or user names from log lines using similar slice logic. |
| **`.index()`** to find substrings | `if "ERROR" in line.upper():` uses the `in` operator to locate substrings (finding "ERROR" in a log). |
| **Concatenation** (`+`) | Building custom log messages or constructing file paths using string concatenation. |
| **String Methods** (like `.upper()`) | `text_parser.py` uses `.upper()` to make searches case‑insensitive, ensuring "error", "Error", and "ERROR" are all detected reliably. |

`text_parser.py` takes the **building blocks** from this lab (finding substrings, comparing strings, and applying logic) and applies them to parsing live security logs. This demonstrates the progression from understanding syntax to building production‑ready automation tools.

---

## Reflection

This lab reinforced the importance of string manipulation in security automation. Converting data types, checking lengths, and extracting substrings are foundational tasks that appear repeatedly in security scripting.

The `.index()` method was particularly valuable because it enables dynamic parsing of URLs and log entries. In a real‑world SOC environment, analysts often need to extract domains, IPs, or file extensions from unstructured strings—and these techniques make that possible.

Mastering string operations is a critical step toward building more advanced security tools. The `text_parser.py` script is a direct example of this progression: it takes the simple string‑searching logic I practiced here and scales it to analyze hundreds of log lines, flagging critical security events automatically. Understanding how to manipulate, standardize, and search strings is essential for any security automation role.

---

> *This lab was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*

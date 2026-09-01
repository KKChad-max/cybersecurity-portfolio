# Python Variables Lab: Assigning and Using Variables

**Date:** September 1, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I am responsible for writing code that will automate analysis of login attempts made to a specific device. The first step is to create variables to keep track of information relevant to the login process, including:

- Device ID
- List of approved usernames
- Maximum login attempts allowed per user
- Current login attempts made by a user
- Login status

Throughout this lab, I assigned these variables and checked their data types.

---

## Task 1: Assign a String Variable

I assigned the device ID `"72e08x0"` to a variable named `device_id` and displayed it.

**Code & Output:**

```python
# Assign the `device_id` variable to the device ID that only specified users can access
device_id = "72e08x0"

# Display `device_id`
print(device_id)
```

**Output:** `72e08x0`

**Observation:** This value is text, so it must be stored as a string.

---

## Task 2: Checking Data Types (String)

To verify the data type of `device_id`, I used the `type()` function and stored the result in `device_id_type`.

**Code & Output:**

```python
# Assign the `device_id` variable to the device ID that only specified users can access
device_id = "72e08x0"

# Assign `device_id_type` to the data type of `device_id`
device_id_type = type(device_id)

# Display `device_id_type`
print(device_id_type)
```

**Output:** `<class 'str'>`

**Key Insight:** The output confirms that the `device ID` is stored as a `str` (string). In Python, strings are used for textual data, which is perfect for identifiers like this.

---

## Task 3: Creating a List Variable

The next step was to manage the authorized usernames. I created a variable named `username_list` and assigned it a list containing the approved users.

**Code & Output:**

``python
# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]

# Display `username_list`
print(username_list)
```

**Output:** `['madebowa', 'jnguyen', 'tbecker', 'nhersh', 'redwards']`

**Observation:** The output shows that the data is neatly contained in brackets, indicating a collection.

---

## Task 4: Checking Data Types (List)

I verified the data type of username_list to ensure it was structured correctly for a collection of multiple values.

**Code & Output:**

```python
# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]

# Assign `username_list_type` to the data type of `username_list`
username_list_type = type(username_list)

# Display `username_list_type`
print(username_list_type)
```

**Output:** `<class 'list'>`

**Key Insight:** The data type is list, which is the appropriate Python structure for storing and iterating over multiple usernames.

---

## Task 5: Reassigning a Variable

The organization updated the allow list to include a new employee, `"lpoe"`. I demonstrated the flexibility of variables by reassigning `username_list` to the updated list and printing the change.

**Code & Output:**

```python
# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]

# Display `username_list`
print("Original:", username_list)

# Assign `username_list` to the updated list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards", "lpoe"]

# Display `username_list`
print("Updated:", username_list)
```

**Output:**
```text
Original: ['madebowa', 'jnguyen', 'tbecker', 'nhersh', 'redwards']
Updated: ['madebowa', 'jnguyen', 'tbecker', 'nhersh', 'redwards', 'lpoe']
```

**Key Insight:** Variables in Python are dynamic. Reassigning `sername_list` to a new list overwrites the previous data, allowing for easy updates as organizational needs change.

---

## Task 6: Assigning an Integer Variable

I created a variable named `max_logins` to store the maximum number of login attempts allowed, which is `3`.

**Code & Output:**

```python
# Assign `max_logins` to the value 3
max_logins = 3

# Assign `max_logins_type` to the data type of `max_logins`
max_logins_type = type(max_logins)

# Display `max_logins_type`
print(max_logins_type)
```

**Output:** `<class 'int'>`

**Key Insight:** The `int` (integer) data type is used for numeric values that don’t require decimal places. This is ideal for counting limits like login attempts.

---

## Task 7: Tracking Current Attempts with Integers

I stored the current number of login attempts made by a user, `2`, in the variable `login_attempts`.

**Code & Output:**

```python
# Assign `login_attempts` to the value 2
login_attempts = 2

# Assign `login_attempts_type` to the data type of `login_attempts`
login_attempts_type = type(login_attempts)

# Display `login_attempts_type`
print(login_attempts_type)
```

**Output:** `<class 'int'>`

**Key Insight:** Like `max_logins`, `login_attempts` is an integer. Tracking these counts numerically allows for easy mathematical comparisons later.

---

## Task 8: Boolean Comparison (Under the Limit)

I evaluated whether the current attempts (2) are within the allowable limit (3). This produces a Boolean (`True` or `False`) result.

**Code & Output:**

```python
# Assign `max_logins` to the value 3
max_logins = 3

# Assign `login_attempts` to the value 2
login_attempts = 2

# Determine whether the current number of login attempts is less than or equal to the maximum
print(login_attempts <= max_logins)
```

**Output:** `True`

**Observation:** The result is `True`, meaning the user is still permitted to try logging in because they haven't exceeded the limit.

---

## Task 9: Boolean Comparison (Exceeding the Limit)

To test the logic, I changed login_attempts to 5, exceeding the limit.

Code & Output:

```python
# Assign `max_logins` to the value 3
max_logins = 3

# Assign `login_attempts` to a specific value
login_attempts = 5

# Determine whether the current number of login attempts is less than or equal to the maximum
print(login_attempts <= max_logins)
```

**Output:** `False`

**Key Insight:** The output is `False`, signaling that the user has surpassed the maximum allowed attempts. This demonstrates how comparison operators create Boolean flags, which are essential for conditional logic (e.g., locking out a user).

---

## Task 10: Assigning a Boolean Variable

Finally, I created a variable named `login_status` to represent whether a user is currently logged in. I initially set it to False.

**Code & Output:**

```python
# Assign `login_status` to the Boolean value `False`
login_status = False

# Assign `login_status_type` to the data type of `login_status`
login_status_type = type(login_status)

# Display `login_status_type`
print(login_status_type)
```

**Output:** `<class 'bool'>`

**Key Insight:** The `bool` (Boolean) data type is specifically designed for `True` or `False` states, making it perfect for tracking statuses like login session activity.

---

## Consolidated Key Takeaways

- **Strings (`str`)** are used for textual data such as `device_id`.
- **Lists (`list`)** are used for ordered collections, such as usernames on an allow list.
- **Integers (`int`)** are used for numerical counters, such as `max_logins` and `login_attempts`.
- **Booleans (`bool`)** are used for logical states, such as whether a comparison is `True` or `False`.
- **Variables are dynamic** and can be easily reassigned to new values, which is crucial for handling updated security data.
- **Comparison operators (`<=`)** return Boolean values that enable decision-making in security scripts.

---

## Conclusion

This lab provided a hands-on introduction to the fundamental Python data types and variable operations that form the backbone of security automation. By the end of the exercises, I had successfully:

- Assigned and displayed variables for strings, lists, integers, and Booleans.
- Checked and confirmed data types to ensure correct usage.
- Reassigned variables to reflect updated security requirements.
- Used Boolean comparisons to implement login attempt logic.

These skills are directly transferable to real-world security tasks, such as writing Python scripts that check if a user is on an allow list, monitoring login attempts, and responding to suspicious activity.

---

## Reflection

This lab reinforced the critical importance of understanding data types in Python. In a security context, mismanaging data types—such as treating a list as a string—could break critical automation scripts. The ability to identify and manipulate these types efficiently is a foundational step toward building robust, error-free security tools.

I found the Boolean logic particularly insightful, as it directly mirrors the decision-making processes used in incident response and access control. Mastering these basics prepares me for more advanced concepts, such as loops and conditionals, which will be essential for automating threat detection and response tasks.
# Python Conditional Statements Lab: Access Control & System Updates

**Date:** September 1, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I am responsible for two key automation tasks:

1. **Checking OS Update Status:** Determining whether a user's operating system requires an update.
2. **Investigating Login Attempts:** Verifying whether login attempts were made by approved users during organization hours.

Throughout this lab, I used conditional statements (`if`, `elif`, `else`) and logical operators (`and`, `or`, `in`) to automate these decision-making processes.

---

## Task 1: Basic `if` Statement

I created a variable `system` representing the operating system and used an `if` statement to check if it was `"OS 2"` (the up‑to‑date version).

**Code:**

```python
# Assign a variable named `system` to a specific operating system
system = "OS 2"

# If OS 2 is running, then display a "no update needed" message
if system == "OS 2":
    print("no update needed")
```

**Output:**

```text
no update needed
```

**Observation:** The `if` statement executed the `print()` function only when the condition was `True`.

---

## Task 2: Testing Different Values

I reassigned `system` to `"OS 1"` and `"OS 3"` and observed that nothing was displayed.

**Code:**

```python
# Assign `system` to a specific operating system
system = "OS 1"

# If OS 2 is running, then display a "no update needed" message
if system == "OS 2":
    print("no update needed")
```

**Output:**

```text
(No output)
```

**Observation:** The condition `system == "OS 2"` only evaluates to `True` for `"OS 2"`. For any other value, the condition is `False`, so no message is printed.

---

## Task 3: Adding an `else` Clause

I added an `else` clause to provide a message when updates are needed.

**Code:**

```python
# Assign `system` to a specific operating system
system = "OS 1"

# If OS 2 is running, then display a "no update needed" message
# Otherwise, display a "update needed" message
if system == "OS 2":
    print("no update needed")
else:
    print("update needed")
```

**Output:**

```text
update needed
```

**Observation:** The `else` clause catches all cases where the `if` condition is `False`, providing a fallback message.

---

## Task 4: Using `elif` for Multiple Conditions

I added `elif` statements to handle `"OS 1"` and `"OS 3"` separately.

**Code:**

```python
# Assign `system` to a specific operating system
system = "OS 1"

# If OS 2 is running, then display a "no update needed" message
# Otherwise if OS 1 is running, display a "update needed" message
# Otherwise if OS 3 is running, display a "update needed" message
if system == "OS 2":
    print("no update needed")
elif system == "OS 1":
    print("update needed")
elif system == "OS 3":
    print("update needed")
```

**Output:**

```text
update needed
```

**Observation:** 
- `"OS 2"` → `"no update needed"`
- `"OS 1"` → `"update needed"`
- `"OS 3"` → `"update needed"`
- `"OS 4"` → No output (the `elif` conditions were all `False`)

---

## Task 5: Combining Conditions with `or`

I used the `or` operator to combine the two update‑needed conditions into a single `elif`.

**Code:**

```python
# Assign `system` to a specific operating system
system = "OS 3"

# If OS 2 is running, then display a "no update needed" message
# Otherwise if either OS 1 or OS 3 is running, display a "update needed" message
if system == "OS 2":
    print("no update needed")
elif system == "OS 1" or system == "OS 3":
    print("update needed")
```

**Output:**

```text
update needed
```

**Observation:** This makes the code more concise and readable. The `or` operator allows multiple conditions to be evaluated in one line.

---

## Task 6: Checking Against Individual Approved Users

I stored two approved usernames in variables and compared them to a `username` variable.

**Code:**

```python
# Assign `approved_user1` and `approved_user2` to usernames of approved users
approved_user1 = "elarson"
approved_user2 = "bmoreno"

# Assign `username` to the username of a specific user trying to log in
username = "bmoreno"

# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device
if username == approved_user1 or username == approved_user2:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")
```

**Output:**

```text
This user has access to this device.
```

**Observation:** The `or` operator checks multiple conditions. If either is `True`, the `if` block executes.

---

## Task 7: Using the `in` Operator with a List

I expanded the approved users into a list and used the `in` operator to check membership.

**Code:**

```python
# Assign `approved_list` to a list of approved usernames
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in
username = "bmoreno"

# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device
if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")
```

**Output:**

```text
This user has access to this device.
```

**Observation:** The `in` operator simplifies membership checking and makes the code more scalable as the list grows.

---

## Task 8: Boolean Condition for Organization Hours

I introduced a Boolean variable `organization_hours` to track whether the login attempt occurred during business hours.

**Code:**

```python
# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours
organization_hours = True

# If the entered `organization_hours` has a value of `True`, then display "Login attempt made during organization hours."
# Otherwise, display "Login attempt made outside of organization hours."
if organization_hours == True:
    print("Login attempt made during organization hours.")
else:
    print("Login attempt made outside of organization hours.")
```

**Output:**

```text
Login attempt made during organization hours.
```

**Observation:** Booleans are ideal for representing binary states like "during hours / outside hours."

---

## Task 9: Combining Both Conditions

I combined the allow‑list check and the organization‑hours check into a single script.

**Code:**

```python
# Assign `approved_list` to a list of approved usernames
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in
username = "bmoreno"

# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours
organization_hours = True

# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device
if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")

# If the entered `organization_hours` has a value of True, then display "Login attempt made during organization hours."
# Otherwise, display "Login attempt made outside of organization hours."
if organization_hours == True:
    print("Login attempt made during organization hours.")
else:
    print("Login attempt made outside of organization hours.")
```

**Output:**

```text
This user has access to this device.
Login attempt made during organization hours.
```

**Observation:** The two conditions are evaluated independently, providing separate messages for access status and timing.

---

## Task 10: Single Combined Condition

I used the `and` operator to combine both conditions into a single `if` statement.

**Code:**

```python
# Assign `approved_list` to a list of approved usernames
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in
username = "bmoreno"

# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours
organization_hours = True

# If the user is among the approved users and they are logging in during organization hours, then convey that the user is logged
# Otherwise, convey that either the username is not approved or the login attempt was made outside of organization hours
if username in approved_list and organization_hours:
    print("Login attempt made by an approved user during organization hours.")
else:
    print("Username not approved or login attempt made outside of organization hours.")
```

**Output:**

```text
Login attempt made by an approved user during organization hours.
```

**Observation:** The `and` operator ensures that **both** conditions must be `True` for the success message to display. This makes the code more concise and directly reflects the business rule: "Only approved users logging in during organization hours are fully authorized."

---

## Consolidated Key Takeaways

- **`if`, `elif`, `else`** structures allow for multiple decision paths.
- **`and` and `or`** operators enable complex logical conditions.
- **The `in` operator** simplifies membership checking in lists.
- **Booleans (`True`/`False`)** are ideal for representing binary states.
- **Concise code** improves readability and maintainability.
- **Conditional statements** are fundamental to automating security workflows such as access control and system updates.

---

## Conclusion

This lab provided hands‑on practice with Python conditional statements in a security context. By the end of the exercises, I had successfully:

- Used `if`, `elif`, and `else` to handle multiple conditions.
- Applied `and`, `or`, and `in` to build complex logical checks.
- Combined access control with timing conditions to simulate real‑world security logic.
- Tested different scenarios to observe how conditional statements behave.

These skills are directly applicable to automating security tasks such as allow‑list management, login monitoring, and system update checks.

---

## Reflection

This lab reinforced the importance of conditional logic in security automation. Being able to evaluate multiple conditions—such as "is this user approved?" and "is this during organization hours?"—is essential for building robust access control systems. The ability to combine conditions using logical operators not only makes the code more efficient but also more readable, which is critical when collaborating with other analysts.

I found the transition from individual variables to lists (`in` operator) particularly insightful. In a real security environment, the number of authorized users can grow rapidly, and relying on lists with `in` is far more scalable than comparing to multiple variables.

Mastering conditional statements is a foundational step toward building more advanced security tools, such as automated incident response scripts and policy enforcement systems.

---

> *This lab was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*
# Python Loops Lab: Automating Repetitive Security Tasks

**Date:** September 1, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I am responsible for automating repetitive processes to improve efficiency. In this lab, I wrote Python programs to:

- Display network connection messages multiple times.
- Detect IP addresses attempting to access restricted data.
- Generate unique employee ID numbers for a Sales department.

Throughout this lab, I used `for` loops, `while` loops, and loop control statements (`break`) to automate these tasks.

---

## Task 1: Basic `for` Loop with `range()`

I created a `for` loop that displays the message `"Connection could not be established."` three times using the `range()` function.

**Code:**

```python
# Iterative statement using `for`, `range()`, and a loop variable of `i`
# Display "Connection could not be established." three times

for i in range(3):
    print("Connection could not be established.")
```

**Output:**

```text
Connection could not be established.
Connection could not be established.
Connection could not be established.
```

**Observation:** The `range(3)` function generates a sequence of numbers from `0` to `2` (three iterations). The loop variable `i` takes each value in sequence, and the `print()` statement executes during each iteration.

---

## Task 2: Using a Variable in `range()`

I assigned the number of connection attempts to a variable called `connection_attempts` and passed it into the `range()` function.

**Code:**

```python
# Create a variable called `connection_attempts` that stores the number of times the user has tried to connect to the network
connection_attempts = 5

# Iterative statement using `for`, `range()`, a loop variable of `i`, and `connection_attempts`
# Display "Connection could not be established." as many times as specified by `connection_attempts`

for i in range(connection_attempts):
    print("Connection could not be established.")
```

**Output:**

```text
Connection could not be established.
Connection could not be established.
Connection could not be established.
Connection could not be established.
Connection could not be established.
```

**Observation:** Using a variable in `range()` makes the loop dynamic. By changing the value of `connection_attempts`, the loop automatically adjusts the number of iterations without modifying the loop structure.

---

## Task 3: `while` Loop Comparison

I rewrote the same logic using a `while` loop to understand the difference between the two loop types.

**Code:**

```python
# Assign `connection_attempts` to an initial value of 0, to keep track of how many times the user has tried to connect to the network
connection_attempts = 0

# Iterative statement using `while` and `connection_attempts`
# Display "Connection could not be established." every iteration, until connection_attempts reaches a specified number

while connection_attempts < 3:
    print("Connection could not be established.")
    # Update `connection_attempts` (increment it by 1 at the end of each iteration)
    connection_attempts = connection_attempts + 1
```

**Output:**

```text
Connection could not be established.
Connection could not be established.
Connection could not be established.
```

**Observation:** The `while` loop continues to execute as long as the condition `connection_attempts < 3` remains `True`. Unlike a `for` loop, which iterates a predetermined number of times, a `while` loop is driven by a condition and is useful when the number of iterations is unknown.

---

## Task 4: Iterating Over a List

I used a `for` loop to display each IP address from a list of login attempts.

**Code:**

```python
# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147", "192.168.205.12", "192.168.200.48"]

# For Loop that displays the elements of `ip_addresses` one at a time
for i in ip_addresses:
    print(i)
```

**Output:**

```text
192.168.142.245
192.168.109.50
192.168.86.232
192.168.131.147
192.168.205.12
192.168.200.48
```

**Observation:** The `for` loop iterates over each element in the `ip_addresses` list, assigning the current IP address to the loop variable `i` and executing the `print()` statement for each.

---

## Task 5: Checking Membership with `in`

I added an `if` statement inside the loop to check whether each IP address is on an `allow_list`.

**Code:**

```python
# Assign `allow_list` to a list of IP addresses that are allowed to log in
allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71",
    "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
    "192.168.205.12", "192.168.200.48"]

# For each IP address in the list of IP addresses from which users have tried to log in,
# If it is among the allowed addresses, then display "IP address is allowed"
# Otherwise, display "IP address is not allowed"

for i in ip_addresses:
    if i in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed")
```

**Output:**

```text
IP address is not allowed
IP address is not allowed
IP address is allowed
IP address is not allowed
IP address is allowed
IP address is not allowed
```

**Observation:** The `in` operator checks whether the current IP address exists in `allow_list`. This is a practical application of membership testing in security workflows.

---

## Task 6: Using `break` for Early Termination

I added a `break` statement to terminate the loop when an unapproved IP address is encountered, simulating an investigation trigger.

**Code:**

```python
# Assign `allow_list` to a list of IP addresses that are allowed to log in
allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71",
    "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in
ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
    "192.168.205.12", "192.168.200.48"]

# For each IP address in the list of IP addresses from which users have tried to log in,
# If it is among the allowed addresses, then display "IP address is allowed"
# Otherwise, display a more specific message and break out of the loop

for i in ip_addresses:
    if i in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed. Further investigation of login activity required")
        break
```

**Output:**

```text
IP address is not allowed. Further investigation of login activity required
```

**Observation:** The `break` statement immediately terminates the loop when the first unapproved IP address is encountered. This is useful when the security policy requires immediate action upon detecting unauthorized access attempts.

---

## Task 7: Generating Employee IDs with a `while` Loop

I used a `while` loop to generate employee IDs that are divisible by 5 and range from 5000 to 5150 (inclusive).

**Code:**

```python
# Assign the loop variable `i` to an initial value of 5000
i = 5000

# While Loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created

while i <= 5150:
    print(i)
    i = i + 5
```

**Output:**

```text
5000
5005
5010
5015
5020
5025
5030
5035
5040
5045
5050
5055
5060
5065
5070
5075
5080
5085
5090
5095
5100
5105
5110
5115
5120
5125
5130
5135
5140
5145
5150
```

**Observation:** The `while` loop starts at 5000 and increments by 5 until the condition `i <= 5150` is no longer `True`. This ensures all IDs are divisible by 5 and within the specified range.

---

## Task 8: Adding a Conditional Alert

I added an `if` statement inside the loop to display a warning when the loop reaches 5100, indicating that only 10 valid IDs remain.

**Code:**

```python
# Assign the loop variable `i` to an initial value of `5000`
i = 5000

# While Loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created
# This Loop displays "Only 10 valid employee ids remaining" once `i` reaches 5100

while i <= 5150:
    print(i)
    if i == 5100:
        print("Only 10 valid employee ids remaining")
    i = i + 5
```

**Output:**

```text
5000
5005
5010
5015
5020
5025
5030
5035
5040
5045
5050
5055
5060
5065
5070
5075
5080
5085
5090
5095
5100
Only 10 valid employee ids remaining
5105
5110
5115
5120
5125
5130
5135
5140
5145
5150
```

**Observation:** The `print(i)` statement is placed **before** the `if` statement, ensuring that the ID is displayed before the alert. If `print(i)` were inside the conditional, only the alert would be displayed without the ID.

---

## Consolidated Key Takeaways

- **`for` loops** with `range()` are ideal when you know the number of iterations in advance.
- **`while` loops** are better suited when you need to loop until a condition is met.
- **Loop variables** can be used to store and display values from lists or sequences.
- **The `in` operator** is useful for membership checking in lists.
- **The `break` statement** allows early termination of a loop, which is useful for security investigations.
- **Loops combined with conditionals** enable complex automation logic.
- **Incrementing loop variables** in `while` loops requires explicit updates to avoid infinite loops.

---

## Conclusion

This lab provided hands‑on practice with Python loops in a security context. By the end of the exercises, I had successfully:

- Used `for` loops with `range()` for repeated actions.
- Used `while` loops for condition‑driven repetition.
- Iterated over lists of IP addresses and checked membership.
- Used `break` to terminate loops when unauthorized activity is detected.
- Generated employee IDs using a `while` loop with a conditional alert.

These skills are directly applicable to automating security tasks such as monitoring network connections, analyzing login attempts, and generating identifiers.

---

## Reflection

This lab reinforced the importance of loops in security automation. Being able to iterate over lists of IP addresses and check them against an allow list is a foundational task for any SOC analyst. The `break` statement added an important layer of control, allowing the script to stop processing when a critical condition is met.

The `while` loop employee ID generation task was a good reminder that loops are not just for list processing—they are also useful for generating sequences that follow specific rules. The conditional alert inside the loop demonstrated how to provide real‑time feedback during automation.

Mastering loops is essential for building more advanced security tools, such as scripts that process logs, analyze network traffic, and respond to incidents.

---

> *This lab was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*
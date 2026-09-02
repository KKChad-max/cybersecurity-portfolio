# Python Functions Lab 2: Built-in Functions, Parameters, and Return Statements

**Date:** September 2, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I am responsible for analyzing login attempt data to identify patterns that might indicate malicious activity. In this lab, I:

- Used built-in functions (`sorted()`, `max()`) to analyze a list of failed login attempts per month.
- Defined a user-defined function (`analyze_logins()`) with parameters to compare a user's current login attempts to their average.
- Added a `return` statement to the function so the output could be reused.
- Used the returned value in a conditional statement to trigger an alert.

---

## Task 1: Sorting a List with `sorted()`

I was provided with a list of failed login attempts per month:

```text
[119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]
```

I used the built-in `sorted()` function to sort the list in ascending order and display the result.

**Code:**

```python
# Assign `failed_login_list` to the list of the number of failed login attempts per month
failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]

# Sort `failed_login_list` in ascending numerical order and display the result
print(sorted(failed_login_list))
```

**Output:**

```text
[85, 88, 90, 91, 92, 99, 101, 105, 108, 119, 223, 264]
```

**Observation:** The `sorted()` function returns a new sorted list without modifying the original. The sorted list reveals two outlying numbers: `223` and `264`, which are significantly higher than the rest (which range from 85 to 119). These outliers indicate a potential increase in failed login attempts in November and December.

---

## Task 2: Finding the Maximum Value with `max()`

I used the built-in `max()` function to identify the highest number of failed login attempts.

**Code:**

```python
# Assign `failed_login_list` to the list of the number of failed login attempts per month
failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]

# Determine the highest number of failed login attempts from `failed_login_list` and display the result
print(max(failed_login_list))
```

**Output:**

```text
264
```

**Observation:** The `max()` function returns `264`, which is the highest value in the list. This indicates that the month of December (the 12th month) had the most failed login attempts and requires further investigation.

---

## Task 3: Defining a Function with Parameters

I defined a function named `analyze_logins()` that takes two parameters: `username` and `current_day_logins`. The function displays a message about the user's current login attempts.

**Code:**

```python
# Define a function named `analyze_logins()` that takes in two parameters, `username` and `current_day_logins`
def analyze_logins(username, current_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
```

**Observation:** The function is defined but not called, so running this cell produces no output. The `def` keyword is used to define the function, followed by the function name and parameters in parentheses.

---

## Task 4: Calling a Function with Arguments

I called the `analyze_logins()` function with the arguments `"Chad"` and `9`.

**Code:**

```python
# Define a function named `analyze_logins()` that takes in two parameters, `username` and `current_day_logins`
def analyze_logins(username, current_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)

# Call `analyze_logins()`
analyze_logins("Chad", 9)
```

**Output:**

```text
Current day login total for Chad is 9
```

**Observation:** The function executes and displays the message. The output would vary for different users because the arguments passed to the function determine what is displayed.

---

## Task 5: Adding a Third Parameter

I expanded the function to include a third parameter, `average_day_logins`, and added a message displaying the average login attempts.

**Code:**

```python
# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)

# Call `analyze_logins()`
analyze_logins("Chad", 9, 3)
```

**Output:**

```text
Current day login total for Chad is 9
Average logins per day for Chad is 3
```

**Observation:** The function now displays both the current day's login total and the average login total for the user. Adding parameters increases the flexibility of the function.

---

## Task 6: Calculating a Ratio Inside the Function

I added a calculation to determine the ratio of the current day's logins to the average day's logins and displayed the result.

**Code:**

```python
# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)
    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
    login_ratio = current_day_logins / average_day_logins
    # Display a message about the ratio
    print(username, "logged in", login_ratio, "times as much as they do on an average day.")

# Call `analyze_logins()`
analyze_logins("Chad", 9, 3)
```

**Output:**

```text
Current day login total for Chad is 9
Average logins per day for Chad is 3
Chad logged in 3.0 times as much as they do on an average day.
```

**Observation:** The function calculates the ratio (`9 / 3 = 3.0`) and displays it. The output would vary for different users based on their login totals. For example, if `current_day_logins` were `15` and `average_day_logins` were `3`, the ratio would be `5.0`.

---

## Task 7: Using `return` to Output a Value

I added a `return` statement to the `analyze_logins()` function so the ratio could be stored in a variable and used later. I called the function, stored the result in `login_analysis`, and displayed it.

**Code:**

```python
# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)
    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
    login_ratio = current_day_logins / average_day_logins
    # Return the ratio
    return login_ratio

# Call `analyze_logins()` and store the output in a variable named `login_analysis`
login_analysis = analyze_logins("Chad", 9, 3)

# Display a message about the `login_analysis`
print("Chad", "logged in", login_analysis, "times as much as they do on an average day.")
```

**Output:**

```text
Current day login total for Chad is 9
Average logins per day for Chad is 3
Chad logged in 3.0 times as much as they do on an average day.
```

**Observation:** The `return` statement allows the function to send the `login_ratio` value back to the call, storing it in `login_analysis`. This value can then be used elsewhere in the code, such as in conditional statements. Unlike previous versions, the final line of output now originates from the `print()` statement outside the function.

---

## Task 8: Using the Returned Value in a Conditional Statement

I used the `login_analysis` value in a conditional statement to trigger an alert if the ratio is greater than or equal to `3`.

**Code:**

```python
# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):
    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)
    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)
    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
    login_ratio = current_day_logins / average_day_logins
    # Return the ratio
    return login_ratio

# Call `analyze_logins()` and store the output in a variable named `login_analysis`
login_analysis = analyze_logins("Chad", 9, 3)

# Conditional statement that displays an alert about the login activity if it's more than normal
if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")
```

**Output:**

```text
Current day login total for Chad is 9
Average logins per day for Chad is 3
Alert! This account has more login activity than normal.
```

**Observation:** The conditional statement checks whether `login_analysis` is greater than or equal to `3`. Since the ratio is `3.0`, the condition evaluates to `True`, and the alert message is displayed. This is a practical application of using a function's return value to trigger an action in a security context.

---

## Consolidated Key Takeaways

- **Built-in functions** like `sorted()` and `max()` can be used to analyze lists of security data efficiently.
- **User-defined functions** allow for reusable, organized code.
- **Parameters** make functions more flexible by allowing them to accept different inputs.
- **`return` statements** allow functions to output data that can be stored and reused.
- **Returned values can be used in conditional statements** to automate decision-making, such as triggering alerts.

---

## Conclusion

This lab provided hands‑on practice with built-in functions (`sorted()`, `max()`), user-defined functions, parameters, `return` statements, and conditional logic. By the end of the exercises, I had successfully:

- Used `sorted()` and `max()` to analyze a list of failed login attempts.
- Defined and called a function with multiple parameters.
- Added a calculation inside the function to determine a login ratio.
- Used `return` to output the ratio from the function.
- Stored the returned value and used it in a conditional statement to trigger an alert.

### Bridging the Gap to Real‑World Security Automation

While this lab used a simple list of numbers and static `print()` statements, it directly maps to the **`log_analyzer.py`** script I built earlier in my portfolio. 

Here is how the concepts scale:

| Lab Concept (This Activity) | `log_analyzer.py` Implementation |
| :--- | :--- |
| **Analyzing a List** | Analyzing lines in a live `auth.log` file. |
| **Using `max()` to find outliers** | Using `re` (regex) to extract IPs and `defaultdict` to count them. |
| **Conditional `if` statement (ratio >= 3)** | **Threshold alerting** (`if count >= THRESHOLD: print("🚨 ALERT")`). |
| **Function with `return`** | Using the `analyze_log()` function to encapsulate the entire parsing logic and return results to the caller. |

The `log_analyzer.py` script takes the **same logic** (counting events, comparing against a threshold) and applies it to parsing raw log files on a system. This lab taught me the **building blocks**; `log_analyzer.py` proves I can apply those blocks to solve a real SOC problem (detecting brute‑force attacks).

## Reflection

This lab reinforced the critical importance of functions and return values in security automation. The ability to pass parameters into functions makes code reusable, while `return` statements allow data to flow between different parts of a script.

The final task—triggering an alert based on a login ratio—directly mirrors the **alerting logic** used in real‑world Security Operations Centers (SOCs). This same logic powers my `log_analyzer.py` script, where I set thresholds to flag suspicious IP addresses.

By understanding how to move from static list analysis (this lab) to parsing dynamic log files (`log_analyzer.py`), I am building the foundation needed to write robust, production-grade security tools that can monitor, analyze, and respond to live threats.

---

> *This lab was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*
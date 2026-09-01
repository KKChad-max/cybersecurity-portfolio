# Python Functions Lab: Defining and Calling Functions

**Date:** September 1, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I often need to reuse the same block of code multiple times. Functions allow me to encapsulate logic and call it whenever needed. In this lab, I defined and called functions to:

- Display an alert about a potential security issue.
- Convert a list of employee usernames into a single string.

Throughout this lab, I practiced defining functions with `def`, using `for` loops inside functions, and applying string concatenation.

---

## Task 1: Analyzing a Function Definition

I analyzed a user-defined function named `alert()` that displays a security alert message.

**Code:**

```python
# Define a function named `alert()`
def alert():
    print("Potential security issue. Investigate further.")
```

**Observation:** The function definition begins with the `def` keyword, followed by the function name `alert`, parentheses `()`, and a colon `:`. The body of the function is indented and contains a single `print()` statement. At this stage, the function is defined but not executed.

---

## Task 2: Calling a Function

I called the `alert()` function to execute its code and observe the output.

**Code:**

```python
# Define a function named `alert()`
def alert():
    print("Potential security issue. Investigate further.")

# Call the `alert()` function
alert()
```

**Output:**

```text
Potential security issue. Investigate further.
```

**Observation:** Calling the function by writing `alert()` executes the code inside the function body. The `print()` statement runs, and the message is displayed.

---

## Task 3: Functions with Loops

I modified the `alert()` function to include a `for` loop, displaying the message three times.

**Code:**

```python
# Define a function named 'alert()'
def alert():
    for i in range(3):
        print("Potential security issue. Investigate further.")

# Call the 'alert()' function
alert()
```

**Output:**

```text
Potential security issue. Investigate further.
Potential security issue. Investigate further.
Potential security issue. Investigate further.
```

**Observation:** The output now displays the message three times instead of once. The function body can contain any Python code, including loops, conditionals, and other functions.

---

## Task 4: Defining a Function Header

I started defining a function named `list_to_string()` by writing the function header.

**Code:**

```python
# Define a function named `list_to_string()`
def list_to_string():
```

**Observation:** The function header sets up the structure for the function. The body will be added in subsequent tasks.

---

## Task 5: Iterating Through a List Inside a Function

I completed the body of `list_to_string()` to iterate through a list of usernames and display each element.

**Code:**

```python
# Define a function named `list_to_string()`
def list_to_string():
    # Store the list of approved usernames in a variable named `username_list`
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

    # Write a for loop that iterates through the elements of `username_list` and displays each element
    for i in username_list:
        print(i)

# Call the `list_to_string()` function
list_to_string()
```

**Output:**

```text
elarson
bmoreno
tshah
sgilmore
eraab
gesparza
alevitsk
wjaffrey
```

**Observation:** The function iterates through the list and displays each username on a separate line.

---

## Task 6: String Concatenation Inside a Function

I modified the function to concatenate all usernames into a single string using the `+` operator.

**Code:**

```python
# Define a function named `list_to_string()`
def list_to_string():
    # Store the list of approved usernames in a variable named `username_list`
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

    # Assign `sum_variable` to an empty string
    sum_variable = ""

    # Write a for loop that iterates through the elements of `username_list` and displays each element
    for i in username_list:
        sum_variable += i

    # Display the value of `sum_variable`
    print(sum_variable)

# Call the `list_to_string()` function
list_to_string()
```

**Output:**

```text
elarsonbmorenotshahsgilmoreeraabgesparzaalevitskwjaffrey
```

**Observation:** The usernames are concatenated into a single string, but they run together without any separators, making it difficult to read.

---

## Task 7: Improving Readability with Separators

I added a comma and a space (", ") after each username to improve readability.

**Code:**

```python
# Define a function named `list_to_string()`
def list_to_string():
    # Store the list of approved usernames in a variable named `username_list`
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

    # Assign `sum_variable` to an empty string
    sum_variable = ""

    # Write a for loop that iterates through the elements of `username_list` and displays each element
    for i in username_list:
        sum_variable += i + ", "

    # Display the value of `sum_variable`
    print(sum_variable)

# Call the `list_to_string()` function
list_to_string()
```

**Output:**

```text
elarson, bmoreno, tshah, sgilmore, eraab, gesparza, alevitsk, wjaffrey, 
```

**Observation:** The usernames are now separated by commas and spaces, making the output much easier to read. This format is useful for generating readable lists, such as for reports or logs.

---

## Consolidated Key Takeaways

- **Functions are defined using the `def` keyword**, followed by the function name, parentheses, and a colon.
- **Calling a function** executes its body.
- **Functions can contain any Python code**, including loops, conditionals, and other functions.
- **String concatenation (`+`)** combines multiple strings into one.
- **Adding separators** improves readability when concatenating list elements.
- **Functions promote code reuse**, making scripts more efficient and maintainable.

---

## Conclusion

This lab provided hands‑on practice with defining and calling functions in Python. By the end of the exercises, I had successfully:

- Defined a simple `alert()` function.
- Called the function to execute its code.
- Modified the function to include a `for` loop.
- Defined a `list_to_string()` function to iterate through a list.
- Used string concatenation to combine list elements into a single string.
- Improved the output with separators for readability.

These skills are directly applicable to automating security tasks such as generating reports, formatting data, and creating reusable alert systems.

---

## Reflection

This lab reinforced the importance of functions in security automation. Functions allow me to write reusable, organized, and maintainable code. By encapsulating logic into functions, I can avoid repetition and make my scripts more efficient.

The `list_to_string()` function was particularly useful for converting lists into readable strings—a common task when preparing data for logs, reports, or notifications. The addition of separators demonstrates how small details can significantly improve the usability of output.

Mastering functions is a critical step toward building more advanced security tools, such as automated log analyzers, threat detection scripts, and incident response workflows.

---

> *This lab was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*
# Python Algorithm Lab: Developing an Algorithm

**Date:** September 2, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Introduction & Scenario

As a security analyst, I am responsible for developing an algorithm that connects users to their assigned devices. The algorithm checks:

1. Whether a user is approved to access the system.
2. Whether the device they have brought is the one assigned to them.

Throughout this lab, I used list operations (`append()`, `remove()`, `.index()`) and conditional statements to build a complete authentication function.

---

## Task 1: Exploring List Indices

I explored how indices in two synchronized lists correspond to each other. The `approved_users` list and `approved_devices` list are synchronized—the user at index `0` uses the device at index `0`.

**Code:**

```python
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

# Display the element at the specified index in `approved_users`
print(approved_users[0])

# Display the element at the specified index in `approved_devices`
print(approved_devices[0])
```

**Output:**

```text
elarson
8rp2k75
```

**Observation:** `approved_users[0]` returns the first username (`"elarson"`), and `approved_devices[0]` returns the corresponding device ID (`"8rp2k75"`). When I replace `0` with another index, the corresponding element from each list is displayed, demonstrating the synchronization.

---

## Task 2: Adding a New User with `.append()`

I added a new employee (`"gesparza"`) and their device ID (`"3rcv4w6"`) to the lists using the `.append()` method.

**Code:**

```python
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s501", "2ye3lzg", "4n482ts", "a30vvir"]

# Assign `new_user` to the username of a new approved user
new_user = "gesparza"

# Assign `new_device` to the device ID of the new approved user
new_device = "3rcv4w6"

# Add that user's username and device ID to `approved_users` and `approved_devices` respectively
approved_users.append(new_user)
approved_devices.append(new_device)

# Display the contents of `approved_users`
print(approved_users)

# Display the contents of `approved_devices`
print(approved_devices)
```

**Output:**

```text
['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab', 'gesparza']
['8rp2k75', 'hl0s501', '2ye3lzg', '4n482ts', 'a30vvir', '3rcv4w6']
```

**Observation:** The `.append()` method adds the new element to the end of each list. The new user `"gesparza"` and their device `"3rcv4w6"` are now at index `5` in both lists, maintaining synchronization.

---

## Task 3: Removing a User with `.remove()`

I removed an employee who left the team (`"tshah"`) and their device ID (`"2ye3lzg"`) using the `.remove()` method.

**Code:**

```python
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a3o7vir", "3rcv4w6"]

# Assign `removed_user` to the username of the employee who has left the team
removed_user = "tshah"

# Assign `removed_device` to the device ID of the employee who has left the team
removed_device = "2ye3lzg"

# Remove that employee's username and device ID from `approved_users` and `approved_devices` respectively
approved_users.remove(removed_user)
approved_devices.remove(removed_device)

# Display `approved_users`
print(approved_users)

# Display `approved_devices`
print(approved_devices)
```

**Output:**

```text
['elarson', 'bmoreno', 'sgilmore', 'eraab', 'gesparza']
['8rp2k75', 'hl0s5o1', '4n482ts', 'a3o7vir', '3rcv4w6']
```

**Observation:** The `.remove()` method removes the first occurrence of the specified value. Both lists remain synchronized because the user and device at the same position are removed.

---

## Task 4: Checking Membership with `in`

I wrote a conditional statement to check if a username is in the `approved_users` list.

**Code:**

```python
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s501", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Conditional statement
# If `username` belongs to `approved_users`, then display "The user ______ is approved to access the system."
# Otherwise display "The user ______ is not approved to access the system."
if username in approved_users:
    print("The username", username, "is approved to access the system.")
else:
    print("The username", username, "is not approved to access the system.")
```

**Output:**

```text
The username sgilmore is approved to access the system.
```

**Observation:** The `in` operator checks if `username` exists in `approved_users`. Since `"sgilmore"` is in the list, the `if` block executes.

---

## Task 5: Finding an Index with `.index()`

I used the `.index()` method to find the position of `username` in `approved_users` and stored it in a variable `ind`.

**Code:**

```python
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s501", "4n482ts", "a3o7vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# Display the value of `ind`
print(ind)
```

**Output:**

```text
2
```

**Observation:** The `.index()` method returns `2`, which is the position of `"sgilmore"` in the list. This index can now be used to retrieve the corresponding device ID.

---

## Task 6: Connecting Lists with Index

I used the `ind` variable to retrieve the corresponding device ID from `approved_devices`.

**Code:**

```python
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s501", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# Display the device ID at the index that matches the value of `ind` in `approved_devices`
print(approved_devices[ind])
```

**Output:**

```text
4n482ts
```

**Observation:** The device ID at index `2` in `approved_devices` is `"4n482ts"`. This demonstrates how to connect two synchronized lists using an index.

---

## Task 7: Verifying Username and Device ID

I wrote a conditional that checks if the username is approved **and** if the entered device ID matches the assigned device.

**Code:**

```python
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s501", "4n482ts", "a3o7vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Assign `device_id` to a device ID
device_id = "4n482ts"

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# Conditional statement
# If `username` belongs to `approved_users`, and if the device ID at `ind` in `approved_devices` matches `device_id`, then display a message that the username is approved,
# followed by a message that the user has the correct device
if username in approved_users and device_id == approved_devices[ind]:
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)
```

**Output:**

```text
The username sgilmore is approved to access the system.
4n482ts is the assigned device for sgilmore
```

**Observation:** Both conditions are `True`, so both messages are displayed. This is the core authentication logic: the user must be approved and have the correct device.

---

## Task 8: Adding an `elif` for Incorrect Device

I added an `elif` statement to handle the case where the username is approved but the device ID is incorrect.

**Code:**

```python
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s501", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Assign `device_id` to a device ID
device_id = "8rp2k75"  # Incorrect device for sgilmore

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# If statement
if username in approved_users and device_id == approved_devices[ind]:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

# elif statement
elif username in approved_users and device_id != approved_devices[ind]:
    print("The user", username, "is approved to access the system, but", device_id, "is not their assigned device.")
```

**Output:**

```text
The user sgilmore is approved to access the system, but 8rp2k75 is not their assigned device.
```

**Observation:** The `elif` condition handles the case where the username is approved but the device ID is incorrect. This provides a more informative message to the user.

---

## Task 9: Defining a Function

I encapsulated the authentication logic into a function named `login()` that takes `username` and `device_id` as parameters.

**Code:**

```python
# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s501", "4n482ts", "a307vir", "3rcv4w6"]

# Define a function named `login` that takes in two parameters, `username` and `device_id`
def login(username, device_id):
    # If `username` belongs to `approved_users`,
    if username in approved_users:
        # then display "The user ______ is approved to access the system."
        print("The user", username, "is approved to access the system.")
        # assign `ind` to the index of `username` in `approved_users`
        ind = approved_users.index(username)
        # if `device_id` matches the element at the index `ind` in `approved_devices`,
        if device_id == approved_devices[ind]:
            # then display "______ is the assigned device for ______"
            print(device_id, "is the assigned device for", username)
        else:
            # display "______ is not their assigned device"
            print(device_id, "is not their assigned device.")
    else:
        # Display "The user ______ is not approved to access the system."
        print("The username", username, "is not approved to access the system.")

# Call the function with different combinations
login("sgilmore", "4n482ts")   # Correct
login("sgilmore", "8rp2k75")   # Incorrect device
login("unknown", "4n482ts")    # Unapproved user
```

**Output:**

```text
The user sgilmore is approved to access the system.
4n482ts is the assigned device for sgilmore

The user sgilmore is approved to access the system.
8rp2k75 is not their assigned device.

The username unknown is not approved to access the system.
```

**Observation:** The function successfully handles all three cases:
1. Approved user with correct device.
2. Approved user with incorrect device.
3. Unapproved user.

This function can now be reused for any user/device combination.

---

## Consolidated Key Takeaways

- **Lists can be synchronized** by maintaining the same order and using the same index.
- **`.append()`** adds elements to the end of a list.
- **`.remove()`** removes the first occurrence of a specified value.
- **The `in` operator** checks membership in a list.
- **`.index()`** returns the position of a value in a list.
- **Synchronized lists** allow you to connect related data using an index.
- **Functions** encapsulate reusable logic.
- **Nested conditionals** handle complex decision‑making.

---

## Conclusion

This lab provided hands‑on practice with developing an algorithm for user authentication. By the end of the exercises, I had successfully:

- Explored how synchronized lists work.
- Added and removed users from the system.
- Used membership checks and index retrieval.
- Connected two lists using an index.
- Applied `and` operators for combined conditions.
- Added `elif` for alternative scenarios.
- Encapsulated the entire authentication logic into a reusable function.

These skills are directly applicable to automating security tasks such as verifying user credentials, managing allow lists, and controlling device access.

---

## Reflection

This lab reinforced the importance of algorithm development in security automation. The ability to connect two related lists—approved users and their assigned devices—is a fundamental pattern in access control systems.

The progression from simple list operations to a complete function demonstrated how to build modular, reusable code. In a real‑world SOC environment, this logic could be expanded to include additional factors, such as time‑of‑day restrictions, multi‑factor authentication, or device health checks.

Mastering algorithms like this is essential for building robust security tools that automate identity verification and access management.

---

> *This lab was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*
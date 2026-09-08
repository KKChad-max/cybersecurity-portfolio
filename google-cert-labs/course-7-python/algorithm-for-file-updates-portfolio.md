# Algorithm for File Updates in Python

**Date:** September 8, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 7  

---

## Project Description

In this project, I developed a Python algorithm to automate the updating of an allow list for a healthcare company. The allow list contains IP addresses permitted to access restricted patient records. I was provided with a remove list containing IP addresses that no longer have access. The algorithm reads the allow list file, converts its contents into a list, removes any IP addresses found in the remove list, and updates the file with the revised list. This automation ensures that only authorised employees retain access to sensitive patient data, improving security and operational efficiency.
---

## Open the File that Contains the Allow List

For the first part of the algorithm, I opened the `"allow_list.txt"` file. First, I assigned this file name as a string to the `import_file` variable:

```python
# Assign `import_file` to the name of the file
import_file = "allow_list.txt"
```

Then, I used a `with` statement to open the file:

```python
# Build `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:
```

In my algorithm, the `with` statement is used with the `.open()` function in read mode to open the allow list file for the purpose of reading it. The purpose of opening the file is to allow me to access the IP addresses stored in the allow list file. The `with` keyword will help manage the resources by closing the file after exiting the `with` statement. In the code `with open(import_file, "r") as file:`, the `open()` function has two parameters. The first identifies the file to import, and then the second indicates what I want to do with the file. In this case, `"r"` indicates that I want to read it. The code also uses the `as` keyword to assign a variable named `file`; `file` stores the output of the `.open()` function while I work within the `with` statement.

---

## Read the File Contents

In order to read the file contents, I used the `.read()` method to convert it into the string.

```python
with open(import_file, "r") as file:
    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    ip_addresses = file.read()
```

When using an `.open()` function that includes the argument `"r"` for "read," I can call the `.read()` function in the body of the `with` statement. The `.read()` method converts the file into a string and allows me to read it. I applied the `.read()` method to the `file` variable identified in the `with` statement. Then, I assigned the string output of this method to the variable `ip_addresses`.

In summary, this code reads the contents of the `"allow_list.txt"` file into a string format that allows me to later use the string to organize and extract data in my Python program.

---

## Convert the String into a List

In order to remove individual IP addresses from the allow list, I needed it to be in list format. Therefore, I next used the `.split()` method to convert the `ip_addresses` string into a list:

```python
# Use `.split()` to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()
```

The `.split()` function is called by appending it to a string variable. It works by converting the contents of a string to a list. The purpose of splitting `ip_addresses` into a list is to make it easier to remove IP addresses from the allow list. By default, the `.split()` function splits the text by whitespace into list elements. In this algorithm, the `.split()` function takes the data stored in the variable `ip_addresses`, which is a string of IP addresses that are each separated by a whitespace, and it converts this string into a list of IP addresses. To store this list, I reassigned it back to the variable `ip_addresses`.

---

## Iterate Through the Remove List

A key part of my algorithm involves iterating through the IP addresses that are elements in the `remove_list`. To do this, I incorporated a `for` loop:

```python
# Build iterative statement
# Name loop variable 'element'
# Loop through 'remove_list'
for element in remove_list:
```

The `for` loop in Python repeats code for a specified sequence. The overall purpose of the `for` loop in a Python algorithm like this is to apply specific code statements to all elements in a sequence. The `for` keyword starts the `for` loop. It is followed by the loop variable `element` and the keyword `in`. The keyword `in` indicates to iterate through the sequence `remove_list` and assign each value to the loop variable `element`.

---

## Remove IP Addresses that are on the Remove List

My algorithm requires removing any IP address from the allow list, `ip_addresses`, that is also contained in `remove_list`. Because there were not any duplicates in `ip_addresses`, I was able to use the following code to do this:

```python
for element in remove_list:
    # Create conditional statement to evaluate if 'element' is in 'ip_addresses'
    if element in ip_addresses:
        # Use the '.remove()' method to remove
        # elements from 'ip_addresses'
        ip_addresses.remove(element)
```

First, within my `for` loop, I created a conditional that evaluated whether or not the loop variable `element` was found in the `ip_addresses` list. I did this because applying `.remove()` to elements that were not found in `ip_addresses` would result in an error.

Then, within that conditional, I applied `.remove()` to `ip_addresses`. I passed in the loop variable `element` as the argument so that each IP address that was in the `remove_list` would be removed from `ip_addresses`.

---

## Update the File with the Revised List of IP Addresses

As a final step in my algorithm, I needed to update the allow list file with the revised list of IP addresses. To do so, I first needed to convert the list back into a string. I used the `.join()` method for this:

```python
# Convert `ip_addresses` back to a string so that it can be written into the text file
ip_addresses = "\n".join(ip_addresses)
```

The `.join()` method combines all items in an iterable into a string. The `.join()` method is applied to a string containing characters that will separate the elements in the iterable once joined into a string. In this algorithm, I used the `.join()` method to create a string from the list `ip_addresses` so that I could pass it in as an argument to the `.write()` method when writing to the file `"allow_list.txt"`. I used the string (`"\n"`) as the separator to instruct Python to place each element on a new line.

Then, I used another `with` statement and the `.write()` method to update the file:

```python
# Build `with` statement to rewrite the original file
with open(import_file, "w") as file:
    # Rewrite the file, replacing its contents with `ip_addresses`
    file.write(ip_addresses)
```

This time, I used a second argument of `"w"` with the `open()` function in my `with` statement. This argument indicates that I want to open a file to write over its contents. When using this argument `"w"`, I can call the `.write()` function in the body of the `with` statement. The `.write()` function writes string data to a specified file and replaces any existing file content.

In this case I wanted to write the updated allow list as a string to the file `"allow_list.txt"`. This way, the restricted content will no longer be accessible to any IP addresses that were removed from the allow list. To rewrite the file, I appended the `.write()` function to the file object `file` that I identified in the `with` statement. I passed in the `ip_addresses` variable as the argument to specify that the contents of the file specified in the `with` statement should be replaced with the data in this variable.

---

## Summary

This Python algorithm automates the process of updating an allow list file for a healthcare company. It begins by opening the file and reading its contents as a string. The string is then converted into a list using the `.split()` method. A `for` loop iterates through the remove list, and a conditional statement checks whether each IP address exists in the allow list. If so, the `.remove()` method removes it. Finally, the updated list is converted back into a string using the `"\n".join()` method and written to the file using the `.write()` method. This algorithm ensures that only authorised employees retain access to sensitive patient records, improving security and operational efficiency.

---


> *This activity was completed as part of the Google Cybersecurity Certificate – Course 7: Automate Cybersecurity Tasks with Python.*
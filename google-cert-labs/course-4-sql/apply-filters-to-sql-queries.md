# Apply Filters to SQL Queries

**Date:** August 21, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 4  

---

## Project Description

In this project, I used SQL queries with filters to investigate potential security issues at a large organization. I queried the `log_in_attempts` and `employees` tables to retrieve specific records related to failed login attempts, suspicious activity on certain dates, login attempts outside of Mexico, and employee machine updates for various departments. These queries help security teams quickly identify and respond to potential threats.

---

## Retrieve After Hours Failed Login Attempts

A potential security incident occurred after business hours. I needed to retrieve all failed login attempts that occurred after 18:00 (6:00 PM). I used the `AND` operator to combine two conditions: `login_time > '18:00'` and `success = 0` (where `0` indicates a failed attempt).

**SQL query:**

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00' AND success = 0;
```

**Output:**
This query returns all login attempts made after 6:00 PM that resulted in failure. It helps the security team investigate unauthorized access attempts during off-hours.

---

## Retrieve Login Attempts on Specific Dates

A suspicious event occurred on `2022-05-09`. I needed to review all login attempts on that day and the day before. I used the `OR` operator to filter for login attempts that occurred on either `2022-05-09` or `2022-05-08`.

**SQL query:**
```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';
```

**Output:**
This query returns all login attempts on the two specified dates. It provides a focused dataset for investigating the suspicious event.

---

Retrieve Login Attempts Outside of Mexico
The security team determined that suspicious login activity did not originate in Mexico. I needed to retrieve all login attempts that occurred outside of Mexico. Since the country column contains values like MEX and MEXICO, I used the NOT LIKE operator with the % wildcard to exclude both.

**SQL query:**
```sql
SELECT *
FROM log_in_attempts
WHERE country NOT LIKE 'MEX%';
```
**Output:**
This query returns all login attempts from countries other than Mexico, helping the team focus on potentially malicious traffic from other regions.

---

## Retrieve Employees in Marketing
The team needed to update machines for employees in the Marketing department who work in the East Building. I filtered the `employees` table for employees in the `Marketing` department whose office location starts with `East-` using the `LIKE` operator with `%`.

**SQL query:**
``sql
SELECT *
FROM employees
WHERE department = 'Marketing' AND office LIKE 'East-%';
```

**Output:**
This query returns all Marketing employees in East Building offices. It helps the team scope the security update to the correct group of machines.

---

## Retrieve Employees in Finance or Sales
A different security update was needed for employees in the Sales and Finance departments. I used the `OR` operator to retrieve employees from either department.

**SQL query:**
``sql
SELECT *
FROM employees
WHERE department = 'Sales' OR department = 'Finance';
```

**Output:**
This query returns all employees in the Sales and Finance departments, allowing the team to target the correct machines for the update.

---

## Retrieve All Employees Not in IT
The final update needed to be applied to all employees except those in the Information Technology department, since IT had already received the update. I used the `NOT` operator with the `=` operator to exclude the IT department.

**SQL query:**
``sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

**Output:**
This query returns all employees outside of the IT department. It ensures that the security update is applied to all remaining departments.

---

## Summary
By applying SQL filters with `AND`, `OR`, `NOT`, and `LIKE` operators, I successfully retrieved specific datasets to support security investigations and machine updates. I identified after-hours failed login attempts, isolated login activity on specific dates, filtered out Mexico-origin attempts, and targeted employees by department and office location. These queries demonstrate how SQL can be used to efficiently analyze security data and support incident response workflows.
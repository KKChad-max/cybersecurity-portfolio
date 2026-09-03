# Database Assignment: Garden Centre Database

**Module:** Databases  
**Institution:** ZCAS University  
**Programme:** NCC Level 4 Diploma in Computing  
**Year:** 2025  

---

## Overview

This assignment involved the design and implementation of a relational database for a garden centre. The database supports product inventory, employee management, customer records, sales tracking, and event management. The project included an ER diagram, data dictionary, SQL table creation, sample data population, role-based access control, and complex queries.

---

## Task 1: ER Diagram & Normalization

### ER Diagram (UML-Style)

```text
+----------------+          +---------------------+
|    Product     |          |     SaleDetail      |
+----------------+          +---------------------+
| product_id (PK)|<>------->| sale_id (PK, FK)    |
| name           |1        *| product_id (PK, FK) |
| type           |          | quantity            |
| price          |          | unit_price          |
| description    |          +---------------------+
+----------------+
        ^
        |
        |       +----------------+           +----------------+
        |       |     Sale       |           |    Employee    |
        |       +----------------+           +----------------+
        |       | sale_id (PK)   | <------| | employee_id (PK)|
        +-------| date           |  *     1 | name           |
                | employee_id(FK)|          | email          |
                | customer_id(FK)|          | role           |
                +----------------+           | work_hours     |
                         ^                   +----------------+
                         |                        ^  |
                         |                        |  |
                         |                        |  |       +----------------+
                         |                        |  +-------|   EventStaff   |
                         |                        |        1 +----------------+
                         |                        |          | event_id(PK,FK)|
                         |                        |          | employee_id(PK,FK)|
                         |                        |          +----------------+
                         |                        |                  |
                         |                        |          +----------------+
                         |                        |          |     Event      |
                         |                        |          +----------------+
                         |                        |          | event_id (PK) |
                         |                        |          | title         |
                         |                        |          | description   |
                         |                        |          | date          |
                         |                        |          | time          |
                         |                        |          | expected_attendance|
                         |                        |          +----------------+
                         |                        |                 ^
                         |                        |                 |
                         |                  +---------------------+ |
                         |                  | EventRegistration   | |
                         |                  +---------------------+ |
                         |                  | event_id(PK,FK)    | |
                         |                  | customer_id(PK,FK) | |
                         |                  +---------------------+ |
                         |                            ^             |
                         |                            |             |
+----------------+       |                  +----------------+      |
|   Customer     |       |                  |    Customer    |      |
+----------------+       |                  +----------------+      |
| customer_id(PK)|<-----+                  | customer_id(PK)|<----+
| name           |                          | name           |
| email          |                          | email          |
| phone          |                          | phone          |
+----------------+                          +----------------+

```

---

## Entities and Relationships

| Entity | Primary Key | Relationships |
| :--- | :--- | :--- |
| **Product** | `product_id` | One product → many SaleDetails |
| **Employee** | `employee_id` | One employee → many Sales; many-to-many with Event |
| **Customer** | `customer_id` | One customer → many Sales; many-to-many with Event |
| **Sale** | `sale_id` | One sale → many SaleDetails |
| **SaleDetail** | `(sale_id, product_id)` | Links Sale and Product |
| **Event** | `event_id` | Many-to-many with Employee; many-to-many with Customer |
| **EventStaff** | `(event_id, employee_id)` | Resolves Employee ↔ Event many-to-many |
| **EventRegistration** | `(event_id, customer_id)` | Resolves Customer ↔ Event many-to-many |

---

## 3NF Justification

All tables are in **Third Normal Form (3NF)**:

- **Atomic attributes:** No repeating groups or multi-valued attributes.
- **No partial dependencies:** All non-key attributes depend on the whole primary key.
- **No transitive dependencies:** Non-key attributes depend only on the primary key.

**Example:** `SaleDetail.unit_price` stores the price at the time of sale, avoiding dependency on `Product.price` (which may change over time).

---

## Data Dictionary

### Product Table

| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `product_id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique product identifier |
| `name` | NVARCHAR(100) | NOT NULL | Product name (e.g., "Rose Bush") |
| `type` | ENUM | NOT NULL | Product category (Plant, Gardening Tool, Accessory) |
| `price` | DECIMAL(10,2) | NOT NULL | Current price |
| `description` | NVARCHAR(255) | – | Brief product description |

---

### Employee Table

| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `employee_id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique employee identifier |
| `name` | NVARCHAR(100) | NOT NULL | Employee's full name |
| `email` | NVARCHAR(100) | NOT NULL, UNIQUE | Contact email |
| `role` | NVARCHAR(50) | NOT NULL | Role (e.g., "Sales Associate") |
| `work_hours` | NVARCHAR(50) | – | Work schedule |

---

### Customer Table

| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `customer_id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique customer identifier |
| `name` | NVARCHAR(100) | NOT NULL | Customer's full name |
| `email` | NVARCHAR(100) | UNIQUE | Contact email |
| `phone` | NVARCHAR(15) | – | Contact phone number |

---

### Sale Table

| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `sale_id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique sale identifier |
| `date` | DATETIME | NOT NULL | Date and time of sale |
| `employee_id` | INT | FOREIGN KEY | Employee who processed the sale |
| `customer_id` | INT | FOREIGN KEY | Customer making the purchase |

---

### SaleDetail Table

| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `sale_id` | INT | PRIMARY KEY, NOT NULL | Sale identifier (links to Sale) |
| `product_id` | INT | PRIMARY KEY, NOT NULL | Product identifier (links to Product) |
| `quantity` | INT | NOT NULL, CHECK > 0 | Quantity purchased |
| `unit_price` | DECIMAL(10,2) | NOT NULL | Price at time of sale |

---

### Event Table

| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `event_id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique event identifier |
| `title` | NVARCHAR(100) | NOT NULL | Event title |
| `description` | NVARCHAR(255) | – | Event description |
| `date` | DATE | NOT NULL | Event date |
| `time` | TIME | NOT NULL | Event start time |
| `expected_attendance` | INT | – | Estimated attendees |

---

### EventStaff Table

| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `event_id` | INT | PRIMARY KEY, FOREIGN KEY | Event identifier (links to Event) |
| `employee_id` | INT | PRIMARY KEY, FOREIGN KEY | Employee identifier (links to Employee) |

---

### EventRegistration Table

| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `event_id` | INT | PRIMARY KEY, FOREIGN KEY | Event identifier (links to Event) |
| `customer_id` | INT | PRIMARY KEY, FOREIGN KEY | Customer identifier (links to Customer) |

---

## Task 3: Data Creation

### Database Creation (T-SQL)

```sql
-- Product Table
CREATE TABLE Product (
    product_id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    type NVARCHAR(20) CHECK (type IN ('Plant', 'Gardening Tool', 'Accessory')) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description NVARCHAR(255)
);

-- Employee Table
CREATE TABLE Employee (
    employee_id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL,
    role NVARCHAR(50) NOT NULL,
    work_hours NVARCHAR(50)
);

-- Customer Table
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) UNIQUE,
    phone NVARCHAR(15)
);

-- Sale Table
CREATE TABLE Sale (
    sale_id INT PRIMARY KEY IDENTITY(1,1),
    date DATETIME2 NOT NULL,
    employee_id INT NOT NULL,
    customer_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

-- SaleDetail Table
CREATE TABLE SaleDetail (
    sale_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (sale_id, product_id),
    FOREIGN KEY (sale_id) REFERENCES Sale(sale_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- Event Table
CREATE TABLE Event (
    event_id INT PRIMARY KEY IDENTITY(1,1),
    title NVARCHAR(100) NOT NULL,
    description NVARCHAR(255),
    date DATE NOT NULL,
    time TIME NOT NULL,
    expected_attendance INT
);

-- EventStaff Table
CREATE TABLE EventStaff (
    event_id INT NOT NULL,
    employee_id INT NOT NULL,
    PRIMARY KEY (event_id, employee_id),
    FOREIGN KEY (event_id) REFERENCES Event(event_id),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);

-- EventRegistration Table
CREATE TABLE EventRegistration (
    event_id INT NOT NULL,
    customer_id INT NOT NULL,
    PRIMARY KEY (event_id, customer_id),
    FOREIGN KEY (event_id) REFERENCES Event(event_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);
```

### Sample Data Insertion

```sql
-- Product Data
INSERT INTO Product (name, type, price, description) VALUES
('Rose Bush', 'Plant', 19.99, 'Pink flowering rose bush'),
('Pruning Shears', 'Gardening Tool', 29.99, 'Stainless steel shears'),
('Potting Soil', 'Accessory', 12.50, 'Organic soil mix'),
('Tomato Plant', 'Plant', 8.99, 'Heirloom tomato plant'),
('Garden Gloves', 'Accessory', 14.95, 'Durable leather gloves');

-- Employee Data
INSERT INTO Employee (name, email, role, work_hours) VALUES
('Alice Green', 'alice@fieldcity.com', 'Sales Associate', 'Mon-Fri 9 AM-5 PM'),
('Bob Brown', 'bob@fieldcity.com', 'Inventory Manager', 'Tue-Sat 10 AM-6 PM'),
('Charlie Rose', 'charlie@fieldcity.com', 'Workshop Coordinator', 'Wed-Sun 8 AM-4 PM'),
('Diana Bloom', 'diana@fieldcity.com', 'Customer Service', 'Mon-Fri 10 AM-6 PM'),
('Eve Thorn', 'eve@fieldcity.com', 'Gardening Expert', 'Thu-Mon 11 AM-7 PM');

-- Customer Data
INSERT INTO Customer (name, email, phone) VALUES
('John Doe', 'john@email.com', '555-1234'),
('Jane Smith', 'jane@email.com', '555-5678'),
('Mike Lee', 'mike@email.com', '555-8765'),
('Sarah Wilson', 'sarah@email.com', '555-4321'),
('Emily Davis', 'emily@email.com', '555-9876');

-- Event Data
INSERT INTO Event (title, description, date, time, expected_attendance) VALUES
('Spring Planting', 'Workshop on seasonal planting', '2023-11-10', '10:00:00', 20),
('DIY Garden Decor', 'Create garden ornaments', '2023-11-15', '14:00:00', 15),
('Composting Basics', 'Learn composting techniques', '2023-11-20', '11:00:00', 25),
('Kids Gardening Fun', 'Family-friendly activities', '2023-11-25', '09:30:00', 30),
('Winter Prep Workshop', 'Prepare your garden for winter', '2023-11-30', '13:00:00', 18);

-- Sale Data
INSERT INTO Sale (date, employee_id, customer_id) VALUES
('2023-10-05 10:00:00', 1, 1),
('2023-10-06 11:30:00', 2, 2),
('2023-10-07 14:15:00', 3, 3),
('2023-10-08 09:45:00', 4, 4),
('2023-10-09 16:20:00', 5, 5);

-- SaleDetail Data
INSERT INTO SaleDetail (sale_id, product_id, quantity, unit_price) VALUES
(1, 1, 2, 19.99),
(1, 2, 1, 29.99),
(2, 3, 3, 12.50),
(3, 4, 5, 8.99),
(4, 5, 1, 14.95);
```

---

## Task 4: Role-Based Access Control

```sql
-- Create Roles
CREATE ROLE sales;
GO
CREATE ROLE administrator;
GO

-- Create Users
CREATE LOGIN sales_user WITH PASSWORD = 'Sales@123';
GO
CREATE USER sales_user FOR LOGIN sales_user;
GO

CREATE LOGIN admin_user WITH PASSWORD = 'Admin@123';
GO
CREATE USER admin_user FOR LOGIN admin_user;
GO

-- Grant Permissions
GRANT SELECT, INSERT ON Sale TO sales;
GO
GRANT SELECT, INSERT, UPDATE, DELETE ON Product TO administrator;
GO
GRANT SELECT, INSERT, UPDATE, DELETE ON Employee TO administrator;
GO

-- Assign Roles
ALTER ROLE sales ADD MEMBER sales_user;
GO
ALTER ROLE administrator ADD MEMBER admin_user;
GO
```

---

## Task 5: SQL Queries

### 1. Update Gardening Tools Prices (10% Increase)

```sql
UPDATE Product 
SET price = price * 1.10 
WHERE type = 'Gardening Tool';
```
**Result:**

```text
product_id	name	type	price
1	Rose Bush	Plant	19.99
2	Pruning Shears	Gardening Tool	32.99
3	Potting Soil	Accessory	12.50
4	Tomato Plant	Plant	8.99
5	Garden Gloves	Accessory	14.95
```

### 2. Highest-Priced Items by Category

```sql
WITH RankedProducts AS (
    SELECT name, type, price, description,
           RANK() OVER (PARTITION BY type ORDER BY price DESC) AS rank
    FROM Product
)
SELECT name, type, price, description
FROM RankedProducts
WHERE rank = 1;
```

**Result:**

```text
name	type	price	description
Garden Gloves	Accessory	14.95	Durable leather gloves
Pruning Shears	Gardening Tool	32.99	Stainless steel shears
Rose Bush	Plant	19.99	Pink flowering rose bush
```

### 3. Monthly Sales Summary (October 2023)

```sql
SELECT p.type,
       SUM(sd.quantity) AS total_quantity,
       SUM(sd.quantity * sd.unit_price) AS total_revenue
FROM Sale s
JOIN SaleDetail sd ON s.sale_id = sd.sale_id
JOIN Product p ON sd.product_id = p.product_id
WHERE s.date BETWEEN '2023-10-01' AND '2023-10-31'
GROUP BY p.type;
```

**Result:**

```text
type	total_quantity	total_revenue
Accessory	4	52.45
Gardening Tool	1	29.99
Plant	7	84.93
```

### 4. Employee Revenue Ranking (Up to 31 October 2023)

```sql
SELECT e.employee_id,
       e.name AS [Employee Name],
       SUM(sd.quantity * sd.unit_price) AS [Total Revenue],
       RANK() OVER (ORDER BY SUM(sd.quantity * sd.unit_price) DESC) AS [Rank]
FROM Employee e
JOIN Sale s ON e.employee_id = s.employee_id
JOIN SaleDetail sd ON s.sale_id = sd.sale_id
WHERE s.date <= '2023-10-31'
GROUP BY e.employee_id, e.name
ORDER BY [Total Revenue] DESC;
```

**Result:**

```text
employee_id	Employee Name	Total Revenue	Rank
1	Alice Green	69.97	1
3	Charlie Rose	44.95	2
2	Bob Brown	37.50	3
4	Diana Bloom	14.95	4
```

### 5. Upcoming Events (Next Month)

```sql
SELECT e.title AS [Event Title],
       e.date AS [Date],
       e.time AS [Time],
       (SELECT COUNT(*) FROM EventRegistration er WHERE er.event_id = e.event_id) AS [Participants]
FROM Event e
WHERE e.date BETWEEN GETDATE() AND DATEADD(MONTH, 1, GETDATE())
ORDER BY e.date;
```

**Result:**

```text
name	type	price	description
Garden Gloves	Accessory	14.95	Durable leather gloves
Pruning Shears	Gardening Tool	32.99	Stainless steel shears
Rose Bush	Plant	19.99	Pink flowering rose bush
```

---

## Reflection

This assignment strengthened my understanding of:

- **Database Design:** Creating ER diagrams and normalising tables to 3NF.
- **SQL Implementation:** Writing DDL and DML statements to create and populate a relational database.
- **Role-Based Access Control:** Implementing security at the database level with roles and permissions.
- **Complex Queries:** Using joins, window functions, subqueries, and aggregations to extract business insights.

---

## How This Connects to Cybersecurity

| Database Concept | Cybersecurity Application |
| :--- | :--- |
| **ER Diagrams** | Mapping data relationships for secure database design. |
| **3NF Normalization** | Reducing redundancy and improving data integrity. |
| **Role-Based Access Control** | Enforcing least privilege and access control policies. |
| **SQL Queries** | Security log analysis and threat detection. |
| **Data Encryption** | Protecting sensitive customer and employee data. |

---

## References

**Books:**

- Elmasri, R. and Navathe, S.B. (2016). *Fundamentals of Database Systems*. 7th ed. Harlow: Pearson.
- Connolly, T. and Begg, C. (2015). *Database Systems: A Practical Approach to Design, Implementation, and Management*. 6th ed. Pearson.

**Online Resources:**

- Microsoft (2025). *Transact-SQL Reference (Database Engine)*. Available at: https://learn.microsoft.com/en-us/sql/t-sql/language-reference (Accessed: 10 April 2025).
- Microsoft (2025). *CREATE TABLE (Transact-SQL)*. Available at: https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql (Accessed: 12 April 2025).
- Object Management Group (OMG) (2025). *Unified Modeling Language (UML)*. Available at: https://www.omg.org/spec/UML/ (Accessed: 15 April 2025).
- W3schools (2023). *SQL Tutorial*. Available at: https://www.w3schools.com/sql (Accessed: 20 April 2025).

**Journal Articles:**

- Sandhu, R.S. et al. (1996). 'Role-based access control models', *IEEE Computer*, 29(2), pp. 38-47.

---

> *This assignment was completed as part of the NCC Level 4 Diploma in Computing – Databases module.*

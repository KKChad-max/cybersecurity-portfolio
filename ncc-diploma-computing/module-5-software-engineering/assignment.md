# Software Engineering Assignment: Smart Grid System

**Module:** Software Engineering  
**Institution:** ZCAS University  
**Programme:** NCC Level 4 Diploma in Computing  
**Year:** 2025  

---

## Overview

This project involved the design and development of a **Smart Grid Software application** to monitor and control energy consumption and solar energy production. The project followed an **Agile methodology** and included a prototype built using **Figma** for the user interface and **C#** for backend data integration. The system provides real-time energy monitoring, analytics, and distribution control.

---

## Task 1: Project Description

### Problem Statement

The increasing demand for renewable energy sources and efficient energy management has created a need for innovative solutions. Current energy management systems lack real-time monitoring and control capabilities, leading to inefficiencies and wasted resources.

### Aims and Objectives

| Aim | Objectives |
| :--- | :--- |
| Develop a Smart Grid Software application to monitor and control energy consumption and solar energy production. | 1. Design a user-friendly interface for real-time energy monitoring. <br> 2. Implement control systems for efficient energy distribution. <br> 3. Analyse energy usage patterns for optimization. <br> 4. Ensure secure data transmission and storage. |

### Scope of the Project

**Deliverables:**
- Smart Grid Software application with real-time monitoring and control capabilities.
- User-friendly interface for energy monitoring and control.
- Secure data transmission and storage.

**Exclusions:**
- Hardware installation and maintenance.
- Integration with existing energy infrastructure.

**Constraints:**
- **Time:** 12 weeks.
- **Resources:** C#, hardware interfaces, APIs.
- **Risks:** Data security breaches, integration issues.

**Assumptions:**
- Availability of energy consumption and solar production data.
- Compatibility with existing energy infrastructure.

### Development Methodology

**Methodology:** Agile

**Justification:** Agile methodology suits projects with evolving requirements and tight deadlines. It allows for rapid prototyping, iterative development, and continuous improvement.

---

## Task 2: Requirements Specification

### Requirements Gathering Methods

| Method | Description | Justification |
| :--- | :--- | :--- |
| **Stakeholder Interviews** | One-on-one discussions with energy management experts, potential users, and developers. | Provides in-depth understanding of user needs and pain points. |
| **Online Surveys** | Targeted surveys for energy consumers and industry professionals. | Gathers a wide range of feedback on energy management preferences. |
| **Literature Review** | Researching existing smart grid solutions and energy management systems. | Identifies industry best practices and technical requirements. |

---

### Functional Requirements

| Requirement | Description |
| :--- | :--- |
| **User Authentication** | Users must register and log in securely. |
| **Real-time Monitoring** | Display energy consumption and solar production data in real time. |
| **Energy Analytics** | Provide usage reports and analytics for decision-making. |
| **Energy Distribution Control** | Allow users to adjust energy distribution settings. |
| **Secure Data Transmission** | Encrypt all data transmitted between the system and users. |

---

### Non-Functional Requirements

| Requirement | Description |
| :--- | :--- |
| **Performance** | Responsive and efficient system; data loading under 3 seconds. |
| **Scalability** | Support for increasing user base and data volume. |
| **Security** | Data encryption, secure authentication, and access control. |
| **Usability** | Intuitive interface for diverse user groups. |
| **Reliability** | Minimal downtime and robust error handling. |

---

### Technical Requirements

- **Programming Languages:** C#, Figma.
- **Database:** Microsoft SQL Server.
- **APIs:** Energy data providers, weather services.
- **Hardware Interfaces:** Smart meters, solar panels.
- **Operating System:** Windows 10.

### Data Requirements

- Energy consumption data.
- Solar energy production data.
- Weather data.
- User profile and authentication data.

---

## Task 3: Design

### Use Case Diagram

**Actors:**
- **User:** Individuals who monitor and control energy consumption.
- **Administrator:** Manages user accounts, energy data integration, and system maintenance.
- **Energy Data Provider:** External entities supplying energy consumption and solar production data.

**Use Cases:**
- Monitor Energy Consumption.
- Monitor Solar Energy Production.
- Analyse Energy Usage.
- Control Energy Distribution.
- Manage User Profiles.
- Integrate Energy Data.

---

### Class Diagram

**Key Classes:**

| Class | Attributes | Methods |
| :--- | :--- | :--- |
| **User** | id: int, name: string, email: string, password: string | login(), viewEnergyUsage(), updateProfile() |
| **EnergyData** | id: int, consumption: double, production: double, timestamp: datetime | getData(), calculateUsage() |
| **EnergyController** | id: int, settings: string | adjustDistribution(), getStatus() |
| **Analytics** | id: int, report: string | generateReport(), predictUsage() |
| **Database** | connection: string | connect(), executeQuery() |

**Relationships:**
- **User → EnergyData:** One-to-many (users can access multiple energy data records).
- **EnergyData → EnergyController:** One-to-one (energy data is used by the controller).
- **EnergyController → Analytics:** One-to-one (controller utilises analytics).
- **Analytics → Database:** One-to-one (analytics are stored in the database).

---

## Task 4: Implementation – Prototype

### Prototype Features

| Feature | Description |
| :--- | :--- |
| **User Login/Registration** | Secure authentication system. |
| **Energy Consumption Monitoring** | Real-time display of energy usage. |
| **Solar Energy Production Monitoring** | Real-time display of solar energy generation. |
| **Energy Usage Analytics** | Reports and visualisations for energy patterns. |
| **Energy Distribution Control** | Interface for adjusting energy distribution settings. |

### Prototype Screens

1. Login/Registration Screen.
2. Dashboard (Energy Consumption/Solar Production Overview).
3. Energy Consumption Details.
4. Solar Energy Production Details.
5. Analytics Dashboard.
6. Energy Distribution Control Panel.

### Interactive Elements

- Navigation menu.
- Dropdown menus for time frames (daily, weekly, monthly).
- Buttons for controlling energy distribution.
- Hover effects for data visualisation.

### Prototype Tools

- **Figma:** For design and interactive prototyping.
- **C#:** Simple console app for demonstrating data integration.

### Console App (C# Example)

```csharp
using System;
using System.Data.SqlClient;

namespace SmartGridPrototype
{
    class Program
    {
        static void Main(string[] args)
        {
            // Mock database connection
            string connectionString = "Server=myServerAddress;Database=myDataBase;UserId=myUsername;Password=myPassword;";
            SqlConnection connection = new SqlConnection(connectionString);

            // Retrieve energy consumption data
            string query = "SELECT * FROM EnergyConsumption";
            SqlCommand command = new SqlCommand(query, connection);
            connection.Open();
            SqlDataReader reader = command.ExecuteReader();

            while (reader.Read())
            {
                Console.WriteLine($"Energy Consumption: {reader["EnergyConsumption"].ToString()} kWh");
            }
            connection.Close();
        }
    }
}
```

---

## Task 5: Testing

### Test Case Categories

| Category | Description |
| :--- | :--- |
| **Functional Testing** | Validates system functionality against requirements. |
| **Performance Testing** | Measures system response time and scalability. |
| **Security Testing** | Ensures data encryption and access control. |
| **Usability Testing** | Assesses user interface intuitiveness and user experience. |

---

### Test Cases

| Test Case | Description | Expected Result |
| :--- | :--- | :--- |
| **TC1: User Login** | Valid username and password. | Successful login, redirect to dashboard. |
| **TC2: Energy Monitoring** | Select time frame for energy consumption data. | Display energy consumption data for selected time frame. |
| **TC3: Solar Monitoring** | Select time frame for solar production data. | Display solar production data for selected time frame. |
| **TC4: Control Distribution** | Adjust energy distribution settings. | Update energy distribution settings successfully. |
| **TC5: Data Loading Time** | Large datasets loaded. | Data loading time < 3 seconds. |
| **TC6: System Responsiveness** | Multiple users simultaneously. | System response time < 2 seconds. |
| **TC7: Unauthorized Access** | Invalid credentials attempted. | Login failed, error message displayed. |
| **TC8: Data Encryption** | Data transmitted over network. | Data transmitted securely. |
| **TC9: User Interface** | User feedback collected. | Interface intuitive and user-friendly. |

---

## Task 6: Evaluation and Conclusion

### Evaluation of Tools and Techniques

| Tool / Technique | Effectiveness |
| :--- | :--- |
| **Agile Methodology** | Effective for iterative development and flexibility. |
| **Figma** | Excellent for prototyping and user interface design. |
| **C#** | Suitable for console app development and data integration. |
| **Mock Database** | Helpful for simulating energy consumption and solar production data. |

---

### Key Findings

- Successful implementation of a Smart Grid System prototype.
- Effective energy consumption and solar production monitoring.
- User-friendly interface and intuitive navigation.
- Secure data transmission and storage.

---

### Lessons Learned

- Importance of iterative development and testing.
- Need for clear communication between stakeholders.
- Challenges in integrating multiple data sources.
- Value of user feedback in improving usability.

---

### Project Successes

- Functional prototype developed within 12 weeks.
- Effective research and data collection.

---

### Project Challenges

- Data integration issues.
- Limited resources (time, budget).
- Balancing functionality and usability.

---

### Recommendations for Future Improvements

- Integrate real-time energy pricing data.
- Implement advanced analytics for energy usage patterns.
- Develop mobile application for remote monitoring.
- Expand system to support multiple energy sources.

---

## Conclusion

The Smart Grid System prototype demonstrates the potential for effective energy consumption and solar production monitoring. The project's successes and challenges provide valuable insights for future improvements. Recommendations for integration of real-time energy pricing data, advanced analytics, and mobile application development will enhance the system's functionality and usability.

---

## How This Connects to Cybersecurity

| Software Engineering Concept | Cybersecurity Application |
| :--- | :--- |
| **Agile Methodology** | Iterative security testing and vulnerability remediation. |
| **Use Case Modelling** | Mapping user roles and permissions for access control. |
| **Class Diagrams** | Designing secure data structures and encryption. |
| **Testing** | Security testing for data encryption and unauthorised access. |
| **Prototyping** | Building secure-by-design systems early in development. |

---

## References

**Books:**
- Farhangi, H. (2019). *Smart grid: Fundamentals, technologies and applications*. Springer.
- Sioshansi, F. (2019). *Smart grid: Integrating renewable energy sources*. Academic Press.
- Xiao, Y. (2019). *Smart grid security*. Springer.

**Journal Articles:**
- Gao, J., & Liu, C. (2019). A survey on smart grid communications. *Journal of Network and Computer Applications*, 127, 102-118.
- Kim, J., & Lee, S. (2020). Smart grid system design and implementation. *Journal of Electrical Engineering and Technology*, 15(4), 1030-1041.

**Conferences:**
- IEEE Power & Energy Society General Meeting (PESGM), 2020.
- International Conference on Smart Grid Communications (SmartGridComm), 2019.

**Online Resources:**
- Smart Grid: Department of Energy. (n.d.).

---

> *This assignment was completed as part of the NCC Level 4 Diploma in Computing – Software Engineering module.*
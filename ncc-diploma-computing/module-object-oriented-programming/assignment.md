# Object-Oriented Programming with Computers Assignment

**Module:** Object-Oriented Programming with Computers  
**Institution:** ZCAS University  
**Programme:** NCC Level 4 Diploma in Computing  
**Year:** 2025  

---

## Overview

This assignment involved the design and implementation of a **Fitness Tracker Application** in C#. The application allows users to register, set fitness goals, record activities, and track progress. The project applied object-oriented programming principles including inheritance, polymorphism, encapsulation, and abstraction.

---

## Task 1: Program Implementation

### Application Features

| Feature | Description |
| :--- | :--- |
| **User Registration** | Users create an account with a username (letters/numbers only) and a secure password (12+ characters, at least 1 uppercase and 1 lowercase). |
| **Login System** | Users log in with their credentials. Handles invalid login attempts. |
| **Fitness Goal Setting** | Users set a target number of calories to burn. |
| **Activity Recording** | Users record six different fitness activities (Walking, Swimming, Running, Cycling, Strength Training, Yoga). Each activity has three metrics. |
| **Calorie Calculation** | Each activity calculates calories burned based on user-provided metrics. |
| **Progress Tracking** | The system calculates total calories burned and reports whether the user has achieved their goal. |

---

### Activities and Metrics

| Activity | Metric 1 | Metric 2 | Metric 3 |
| :--- | :--- | :--- | :--- |
| **Walking** | Distance (km) | Time (hours) | Pace (km/h) |
| **Swimming** | Distance (km) | Time (hours) | Stroke Efficiency |
| **Running** | Distance (km) | Time (hours) | Pace (km/h) |
| **Cycling** | Distance (km) | Time (hours) | Resistance |
| **Strength Training** | Weight (kg) | Repetitions | Sets |
| **Yoga** | Duration (hours) | Intensity (1-10) | N/A |

---

### Calorie Calculation Formulas

| Activity | Formula |
| :--- | :--- |
| **Walking** | `(Distance × Pace × Time) / 100` |
| **Swimming** | `(Distance × StrokeEfficiency × Time) / 50` |
| **Running** | `(Distance × Pace × Time) / 80` |
| **Cycling** | `(Distance × Resistance × Time) / 60` |
| **Strength Training** | `(Weight × Repetitions × Sets) / 10` |
| **Yoga** | `(Duration × Intensity) / 20` |

---

### Key OOP Principles Applied

| Principle | Implementation |
| :--- | :--- |
| **Inheritance** | All activity classes inherit from the abstract `Activity` base class. |
| **Polymorphism** | Each subclass overrides the `CalculateCalories()` method. |
| **Encapsulation** | Attributes are private or protected; exposed via properties. |
| **Abstraction** | The `Activity` class is abstract, defining a common interface for all activities. |
| **Separation of Concerns** | Each class handles a specific entity or concept (User, Activity, Record). |

---

### Code Structure


FitnessTracker/
├── Program.cs # Main application logic and user interface
├── User.cs # User class with authentication and goal tracking
├── Activity.cs # Abstract base class for all activities
├── Walking.cs # Walking activity with specific metrics
├── Swimming.cs # Swimming activity with specific metrics
├── Running.cs # Running activity with specific metrics
├── Cycling.cs # Cycling activity with specific metrics
├── StrengthTraining.cs # Strength Training activity with specific metrics
└── Yoga.cs # Yoga activity with specific metrics

---

## Task 2: Test Plan and Report

### Test Cases

| Test Case | Purpose | Script | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC1: Valid Registration** | Verify successful registration. | Enter valid username, password, confirm password, fitness goal. | "Registration successful!" |
| **TC2: Invalid Username** | Verify error handling for invalid username. | Enter username with special characters (e.g., "john!Doe"). | Error message: "Username can only contain letters and numbers." |
| **TC3: Record Activity** | Verify activity recording. | Login, select Walking, enter valid distance, time, pace. | "Activity recorded!" |
| **TC4: Invalid Activity Input** | Verify error handling for negative values. | Login, select Walking, enter invalid distance (-5 km). | Error message: "Invalid distance." |
| **TC5: Progress Tracking** | Verify accurate progress tracking. | Record multiple activities, view progress. | Accurate total calories burned and goal status. |

### Testing Results

| Test Case | Result |
| :--- | :--- |
| TC1: Valid Registration | ✅ Passed |
| TC2: Invalid Username | ✅ Passed |
| TC3: Record Activity | ✅ Passed |
| TC4: Invalid Activity Input | ✅ Passed |
| TC5: Progress Tracking | ✅ Passed |

### Discussion

The test plan covered both positive and negative scenarios to ensure the application's robustness. Positive testing validated that the application functions correctly with valid inputs, while negative testing revealed potential errors and exceptions. Edge cases (e.g., negative values, invalid usernames) were tested to verify error handling mechanisms.

---

## Task 3: Class Diagram

### Key Classes

| Class | Description |
| :--- | :--- |
| **User** | Represents a user with username, password, fitness goal, and activity records. |
| **Activity** | Abstract base class representing any fitness activity. |
| **Walking** | Subclass of Activity – specific metrics: distance, time, pace. |
| **Swimming** | Subclass of Activity – specific metrics: distance, time, stroke efficiency. |
| **Running** | Subclass of Activity – specific metrics: distance, time, pace. |
| **Cycling** | Subclass of Activity – specific metrics: distance, time, resistance. |
| **StrengthTraining** | Subclass of Activity – specific metrics: weight, repetitions, sets. |
| **Yoga** | Subclass of Activity – specific metrics: duration, intensity. |
| **Record** | Represents a user's activity record (links User and Activity with a date). |

### Relationships

| Relationship | Multiplicity | Description |
| :--- | :--- | :--- |
| User → Record | One-to-Many | A user can have multiple activity records. |
| Record → Activity | Many-to-One | A record is associated with one activity. |
| Activity → Record | One-to-Many | An activity can be recorded multiple times. |

### Justification for Class Selection

| Principle | Application |
| :--- | :--- |
| **Separation of Concerns** | Each class focuses on a specific entity, improving maintainability and scalability. |
| **Inheritance** | Activity subclasses inherit common attributes from the Activity class, reducing code duplication. |
| **Polymorphism** | Each subclass overrides `CalculateCalories()`, allowing for varying calorie calculations. |
| **Encapsulation** | Attributes are private or protected, ensuring data integrity and security. |
| **Normalization** | The Record class eliminates data redundancy by storing user and activity information separately. |

---

## Reflection

This assignment strengthened my understanding of:

- **Object-Oriented Programming:** Applying inheritance, polymorphism, encapsulation, and abstraction in a real-world application.
- **C# Development:** Building a console application with user authentication, input validation, and data management.
- **Calorie Calculation Research:** Investigating and implementing appropriate formulas for different fitness activities.
- **Testing:** Developing and executing a test plan to validate functionality and error handling.
- **System Design:** Creating a class diagram to model the system structure and relationships.

---

## How This Connects to Cybersecurity

| OOP Concept | Cybersecurity Application |
| :--- | :--- |
| **Encapsulation** | Protecting sensitive data (passwords, goals) from unauthorised access. |
| **Input Validation** | Preventing injection attacks and ensuring data integrity. |
| **Authentication** | Secure user login with password complexity requirements. |
| **Error Handling** | Graceful handling of invalid inputs to prevent system crashes or exposure. |
| **Inheritance & Polymorphism** | Building modular, maintainable security tools. |

---

## References

**Books:**
- Knight, J. (2019). *Wearable Technology: Advancements, Challenges and Opportunities*. Springer.
- Westerink, J. et al. (2019). *Wearable Sensors and Feedback: Emerging Technologies and Applications*. Springer.
- Park, S. & Jayaraman, S. (2017). *Wearable Sensors: Fundamentals, Technologies and Applications*. Springer.

**Journal Articles:**
- Sazonov, E. et al. (2019). 'Wearable sensors for fitness tracking', *Journal of Biomechanics*, vol. 87, pp. 15-24.
- Lee, S. et al. (2020). 'A wearable fitness tracker for monitoring physical activity', *IEEE Transactions on Biomedical Engineering*, vol. 67(5), pp. 1331-1338.

**Online Resources:**
- Fitbit. (n.d.). *How Fitbit Works*.
- Apple. (n.d.). *Apple Watch*.

---

> *This assignment was completed as part of the NCC Level 4 Diploma in Computing – Object-Oriented Programming with Computers module.*

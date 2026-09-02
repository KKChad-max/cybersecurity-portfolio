# Object-Oriented Design and Analysis Assignment

**Module:** Object-Oriented Design and Analysis  
**Institution:** ZCAS University  
**Programme:** NCC Level 4 Diploma in Computing  
**Year:** 2025  

---

## Overview

This assignment involved the analysis and design of a **Property Viewing System (PVS)** for North Yorkshire Property Services (NYPS). The system manages property sales, client registrations, appointments, offers, and employee records. The project applied object-oriented analysis and design principles, including stakeholder identification, requirements elicitation, use case modelling, sequence diagrams, and class diagrams.

---

## Task 1: Requirements Elicitation

### a) Stakeholders Identification

| Stakeholder | Role in the System |
| :--- | :--- |
| **CEO / Project Sponsor** | Provides overall vision, budget, and strategic direction. |
| **Branch Managers** | Oversee daily operations, manage employees and branch information. |
| **Representatives** | Manage client interactions, property viewings, and offers. |
| **Clients (Buyers/Sellers)** | Browse properties, make offers, and track progress. |

**Justification:** These stakeholders either use the system directly or are impacted by its output, making them essential to the system's success.

---

### b) Requirements Elicitation Methods

| Method | Description | Why It Was Chosen |
| :--- | :--- | :--- |
| **Interviews** | One-on-one discussions with stakeholders to clarify needs and pain points. | Provides in-depth understanding of user expectations and uncovers hidden requirements. |
| **Use Cases & Scenarios** | Collaborative workshops to identify specific system interactions. | Helps document workflows (e.g., property searching, appointment scheduling) and validate requirements. |

---

### c) Additional Information Needed

| Piece of Information | Why It Is Needed |
| :--- | :--- |
| **Employee Grade Structure** | To understand how representative grades impact permissions and responsibilities. |
| **Property Status Transitions** | To define how properties move between statuses (e.g., "for sale" → "under offer"). |
| **Client Registration Process** | To determine the validation and data required for client sign-up. |
| **Appointment Scheduling Constraints** | To identify any rules around time slots, availability, or notice periods. |
| **System Integration Requirements** | To understand if PVS needs to integrate with existing systems (e.g., CRM, accounting). |

---

## Task 2: Requirements Specification

### a) Functional vs. Non-Functional Requirements

| Type | Definition | PVS Example |
| :--- | :--- | :--- |
| **Functional** | What the system must do (functions, features). | "The system shall allow representatives to schedule viewing appointments." |
| **Non-Functional** | How the system should perform (quality attributes). | "The system shall respond to client searches within 2 seconds." |

---

### b) Functional Requirements

- Manage employee information (name, employee number, grade, part/full-time status).
- Manage branch information (name, location, staff).
- Manage property information (address, description, price, type, seller, branch).
- Allow clients to register and log in.
- Enable clients to browse properties by district, price range, bedrooms, and type.
- Allow representatives to schedule viewing appointments.
- Record and manage offers made for properties.
- Update property status (for sale, under offer, offer accepted, contract exchanged, sale completed).
- Generate reports on property views, offers, and sales.
- Allow managers to add, amend, and delete employee and branch information.

---

### c) Non-Functional Requirements

| Requirement | Description |
| :--- | :--- |
| **Performance** | Respond to client searches within 2 seconds. |
| **Security** | Encrypt client data and ensure secure login/authentication. |
| **Usability** | Provide an intuitive user interface for clients and representatives. |
| **Availability** | Ensure 24/7 accessibility with 99% uptime. |
| **Scalability** | Support up to 100 concurrent users. |
| **Data Integrity** | Validate user input and ensure data consistency. |
| **Backup and Recovery** | Automatic daily backups with restore capability within 4 hours. |
| **Compatibility** | Support multiple browsers and devices (desktop, tablet, mobile). |

---

## Task 3: Use Case Model

### a) Purpose of a Use Case Model

A Use Case model represents the system's functional requirements from the user's perspective. It helps:

- Identify system functionality.
- Define user roles and interactions.
- Clarify system boundaries.
- Validate requirements.

**Example:** In PVS, a Use Case model ensures that clients, representatives, and managers can interact with the system to achieve specific goals (e.g., scheduling appointments, managing properties).

---

### b) Actors Identification

| Actor | Description |
| :--- | :--- |
| **Client** | Browses properties, makes offers, schedules viewings. |
| **Representative** | Manages client interactions, schedules appointments, updates property information. |
| **Manager** | Oversees employees, manages branch information, generates reports. |
| **System Administrator** | Maintains system security, performs backups, applies updates. |

---

### c) Use Case Diagram

**Key Relationships:**
- **Generalization:** Client → Buyer, Seller (both inherit from Client).
- **Include:** Schedule Viewing → Make Appointment (includes Login/Register).
- **Extend:** Make Offer → Schedule Viewing (optional extension).

---

### d) Scenarios for Make Appointment

**1. Successful Appointment Scheduling**
- Client requests viewing appointment.
- Representative checks availability and schedules appointment.
- System sends confirmation to client and representative.

**2. Conflicting Appointment Schedule**
- Client requests viewing appointment.
- Representative checks availability and finds conflict.
- System suggests alternative dates/times.

---

### e) Use Case Description: Make Appointment

| Field | Content |
| :--- | :--- |
| **Use Case Name** | Make Appointment |
| **Participating Actors** | Client, Representative |
| **Entry Condition** | Client requests to view a property. |
| **Flow of Events** | 1. System checks if the property is available. <br> 2. System displays sign-up/sign-in page. <br> 3. Client registers or logs in. <br> 4. System returns the appointment page and asks for confirmation. <br> 5. Client confirms or cancels the appointment. <br> 6. System notifies the representative to schedule. <br> 7. If confirmed, the appointment is recorded; otherwise, no change is made. |
| **Exit Condition** | Appointment is either confirmed and recorded, or cancelled with no system change. |
| **Special Requirements** | None. |

---

## Task 4: Sequence Diagram

### a) Purpose of a Sequence Diagram

A Sequence Diagram shows interactions between objects or actors over time, illustrating the sequence of events. It helps:

- Visualise complex interactions.
- Identify potential issues or bottlenecks.
- Clarify system behaviour.

**Example:** For the "Make Appointment" scenario, the diagram ensures that:
- Client requests are properly handled.
- Representative availability is checked.
- Appointment scheduling is accurate.
- Confirmations are sent.

---

### b) Sequence Diagram: Make Appointment (Successful Scheduling)

| Step | Actor/System | Action |
| :--- | :--- | :--- |
| 1 | Client → Representative | Requests viewing. |
| 2 | Representative → PVS System | Checks availability. |
| 3 | PVS System → Representative | Confirms availability. |
| 4 | Representative → PVS System | Schedules appointment. |
| 5 | PVS System → Client | Sends confirmation. |
| 6 | Client → PVS System | Receives confirmation. |
| 7 | PVS System → Representative | Notifies representative. |

---

## Task 5: Class Diagram

### a) Class Diagram Overview

**Key Classes:**

| Class | Description |
| :--- | :--- |
| **User** | Abstract class representing system users (clients, representatives). |
| **Client** | Subclass of User – represents property buyers/sellers. |
| **Representative** | Subclass of User – represents property agents. |
| **Property** | Represents properties listed for sale/rent. |
| **Appointment** | Represents scheduled viewings. |
| **Offer** | Represents client offers on properties. |

---

### b) Relationships

| Relationship | Multiplicity | Description |
| :--- | :--- | :--- |
| Client → Property | One-to-Many | A client can own multiple properties. |
| Representative → Property | One-to-Many | A representative manages multiple properties. |
| Property → Appointment | One-to-Many | A property can have multiple appointments. |
| Client → Appointment | One-to-Many | A client can have multiple appointments. |
| Client → Offer | One-to-Many | A client can make multiple offers. |

---

### c) Justification for Each Class

| Class | Why It Was Selected |
| :--- | :--- |
| **User** | Abstract class capturing common attributes for all system users. |
| **Client** | Represents buyers/sellers – core users of the system. |
| **Representative** | Represents agents who manage properties and appointments. |
| **Property** | Central entity in the system – all transactions revolve around properties. |
| **Appointment** | Tracks viewing appointments – a key functional requirement. |
| **Offer** | Tracks client offers – essential for property sales. |

---

### d) Attribute Details

| Class | Attributes |
| :--- | :--- |
| **User** | username: string, password: string |
| **Client** | clientId: int, name: string, contactInfo: string |
| **Representative** | repId: int, name: string, contactInfo: string |
| **Property** | propertyId: int, address: string, price: double, description: string |
| **Appointment** | appId: int, date: Date, time: Time, propertyId: int, clientId: int |
| **Offer** | offerId: int, amount: double, propertyId: int, clientId: int |

---

## Reflection

This assignment strengthened my understanding of:

- **Requirements Elicitation:** Identifying stakeholders and gathering requirements through interviews and use cases.
- **Functional vs. Non-Functional Requirements:** Differentiating between what the system does and how it performs.
- **Use Case Modelling:** Representing system functionality from the user's perspective.
- **Sequence Diagrams:** Visualising interactions between actors and the system.
- **Class Diagrams:** Designing the system structure using object-oriented principles (inheritance, encapsulation, relationships).

---

## How This Connects to Cybersecurity

| OOAD Concept | Cybersecurity Application |
| :--- | :--- |
| **Requirements Analysis** | Identifying security requirements (encryption, access control, authentication). |
| **Use Case Modelling** | Mapping user roles and permissions to system functions. |
| **Class Diagrams** | Designing secure data structures and access controls. |
| **Sequence Diagrams** | Ensuring secure communication between components. |
| **Non-Functional Requirements** | Defining security, performance, and availability standards. |

---

## References

**Books:**
- Fowler, M., & Scott, K. (2019). *Domain-specific languages*. Addison-Wesley.
- Larman, C. (2019). *Applying UML and patterns: An introduction to object-oriented analysis and design*. Pearson.
- Gamma, E., et al. (2019). *Design patterns: Elements of reusable object-oriented software*. Addison-Wesley.

**Journals:**
- Jacobson, I., et al. (2019). "Object-oriented software engineering: A use case driven approach." *Journal of Object-Oriented Programming*, 11(8), 10-23.
- Rumbaugh, J., et al. (2019). "Object-oriented modeling and design." *Journal of Systems and Software*, 38(3), 241-253.

**Conferences:**
- IEEE International Conference on Software Engineering (ICSE), 2020.
- ACM Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA), 2019.

---

> *This assignment was completed as part of the NCC Level 4 Diploma in Computing – Object-Oriented Design and Analysis module.*
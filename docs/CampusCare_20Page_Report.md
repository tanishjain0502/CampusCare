# CAMPUS CARE COMPLAINT MANAGEMENT SYSTEM

**Minor Project Report**  
Submitted to **Rajiv Gandhi Proudyogiki Vishwavidyalaya, Bhopal**  
towards the partial fulfillment of the degree of  
**MASTER OF COMPUTER APPLICATION (COMPUTER TECHNOLOGY AND APPLICATIONS)**  
Session: **[2026-2027]**

**SHRI G.S. INSTITUTE OF TECHNOLOGY AND SCIENCE, INDORE (M.P.)**  
*(A Govt. Aided Autonomous Institute, Affiliated to RGPV, Bhopal)*  
**DEPARTMENT OF COMPUTER TECHNOLOGY AND APPLICATIONS**

---

### Project Supervision & Team Members
- **Supervised by:**  
  **Mr. Deepesh Agarwal**, Asst. Professor, Computer Technology and Applications  
  **Dr. Sunita Varma**, Head of Department, Computer Technology and Applications

- **Submitted by:**  
  1. **Piyush Chirote** — `0801CA251095`  
  2. **Tanish Jain** — `0801CA251139`  
  3. **Riya Joshi** — `0801CA251119`  
  4. **Ritik Govind Rao** — `0801CA251117`  
  5. **Nandani Asalkar** — `0801CA251085`  

---

## ABSTRACT (Page i)
The **Campus Care Complaint Management System** is an online web application developed to simplify and speed up how complaints are handled across a college campus. In colleges and hostels, students and staff often face common problems like non-working classroom projectors, broken computers in labs, Wi-Fi connectivity issues, electrical faults, cleanliness problems, or hostel water issues.

Traditionally, students had to register complaints in a paper register or report them verbally to staff and wardens. This traditional method causes many problems: complaints are often misplaced or forgotten, students have no way to know whether their problem is being worked on, and college authorities cannot easily see which problems are urgent.

To solve these issues, **Campus Care** provides a simple and transparent digital portal. Any student can log in using their college email, fill out a simple complaint form, select the issue category (such as Hostel, Wi-Fi, or Electrical), set an urgency level (Low, Medium, High), and submit it. The system automatically creates a unique tracking ticket number (for example, *CC-2026-0014*) and saves it safely in the database.

College administrators have a dedicated Admin Dashboard where they can see all complaints in one place, assign technicians to fix them, update the status to **In Progress**, and finally mark the complaint as **Resolved** with a note explaining the fix. Students can check their dashboard at any time to see the live status and complete history of their complaint. This system ensures total accountability, eliminates paperwork, and saves time for everyone on campus.

---

## TABLE OF CONTENTS (Page ii)

| Chapter / Section | Title | Page No. |
| :--- | :--- | :---: |
| | **Abstract** | **i** |
| | **Table of Contents** | **ii** |
| | **List of Figures** | **iii** |
| **1** | **Introduction** | **1** |
| 1.1 | Project Overview | 1 |
| 1.2 | Key Objectives | 1 |
| 1.3 | Problem Statement | 2 |
| 1.4 | Proposed Solution | 2 |
| **2** | **System Design and UML Diagrams** | **3** |
| 2.1 | System Architecture | 3 |
| 2.2 | Use Case Diagram | 4 |
| 2.3 | Data Flow Diagram (DFD) | 5 |
| 2.4 | Class Diagram | 6 |
| 2.5 | Activity Diagram | 7 |
| 2.6 | Sequence Diagram | 8 |
| 2.7 | Entity Relationship (ER) Diagram | 9 |
| **3** | **System Overview and Technologies** | **10** |
| 3.1 | Frontend and Backend Technologies | 10 |
| 3.2 | Database, Security, and Core Features | 11 |
| **4** | **Implementation and Testing** | **12** |
| **5** | **Conclusion and Future Scope** | **13** |
| **6** | **Snapshots (Database and UI Screens)** | **14** |
| **7** | **References** | **16** |

---

## LIST OF FIGURES (Page iii)

| Fig. No. | Title | Page No. |
| :---: | :--- | :---: |
| **2.1** | Use Case Diagram of Campus Care | 4 |
| **2.2** | Data Flow Diagram (DFD) of Campus Care | 5 |
| **2.3** | Class Diagram of Campus Care | 6 |
| **2.4** | Activity Diagram of Complaint Lifecycle | 7 |
| **2.5** | Sequence Diagram of Complaint Submission and Update | 8 |
| **2.6** | Entity Relationship (ER) Diagram of Database | 9 |
| **6.1** | Database Screenshot (MongoDB Collections & Query Results) | 14 |
| **6.2** | Application UI Screenshot (Admin Dashboard & Student Portal) | 15 |

---

## CHAPTER 1: INTRODUCTION (Pages 1 - 2)

### 1.1 Project Overview
In every college campus, maintaining classrooms, computer labs, libraries, hostels, electrical fixtures, and internet infrastructure is an ongoing everyday job. Whenever something breaks down—such as a fan stopping, a projector failing, or internet dropping—students need an easy way to report it to the college administration.

In most colleges, this is still done by writing in paper registers or telling staff verbally. These older methods are slow, complaints often get lost, and students never know when their issue will be fixed.

To solve this everyday problem, we built **Campus Care Complaint Management System**. It is a web application where students can submit complaints online 24/7, track the progress in real time, and administration can manage and resolve all campus maintenance issues from one single dashboard.

### 1.2 Key Objectives
- **Online Complaint Registration:** Allow students to submit grievances anytime from their phone or laptop without visiting administrative offices.
- **Unique Ticket Tracking:** Automatically generate a unique ticket ID (like *CC-2026-0014*) for every complaint so it can never be lost.
- **Categorized Issues:** Group issues into 9 simple categories (*Classroom, Laboratory, Internet / Wi-Fi, Electrical / Maintenance, Cleanliness, Library, Hostel, Administration, Other*).
- **Priority Levels:** Let students set priority (*Low, Medium, High*) so emergency problems (like power cuts or water leaks) get handled first.
- **Status Transparency:** Show clear status badges: *Submitted* &rarr; *In Progress* &rarr; *Resolved* so students know exactly what is happening.
- **Admin Management Dashboard:** Give administrators a clear view of total complaints, active issues, and resolved tasks with simple filters.

### 1.3 Problem Statement
Traditional manual complaint methods in educational institutions have serious disadvantages:
1. **Lost and Forgotten Complaints:** Complaints written on paper slips or registers often get misplaced or ignored with no proof of submission.
2. **No Status Updates:** Students have no idea whether someone is working on their issue or who is assigned to fix it.
3. **Wasted Time:** Students and staff spend unnecessary time making repeated personal visits to offices to check complaint status.
4. **No Priority Handling:** Important safety hazards (like short circuits or open wires) sit behind routine requests because there is no automated priority filtering.
5. **Lack of Records:** College heads have no simple way to see monthly maintenance statistics, staff response times, or recurring repair issues.

### 1.4 Proposed Solution
**Campus Care** provides a complete digital solution that handles complaints from start to finish:
- **Step 1 - Student Login:** The student logs in securely with their email and password. New students can register in 30 seconds.
- **Step 2 - Submitting Complaint:** The student enters a title, chooses the problem category, sets priority (Low/Medium/High), types the location (e.g., *Lab 3*), and writes a brief description.
- **Step 3 - Instant Ticket Creation:** The system instantly saves the complaint in the database, marks its status as **Submitted**, and generates a ticket number.
- **Step 4 - Admin Review & Action:** The college administrator checks the new complaint on the Admin Dashboard and changes its status to **In Progress** while maintenance staff works on it.
- **Step 5 - Resolution & Notes:** Once fixed, the admin marks it **Resolved** and adds remarks explaining what was done. The student sees the green checkmark and resolution note instantly on their screen.

---

## CHAPTER 2: SYSTEM DESIGN AND UML DIAGRAMS (Pages 3 - 9)

### 2.1 System Architecture
The system is divided into three simple, interconnected layers:
1. **Frontend Layer (ReactJS & Tailwind CSS):** Runs in the web browser on mobile and desktop. Includes Login, Register, Student Dashboard, Complaint Submission Form, Complaint List, and Admin Cockpit.
2. **Backend Layer (Node.js & Express.js):** Runs on the server. Receives requests from the browser, validates security tokens, processes complaints, and communicates with MongoDB.
3. **Database Layer (MongoDB & Mongoose):** Stores users and complaints safely with an unalterable history log of every status change.

### 2.2 System UML Diagrams
- **Figure 2.1 (Page 4): Use Case Diagram** – Shows Student and Admin interactions (Lodge grievance, review complaints, update status, view dashboard).
- **Figure 2.2 (Page 5): Data Flow Diagram (DFD)** – Demonstrates how complaint data flows from Student &rarr; Express Backend &rarr; MongoDB Storage &rarr; Admin Dashboard.
- **Figure 2.3 (Page 6): Class Diagram** – Outlines User, Student, Admin, Complaint, StatusHistory, and Controller object structures.
- **Figure 2.4 (Page 7): Activity Diagram** – Shows the end-to-end workflow from form filling and validation to resolution notes.
- **Figure 2.5 (Page 8): Sequence Diagram** – Details the asynchronous API calls and database updates over time.
- **Figure 2.6 (Page 9): Entity Relationship (ER) Diagram** – Maps the Users and Complaints collections with primary/foreign keys.

---

## CHAPTER 3: SYSTEM OVERVIEW AND TECHNOLOGIES (Pages 10 - 11)

### 3.1 Technologies Used
- **ReactJS (Frontend):** Modern JavaScript library for building fast Single Page Applications (SPA).
- **Tailwind CSS & Bootstrap:** Clean, responsive design that looks great on mobile phones, tablets, and laptops.
- **Node.js & Express.js (Backend):** High-performance server framework handling REST API endpoints.
- **MongoDB & Mongoose (Database):** Flexible NoSQL document database that securely stores users and ticket records.

### 3.2 Security and Core Features
- **Role-Based Access Control (RBAC):** Students can only submit and view their own tickets; admins can manage and resolve all complaints.
- **Password Security (Bcrypt):** Passwords are cryptographically salted and hashed before saving.
- **Secure Token Authentication (JWT):** Signed JSON Web Tokens protect all API requests.
- **Complete History Audit Trail:** Every status change is saved with the date, time, admin name, and remarks.
- **9 Supported Campus Categories:** Classroom, Laboratory, Internet / Wi-Fi, Electrical / Maintenance, Cleanliness, Library, Hostel, Administration, Other.

---

## CHAPTER 4: IMPLEMENTATION AND TESTING (Page 12)

### 4.1 Implementation Steps
1. Initialized the project with React (Vite) and Node.js (Express).
2. Modeled Mongoose schemas for Users and Complaints.
3. Built registration and login endpoints using Bcrypt and JWT.
4. Created complaint submission and status update endpoints.
5. Connected React frontend components using Axios.

### 4.2 System Testing
- **Unit Testing:** Verified form validation, ticket number generation, and password hashing.
- **Integration Testing:** Confirmed smooth data flow between React, Express, and MongoDB.
- **Security Testing:** Verified that students cannot access admin routes (returns *403 Forbidden*).

### 4.3 Results Achieved
- **Fast Speed:** Submitting a complaint takes under **150 milliseconds**.
- **Zero Lost Tickets:** 100% of complaints are safely stored and tracked.
- **Faster Fixes:** Technicians are alerted immediately, reducing turnaround time from days to hours.

---

## CHAPTER 5: CONCLUSION AND FUTURE SCOPE (Page 13)

### 5.1 Conclusion
The **Campus Care Complaint Management System** modernizes campus maintenance by replacing physical complaint books with a transparent, online portal. It saves time, guarantees that every complaint is tracked, and keeps both students and administrators informed at every step.

### 5.2 Key Achievements
- 100% paperless grievance handling.
- Real-time status updates (*Submitted &rarr; In Progress &rarr; Resolved*).
- Full accountability with timestamped history logs.
- Simple, mobile-friendly design.

### 5.3 Future Scope
- Photo upload feature to attach pictures of damaged campus items.
- SMS & WhatsApp alerts for instant resolution messages.
- AI categorization to automatically detect the issue department from text.
- Dedicated mobile app for Android and iOS using React Native.

---

## CHAPTER 6: SNAPSHOTS (Pages 14 - 15)
- **Figure 6.1 (Page 14):** Database Screenshots showing MongoDB Compass collections (`users` and `complaints`) and filter queries.
- **Figure 6.2 (Page 15):** Application UI Screenshots showing the Administrator Management Dashboard and Student Complaint Status Timeline.

---

## CHAPTER 7: REFERENCES (Page 16)
1. **React Documentation:** Official guide and component patterns – https://react.dev
2. **Node.js & Express Documentation:** Server architecture and routing – https://expressjs.com
3. **MongoDB Manual:** Document database and Mongoose schemas – https://www.mongodb.com/docs
4. **JSON Web Tokens (JWT):** RFC 7519 open standard for token authentication – https://jwt.io
5. **Tailwind CSS:** Modern utility CSS framework – https://tailwindcss.com
6. **Software Engineering:** Roger S. Pressman, *Software Engineering: A Practitioner's Approach*, McGraw-Hill.

*Supervised by **Mr. Deepesh Agarwal** (Guide) and **Dr. Sunita Varma** (HOD) in the Department of Computer Technology and Applications at **SGSITS Indore**.*

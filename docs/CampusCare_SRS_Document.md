# SHRI G.S .INSTITUTE OF TECHNOLOGY AND SCIENCE, INDORE (M.P)
### Department of Computer Technology and Applications
**MCA First Year Semester-I**  
**Session:** July 2025 – December 2025  
**Subject:** Software Engineering  

---

# Software Requirements Specification (SRS)
## Project: CampusCare – College Complaint Management System

**Submitted to:**  
- Ms. Priyanka Kabra  
- Ms. Shweta Gupta  

**Submitted by:**  
- Surbhi Lahri  
- Tanish Jain  
- Tanisha Mandhani  

---

## Table of Contents

- [1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 References](#13-references)
- [2. Overall Description](#2-overall-description)
  - [2.1 Product Functions](#21-product-functions)
- [3. Functional Requirements](#3-functional-requirements)
  - [3.1 User Account Management](#31-user-account-management)
  - [3.2 Product Browsing and Search](#32-product-browsing-and-search)
  - [3.3 Cart and Order Management](#33-cart-and-order-management)
  - [3.4 Payment and Checkout](#34-payment-and-checkout)
  - [3.5 Delivery and Tracking](#35-delivery-and-tracking)
  - [3.6 Customer Support](#36-customer-support)
  - [3.7 Admin and Vendor Functions](#37-admin-and-vendor-functions)
- [4. Non-Functional Requirements](#4-non-functional-requirements)
  - [4.1 Performance Requirements](#41-performance-requirements)
  - [4.2 Reliability and Availability](#42-reliability-and-availability)
  - [4.3 Security Requirements](#43-security-requirements)
  - [4.4 Usability Requirements](#44-usability-requirements)
  - [4.5 Scalability Requirements](#45-scalability-requirements)
  - [4.6 Maintainability Requirements](#46-maintainability-requirements)
  - [4.7 Compatibility Requirements](#47-compatibility-requirements)
- [5. Accuracy](#5-accuracy)
  - [1. Product Search Accuracy](#1-product-search-accuracy)
  - [2. Order Accuracy](#2-order-accuracy)
  - [3. Inventory Accuracy](#3-inventory-accuracy)
  - [4. Location Accuracy](#4-location-accuracy)
  - [5. Transaction Accuracy](#5-transaction-accuracy)
- [6. Conclusion](#6-conclusion)

---

## 1. Introduction

### 1.1 Purpose
This Software Requirement Specification (SRS) document specifies the requirements for the **CampusCare College Complaint Management System (Version 1.0)**. The purpose of this document is to define the complete set of software requirements for the CampusCare platform, ensuring that all stakeholders have a clear and common understanding of its objectives, scope, and functionalities.

The scope of this SRS is limited to the software system supporting CampusCare’s core operations, including:
- **Customer/Student-facing web application** for browsing categories, lodging complaints, searching, and tracking college infrastructure, laboratory, academic, and hostel grievances.
- **Admin module** for managing complaint status, investigating issues, assigning priority, and reviewing institutional resolution reports.
- **Maintenance and staff workflow** for accepting grievance requests, location identification, and on-ground issue fulfillment.
- **Backend services** including user authentication, ticket number generation, search filters, state transitions, and database persistence.

### 1.2 Product Scope
The CampusCare College Complaint Management System is a **software system designed to enable college students to lodge, manage, and resolve campus-related complaints online and track them in real time**. The primary purpose of this product is to provide a fast, reliable, and convenient grievance redressal experience while strengthening the connection between students, maintenance departments, faculty, and college administration.

#### Objectives and Goals
- To provide a **user-friendly platform** where students can browse categories, search issues, and lodge complaints with ease.
- To enable **real-time complaint tracking** for administrators, ensuring accurate status updates and timely service delivery.
- To support maintenance teams with optimized location markers, status updates, and resolution performance tracking.
- To ensure secure, authenticated, and role-separated access across both student and administrator interfaces.
- To maintain a scalable and reliable cloud database backend capable of handling high query volume throughout academic semesters.

#### Relevant Benefits
- **Students** benefit from time savings and the convenience of tracking complaint redressal digitally without paper registers.
- **Campus departments** gain access to a centralized portal, improving accountability, visibility, and resolution speed.
- **Administrative staff** benefit from structured grievance logging, priority indicators, and measurable resolution metrics.
- **The institution** benefits by strengthening its governance strategy of prompt service delivery, which aligns with modern educational demand for transparency, convenience, and trust.

#### Relation to Institutional Strategy
The software directly supports the college’s institutional strategy of being a progressive, digitally empowered smart campus. By focusing on fast redressal, student satisfaction, and administrative responsiveness, the CampusCare application contributes to:
- Building student confidence and institutional satisfaction.
- Streamlining resource allocation across electrical, Wi-Fi, lab, and cleanliness facilities.
- Driving long-term institutional excellence and compliance with educational accreditation bodies (e.g., NAAC, NBA, and NIRF).

### 1.3 References
1. IEEE Std 830-1998 – IEEE Recommended Practice for Software Requirements Specifications.
2. CampusCare Official Repository & Documentation – [https://github.com/tanishjain0502/CampusCare](https://github.com/tanishjain0502/CampusCare).
3. Agile Manifesto – Beck, K. et al., 2001.
4. MERN Stack Software Architecture – Node.js, Express, React, MongoDB Reference, 2024.
5. Nielsen Norman Group – Usability Heuristics for User Interface Design, 2020.

---

## 2. Overall Description

### 2.1 Product Functions

#### 1. User Account Management
The application allows users to create and manage their accounts through secure registration and login features. Students can sign up with their institutional email, full name, and password. The system enforces role-based access control, automatically designating public registrations as STUDENT accounts, while ADMIN roles are securely initialized server-side. Secure authentication via JSON Web Tokens (JWT) ensures data protection.

#### 2. Product Browsing and Search
CampusCare provides users with the ability to browse campus grievance categories including Classroom, Laboratory, Internet / Wi-Fi, Electrical / Maintenance, Cleanliness, Library, Hostel, Administration, and Other. An advanced search bar with multi-parameter filters such as status, category, and priority ensures that students and administrators can quickly locate and track grievances of their choice.

#### 3. Cart and Order Management
Students can draft, review, and lodge complaints through an intuitive submission interface. Each submission incorporates priority setting (LOW, MEDIUM, HIGH), detailed descriptions, and physical location tags. The system enables order tracking, status monitoring, and auto-generates permanent cryptographic ticket numbers (`CC-YYYYMMDD-XXXXXX`) for every complaint.

#### 4. Payment and Checkout
In CampusCare, this verification workflow handles request submission validation and audit confirmation. A secure and streamlined submission process verifies input lengths, prevents accidental double-submissions, and guarantees that complaint payloads cannot tamper with server-side creator IDs or status assignments. The software ensures encrypted transactions between client and server for error-free confirmation.

#### 5. Delivery Management
Once a complaint is lodged, the system assigns initial status (`SUBMITTED`) and provides students with real-time tracking of their grievance. Status transitions to `IN_PROGRESS` and `RESOLVED` keep users informed throughout the redressal lifecycle, ensuring transparent and timely resolution.

#### 6. Customer Support
CampusCare integrates dedicated student support mechanisms directly within the platform. Students can inspect full complaint timelines, view administrative resolution remarks, and verify completion details. Clear empty states, status badges, and descriptive feedback ensure that users can quickly resolve queries regarding their lodged tickets without needing to physically visit administrative offices.

#### 7. Administrative and Backend Functions
The backend system provides comprehensive tools for college administrators and maintenance supervisors to monitor grievances, review departmental trends, and oversee resolution workflows. Additionally, it includes executive dashboards for complaint statistics tracking (Total, Submitted, In-Progress, Resolved), student management, and resolution audit reports, supporting data-driven institutional decision making.

---

## 3. Functional Requirements

Functional requirements describe what the system should do. For CampusCare, these include:

### 3.1 User Account Management
- The system shall allow new users to register via name, valid institutional email, and secure password.
- The system shall provide secure login/logout functionality with JWT authentication and bcrypt password encryption.
- The system shall enforce role segregation, ensuring public registrations cannot provision ADMIN accounts.

### 3.2 Product Browsing and Search
- The system shall allow users to browse grievances across predefined campus categories such as Classroom, Laboratory, Internet / Wi-Fi, Electrical, Cleanliness, Library, and Hostel.
- The system shall provide search functionality with filters like ticket number, category, status, priority, and date sorting.
- The system shall allow users to view detailed complaint descriptions, locations, status timelines, and resolution remarks.

### 3.3 Cart and Order Management
- The system shall allow students to compose, review, and lodge complaints through a validated submission form.
- The system shall automatically generate a unique ticket number (`CC-YYYYMMDD-XXXXXX`) upon submission.
- The system shall maintain a dedicated "My Complaints" repository strictly scoped to the authenticated student.
- The system shall display the submission timestamp and last updated date for every lodged complaint.

### 3.4 Payment and Checkout
- The system shall validate all submitted payloads against schema bounds (title 5–100 chars, description 20–2000 chars).
- The system shall disable submission controls during network requests to prevent duplicate ticket generation.
- The system shall encrypt all communication between client and backend over TLS/HTTPS to ensure data integrity.
- The system shall generate confirmation acknowledgments with ticket receipts immediately upon successful database insertion.

### 3.5 Delivery and Tracking
- The system shall assign grievances to relevant campus categories automatically based on student selection.
- The system shall provide real-time grievance tracking with live status indicators (`SUBMITTED`, `IN_PROGRESS`, `RESOLVED`).
- The system shall notify students of status updates and display administrative resolution remarks on the complaint detail page.

### 3.6 Customer Support
- The system shall provide an in-app help interface with clear status badge legends and workflow explanations.
- The system shall allow students to track grievance progress and review specific resolution comments provided by administrators.
- The system shall maintain permanent ticket histories until the issue is fully addressed and closed.

### 3.7 Admin and Vendor Functions
- The system shall allow administrators to view, filter, and search across all student complaints.
- The system shall allow administrators to update grievance status to `IN_PROGRESS` or `RESOLVED`, requiring mandatory resolution remarks (minimum 5 characters) on closure.
- The system shall generate real-time metrics on total complaints, pending reviews, active investigations, and resolved issues.

---

## 4. Non-Functional Requirements

Non-functional requirements describe how the system should perform rather than what it should do.

### 4.1 Performance Requirements
- The system should be able to handle at least **10,000 active students and staff users** without performance degradation.
- The application should load the homepage within **2 seconds** under normal campus network conditions.
- Complaint submission and dashboard metric calculations should be completed within **1 second**.

### 4.2 Reliability and Availability
- The system should ensure **99.9% uptime** to support 24/7 service throughout academic semesters.
- In case of system failure, recovery time should not exceed **30 seconds** via cloud process managers.
- Data backup must occur at least **every 24 hours** via automated MongoDB Atlas snapshots.

### 4.3 Security Requirements
- All user data (credentials and grievance details) must be encrypted in transit using **TLS 1.3 / HTTPS**.
- Passwords must be securely hashed using **bcrypt with 10–12 salt rounds** before database persistence.
- Horizontal data isolation must prevent students from viewing or accessing other students' grievances.

### 4.4 Usability Requirements
- The app must provide a simple and intuitive interface for students, faculty, and administrative staff.
- All major features (submitting a complaint, checking status) should be accessible within **2 clicks from the dashboard**.
- The app should provide clear visual feedback, including status badges, loading indicators, and informative error messages.

### 4.5 Scalability Requirements
- The system must scale horizontally to handle peak loads, such as semester exam periods or campus-wide maintenance drives.
- Cloud-based deployment on Render, Vercel, and MongoDB Atlas should allow automatic resource scaling.

### 4.6 Maintainability Requirements
- The system architecture must be modular (MERN stack separation of client, routes, controllers, middleware, and models) to allow easy updates and bug fixes.
- The codebase should follow standard documentation practices and maintain automated test suites (`npm run test:part4`) for maintainability.

### 4.7 Compatibility Requirements
- The system must be compatible with major mobile operating systems (**Android 9.0+** and **iOS 13+**).
- The web version must support popular modern browsers (**Chrome, Edge, Safari, Firefox**).

---

## 5. Accuracy

### 1. Product Search Accuracy
The system must return relevant complaints based on user input (e.g., searching "Lab 3" or ticket number "CC-20261017-481AAA" should display the exact matching complaints without irrelevant records).  
Accuracy can be measured as the percentage of correct search results vs. irrelevant results.

### 2. Order Accuracy
The registered complaint details must exactly match the data submitted by the student (category, priority, description, location).  
**Requirement:** 100% complaint registration and ticket number assignment accuracy.

### 3. Inventory Accuracy
Complaint status counts shown in the administrator and student dashboards must match the actual database records across all categories.  
**Requirement:** Dashboard metrics data should be updated in real-time with 100% accuracy.

### 4. Location Accuracy
The campus location identified through entered details (classroom number, laboratory, hostel wing) must accurately guide maintenance staff to the exact physical issue site.  
**Requirement:** Maintenance personnel should reach the correct location with ≥ 98% accuracy.

### 5. Transaction Accuracy
Status transitions, resolution timestamps, and administrative remarks must be recorded correctly without data corruption or unauthorized modifications.  
**Requirement:** 100% accuracy in audit logging and status history preservation.

---

## 6. Conclusion

The CampusCare application SRS defines the functional and non-functional requirements needed to design, develop, and operate an efficient college complaint management platform. This document has outlined the objectives, scope, system features, user requirements, performance metrics, and constraints of the system.

By ensuring high levels of accuracy in complaint search, categorization, real-time metrics, status transitions, and audit tracking, the system aims to provide students and campus authorities with a fast, reliable, and user-friendly grievance redressal experience. Additionally, non-functional requirements such as security, scalability, and usability have been clearly identified to support long-term growth and maintain student and administrator trust.

This SRS will serve as the foundation for the development team, testers, and stakeholders, ensuring that all parties have a clear understanding of the system’s goals and expectations. Once implemented, the CampusCare system will enable seamless campus grievance redressal, maintaining consistency, reliability, and institutional satisfaction.

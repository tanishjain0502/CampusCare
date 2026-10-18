import os
import subprocess

with open('docs/logo_b64.txt', 'r') as f:
    logo_b64 = f.read().strip()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Software Requirements Specification - CampusCare</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  body {{
    margin: 0;
    padding: 0;
    background-color: #e0e0e0;
    font-family: "Times New Roman", Times, serif;
    color: #000;
  }}
  .page {{
    width: 210mm;
    height: 297mm;
    margin: 0 auto;
    padding: 10mm 14mm;
    background: #fff;
    page-break-after: always;
    page-break-inside: avoid;
    position: relative;
    display: flex;
    flex-direction: column;
  }}
  .border-box {{
    width: 100%;
    height: 100%;
    border: 3.5px double #000;
    padding: 22px 30px 16px 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
  }}
  .page-num {{
    text-align: center;
    font-size: 11pt;
    font-family: "Times New Roman", Times, serif;
    margin-top: 8px;
  }}
  h1.doc-title {{
    font-size: 17pt;
    font-weight: bold;
    text-align: center;
    text-decoration: underline;
    margin-top: 5px;
    margin-bottom: 20px;
    letter-spacing: 0.5px;
  }}
  h2.section-heading {{
    font-size: 15pt;
    font-weight: bold;
    text-decoration: underline;
    margin-top: 0;
    margin-bottom: 14px;
    text-align: center;
  }}
  h3.sub-heading {{
    font-size: 13pt;
    font-weight: bold;
    margin-top: 8px;
    margin-bottom: 5px;
  }}
  h4.item-heading {{
    font-size: 11.5pt;
    font-weight: bold;
    margin-top: 7px;
    margin-bottom: 3px;
  }}
  p {{
    font-size: 11pt;
    line-height: 1.40;
    margin-top: 0;
    margin-bottom: 7px;
    text-align: justify;
  }}
  ul {{
    margin-top: 2px;
    margin-bottom: 7px;
    padding-left: 20px;
  }}
  li {{
    font-size: 11pt;
    line-height: 1.36;
    margin-bottom: 5px;
    text-align: justify;
  }}
  .toc-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 11pt;
    margin-top: 2px;
  }}
  .toc-table td {{
    padding: 3px 0;
    vertical-align: bottom;
  }}
  .toc-table .title {{
    font-weight: bold;
    font-size: 11.5pt;
  }}
  .toc-table .sub {{
    padding-left: 20px;
    font-size: 10.5pt;
  }}
  .toc-dots {{
    border-bottom: 1px dotted #000;
    height: 14px;
  }}
  .toc-page {{
    text-align: right;
    width: 25px;
    font-weight: normal;
  }}
  .cover-inst-header {{
    text-align: center;
    font-size: 14pt;
    font-weight: bold;
    letter-spacing: 0.5px;
    line-height: 1.35;
    margin-top: 15px;
  }}
  .cover-logo-container {{
    text-align: center;
    margin: 25px 0 20px 0;
  }}
  .cover-logo {{
    width: 155px;
    height: auto;
  }}
  .cover-dept-info {{
    text-align: center;
    font-size: 13pt;
    font-weight: 500;
    line-height: 1.35;
    margin-bottom: 22px;
  }}
  .cover-subject {{
    text-align: center;
    font-size: 13pt;
    font-weight: bold;
    margin-bottom: 20px;
  }}
  .cover-doc-type {{
    text-align: center;
    font-size: 14pt;
    font-weight: bold;
    margin-bottom: 12px;
  }}
  .cover-project-title {{
    text-align: center;
    font-size: 13.5pt;
    font-weight: bold;
    margin-bottom: 45px;
  }}
  .cover-submission-table {{
    width: 100%;
    font-size: 12pt;
    margin-top: auto;
    margin-bottom: 15px;
  }}
  .cover-submission-table td {{
    vertical-align: top;
    line-height: 1.35;
  }}
</style>
</head>
<body>

<!-- PAGE 1: TITLE / COVER PAGE -->
<div class="page">
  <div class="border-box">
    <div>
      <div class="cover-inst-header">
        SHRI G.S .INSTITUTE OF TECHNOLOGY AND SCIENCE<br>
        INDORE (M.P)
      </div>

      <div class="cover-logo-container">
        <img class="cover-logo" src="data:image/jpeg;base64,{logo_b64}" alt="SGSITS Logo">
      </div>

      <div class="cover-dept-info">
        Department of Computer Technology and Applications<br>
        MCA First Year Semester-I<br>
        Session:- July 2025 – December 2025
      </div>

      <div class="cover-subject">
        Subject:- Software Engineering
      </div>

      <div class="cover-doc-type">
        Software Requirements Specification
      </div>

      <div class="cover-project-title">
        Project:- CampusCare – College Complaint Management System
      </div>
    </div>

    <div>
      <table class="cover-submission-table">
        <tr>
          <td style="width: 50%; padding-left: 10px;">
            <strong>Submitted to:</strong><br>
            Ms. Priyanka Kabra<br>
            Ms. Shweta Gupta
          </td>
          <td style="width: 50%; padding-left: 30px;">
            <strong>Submitted by:</strong><br>
            Surbhi Lahri<br>
            Tanish Jain<br>
            Tanisha Mandhani
          </td>
        </tr>
      </table>
      <div class="page-num">1</div>
    </div>
  </div>
</div>

<!-- PAGE 2: TABLE OF CONTENTS -->
<div class="page">
  <div class="border-box">
    <div>
      <h1 class="doc-title">Table of Contents</h1>
      <table class="toc-table">
        <tr>
          <td colspan="2" class="title">1. Introduction</td>
          <td class="toc-dots"></td>
          <td class="toc-page"><strong>3</strong></td>
        </tr>
        <tr>
          <td style="width: 20px;"></td>
          <td class="sub">1.1 Purpose</td>
          <td class="toc-dots"></td>
          <td class="toc-page">3</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">1.2 Product Scope</td>
          <td class="toc-dots"></td>
          <td class="toc-page">3</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">1.3 References</td>
          <td class="toc-dots"></td>
          <td class="toc-page">4</td>
        </tr>
        <tr><td style="height: 5px;"></td></tr>
        <tr>
          <td colspan="2" class="title">2. Overall Description</td>
          <td class="toc-dots"></td>
          <td class="toc-page"><strong>5</strong></td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">2.1 Product Functions</td>
          <td class="toc-dots"></td>
          <td class="toc-page">5</td>
        </tr>
        <tr><td style="height: 5px;"></td></tr>
        <tr>
          <td colspan="2" class="title">3. Functional Requirements</td>
          <td class="toc-dots"></td>
          <td class="toc-page"><strong>7</strong></td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.1 User Account Management</td>
          <td class="toc-dots"></td>
          <td class="toc-page">7</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.2 Product Browsing and Search</td>
          <td class="toc-dots"></td>
          <td class="toc-page">7</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.3 Cart and Order Management</td>
          <td class="toc-dots"></td>
          <td class="toc-page">7</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.4 Payment and Checkout</td>
          <td class="toc-dots"></td>
          <td class="toc-page">7</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.5 Delivery and Tracking</td>
          <td class="toc-dots"></td>
          <td class="toc-page">8</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.6 Customer Support</td>
          <td class="toc-dots"></td>
          <td class="toc-page">8</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.7 Admin and Vendor Functions</td>
          <td class="toc-dots"></td>
          <td class="toc-page">8</td>
        </tr>
        <tr><td style="height: 5px;"></td></tr>
        <tr>
          <td colspan="2" class="title">4. Non-Functional Requirements</td>
          <td class="toc-dots"></td>
          <td class="toc-page"><strong>9</strong></td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">4.1 Performance Requirements</td>
          <td class="toc-dots"></td>
          <td class="toc-page">9</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">4.2 Reliability and Availability</td>
          <td class="toc-dots"></td>
          <td class="toc-page">9</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">4.3 Security Requirements</td>
          <td class="toc-dots"></td>
          <td class="toc-page">9</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">4.4 Usability Requirements</td>
          <td class="toc-dots"></td>
          <td class="toc-page">9</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">4.5 Scalability Requirements</td>
          <td class="toc-dots"></td>
          <td class="toc-page">9</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">4.6 Maintainability Requirements</td>
          <td class="toc-dots"></td>
          <td class="toc-page">10</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">4.7 Compatibility Requirements</td>
          <td class="toc-dots"></td>
          <td class="toc-page">10</td>
        </tr>
        <tr><td style="height: 5px;"></td></tr>
        <tr>
          <td colspan="2" class="title">5. Accuracy</td>
          <td class="toc-dots"></td>
          <td class="toc-page"><strong>11</strong></td>
        </tr>
        <tr><td style="height: 5px;"></td></tr>
        <tr>
          <td colspan="2" class="title">6. Conclusion</td>
          <td class="toc-dots"></td>
          <td class="toc-page"><strong>12</strong></td>
        </tr>
      </table>
    </div>
    <div class="page-num">2</div>
  </div>
</div>

<!-- PAGE 3: 1. INTRODUCTION -->
<div class="page">
  <div class="border-box">
    <div>
      <h2 class="section-heading">1. Introduction</h2>

      <h3 class="sub-heading">1.1 Purpose</h3>
      <p>
        This Software Requirement Specification (SRS) document specifies the requirements
        for the <strong>CampusCare College Complaint Management System (Version 1.0)</strong>. The purpose of this
        document is to define the complete set of software requirements for the CampusCare platform,
        ensuring that all stakeholders have a clear and common understanding of its objectives,
        scope, and functionalities.
      </p>
      <p>
        The scope of this SRS is limited to the software system supporting CampusCare’s core
        operations, including:
      </p>
      <ul>
        <li><strong>Student-facing web application</strong> for browsing categories, lodging complaints, searching, and tracking college infrastructure, laboratory, academic, and hostel grievances.</li>
        <li><strong>Admin module</strong> for managing complaint status, investigating issues, assigning priority, and reviewing institutional resolution reports.</li>
        <li><strong>Maintenance and staff workflow</strong> for accepting grievance requests, location identification, and on-ground issue fulfillment.</li>
        <li><strong>Backend cloud services</strong> including user authentication, ticket number generation, search filters, state transitions, and database persistence.</li>
      </ul>

      <h3 class="sub-heading">1.2 Product Scope</h3>
      <p>
        The CampusCare College Complaint Management System is a <strong>software system designed to
        enable college students to lodge, manage, and resolve campus-related complaints
        online and track them in real time</strong>. The primary purpose of this product is to
        provide a fast, reliable, and convenient grievance redressal experience while strengthening the
        connection between students, maintenance departments, faculty, and college administration.
      </p>
      <h4 class="item-heading">Objectives and Goals</h4>
      <ul>
        <li>To provide a <strong>user-friendly platform</strong> where students can browse categories, search issues, and lodge complaints with ease.</li>
        <li>To enable <strong>real-time complaint tracking</strong> for administrators, ensuring accurate status updates and timely service delivery.</li>
      </ul>
    </div>
    <div class="page-num">3</div>
  </div>
</div>

<!-- PAGE 4: 1.2 SCOPE (CONT.) & 1.3 REFERENCES -->
<div class="page">
  <div class="border-box">
    <div>
      <ul>
        <li>To support maintenance teams with optimized location markers, status updates, and resolution performance tracking.</li>
        <li>To ensure secure, authenticated, and role-separated access across both student and administrator interfaces.</li>
        <li>To maintain a scalable and reliable cloud database backend capable of handling high query volume throughout academic semesters.</li>
      </ul>

      <h4 class="item-heading">Relevant Benefits</h4>
      <ul>
        <li><strong>Students</strong> benefit from time savings and the convenience of tracking complaint redressal digitally without paper registers.</li>
        <li><strong>Campus departments</strong> gain access to a centralized portal, improving accountability, visibility, and resolution speed.</li>
        <li><strong>Administrative staff</strong> benefit from structured grievance logging, priority indicators, and measurable resolution metrics.</li>
        <li><strong>The institution</strong> benefits by strengthening its governance strategy of prompt service delivery, which aligns with modern educational demand for transparency, convenience, and trust.</li>
      </ul>

      <h4 class="item-heading">Relation to Institutional Strategy</h4>
      <p>
        The software directly supports the college’s institutional strategy of being a progressive,
        digitally empowered smart campus. By focusing on fast redressal, student satisfaction, and
        administrative responsiveness, the CampusCare application contributes to:
      </p>
      <ul>
        <li>Building student confidence and institutional satisfaction.</li>
        <li>Streamlining resource allocation across electrical, Wi-Fi, lab, and cleanliness facilities.</li>
        <li>Driving long-term institutional excellence and compliance with educational accreditation bodies (e.g., NAAC, NBA, and NIRF).</li>
      </ul>

      <h3 class="sub-heading">1.3 References</h3>
      <ol style="margin-top: 4px; padding-left: 20px; font-size: 11pt; line-height: 1.45;">
        <li>IEEE Std 830-1998 – IEEE Recommended Practice for Software Requirements Specifications.</li>
        <li>CampusCare Official Repository & Documentation – https://github.com/tanishjain0502/CampusCare.</li>
        <li>Agile Manifesto – Beck, K. et al., 2001.</li>
        <li>MERN Stack Software Architecture – Node.js, Express, React, MongoDB Reference, 2024.</li>
        <li>Nielsen Norman Group – Usability Heuristics for User Interface Design, 2020.</li>
      </ol>
    </div>
    <div class="page-num">4</div>
  </div>
</div>

<!-- PAGE 5: 2. OVERALL DESCRIPTION -->
<div class="page">
  <div class="border-box">
    <div>
      <h2 class="section-heading">2. Overall Description</h2>

      <h3 class="sub-heading">2.1 Product Functions</h3>

      <h4 class="item-heading">1. User Account Management</h4>
      <p>
        The application allows users to create and manage their accounts through secure registration
        and login features. Students can sign up with their institutional email, full name, and password.
        The system enforces role-based access control, automatically designating public registrations as STUDENT
        accounts, while ADMIN roles are securely initialized server-side. Secure authentication via JSON Web
        Tokens (JWT) ensures data protection.
      </p>

      <h4 class="item-heading">2. Product Browsing and Search</h4>
      <p>
        CampusCare provides users with the ability to browse campus grievance categories including Classroom,
        Laboratory, Internet / Wi-Fi, Electrical / Maintenance, Cleanliness, Library, Hostel, Administration,
        and Other. An advanced search bar with multi-parameter filters such as status, category, and priority
        ensures that students and administrators can quickly locate and track grievances of their choice.
      </p>

      <h4 class="item-heading">3. Cart and Order Management</h4>
      <p>
        Students can draft, review, and lodge complaints through an intuitive submission interface.
        Each submission incorporates priority setting (LOW, MEDIUM, HIGH), detailed descriptions, and physical
        location tags. The system enables order tracking, status monitoring, and auto-generates permanent
        cryptographic ticket numbers (<code>CC-YYYYMMDD-XXXXXX</code>) for every complaint.
      </p>

      <h4 class="item-heading">4. Payment and Checkout</h4>
      <p>
        In CampusCare, this verification workflow handles request submission validation and audit confirmation.
        A secure and streamlined submission process verifies input lengths, prevents accidental double-submissions,
        and guarantees that complaint payloads cannot tamper with server-side creator IDs or status assignments.
        The software ensures encrypted transactions between client and server for error-free confirmation.
      </p>

      <h4 class="item-heading">5. Delivery Management</h4>
      <p>
        Once a complaint is lodged, the system assigns initial status (SUBMITTED) and provides students with
        real-time tracking of their grievance. Status transitions to IN_PROGRESS and RESOLVED keep users
        informed throughout the redressal lifecycle, ensuring transparent and timely resolution.
      </p>
    </div>
    <div class="page-num">5</div>
  </div>
</div>

<!-- PAGE 6: 2. OVERALL DESCRIPTION (CONT.) -->
<div class="page">
  <div class="border-box">
    <div>
      <h4 class="item-heading">6. Customer Support</h4>
      <p>
        CampusCare integrates dedicated student support mechanisms directly within the platform.
        Students can inspect full complaint timelines, view administrative resolution remarks, and
        verify completion details. Clear empty states, status badges, and descriptive feedback ensure that
        users can quickly resolve queries regarding their lodged tickets without needing to physically visit administrative offices.
      </p>

      <h4 class="item-heading">7. Administrative and Backend Functions</h4>
      <p>
        The backend system provides comprehensive tools for college administrators and maintenance supervisors
        to monitor grievances, review departmental trends, and oversee resolution workflows. Additionally,
        it includes executive dashboards for complaint statistics tracking (Total, Submitted, In-Progress,
        Resolved), student management, and resolution audit reports, supporting data-driven institutional decision making.
      </p>
    </div>
    <div class="page-num">6</div>
  </div>
</div>

<!-- PAGE 7: 3. FUNCTIONAL REQUIREMENTS -->
<div class="page">
  <div class="border-box">
    <div>
      <h2 class="section-heading">3. Functional Requirements</h2>
      <p>
        Functional requirements describe what the system should do. For CampusCare, these include:
      </p>

      <h3 class="sub-heading">3.1 User Account Management</h3>
      <ul>
        <li>The system shall allow new users to register via name, valid institutional email, and secure password.</li>
        <li>The system shall provide secure login/logout functionality with JWT authentication and bcrypt password encryption.</li>
        <li>The system shall enforce role segregation, ensuring public registrations cannot provision ADMIN accounts.</li>
      </ul>

      <h3 class="sub-heading">3.2 Product Browsing and Search</h3>
      <ul>
        <li>The system shall allow users to browse grievances across predefined campus categories such as Classroom, Laboratory, Internet / Wi-Fi, Electrical, Cleanliness, Library, and Hostel.</li>
        <li>The system shall provide search functionality with filters like ticket number, category, status, priority, and date sorting.</li>
        <li>The system shall allow users to view detailed complaint descriptions, locations, status timelines, and resolution remarks.</li>
      </ul>

      <h3 class="sub-heading">3.3 Cart and Order Management</h3>
      <ul>
        <li>The system shall allow students to compose, review, and lodge complaints through a validated submission form.</li>
        <li>The system shall automatically generate a unique ticket number (<code>CC-YYYYMMDD-XXXXXX</code>) upon submission.</li>
        <li>The system shall maintain a dedicated "My Complaints" repository strictly scoped to the authenticated student.</li>
        <li>The system shall display the submission timestamp and last updated date for every lodged complaint.</li>
      </ul>

      <h3 class="sub-heading">3.4 Payment and Checkout</h3>
      <ul>
        <li>The system shall validate all submitted payloads against schema bounds (title 5–100 chars, description 20–2000 chars).</li>
        <li>The system shall disable submission controls during network requests to prevent duplicate ticket generation.</li>
        <li>The system shall encrypt all communication between client and backend over TLS/HTTPS to ensure data integrity.</li>
      </ul>
    </div>
    <div class="page-num">7</div>
  </div>
</div>

<!-- PAGE 8: 3. FUNCTIONAL REQUIREMENTS (CONT.) -->
<div class="page">
  <div class="border-box">
    <div>
      <ul>
        <li>The system shall generate confirmation acknowledgments with ticket receipts immediately upon successful database insertion.</li>
      </ul>

      <h3 class="sub-heading">3.5 Delivery and Tracking</h3>
      <ul>
        <li>The system shall assign grievances to relevant campus categories automatically based on student selection.</li>
        <li>The system shall provide real-time grievance tracking with live status indicators (SUBMITTED, IN_PROGRESS, RESOLVED).</li>
        <li>The system shall notify students of status updates and display administrative resolution remarks on the complaint detail page.</li>
      </ul>

      <h3 class="sub-heading">3.6 Customer Support</h3>
      <ul>
        <li>The system shall provide an in-app help interface with clear status badge legends and workflow explanations.</li>
        <li>The system shall allow students to track grievance progress and review specific resolution comments provided by administrators.</li>
        <li>The system shall maintain permanent ticket histories until the issue is fully addressed and closed.</li>
      </ul>

      <h3 class="sub-heading">3.7 Admin and Vendor Functions</h3>
      <ul>
        <li>The system shall allow administrators to view, filter, and search across all student complaints.</li>
        <li>The system shall allow administrators to update grievance status to IN_PROGRESS or RESOLVED, requiring mandatory resolution remarks (minimum 5 characters) on closure.</li>
        <li>The system shall generate real-time metrics on total complaints, pending reviews, active investigations, and resolved issues.</li>
      </ul>
    </div>
    <div class="page-num">8</div>
  </div>
</div>

<!-- PAGE 9: 4. NON-FUNCTIONAL REQUIREMENTS -->
<div class="page">
  <div class="border-box">
    <div>
      <h2 class="section-heading">4. Non-Functional Requirements</h2>
      <p>
        Non-functional requirements describe how the system should perform rather than what it should do.
      </p>

      <h3 class="sub-heading">4.1 Performance Requirements</h3>
      <ul>
        <li>The system should be able to handle at least <strong>10,000 active students and staff users</strong> without performance degradation.</li>
        <li>The application should load the homepage within <strong>2 seconds</strong> under normal campus network conditions.</li>
        <li>Complaint submission and dashboard metric calculations should be completed within <strong>1 second</strong>.</li>
      </ul>

      <h3 class="sub-heading">4.2 Reliability and Availability</h3>
      <ul>
        <li>The system should ensure <strong>99.9% uptime</strong> to support 24/7 service throughout academic semesters.</li>
        <li>In case of system failure, recovery time should not exceed <strong>30 seconds</strong> via cloud process managers.</li>
        <li>Data backup must occur at least <strong>every 24 hours</strong> via automated MongoDB Atlas snapshots.</li>
      </ul>

      <h3 class="sub-heading">4.3 Security Requirements</h3>
      <ul>
        <li>All user data (credentials and grievance details) must be encrypted in transit using <strong>TLS 1.3 / HTTPS</strong>.</li>
        <li>Passwords must be securely hashed using <strong>bcrypt with 10–12 salt rounds</strong> before database persistence.</li>
        <li>Horizontal data isolation must prevent students from viewing or accessing other students' grievances.</li>
      </ul>

      <h3 class="sub-heading">4.4 Usability Requirements</h3>
      <ul>
        <li>The app must provide a simple and intuitive interface for students, faculty, and administrative staff.</li>
        <li>All major features (submitting a complaint, checking status) should be accessible within <strong>2 clicks from the dashboard</strong>.</li>
        <li>The app should provide clear visual feedback, including status badges, loading indicators, and informative error messages.</li>
      </ul>

      <h3 class="sub-heading">4.5 Scalability Requirements</h3>
      <ul>
        <li>The system must scale horizontally to handle peak loads, such as semester exam periods or campus-wide maintenance drives.</li>
        <li>Cloud-based deployment on Render, Vercel, and MongoDB Atlas should allow automatic resource scaling.</li>
      </ul>
    </div>
    <div class="page-num">9</div>
  </div>
</div>

<!-- PAGE 10: 4. NON-FUNCTIONAL REQUIREMENTS (CONT.) -->
<div class="page">
  <div class="border-box">
    <div>
      <h3 class="sub-heading">4.6 Maintainability Requirements</h3>
      <ul>
        <li>The system architecture must be modular (MERN stack separation of client, routes, controllers, middleware, and models) to allow easy updates and bug fixes.</li>
        <li>The codebase should follow standard documentation practices and maintain automated test suites (<code>npm run test:part4</code>) for maintainability.</li>
      </ul>

      <h3 class="sub-heading">4.7 Compatibility Requirements</h3>
      <ul>
        <li>The system must be compatible with major mobile operating systems (<strong>Android 9.0+</strong> and <strong>iOS 13+</strong>).</li>
        <li>The web version must support popular modern browsers (<strong>Chrome, Edge, Safari, Firefox</strong>).</li>
      </ul>
    </div>
    <div class="page-num">10</div>
  </div>
</div>

<!-- PAGE 11: 5. ACCURACY -->
<div class="page">
  <div class="border-box">
    <div>
      <h2 class="section-heading">5. Accuracy</h2>

      <h4 class="item-heading">1. Product Search Accuracy</h4>
      <p>
        The system must return relevant complaints based on user input (e.g., searching "Lab 3" or ticket number "CC-20261017-481AAA" should display the exact matching complaints without irrelevant records).<br>
        Accuracy can be measured as the percentage of correct search results vs. irrelevant results.
      </p>

      <h4 class="item-heading">2. Order Accuracy</h4>
      <p>
        The registered complaint details must exactly match the data submitted by the student (category, priority, description, location).<br>
        <strong>Requirement:</strong> 100% complaint registration and ticket number assignment accuracy.
      </p>

      <h4 class="item-heading">3. Inventory Accuracy</h4>
      <p>
        Complaint status counts shown in the administrator and student dashboards must match the actual database records across all categories.<br>
        <strong>Requirement:</strong> Dashboard metrics data should be updated in real-time with 100% accuracy.
      </p>

      <h4 class="item-heading">4. Location Accuracy</h4>
      <p>
        The campus location identified through entered details (classroom number, laboratory, hostel wing) must accurately guide maintenance staff to the exact physical issue site.<br>
        <strong>Requirement:</strong> Maintenance personnel should reach the correct location with ≥ 98% accuracy.
      </p>

      <h4 class="item-heading">5. Transaction Accuracy</h4>
      <p>
        Status transitions, resolution timestamps, and administrative remarks must be recorded correctly without data corruption or unauthorized modifications.<br>
        <strong>Requirement:</strong> 100% accuracy in audit logging and status history preservation.
      </p>
    </div>
    <div class="page-num">11</div>
  </div>
</div>

<!-- PAGE 12: 6. CONCLUSION -->
<div class="page">
  <div class="border-box">
    <div>
      <h2 class="section-heading">6. Conclusion</h2>
      <p>
        The CampusCare application SRS defines the functional and non-functional requirements
        needed to design, develop, and operate an efficient college complaint management platform.
        This document has outlined the objectives, scope, system features, user requirements,
        performance metrics, and constraints of the system.
      </p>
      <p>
        By ensuring high levels of accuracy in complaint search, categorization, real-time metrics,
        status transitions, and audit tracking, the system aims to provide students and campus authorities with a
        fast, reliable, and user-friendly grievance redressal experience. Additionally, non-functional
        requirements such as security, scalability, and usability have been clearly identified to
        support long-term growth and maintain student and administrator trust.
      </p>
      <p>
        This SRS will serve as the foundation for the development team, testers, and
        stakeholders, ensuring that all parties have a clear understanding of the system’s goals
        and expectations. Once implemented, the CampusCare system will enable seamless campus grievance
        redressal, maintaining consistency, reliability, and institutional satisfaction.
      </p>
    </div>
    <div class="page-num">12</div>
  </div>
</div>

</body>
</html>
"""

with open('docs/CampusCare_SRS_Document.html', 'w') as f:
    f.write(html_content)

print("Generated docs/CampusCare_SRS_Document.html successfully!")

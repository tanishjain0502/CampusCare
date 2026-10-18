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
    background-color: #f0f0f0;
    font-family: "Times New Roman", Times, serif;
    color: #000;
  }}
  .page {{
    width: 210mm;
    height: 297mm;
    margin: 0 auto;
    padding: 12mm 15mm;
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
    padding: 24px 32px 20px 32px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
  }}
  .page-num {{
    text-align: center;
    font-size: 11pt;
    font-family: "Times New Roman", Times, serif;
    margin-top: 10px;
  }}
  h1.doc-title {{
    font-size: 17pt;
    font-weight: bold;
    text-align: center;
    text-decoration: underline;
    margin-top: 5px;
    margin-bottom: 22px;
    letter-spacing: 0.5px;
  }}
  h2.section-heading {{
    font-size: 14pt;
    font-weight: bold;
    text-decoration: underline;
    margin-top: 0;
    margin-bottom: 14px;
    text-align: center;
  }}
  h3.sub-heading {{
    font-size: 13pt;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: 6px;
  }}
  h4.item-heading {{
    font-size: 11.5pt;
    font-weight: bold;
    margin-top: 8px;
    margin-bottom: 4px;
  }}
  p {{
    font-size: 11pt;
    line-height: 1.42;
    margin-top: 0;
    margin-bottom: 8px;
    text-align: justify;
  }}
  ul {{
    margin-top: 2px;
    margin-bottom: 8px;
    padding-left: 20px;
  }}
  li {{
    font-size: 11pt;
    line-height: 1.38;
    margin-bottom: 5px;
    text-align: justify;
  }}
  .toc-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 11pt;
    margin-top: 5px;
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
    line-height: 1.3;
    margin-top: 10px;
  }}
  .cover-logo-container {{
    text-align: center;
    margin: 20px 0;
  }}
  .cover-logo {{
    width: 145px;
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
    margin-bottom: 40px;
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
        <img class="cover-logo" src="data:image/png;base64,{logo_b64}" alt="SGSITS Logo">
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
          <td colspan="2" class="title">Table of Contents</td>
          <td class="toc-dots"></td>
          <td class="toc-page"><strong>2</strong></td>
        </tr>
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
        <tr><td style="height: 6px;"></td></tr>
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
        <tr><td style="height: 6px;"></td></tr>
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
          <td class="sub">3.2 Complaint Lodging and Ticket Generation</td>
          <td class="toc-dots"></td>
          <td class="toc-page">7</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.3 Student Complaint Tracking and History</td>
          <td class="toc-dots"></td>
          <td class="toc-page">7</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.4 Admin Dashboard and Live Metrics</td>
          <td class="toc-dots"></td>
          <td class="toc-page">7</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.5 All Complaints Listing and Multi-Filtering</td>
          <td class="toc-dots"></td>
          <td class="toc-page">8</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.6 Status Transition and Resolution Management</td>
          <td class="toc-dots"></td>
          <td class="toc-page">8</td>
        </tr>
        <tr>
          <td></td>
          <td class="sub">3.7 Authorization and Privacy Enforcement</td>
          <td class="toc-dots"></td>
          <td class="toc-page">8</td>
        </tr>
        <tr><td style="height: 6px;"></td></tr>
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
        ensuring that all stakeholders—including students, academic staff, maintenance personnel, and
        institutional administrators—have a clear and common understanding of its objectives,
        scope, and functionalities.
      </p>
      <p>
        The scope of this SRS encompasses the full-stack software system supporting CampusCare’s core
        operations, including:
      </p>
      <ul>
        <li><strong>Student-facing web application</strong> for submitting, categorizing, tracking, and reviewing complaints regarding campus infrastructure, laboratories, academic facilities, and campus services.</li>
        <li><strong>Administrative management module</strong> for reviewing, triaging, filtering, searching, and resolving complaints with verified audit trails.</li>
        <li><strong>Lifecycle state management</strong> governing grievance transitions from initial submission to active investigation and final resolution.</li>
        <li><strong>Backend cloud services</strong> incorporating JWT authentication, role-based authorization, automated cryptographic ticket generation, and secure data persistence using MongoDB Atlas.</li>
      </ul>

      <h3 class="sub-heading">1.2 Product Scope</h3>
      <p>
        The CampusCare College Complaint Management System is an independent, full-stack MERN software
        solution designed to digitize and streamline institutional grievance redressal in higher education colleges.
        The primary purpose of this product is to provide a fast, reliable, and completely transparent platform
        where students can register grievances without bureaucratic delays, while college administrators
        can systematically track, assign, and resolve campus issues efficiently.
      </p>
      <h4 class="item-heading">Objectives and Goals</h4>
      <ul>
        <li>To provide a responsive, student-centric platform where students can file complaints across distinct categories with physical location tags in under two minutes.</li>
        <li>To eliminate lost paperwork, informal verbal complaints, and untracked maintenance issues by generating a permanent cryptographic ticket number for every registered grievance.</li>
        <li>To enable real-time administrative triage, giving department heads and campus staff clear visibility over pending, in-progress, and resolved issues.</li>
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
        <li>To enforce institutional accountability by requiring mandatory resolution remarks and logging immutable audit histories with acting administrator identities and timestamps.</li>
        <li>To ensure strict role-based access control and horizontal data isolation, ensuring student complaint privacy while empowering administrators with campus-wide oversight.</li>
        <li>To provide reliable cloud-native database storage capable of scaling effortlessly across academic semesters and varying complaint volumes.</li>
      </ul>

      <h4 class="item-heading">Relevant Benefits</h4>
      <ul>
        <li><strong>Students</strong> benefit from transparent, real-time grievance tracking, eliminating the need to physically visit departmental administrative offices.</li>
        <li><strong>Maintenance and Facilities Staff</strong> gain structured ticket details, precise room/lab locations, and clear priority levels for rapid dispatch.</li>
        <li><strong>College Administration</strong> obtains live metrics on recurring campus issues (such as Wi-Fi disruptions, electrical faults, or cleanliness concerns) for data-driven facility planning.</li>
        <li><strong>The Institution</strong> benefits by strengthening internal quality assurance, fostering student satisfaction, and maintaining compliant records for accreditation audits (e.g., NAAC, NBA, and NIRF).</li>
      </ul>

      <h4 class="item-heading">Relation to Institutional Strategy</h4>
      <p>
        The software directly supports the college's strategic roadmap of transitioning into a digitally empowered,
        smart academic campus. By delivering prompt issue resolution, accountability, and student-focused
        communication, the CampusCare application contributes to:
      </p>
      <ul>
        <li>Enhancing campus safety, infrastructure reliability, and hygienic standards.</li>
        <li>Building trust and open communication channels between students and college management.</li>
        <li>Supporting paperless administration and eco-friendly institutional governance.</li>
      </ul>

      <h3 class="sub-heading">1.3 References</h3>
      <ol style="margin-top: 4px; padding-left: 20px; font-size: 11pt; line-height: 1.45;">
        <li>IEEE Std 830-1998 – IEEE Recommended Practice for Software Requirements Specifications.</li>
        <li>CampusCare Project Repository & Documentation – https://github.com/tanishjain0502/CampusCare.</li>
        <li>Agile Software Development Principles – Beck, K. et al., 2001.</li>
        <li>MERN Stack Architecture Reference (MongoDB, Express, React, Node.js), 2024.</li>
        <li>Nielsen Norman Group – Usability Heuristics for User Interface Design, 2020.</li>
        <li>OWASP Top 10 Web Application Security Risks – Open Web Application Security Project, 2021.</li>
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

      <h4 class="item-heading">1. User Account Management and Authentication</h4>
      <p>
        The application enables students to register accounts using their institutional email, full name, and password.
        The system enforces strict role-based authorization, automatically designating public registrations as STUDENT
        accounts, while ADMIN privileges can only be provisioned through secure server-side initialization. Secure login
        is established through JSON Web Tokens (JWT) with bcrypt-encrypted passwords, ensuring credential safety.
      </p>

      <h4 class="item-heading">2. Complaint Lodging and Ticket Generation</h4>
      <p>
        Students can log grievances across centrally defined campus categories including Classroom, Laboratory,
        Internet / Wi-Fi, Electrical / Maintenance, Cleanliness, Library, Hostel, Administration, and Other.
        Each submission incorporates priority classification (LOW, MEDIUM, HIGH), detailed descriptions (20–2000 characters),
        and optional physical location markers (e.g., Lab 301, Block B). Upon submission, the backend generates an
        immutable, collision-resistant ticket number formatted as <code>CC-YYYYMMDD-XXXXXX</code>.
      </p>

      <h4 class="item-heading">3. Student Complaint Tracking and History</h4>
      <p>
        The student portal features a dedicated "My Complaints" repository scoped strictly to complaints authored by
        the logged-in student. It provides multi-criteria keyword search, status filtering, category filtering,
        and newest/oldest sorting. Students can inspect individual complaint pages showing complete submission details,
        real-time status history timelines, and administrative resolution notes upon issue closure.
      </p>

      <h4 class="item-heading">4. Administrative Dashboard and Metric Calculation</h4>
      <p>
        College administrators have access to an executive dashboard powered by real-time MongoDB aggregations.
        The dashboard calculates real-time complaint counts across four key metrics: Total Complaints, Submitted / Pending,
        In Progress, and Resolved. Interactive metric cards serve as one-click filter shortcuts leading directly
        to pre-filtered complaint lists, supplemented by a live feed of the five most recent complaints.
      </p>

      <h4 class="item-heading">5. All Complaints Listing and Multi-Filtering</h4>
      <p>
        The administrative interface provides a unified, campus-wide complaint management table. Authorized staff can
        execute multi-field searches across ticket numbers, complaint titles, and student names or emails simultaneously.
        Combined multi-parameter filters allow administrators to isolate tickets by category, priority level,
        or workflow status, backed by responsive server-side pagination.
      </p>
    </div>
    <div class="page-num">5</div>
  </div>
</div>

<!-- PAGE 6: 2. OVERALL DESCRIPTION (CONT.) -->
<div class="page">
  <div class="border-box">
    <div>
      <h4 class="item-heading">6. Status Triage and Resolution Workflow</h4>
      <p>
        CampusCare implements a disciplined status transition workflow:
      </p>
      <ul>
        <li><strong>SUBMITTED:</strong> Default initial state upon student creation, awaiting administrative evaluation.</li>
        <li><strong>IN_PROGRESS:</strong> Assigned when maintenance personnel or department staff are actively investigating or rectifying the reported issue.</li>
        <li><strong>RESOLVED:</strong> Assigned upon successful resolution. The system strictly enforces mandatory resolution remarks (minimum 5 characters) and records the resolution timestamp (<code>resolvedAt</code>).</li>
      </ul>
      <p>
        To preserve legal and operational integrity, resolved complaints are locked against arbitrary re-modification.
        Every transition automatically appends an entry to the complaint's immutable status history timeline,
        recording the previous status, new status, acting administrator ID, and transition note.
      </p>

      <h4 class="item-heading">7. Access Control, Privacy, and Data Isolation</h4>
      <p>
        CampusCare strictly enforces horizontal and vertical access boundaries:
      </p>
      <ul>
        <li><strong>Horizontal Isolation:</strong> Students are restricted to viewing only their own grievances. Inquiries targeting complaints authored by another student return an HTTP 404 response to eliminate information disclosure.</li>
        <li><strong>Vertical Authorization:</strong> All administrative endpoints (stats, all complaints, status updates) require a valid JWT containing the verified <code>ADMIN</code> role claim, rejecting student tokens with HTTP 403 Forbidden.</li>
        <li><strong>Credential Confidentiality:</strong> Password hashes and sensitive server tokens are permanently excluded from query projections via Mongoose schema filters and serialization transforms.</li>
      </ul>

      <h4 class="item-heading">8. Infrastructure and Database Reliability</h4>
      <p>
        The backend interfaces directly with MongoDB Atlas, maintaining persistent storage for users, complaints,
        and audit records. The database architecture incorporates optimized compound indexes on query fields
        (<code>ticketNumber</code>, <code>createdBy</code>, <code>status</code>, <code>priority</code>, and <code>createdAt</code>) to ensure sub-millisecond retrieval
        even as historical grievance volumes grow across academic years.
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
        Functional requirements define the core operational behaviors and capabilities of the CampusCare system:
      </p>

      <h3 class="sub-heading">3.1 User Account Management</h3>
      <ul>
        <li>The system shall allow new students to register using their full name, valid email address, and password.</li>
        <li>The system shall validate email syntax and reject duplicate registrations containing an existing email.</li>
        <li>The system shall hash passwords using bcrypt with a minimum of 10 salt rounds prior to database insertion.</li>
        <li>The system shall authenticate users against stored password hashes and issue signed JWT tokens on success.</li>
        <li>The system shall enforce role segregation, ensuring public registration endpoints exclusively provision the <code>STUDENT</code> role.</li>
      </ul>

      <h3 class="sub-heading">3.2 Complaint Lodging and Ticket Generation</h3>
      <ul>
        <li>The system shall provide a responsive submission form validating title (5–100 characters), category, description (20–2000 characters), priority (LOW, MEDIUM, HIGH), and location (up to 100 characters).</li>
        <li>The system shall automatically generate a unique ticket number matching the pattern <code>CC-YYYYMMDD-XXXXXX</code> using cryptographic entropy with collision-retry protection.</li>
        <li>The system shall lock initial status to <code>SUBMITTED</code> and safely ignore client-supplied status or assignment payloads.</li>
        <li>The system shall disable submission buttons during network transit to prevent accidental duplicate ticket generation.</li>
      </ul>

      <h3 class="sub-heading">3.3 Student Complaint Tracking and History</h3>
      <ul>
        <li>The system shall allow authenticated students to retrieve a paginated list of only their own submitted grievances.</li>
        <li>The system shall support real-time search across ticket numbers and complaint titles.</li>
        <li>The system shall provide filter dropdowns for complaint status and category, alongside sorting by newest and oldest.</li>
        <li>The system shall provide a dedicated detail view showing title, description, category, priority, location, created/updated timestamps, status timeline, and administrative resolution remarks.</li>
        <li>The system shall return HTTP 404 if a student requests a ticket belonging to another student.</li>
      </ul>

      <h3 class="sub-heading">3.4 Admin Dashboard and Live Metrics</h3>
      <ul>
        <li>The system shall calculate and display real-time counts for Total, Submitted, In-Progress, and Resolved complaints directly from database aggregations.</li>
        <li>The system shall display a list of the five most recent campus grievances with live status badges.</li>
        <li>The system shall provide interactive stat cards that direct administrators to pre-filtered complaint lists upon clicking.</li>
      </ul>
    </div>
    <div class="page-num">7</div>
  </div>
</div>

<!-- PAGE 8: 3. FUNCTIONAL REQUIREMENTS (CONT.) -->
<div class="page">
  <div class="border-box">
    <div>
      <h3 class="sub-heading">3.5 All Complaints Listing and Multi-Filtering</h3>
      <ul>
        <li>The system shall allow authorized administrators to view all college complaints across all students and categories.</li>
        <li>The system shall provide multi-field search capabilities matching ticket numbers, complaint titles, and student names or email addresses simultaneously.</li>
        <li>The system shall support combined multi-parameter filtering by status (<code>SUBMITTED</code>, <code>IN_PROGRESS</code>, <code>RESOLVED</code>), category, and priority (<code>LOW</code>, <code>MEDIUM</code>, <code>HIGH</code>).</li>
        <li>The system shall support server-side pagination with configurable page limits (default: 10, maximum: 50) and return total record counts and page metadata.</li>
      </ul>

      <h3 class="sub-heading">3.6 Status Transition and Resolution Management</h3>
      <ul>
        <li>The system shall allow administrators to transition complaint status between <code>SUBMITTED</code>, <code>IN_PROGRESS</code>, and <code>RESOLVED</code>.</li>
        <li>The system shall strictly require resolution remarks (minimum 5 characters, maximum 1000 characters) when marking a ticket as <code>RESOLVED</code>.</li>
        <li>The system shall store the resolution timestamp (<code>resolvedAt</code>) and resolution remarks permanently on the complaint record.</li>
        <li>The system shall automatically append every transition to an immutable status history array, recording previous status, new status, acting administrator ID, timestamp, and transition note.</li>
        <li>The system shall prevent duplicate resolution attempts or unauthorized modifications on tickets already marked <code>RESOLVED</code>.</li>
      </ul>

      <h3 class="sub-heading">3.7 Authorization and Privacy Enforcement</h3>
      <ul>
        <li>The system shall reject unauthenticated requests to protected API routes with HTTP 401 Unauthorized.</li>
        <li>The system shall reject student tokens targeting administrative endpoints with HTTP 403 Forbidden.</li>
        <li>The system shall provision administrator credentials exclusively through server-side scripts (<code>npm run seed:admin</code>) to prevent unauthorized privilege escalation.</li>
        <li>The system shall permanently exclude password hashes and secret keys from all API responses via schema projection.</li>
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
        Non-functional requirements describe system quality attributes, performance constraints, and operational standards:
      </p>

      <h3 class="sub-heading">4.1 Performance Requirements</h3>
      <ul>
        <li>The system shall support at least <strong>10,000 active students and staff members</strong> without performance degradation.</li>
        <li>The application homepage and dashboard shall load within <strong>2 seconds</strong> under standard campus network conditions.</li>
        <li>API response times for complaint creation, queries, and dashboard metric calculations shall remain below <strong>500 milliseconds</strong>.</li>
      </ul>

      <h3 class="sub-heading">4.2 Reliability and Availability</h3>
      <ul>
        <li>The system shall ensure <strong>99.9% uptime</strong> to support 24/7 student access across academic semesters.</li>
        <li>In case of server process interruption, cloud process managers (e.g., Render / PM2) shall automatically recover and restore service within <strong>30 seconds</strong>.</li>
        <li>Automated database backups shall occur at least <strong>every 24 hours</strong> via MongoDB Atlas automated snapshot management.</li>
      </ul>

      <h3 class="sub-heading">4.3 Security Requirements</h3>
      <ul>
        <li>All network transmissions shall be encrypted over <strong>TLS 1.3 / HTTPS</strong> to safeguard passwords and personal grievance details.</li>
        <li>User passwords shall be cryptographically hashed using <strong>bcrypt with 10–12 salt rounds</strong>; plaintext passwords shall never be logged or stored.</li>
        <li>Search queries shall sanitize special regular expression characters to prevent <strong>Regular Expression Denial of Service (ReDoS)</strong> attacks.</li>
        <li>Request JSON payloads shall be limited to <strong>10 KB</strong> to protect against buffer overflow and resource exhaustion attacks.</li>
      </ul>

      <h3 class="sub-heading">4.4 Usability Requirements</h3>
      <ul>
        <li>The interface shall provide a clean, modern, intuitive design adhering to institutional blue-and-white visual styling.</li>
        <li>All primary student tasks (filing a complaint, tracking status) shall be achievable within <strong>2 clicks from the dashboard</strong>.</li>
        <li>The system shall provide clear visual cues including status color badges, priority indicators, loading spinners, and actionable error alerts.</li>
      </ul>

      <h3 class="sub-heading">4.5 Scalability Requirements</h3>
      <ul>
        <li>The backend architecture shall remain completely stateless, enabling horizontal scaling across multiple container instances.</li>
        <li>Database indexes on ticket numbers, creator IDs, statuses, and timestamps shall maintain logarithmic query performance as records expand.</li>
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
        <li>The codebase shall follow clean modular MERN architecture with distinct separation of models, controllers, routes, middleware, and frontend components.</li>
        <li>Complaint categories, priorities, and status values shall be centrally defined in <code>complaintConstants.js</code> to allow effortless institutional customization.</li>
        <li>Comprehensive automated test suites (student complaint tests, admin tests, and end-to-end security suites) shall be maintained to guarantee regression-free future updates.</li>
      </ul>

      <h3 class="sub-heading">4.7 Compatibility Requirements</h3>
      <ul>
        <li>The web application shall be fully compatible with major modern browsers: <strong>Google Chrome (v90+)</strong>, <strong>Mozilla Firefox (v88+)</strong>, <strong>Apple Safari (v14+)</strong>, and <strong>Microsoft Edge (v90+)</strong>.</li>
        <li>The responsive frontend layout shall flawlessly support all standard viewport sizes across <strong>Android (v9.0+)</strong>, <strong>iOS (v13+)</strong>, Windows, macOS, and Linux devices.</li>
      </ul>
    </div>
    <div class="page-num">10</div>
  </div>
</div>

</body>
</html>
"""

with open('docs/CampusCare_SRS_Document.html', 'w') as f:
    f.write(html_content)

print("Generated docs/CampusCare_SRS_Document.html successfully!")

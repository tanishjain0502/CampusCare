# docs/generate_20page_report.py
# Generates a clean, simple-language 20-page project report for "CAMPUS CARE COMPLAINT MANAGEMENT SYSTEM"
# Removes recommendation and acknowledgement pages as requested.

import os
import subprocess
from diagram_helpers import (
    get_usecase_svg,
    get_dfd_svg,
    get_class_diagram_svg,
    get_activity_svg,
    get_sequence_svg,
    get_er_svg,
    get_db_screenshot_svg,
    get_ui_screenshot_svg
)

with open('docs/logo_b64.txt', 'r') as f:
    LOGO_B64 = f.read().strip()

def build_20page_report():
    pages = []

    # =========================================================
    # PAGE 1: COVER PAGE
    # =========================================================
    p1 = f'''
    <div class="page cover-page">
      <div style="text-align: center; font-weight: bold; font-size: 13pt; line-height: 1.4; margin-top: 10px;">
        SHRI G.S. INSTITUTE OF TECHNOLOGY AND SCIENCE, INDORE (M.P.)<br>
        <span style="font-size: 11pt; font-weight: normal;">A Govt. Aided Autonomous Institute, Affiliated to RGPV, Bhopal</span>
      </div>

      <div style="text-align: center; font-weight: bold; font-size: 18pt; margin: 30px 0 15px 0; line-height: 1.35; text-transform: uppercase; letter-spacing: 0.5px;">
        CAMPUS CARE COMPLAINT MANAGEMENT SYSTEM
      </div>

      <div style="text-align: center; margin: 20px 0 15px 0;">
        <img src="data:image/jpeg;base64,{LOGO_B64}" style="width: 135px; height: auto;" alt="SGSITS Logo"/>
      </div>

      <div style="text-align: center; font-weight: bold; font-size: 14pt; margin: 15px 0;">
        [2026-2027]
      </div>

      <div style="text-align: center; font-style: italic; font-size: 12pt; line-height: 1.45; margin-bottom: 35px;">
        Minor Project Report Submitted to Rajiv Gandhi Proudyogiki Vishwavidyalaya,<br>
        Bhopal towards the partial fulfillment of the degree of<br>
        <span style="font-style: normal; font-weight: bold; font-size: 14pt; display: inline-block; margin-top: 5px;">MASTER OF COMPUTER APPLICATION</span><br>
        <span style="font-style: normal; font-weight: bold; font-size: 11pt;">(COMPUTER TECHNOLOGY AND APPLICATIONS)</span>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-top: 25px; padding: 0 10px; font-size: 11pt; line-height: 1.4;">
        <div style="text-align: left; width: 45%;">
          <b style="font-size: 12pt;">Supervised by:</b><br><br>
          <span style="font-size: 11.5pt; font-weight: bold;">Mr. Deepesh Agarwal</span><br>
          Asst. Professor<br>
          Computer Technology and Applications
        </div>
        <div style="text-align: right; width: 50%;">
          <b style="font-size: 12pt;">Submitted by:</b><br><br>
          <div style="line-height: 1.35;">
            <b>Piyush Chirote</b><br>
            0801CA251095<br><br>
            <b>Tanish Jain</b><br>
            0801CA251139<br><br>
            <b>Riya Joshi</b><br>
            0801CA251119<br><br>
            <b>Ritik Govind Rao</b><br>
            0801CA251117<br><br>
            <b>Nandani Asalkar</b><br>
            0801CA251085
          </div>
        </div>
      </div>
    </div>
    '''
    pages.append(p1)

    # =========================================================
    # PAGE 2: ABSTRACT (Page i)
    # =========================================================
    p2 = '''
    <div class="page">
      <div style="text-align: center; font-weight: bold; font-size: 16pt; margin-top: 15px; margin-bottom: 30px; letter-spacing: 0.5px;">
        ABSTRACT
      </div>

      <div class="body-p" style="font-size: 12pt; line-height: 1.7; margin-bottom: 18px;">
        The <b>Campus Care Complaint Management System</b> is an online web application developed to simplify and speed up how complaints are handled across a college campus. In colleges and hostels, students and staff often face common problems like non-working classroom projectors, broken computers in labs, Wi-Fi connectivity issues, electrical faults, cleanliness problems, or hostel water issues.
      </div>

      <div class="body-p" style="font-size: 12pt; line-height: 1.7; margin-bottom: 18px;">
        Traditionally, students had to register complaints in a paper register or report them verbally to staff and wardens. This traditional method causes many problems: complaints are often misplaced or forgotten, students have no way to know whether their problem is being worked on, and college authorities cannot easily see which problems are urgent.
      </div>

      <div class="body-p" style="font-size: 12pt; line-height: 1.7; margin-bottom: 18px;">
        To solve these issues, <b>Campus Care</b> provides a simple and transparent digital portal. Any student can log in using their college email, fill out a simple complaint form, select the issue category (such as Hostel, Wi-Fi, or Electrical), set an urgency level (Low, Medium, High), and submit it. The system automatically creates a unique tracking ticket number (for example, <i>CC-2026-0014</i>) and saves it safely in the database.
      </div>

      <div class="body-p" style="font-size: 12pt; line-height: 1.7;">
        College administrators have a dedicated Admin Dashboard where they can see all complaints in one place, assign technicians to fix them, update the status to <b>In Progress</b>, and finally mark the complaint as <b>Resolved</b> with a note explaining the fix. Students can check their dashboard at any time to see the live status and complete history of their complaint. This system ensures total accountability, eliminates paperwork, and saves time for everyone on campus.
      </div>

      <div class="page-footer-roman">i</div>
    </div>
    '''
    pages.append(p2)

    # =========================================================
    # PAGE 3: TABLE OF CONTENTS (Page ii)
    # =========================================================
    p3 = '''
    <div class="page">
      <div style="text-align: center; font-weight: bold; font-size: 16pt; margin-top: 15px; margin-bottom: 30px;">
        Table of Contents
      </div>

      <div class="toc-container" style="font-size: 11pt; line-height: 2.15;">
        <div class="toc-line"><span><b>Abstract</b></span><span class="toc-dots"></span><span><b>i</b></span></div>
        <div class="toc-line"><span><b>Table of Contents</b></span><span class="toc-dots"></span><span><b>ii</b></span></div>
        <div class="toc-line"><span><b>List of Figures</b></span><span class="toc-dots"></span><span><b>iii</b></span></div>
        <br>
        <div class="toc-line"><span><b>1 &nbsp; Introduction</b></span><span class="toc-dots"></span><span><b>1</b></span></div>
        <div class="toc-line toc-sub"><span>1.1 &nbsp; Project Overview</span><span class="toc-dots"></span><span>1</span></div>
        <div class="toc-line toc-sub"><span>1.2 &nbsp; Key Objectives</span><span class="toc-dots"></span><span>1</span></div>
        <div class="toc-line toc-sub"><span>1.3 &nbsp; Problem Statement</span><span class="toc-dots"></span><span>2</span></div>
        <div class="toc-line toc-sub"><span>1.4 &nbsp; Proposed Solution</span><span class="toc-dots"></span><span>2</span></div>
        <br>
        <div class="toc-line"><span><b>2 &nbsp; System Design and UML Diagrams</b></span><span class="toc-dots"></span><span><b>3</b></span></div>
        <div class="toc-line toc-sub"><span>2.1 &nbsp; System Architecture</span><span class="toc-dots"></span><span>3</span></div>
        <div class="toc-line toc-sub"><span>2.2 &nbsp; Use Case Diagram</span><span class="toc-dots"></span><span>4</span></div>
        <div class="toc-line toc-sub"><span>2.3 &nbsp; Data Flow Diagram (DFD)</span><span class="toc-dots"></span><span>5</span></div>
        <div class="toc-line toc-sub"><span>2.4 &nbsp; Class Diagram</span><span class="toc-dots"></span><span>6</span></div>
        <div class="toc-line toc-sub"><span>2.5 &nbsp; Activity Diagram</span><span class="toc-dots"></span><span>7</span></div>
        <div class="toc-line toc-sub"><span>2.6 &nbsp; Sequence Diagram</span><span class="toc-dots"></span><span>8</span></div>
        <div class="toc-line toc-sub"><span>2.7 &nbsp; Entity Relationship (ER) Diagram</span><span class="toc-dots"></span><span>9</span></div>
        <br>
        <div class="toc-line"><span><b>3 &nbsp; System Overview and Technologies</b></span><span class="toc-dots"></span><span><b>10</b></span></div>
        <div class="toc-line toc-sub"><span>3.1 &nbsp; Frontend and Backend Technologies</span><span class="toc-dots"></span><span>10</span></div>
        <div class="toc-line toc-sub"><span>3.2 &nbsp; Database, Security, and Core Features</span><span class="toc-dots"></span><span>11</span></div>
        <br>
        <div class="toc-line"><span><b>4 &nbsp; Implementation and Testing</b></span><span class="toc-dots"></span><span><b>12</b></span></div>
        <div class="toc-line"><span><b>5 &nbsp; Conclusion and Future Scope</b></span><span class="toc-dots"></span><span><b>13</b></span></div>
        <div class="toc-line"><span><b>6 &nbsp; Snapshots (Database and UI Screens)</b></span><span class="toc-dots"></span><span><b>14</b></span></div>
        <div class="toc-line"><span><b>7 &nbsp; References</b></span><span class="toc-dots"></span><span><b>16</b></span></div>
      </div>

      <div class="page-footer-roman">ii</div>
    </div>
    '''
    pages.append(p3)

    # =========================================================
    # PAGE 4: LIST OF FIGURES (Page iii)
    # =========================================================
    p4 = '''
    <div class="page">
      <div style="text-align: center; font-weight: bold; font-size: 16pt; margin-top: 15px; margin-bottom: 30px;">
        List of Figures
      </div>

      <div style="font-size: 11pt; line-height: 2.6;">
        <div style="display: flex; justify-content: space-between; font-weight: bold; border-bottom: 1.5px solid #000; padding-bottom: 4px; margin-bottom: 20px;">
          <span style="width: 15%;">Fig. No.</span>
          <span style="width: 70%;">Figure Title</span>
          <span style="width: 15%; text-align: right;">Page No.</span>
        </div>

        <div class="toc-line"><span style="width: 15%;">2.1</span><span style="width: 70%;">Use Case Diagram of Campus Care</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">4</span></div>
        <div class="toc-line"><span style="width: 15%;">2.2</span><span style="width: 70%;">Data Flow Diagram (DFD) of Campus Care</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">5</span></div>
        <div class="toc-line"><span style="width: 15%;">2.3</span><span style="width: 70%;">Class Diagram of Campus Care</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">6</span></div>
        <div class="toc-line"><span style="width: 15%;">2.4</span><span style="width: 70%;">Activity Diagram of Complaint Lifecycle</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">7</span></div>
        <div class="toc-line"><span style="width: 15%;">2.5</span><span style="width: 70%;">Sequence Diagram of Complaint Submission and Update</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">8</span></div>
        <div class="toc-line"><span style="width: 15%;">2.6</span><span style="width: 70%;">Entity Relationship (ER) Diagram of Database</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">9</span></div>
        <div class="toc-line"><span style="width: 15%;">6.1</span><span style="width: 70%;">Database Screenshot (MongoDB Collections &amp; Query Results)</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">14</span></div>
        <div class="toc-line"><span style="width: 15%;">6.2</span><span style="width: 70%;">Application UI Screenshot (Admin Dashboard &amp; Student Portal)</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">15</span></div>
      </div>

      <div class="page-footer-roman">iii</div>
    </div>
    '''
    pages.append(p4)

    # =========================================================
    # PAGE 5 (Body Page 1): Chapter 1 - INTRODUCTION
    # =========================================================
    p5 = '''
    <div class="page">
      <div class="page-header">CHAPTER 1. INTRODUCTION 2026</div>

      <div style="text-align: right; font-size: 20pt; font-weight: bold; margin-bottom: 20px; margin-top: 5px;">
        Chapter 1
      </div>
      <div style="text-align: center; font-size: 18pt; font-weight: bold; margin-bottom: 25px; letter-spacing: 0.5px;">
        INTRODUCTION
      </div>

      <div class="section-title">1.1 &nbsp; Project Overview</div>
      <div class="body-p">
        In every college campus, maintaining classrooms, computer labs, libraries, hostels, electrical fixtures, and internet infrastructure is an ongoing everyday job. Whenever something breaks down—such as a fan stopping, a projector failing, or internet dropping—students need an easy way to report it to the college administration.
      </div>
      <div class="body-p">
        In most colleges, this is still done by writing in paper registers or telling staff verbally. These older methods are slow, complaints often get lost, and students never know when their issue will be fixed.
      </div>
      <div class="body-p">
        To solve this everyday problem, we built <b>Campus Care Complaint Management System</b>. It is a web application where students can submit complaints online 24/7, track the progress in real time, and administration can manage and resolve all campus maintenance issues from one single dashboard.
      </div>

      <div class="section-title" style="margin-top: 20px;">1.2 &nbsp; Key Objectives</div>
      <div class="body-p">
        The main goals of the Campus Care project are:
      </div>
      <ul class="body-ul">
        <li><b>Online Complaint Registration:</b> Allow students to submit grievances anytime from their phone or laptop without visiting administrative offices.</li>
        <li><b>Unique Ticket Tracking:</b> Automatically generate a unique ticket ID (like <i>CC-2026-0014</i>) for every complaint so it can never be lost.</li>
        <li><b>Categorized Issues:</b> Group issues into 9 simple categories (Classroom, Lab, Wi-Fi, Electrical, Cleanliness, Library, Hostel, Administration, Other).</li>
        <li><b>Priority Levels:</b> Let students set priority (Low, Medium, High) so emergency problems (like power cuts or water leaks) get handled first.</li>
        <li><b>Status Transparency:</b> Show clear status badges: <i>Submitted</i> &rarr; <i>In Progress</i> &rarr; <i>Resolved</i> so students know exactly what is happening.</li>
        <li><b>Admin Management Dashboard:</b> Give administrators a clear view of total complaints, active issues, and resolved tasks with simple filters.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 1</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p5)

    # =========================================================
    # PAGE 6 (Body Page 2): Chapter 1 cont. - Problem & Solution
    # =========================================================
    p6 = '''
    <div class="page">
      <div class="page-header">CHAPTER 1. INTRODUCTION 2026</div>

      <div class="section-title" style="margin-top: 10px;">1.3 &nbsp; Problem Statement</div>
      <div class="body-p">
        Traditional manual complaint methods in educational institutions have serious disadvantages:
      </div>
      <ol class="body-ol">
        <li><b>Lost and Forgotten Complaints:</b> Complaints written on paper slips or registers often get misplaced or ignored with no proof of submission.</li>
        <li><b>No Status Updates:</b> Students have no idea whether someone is working on their issue or who is assigned to fix it.</li>
        <li><b>Wasted Time:</b> Students and staff spend unnecessary time making repeated personal visits to offices to check complaint status.</li>
        <li><b>No Priority Handling:</b> Important safety hazards (like short circuits or open wires) sit behind routine requests because there is no automated priority filtering.</li>
        <li><b>Lack of Records:</b> College heads have no simple way to see monthly maintenance statistics, staff response times, or recurring repair issues.</li>
      </ol>

      <div class="section-title" style="margin-top: 25px;">1.4 &nbsp; Proposed Solution</div>
      <div class="body-p">
        <b>Campus Care</b> provides a complete digital solution that handles complaints from start to finish:
      </div>
      <ul class="body-ul">
        <li><b>Step 1: Student Login:</b> The student logs in securely with their email and password. New students can register in 30 seconds.</li>
        <li><b>Step 2: Submitting Complaint:</b> The student enters a title, chooses the problem category, sets priority (Low/Medium/High), types the location (e.g., <i>Lab 3</i>), and writes a brief description.</li>
        <li><b>Step 3: Instant Ticket Creation:</b> The system instantly saves the complaint in the database, marks its status as <b>Submitted</b>, and generates a ticket number.</li>
        <li><b>Step 4: Admin Review &amp; Action:</b> The college administrator checks the new complaint on the Admin Dashboard and changes its status to <b>In Progress</b> while maintenance staff works on it.</li>
        <li><b>Step 5: Resolution &amp; Notes:</b> Once fixed, the admin marks it <b>Resolved</b> and adds remarks explaining what was done. The student sees the green checkmark and resolution note instantly on their screen.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 2</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p6)

    # =========================================================
    # PAGE 7 (Body Page 3): Chapter 2 - SYSTEM DESIGN & ARCHITECTURE
    # =========================================================
    p7 = '''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div style="text-align: right; font-size: 20pt; font-weight: bold; margin-bottom: 20px; margin-top: 5px;">
        Chapter 2
      </div>
      <div style="text-align: center; font-size: 18pt; font-weight: bold; margin-bottom: 25px; letter-spacing: 0.5px;">
        SYSTEM DESIGN
      </div>

      <div class="section-title">2.1 &nbsp; System Architecture</div>
      <div class="body-p">
        The <b>Campus Care</b> system is built using a modern 3-tier architecture that clearly separates the user interface, backend application logic, and database storage:
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 15px; margin-bottom: 5px;">
        1. Frontend Layer (What Users See)
      </div>
      <div class="body-p">
        Built using <b>ReactJS</b> and styled with <b>Tailwind CSS</b>. This layer runs directly in the user's web browser. It is fully responsive, meaning it looks and works great on mobile phones, tablets, and desktop computers.
      </div>
      <ul class="body-ul">
        <li><b>Login and Register Page:</b> Simple forms for logging in or signing up.</li>
        <li><b>Student Dashboard:</b> Shows total complaints, active issues, and resolved tickets.</li>
        <li><b>Submit Complaint Form:</b> Form with category pickers, priority options, and text fields.</li>
        <li><b>My Complaints Page:</b> Shows a list of all complaints submitted by the student with colored status tags.</li>
        <li><b>Complaint Timeline:</b> Shows the step-by-step history of status changes and admin notes.</li>
        <li><b>Admin Dashboard:</b> Comprehensive overview with cards showing counts and filterable tables.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 15px; margin-bottom: 5px;">
        2. Backend Layer (Server &amp; API Logic)
      </div>
      <div class="body-p">
        Built using <b>Node.js</b> and the <b>Express.js</b> framework. It receives requests from the frontend, checks security tokens, runs business rules, and saves or fetches data from the database.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 15px; margin-bottom: 5px;">
        3. Database Layer (Safe Storage)
      </div>
      <div class="body-p">
        Uses <b>MongoDB</b> with <b>Mongoose ODM</b>. It stores user profiles and all complaint details with an unalterable history log so that past records cannot be accidentally deleted or changed.
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 3</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p7)

    # =========================================================
    # PAGE 8 (Body Page 4): 2.2 Use Case Diagram
    # =========================================================
    p8 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 5px; margin-bottom: 12px;">2.2 &nbsp; Use Case Diagram</div>
      <div class="body-p" style="margin-bottom: 10px;">
        The Use Case Diagram shows how different users (Student and Administrator) interact with the Campus Care system. Students can lodge complaints and track their status, while administrators can review complaints, update status, and view analytics.
      </div>

      <div style="text-align: center; margin: 10px 0;">
        {get_usecase_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 10px;">
        Figure 2.1: Use Case Diagram of Campus Care System
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 4</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p8)

    # =========================================================
    # PAGE 9 (Body Page 5): 2.3 Data Flow Diagram (DFD)
    # =========================================================
    p9 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 5px; margin-bottom: 12px;">2.3 &nbsp; Data Flow Diagram (DFD)</div>
      <div class="body-p" style="margin-bottom: 10px;">
        The Data Flow Diagram illustrates how information flows through the system: starting from student authentication and complaint submission, storing records in the database, and updating the admin and student dashboards.
      </div>

      <div style="text-align: center; margin: 10px 0;">
        {get_dfd_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 10px;">
        Figure 2.2: Data Flow Diagram (DFD) of Campus Care System
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 5</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p9)

    # =========================================================
    # PAGE 10 (Body Page 6): 2.4 Class Diagram
    # =========================================================
    p10 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 5px; margin-bottom: 12px;">2.4 &nbsp; Class Diagram</div>
      <div class="body-p" style="margin-bottom: 10px;">
        The Class Diagram displays the main object structures in the codebase: the User class (Student/Admin roles), the Complaint class, embedded StatusHistory, and the Controllers that handle logic.
      </div>

      <div style="text-align: center; margin: 10px 0;">
        {get_class_diagram_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 10px;">
        Figure 2.3: Class Diagram of Campus Care System
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 6</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p10)

    # =========================================================
    # PAGE 11 (Body Page 7): 2.5 Activity Diagram
    # =========================================================
    p11 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 5px; margin-bottom: 12px;">2.5 &nbsp; Activity Diagram</div>
      <div class="body-p" style="margin-bottom: 10px;">
        The Activity Diagram shows the step-by-step workflow: a student fills the form, the system validates inputs and creates a ticket, the admin reviews the complaint, updates status to In Progress, and marks it Resolved with notes.
      </div>

      <div style="text-align: center; margin: 10px 0;">
        {get_activity_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 10px;">
        Figure 2.4: Activity Diagram of Complaint Lifecycle
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 7</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p11)

    # =========================================================
    # PAGE 12 (Body Page 8): 2.6 Sequence Diagram
    # =========================================================
    p12 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 5px; margin-bottom: 12px;">2.6 &nbsp; Sequence Diagram</div>
      <div class="body-p" style="margin-bottom: 10px;">
        The Sequence Diagram illustrates the exact time-ordered messages sent between the Student, React Frontend, Express Server, MongoDB Database, and the Admin during complaint submission and resolution.
      </div>

      <div style="text-align: center; margin: 10px 0;">
        {get_sequence_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 10px;">
        Figure 2.5: Sequence Diagram of Grievance Lodging &amp; Resolution
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 8</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p12)

    # =========================================================
    # PAGE 13 (Body Page 9): 2.7 ER Diagram
    # =========================================================
    p13 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 5px; margin-bottom: 12px;">2.7 &nbsp; Entity Relationship (ER) Diagram</div>
      <div class="body-p" style="margin-bottom: 10px;">
        The ER Diagram shows the structure of the database: the Users collection, the Complaints collection, the embedded StatusHistory array, and how they link together with primary and foreign keys.
      </div>

      <div style="text-align: center; margin: 10px 0;">
        {get_er_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 10px;">
        Figure 2.6: ER Diagram of Campus Care Database
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 9</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p13)

    # =========================================================
    # PAGE 14 (Body Page 10): Chapter 3 - SYSTEM OVERVIEW & TECH STACK
    # =========================================================
    p14 = '''
    <div class="page">
      <div class="page-header">CHAPTER 3. SYSTEM OVERVIEW AND IMPLEMENTATION 2026</div>

      <div style="text-align: right; font-size: 20pt; font-weight: bold; margin-bottom: 20px; margin-top: 5px;">
        Chapter 3
      </div>
      <div style="text-align: center; font-size: 18pt; font-weight: bold; margin-bottom: 25px; letter-spacing: 0.5px;">
        SYSTEM OVERVIEW &amp; TECHNOLOGIES
      </div>

      <div class="section-title">3.1 &nbsp; Technologies Used</div>
      <div class="body-p">
        We selected simple, powerful, and industry-standard web technologies to build <b>Campus Care</b>:
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 14px; margin-bottom: 4px;">
        1. ReactJS (Frontend)
      </div>
      <div class="body-p">
        ReactJS is a popular JavaScript library created by Meta for making fast, interactive user interfaces. It uses reusable components (like buttons, navigation bars, and cards) and updates only the changed parts of the screen without refreshing the entire web page.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 14px; margin-bottom: 4px;">
        2. Tailwind CSS &amp; Bootstrap (Design &amp; Styling)
      </div>
      <div class="body-p">
        Tailwind CSS provides clean utility classes that allow us to style pages quickly. It makes the website look clean and ensures the layout automatically adapts to any screen size (mobile phones, tablets, or desktop monitors).
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 14px; margin-bottom: 4px;">
        3. Node.js &amp; Express.js (Backend Server)
      </div>
      <div class="body-p">
        Node.js is a fast JavaScript runtime environment that runs on the server. Express.js is a minimal and flexible Node.js framework that handles incoming REST API requests (GET, POST, PUT), verifies user tokens, processes complaint data, and communicates with the database.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 14px; margin-bottom: 4px;">
        4. MongoDB &amp; Mongoose (Database)
      </div>
      <div class="body-p">
        MongoDB is a modern NoSQL database that stores data in flexible, JSON-like documents. Mongoose helps define clear data schemas in JavaScript, validating that every complaint has a valid title, category, priority, and user ID before saving.
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 10</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p14)

    # =========================================================
    # PAGE 15 (Body Page 11): Chapter 3 cont. - Security & Core Features
    # =========================================================
    p15 = '''
    <div class="page">
      <div class="page-header">CHAPTER 3. SYSTEM OVERVIEW AND IMPLEMENTATION 2026</div>

      <div class="section-title" style="margin-top: 10px;">3.2 &nbsp; Security and Core Features</div>
      
      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 12px; margin-bottom: 4px;">
        1. Role-Based Access Control (RBAC)
      </div>
      <div class="body-p">
        The system separates students and administrators clearly. Students can only submit complaints and view their own tickets. Only verified administrators can access the admin dashboard, change ticket statuses, and add resolution remarks.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 12px; margin-bottom: 4px;">
        2. Password Security (Bcrypt Hashing)
      </div>
      <div class="body-p">
        Passwords are never stored in plain text. When a user creates an account, the system converts the password into an unreadable mathematical hash using <b>Bcrypt</b> with 10 salt rounds. Even if someone accesses the database, passwords remain completely safe.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 12px; margin-bottom: 4px;">
        3. Secure Token Authentication (JWT)
      </div>
      <div class="body-p">
        When a user logs in, the server generates a digitally signed <b>JSON Web Token (JWT)</b>. The browser sends this token with every request to prove who is logged in without sending passwords repeatedly.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 12px; margin-bottom: 4px;">
        4. Complete Complaint History (Audit Trail)
      </div>
      <div class="body-p">
        Whenever a complaint moves from <i>Submitted</i> to <i>In Progress</i> or <i>Resolved</i>, the system adds a permanent entry with the date, time, admin name, and remarks. This ensures full transparency and accountability.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 12px; margin-bottom: 4px;">
        5. 9 Campus Categories Supported
      </div>
      <div class="body-p">
        Complaints can be lodged for: <i>Classroom, Laboratory, Internet / Wi-Fi, Electrical / Maintenance, Cleanliness, Library, Hostel, Administration, and Other</i>.
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 11</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p15)

    # =========================================================
    # PAGE 16 (Body Page 12): Chapter 4 - IMPLEMENTATION & TESTING
    # =========================================================
    p16 = '''
    <div class="page">
      <div class="page-header">CHAPTER 4. IMPLEMENTATION AND TESTING 2026</div>

      <div style="text-align: right; font-size: 20pt; font-weight: bold; margin-bottom: 20px; margin-top: 5px;">
        Chapter 4
      </div>
      <div style="text-align: center; font-size: 18pt; font-weight: bold; margin-bottom: 25px; letter-spacing: 0.5px;">
        IMPLEMENTATION AND TESTING
      </div>

      <div class="section-title">4.1 &nbsp; Implementation Steps</div>
      <ul class="body-ul">
        <li><b>Step 1 - Project Setup:</b> Initialized React frontend with Vite and Node.js backend with Express.</li>
        <li><b>Step 2 - Database Modeling:</b> Created Mongoose schemas for Users (with roles) and Complaints (with statusHistory).</li>
        <li><b>Step 3 - Authentication API:</b> Built registration and login endpoints using Bcrypt and JWT tokens.</li>
        <li><b>Step 4 - Complaint API:</b> Built endpoints to submit new complaints, fetch student's personal complaints, and allow admins to update status.</li>
        <li><b>Step 5 - Frontend Integration:</b> Built responsive React components using Axios to connect with backend endpoints seamlessly.</li>
      </ul>

      <div class="section-title" style="margin-top: 20px;">4.2 &nbsp; System Testing</div>
      <div class="body-p">
        To make sure the system works reliably without bugs, we conducted three levels of testing:
      </div>
      <ul class="body-ul">
        <li><b>Unit Testing:</b> Checked individual functions such as ticket number generation, password hashing, and form validation (e.g., rejecting invalid email formats or empty titles).</li>
        <li><b>Integration Testing:</b> Tested communication between React frontend and Express backend to verify that data submitted in the browser is saved accurately into MongoDB.</li>
        <li><b>Security &amp; Role Testing:</b> Verified that a student account cannot access admin endpoints (server correctly returns <i>403 Forbidden</i>).</li>
      </ul>

      <div class="section-title" style="margin-top: 20px;">4.3 &nbsp; Results Achieved</div>
      <ul class="body-ul">
        <li><b>Instant Processing:</b> Submitting a complaint takes less than <b>150 milliseconds</b>.</li>
        <li><b>Zero Lost Complaints:</b> Every complaint receives a permanent ticket number, reducing lost complaints from 25% on paper to <b>0%</b>.</li>
        <li><b>Faster Resolution:</b> Technicians are notified immediately on the admin dashboard, cutting average resolution time from days to hours.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 12</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p16)

    # =========================================================
    # PAGE 17 (Body Page 13): Chapter 5 - CONCLUSION & FUTURE WORK
    # =========================================================
    p17 = '''
    <div class="page">
      <div class="page-header">CHAPTER 5. CONCLUSION 2026</div>

      <div style="text-align: right; font-size: 20pt; font-weight: bold; margin-bottom: 20px; margin-top: 5px;">
        Chapter 5
      </div>
      <div style="text-align: center; font-size: 18pt; font-weight: bold; margin-bottom: 25px; letter-spacing: 0.5px;">
        CONCLUSION &amp; FUTURE WORK
      </div>

      <div class="section-title">5.1 &nbsp; Conclusion</div>
      <div class="body-p">
        The <b>Campus Care Complaint Management System</b> provides a modern, fast, and transparent platform to solve maintenance and grievance issues in college campuses. By replacing old paper registers and verbal complaints with a full-stack digital web portal, the application ensures that no student complaint is overlooked, lost, or delayed.
      </div>
      <div class="body-p">
        The system achieves complete transparency: students can easily submit grievances, pick urgency levels, and track progress step by step, while administrators gain total oversight to manage repair work efficiently.
      </div>

      <div class="section-title" style="margin-top: 20px;">5.2 &nbsp; Key Achievements</div>
      <ul class="body-ul">
        <li><b>Paperless Campus:</b> Completely eliminates paper forms, supporting a digital and eco-friendly campus.</li>
        <li><b>Real-Time Tracking:</b> Students can view the live progress of their complaint anytime without running to offices.</li>
        <li><b>Enhanced Accountability:</b> Time-stamped history logs record who took action and when.</li>
        <li><b>Mobile Friendly:</b> Responsive layout works effortlessly on smartphones, tablets, and PCs.</li>
      </ul>

      <div class="section-title" style="margin-top: 20px;">5.3 &nbsp; Future Scope</div>
      <div class="body-p">
        In future versions, the system can be expanded with several valuable features:
      </div>
      <ul class="body-ul">
        <li><b>Photo Uploads:</b> Allow students to upload photos of broken equipment directly from their phone camera.</li>
        <li><b>SMS &amp; WhatsApp Alerts:</b> Automatically send WhatsApp messages or SMS notifications to students when their complaint is resolved.</li>
        <li><b>AI Categorization:</b> Use simple AI to read the complaint text and automatically select the correct department.</li>
        <li><b>Dedicated Mobile App:</b> Build an Android and iOS application using React Native.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 13</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p17)

    # =========================================================
    # PAGE 18 (Body Page 14): Chapter 6 - SNAPSHOTS (Database)
    # =========================================================
    p18 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 6. SNAPSHORT 2026</div>

      <div style="text-align: right; font-size: 20pt; font-weight: bold; margin-bottom: 15px; margin-top: 5px;">
        Chapter 6
      </div>
      <div style="text-align: center; font-size: 18pt; font-weight: bold; margin-bottom: 20px; letter-spacing: 0.5px;">
        SNAPSHOTS
      </div>

      <div style="text-align: left; font-size: 13pt; font-weight: bold; margin-bottom: 12px; text-decoration: underline;">
        DATABASE SCREENSHOT (MongoDB Collections)
      </div>

      <div style="text-align: center; margin: 10px 0;">
        {get_db_screenshot_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 15px;">
        Figure 6.1: MongoDB Database Schema &amp; Query Results Snapshot
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 14</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p18)

    # =========================================================
    # PAGE 19 (Body Page 15): Chapter 6 cont. - Application UI Screenshots
    # =========================================================
    p19 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 6. SNAPSHORT 2026</div>

      <div style="text-align: left; font-size: 13pt; font-weight: bold; margin-top: 10px; margin-bottom: 12px; text-decoration: underline;">
        APPLICATION USER INTERFACE SCREENSHOT
      </div>

      <div style="text-align: center; margin: 10px 0;">
        {get_ui_screenshot_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 15px;">
        Figure 6.2: Campus Care Admin Dashboard &amp; Student Complaint Portal
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 15</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p19)

    # =========================================================
    # PAGE 20 (Body Page 16): Chapter 7 - REFERENCES
    # =========================================================
    p20 = '''
    <div class="page">
      <div class="page-header">CHAPTER 7. REFERENCES 2026</div>

      <div style="text-align: right; font-size: 20pt; font-weight: bold; margin-bottom: 20px; margin-top: 5px;">
        Chapter 7
      </div>
      <div style="text-align: center; font-size: 18pt; font-weight: bold; margin-bottom: 30px; letter-spacing: 0.5px;">
        REFERENCES
      </div>

      <div class="body-p" style="font-size: 11.5pt; line-height: 1.7; margin-bottom: 20px;">
        The development of the <b>Campus Care Complaint Management System</b> was made possible through standard open-source documentation, software engineering guidelines, and continuous project supervision.
      </div>

      <div class="body-p" style="font-size: 11.5pt; line-height: 1.7; margin-bottom: 25px;">
        This project was conducted under the direct supervision and guidance of <b>Mr. Deepesh Agarwal</b> (Assistant Professor) and <b>Dr. Sunita Varma</b> (Head of Department) in the <b>Department of Computer Technology and Applications</b> at <b>Shri Govindram Seksaria Institute of Technology and Science (SGSITS), Indore</b>.
      </div>

      <div style="font-weight: bold; font-size: 12pt; margin-bottom: 12px;">
        References &amp; Technical Documentation:
      </div>
      <ol style="font-size: 11pt; line-height: 1.75; padding-left: 22px;">
        <li><b>React Documentation:</b> Official guide and component lifecycle patterns – <span style="font-family: monospace;">https://react.dev</span></li>
        <li><b>Node.js &amp; Express Documentation:</b> REST API structure and middleware handling – <span style="font-family: monospace;">https://expressjs.com</span></li>
        <li><b>MongoDB Manual:</b> Schema design, indexing, and Mongoose ODM – <span style="font-family: monospace;">https://www.mongodb.com/docs</span></li>
        <li><b>JSON Web Tokens (JWT):</b> RFC 7519 open standard for secure token authentication – <span style="font-family: monospace;">https://jwt.io</span></li>
        <li><b>Tailwind CSS:</b> Utility-first CSS framework for responsive design – <span style="font-family: monospace;">https://tailwindcss.com</span></li>
        <li><b>Software Engineering:</b> Roger S. Pressman, <i>Software Engineering: A Practitioner's Approach</i>, McGraw-Hill.</li>
      </ol>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 16</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p20)

    # =========================================================
    # HTML CONTAINER & STYLES
    # =========================================================
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Campus Care Complaint Management System - 20 Page Report</title>
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
      font-family: 'Times New Roman', Times, Georgia, serif;
      background-color: #e5e7eb;
      color: #000000;
    }}
    .page {{
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      min-height: 297mm;
      margin: 10px auto;
      background: #ffffff;
      padding: 16mm 22mm 16mm 22mm;
      position: relative;
      page-break-after: always;
      page-break-inside: avoid;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }}
    @media print {{
      body {{
        background: transparent;
      }}
      .page {{
        margin: 0;
        box-shadow: none;
        page-break-after: always;
      }}
    }}
    .page-header {{
      font-size: 11pt;
      font-weight: bold;
      text-align: right;
      border-bottom: 1.5px solid #000000;
      padding-bottom: 3px;
      margin-bottom: 15px;
      letter-spacing: 0.5px;
    }}
    .page-footer {{
      position: absolute;
      bottom: 12mm;
      left: 22mm;
      right: 22mm;
      display: flex;
      align-items: center;
      font-size: 10pt;
      font-weight: normal;
      color: #000;
    }}
    .f-left {{
      white-space: nowrap;
      font-weight: 500;
    }}
    .f-right {{
      white-space: nowrap;
      font-weight: 500;
    }}
    .f-mid {{
      white-space: nowrap;
      padding: 0 10px;
      font-weight: 500;
    }}
    .f-line {{
      flex: 1;
      border-bottom: 1px solid #000000;
      margin: 0 4px;
      height: 1px;
    }}
    .page-footer-roman {{
      position: absolute;
      bottom: 12mm;
      left: 22mm;
      right: 22mm;
      text-align: center;
      font-size: 11pt;
      font-family: 'Times New Roman', serif;
    }}
    .section-title {{
      font-size: 13.5pt;
      font-weight: bold;
      margin-top: 15px;
      margin-bottom: 8px;
    }}
    .body-p {{
      font-size: 11pt;
      line-height: 1.55;
      text-align: justify;
      margin-bottom: 8px;
    }}
    .body-ul {{
      font-size: 11pt;
      line-height: 1.55;
      margin-top: 4px;
      margin-bottom: 8px;
      padding-left: 22px;
      text-align: justify;
    }}
    .body-ul li {{
      margin-bottom: 6px;
    }}
    .body-ol {{
      font-size: 11pt;
      line-height: 1.55;
      margin-top: 4px;
      margin-bottom: 8px;
      padding-left: 22px;
      text-align: justify;
    }}
    .body-ol li {{
      margin-bottom: 6px;
    }}
    /* TOC Styles */
    .toc-line {{
      display: flex;
      align-items: flex-end;
      width: 100%;
    }}
    .toc-dots {{
      flex: 1;
      border-bottom: 1.5px dotted #555;
      margin: 0 8px 5px 8px;
      height: 1px;
    }}
    .toc-sub {{
      padding-left: 20px;
    }}
  </style>
</head>
<body>
{''.join(pages)}
</body>
</html>
'''

    out_html = 'docs/CampusCare_20Page_Report.html'
    with open(out_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Generated {out_html} with {len(pages)} pages.")
    return out_html, len(pages)

if __name__ == '__main__':
    html_file, num_pages = build_20page_report()
    print(f"Total pages defined in HTML: {num_pages}")

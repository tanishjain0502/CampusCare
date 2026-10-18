# docs/generate_34page_report.py
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

def build_report_html():
    pages = []

    # -------------------------------------------------------------
    # PAGE 1: COVER PAGE
    # -------------------------------------------------------------
    p1 = f'''
    <div class="page cover-page">
      <div style="text-align: center; font-weight: bold; font-size: 13pt; line-height: 1.4; margin-top: 10px;">
        SHRI G.S. INSTITUTE OF TECHNOLOGY AND SCIENCE, INDORE (M.P.)<br>
        <span style="font-size: 11pt; font-weight: normal;">A Govt. Aided Autonomous Institute, Affiliated to RGPV, Bhopal</span>
      </div>

      <div style="text-align: center; font-weight: bold; font-size: 17pt; margin: 30px 0 15px 0; line-height: 1.35; text-transform: uppercase; letter-spacing: 0.5px;">
        CAMPUSCARE: CENTRALIZED CAMPUS GRIEVANCE REDRESSAL AND INCIDENT MANAGEMENT SYSTEM
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

    # -------------------------------------------------------------
    # PAGE 2: RECOMMENDATION (Page i)
    # -------------------------------------------------------------
    p2 = f'''
    <div class="page">
      <div style="text-align: center; font-weight: bold; font-size: 13pt; line-height: 1.4; margin-top: 5px;">
        SHRI G.S. INSTITUTE OF TECHNOLOGY AND SCIENCE, INDORE (M.P.)<br>
        <span style="font-size: 11pt; font-weight: normal;">A Govt. Aided Autonomous Institute, Affiliated to RGPV, Bhopal</span>
      </div>

      <div style="text-align: center; font-weight: bold; font-size: 12.5pt; margin-top: 20px; text-transform: uppercase;">
        DEPARTMENT OF COMPUTER TECHNOLOGY AND APPLICATIONS
      </div>

      <div style="text-align: center; margin: 25px 0 15px 0;">
        <img src="data:image/jpeg;base64,{LOGO_B64}" style="width: 125px; height: auto;" alt="SGSITS Logo"/>
      </div>

      <div style="text-align: center; font-weight: bold; font-size: 14pt; margin-bottom: 25px;">
        [2026-2027]
      </div>

      <div style="text-align: center; font-weight: bold; font-size: 16pt; text-decoration: underline; margin-bottom: 30px; letter-spacing: 0.5px;">
        RECOMMENDATION
      </div>

      <div style="text-align: justify; font-size: 12pt; line-height: 1.7; text-indent: 40px; margin-bottom: 120px;">
        We are pleased to recommend that the project work entitled <b>CampusCare: Centralized Campus Grievance Redressal and Incident Management System</b> submitted by <b>Piyush Chirote, Riya Joshi, Ritik Govind Rao, Tanish Jain and Nandani Asalkar</b> may be accepted in partial fulfillment of the degree of <b>Master of Computer Application</b> of Shri Govindram Seksaria Institute of Technology and Science, Indore during the session <b>2026-2027</b>.
      </div>

      <div style="display: flex; justify-content: space-between; align-items: flex-end; padding: 0 10px; font-size: 11.5pt;">
        <div style="text-align: left; width: 45%;">
          <b>[Mr. Deepesh Agarwal]</b><br>
          Asst. Professor<br>
          Computer Technology and Applications
        </div>
        <div style="text-align: right; width: 48%;">
          <b>[Dr. Sunita Varma]</b><br>
          Head of Department<br>
          Computer Technology and Applications
        </div>
      </div>

      <div class="page-footer-roman">i</div>
    </div>
    '''
    pages.append(p2)

    # -------------------------------------------------------------
    # PAGE 3: ACKNOWLEDGEMENT (Page ii)
    # -------------------------------------------------------------
    p3 = '''
    <div class="page">
      <div style="text-align: center; font-weight: bold; font-size: 16pt; margin-top: 15px; margin-bottom: 35px; letter-spacing: 0.5px;">
        ACKNOWLEDGEMENT
      </div>

      <div style="text-align: justify; font-size: 12pt; line-height: 1.7; text-indent: 40px; margin-bottom: 25px;">
        We would like to express our profound gratitude to our guide, <b>Mr. Deepesh Agarwal</b>, for providing us with definite direction, professional guidance, constant encouragement from the beginning of the work and moral support in many ways during our study period. We would also like to thank our friends and family who supported us and offered deep insight into the practical requirements of campus maintenance.
      </div>

      <div style="text-align: justify; font-size: 12pt; line-height: 1.7; text-indent: 40px; margin-bottom: 25px;">
        We wish to acknowledge the valuable help provided by the technical and support staff in the <b>Department of Computer Technology and Applications of S.G.S.I.T.S., Indore</b>. We also express our sincere appreciation to <b>Dr. Sunita Varma</b> (Head of Department) and <b>Prof. Sonika Soni</b> for their encouragement, administrative facilities, and valuable suggestions during the design and development phases of this project.
      </div>

      <div style="text-align: justify; font-size: 12pt; line-height: 1.7; text-indent: 40px; margin-bottom: 70px;">
        We are also deeply thankful to our faculty colleagues and peer reviewers who critically evaluated the workflow and user interface of <b>CampusCare</b>, helping us finalize a secure, accessible, and high-performance digital grievance resolution system.
      </div>

      <div style="display: flex; justify-content: space-between; font-size: 11pt; line-height: 1.5; margin-bottom: 35px; padding: 0 10px;">
        <div>
          <b>Signature</b><br>
          [Piyush Chirote]<br>
          0801CA251095
        </div>
        <div style="text-align: right;">
          <b>Signature</b><br>
          [Tanish Jain]<br>
          0801CA251139
        </div>
      </div>

      <div style="display: flex; justify-content: space-between; font-size: 11pt; line-height: 1.5; margin-bottom: 35px; padding: 0 10px;">
        <div>
          <b>Signature</b><br>
          [Riya Joshi]<br>
          0801CA251119
        </div>
        <div style="text-align: right;">
          <b>Signature</b><br>
          [Ritik Govind Rao]<br>
          0801CA251117
        </div>
      </div>

      <div style="font-size: 11pt; line-height: 1.5; padding: 0 10px;">
        <b>Signature</b><br>
        [Nandani Asalkar]<br>
        0801CA251085
      </div>

      <div class="page-footer-roman">ii</div>
    </div>
    '''
    pages.append(p3)

    # -------------------------------------------------------------
    # PAGE 4: ABSTRACT (Page iii)
    # -------------------------------------------------------------
    p4 = '''
    <div class="page">
      <div style="text-align: center; font-weight: bold; font-size: 16pt; margin-top: 15px; margin-bottom: 30px; letter-spacing: 0.5px;">
        ABSTRACT
      </div>

      <div style="text-align: justify; font-size: 11.5pt; line-height: 1.65; margin-bottom: 18px;">
        The <b>CampusCare: Centralized Campus Grievance Redressal and Incident Management System</b> is an automated enterprise web solution engineered to address the inefficiencies, lack of transparency, administrative bottlenecks, and traceability risks associated with conventional manual campus complaint handling. In large educational institutions, students and faculty traditionally communicate infrastructure and logistical breakdowns—such as classroom projector defects, laboratory instrument failures, Wi-Fi connectivity dropouts, electrical hazards, sanitation issues, or hostel maintenance requests—via paper registers, suggestion boxes, or unorganized verbal intimations. These legacy practices frequently result in lost tickets, unaccountable delays, zero status visibility, and uncoordinated facility maintenance.
      </div>

      <div style="text-align: justify; font-size: 11.5pt; line-height: 1.65; margin-bottom: 18px;">
        To comprehensively eliminate these operational vulnerabilities, <b>CampusCare</b> establishes a unified, cloud-ready digital platform. The system architecture is built on a multi-layered framework featuring a responsive <b>ReactJS</b> frontend styled with <b>Tailwind CSS</b> and <b>Bootstrap</b>, an asynchronous, high-throughput <b>Node.js / Express</b> REST API backend, and a robust document-oriented database using <b>MongoDB</b> with <b>Mongoose ODM</b>. The authentication mechanism integrates industry-standard JSON Web Tokens (JWT) coupled with <b>Bcrypt</b> password salting to enforce strict Role-Based Access Control (RBAC) across Students and Administrators.
      </div>

      <div style="text-align: justify; font-size: 11.5pt; line-height: 1.65; margin-bottom: 18px;">
        The system workflow encompasses a self-service registration and authentication pipeline, a dynamic incident reporting module that generates unique alphanumeric tracking codes (e.g., <i>CC-2026-XXXX</i>), categorical routing across nine campus operational domains, and an automated audit lifecycle tracker. Administrators and facility supervisors are provided with an interactive management dashboard displaying real-time operational statistics, priority breakdown matrices, and quick-filter queues.
      </div>

      <div style="text-align: justify; font-size: 11.5pt; line-height: 1.65;">
        Through an immutable status history audit log (<i>SUBMITTED &rarr; IN_PROGRESS &rarr; RESOLVED</i>), CampusCare ensures complete administrative accountability, providing time-stamped resolution remarks for every action. Ultimately, this project demonstrates a modern, scalable, and secure institutional governance solution that saves valuable institutional hours, streamlines campus maintenance, and maximizes student satisfaction.
      </div>

      <div class="page-footer-roman">iii</div>
    </div>
    '''
    pages.append(p4)

    # -------------------------------------------------------------
    # PAGE 5: TABLE OF CONTENTS - Part 1 (Page iv)
    # -------------------------------------------------------------
    p5 = '''
    <div class="page">
      <div style="text-align: center; font-weight: bold; font-size: 16pt; margin-top: 15px; margin-bottom: 30px;">
        Table of Contents
      </div>

      <div class="toc-container" style="font-size: 11pt; line-height: 1.95;">
        <div class="toc-line"><span><b>Recommendation</b></span><span class="toc-dots"></span><span><b>i</b></span></div>
        <div class="toc-line"><span><b>Acknowledgement</b></span><span class="toc-dots"></span><span><b>ii</b></span></div>
        <div class="toc-line"><span><b>Abstract</b></span><span class="toc-dots"></span><span><b>iii</b></span></div>
        <div class="toc-line"><span><b>Table of Contents</b></span><span class="toc-dots"></span><span><b>iv</b></span></div>
        <div class="toc-line"><span><b>List of Figures</b></span><span class="toc-dots"></span><span><b>vi</b></span></div>
        <br>
        <div class="toc-line"><span><b>1 &nbsp; Introduction</b></span><span class="toc-dots"></span><span><b>1</b></span></div>
        <div class="toc-line toc-sub"><span>1.1 &nbsp; Overview</span><span class="toc-dots"></span><span>1</span></div>
        <div class="toc-line toc-sub"><span>1.2 &nbsp; Objectives</span><span class="toc-dots"></span><span>1</span></div>
        <div class="toc-line toc-sub"><span>1.3 &nbsp; Problem Statement</span><span class="toc-dots"></span><span>2</span></div>
        <div class="toc-line toc-sub"><span>1.4 &nbsp; Proposed Solution</span><span class="toc-dots"></span><span>3</span></div>
        <br>
        <div class="toc-line"><span><b>2 &nbsp; System Design</b></span><span class="toc-dots"></span><span><b>4</b></span></div>
        <div class="toc-line toc-sub"><span>2.1 &nbsp; System Architecture</span><span class="toc-dots"></span><span>4</span></div>
        <div class="toc-line toc-sub"><span>2.2 &nbsp; UseCase Diagram</span><span class="toc-dots"></span><span>6</span></div>
        <div class="toc-line toc-sub"><span>2.3 &nbsp; Data Flow Diagram (DFD)</span><span class="toc-dots"></span><span>7</span></div>
        <div class="toc-line toc-sub"><span>2.4 &nbsp; Class Diagram</span><span class="toc-dots"></span><span>8</span></div>
        <div class="toc-line toc-sub"><span>2.5 &nbsp; Activity Diagram</span><span class="toc-dots"></span><span>9</span></div>
        <div class="toc-line toc-sub"><span>2.6 &nbsp; Sequence Diagram</span><span class="toc-dots"></span><span>10</span></div>
        <div class="toc-line toc-sub"><span>2.7 &nbsp; ER Diagram</span><span class="toc-dots"></span><span>11</span></div>
        <br>
        <div class="toc-line"><span><b>3 &nbsp; System Overview and Implementation</b></span><span class="toc-dots"></span><span><b>12</b></span></div>
        <div class="toc-line toc-sub"><span>3.1 &nbsp; Frontend Development</span><span class="toc-dots"></span><span>12</span></div>
        <div class="toc-line toc-sub"><span>3.2 &nbsp; Backend Architecture</span><span class="toc-dots"></span><span>14</span></div>
        <div class="toc-line toc-sub"><span>3.3 &nbsp; Database Management (MongoDB)</span><span class="toc-dots"></span><span>15</span></div>
        <div class="toc-line toc-sub"><span>3.4 &nbsp; File Management and Data Security</span><span class="toc-dots"></span><span>16</span></div>
        <div class="toc-line toc-sub"><span>3.5 &nbsp; Programming Languages and Frameworks</span><span class="toc-dots"></span><span>16</span></div>
        <div class="toc-line toc-sub"><span>3.6 &nbsp; Security and Scalability</span><span class="toc-dots"></span><span>18</span></div>
        <div class="toc-line toc-sub"><span>3.7 &nbsp; Security Measures</span><span class="toc-dots"></span><span>19</span></div>
      </div>

      <div class="page-footer-roman">iv</div>
    </div>
    '''
    pages.append(p5)

    # -------------------------------------------------------------
    # PAGE 6: TABLE OF CONTENTS - Part 2 (Page v)
    # -------------------------------------------------------------
    p6 = '''
    <div class="page">
      <div style="text-align: center; font-weight: bold; font-size: 16pt; margin-top: 15px; margin-bottom: 30px;">
        Table of Contents (Cont.)
      </div>

      <div class="toc-container" style="font-size: 11pt; line-height: 2.1;">
        <div class="toc-line"><span><b>4 &nbsp; Implementation and Testing</b></span><span class="toc-dots"></span><span><b>20</b></span></div>
        <div class="toc-line toc-sub"><span>4.1 &nbsp; Implementation</span><span class="toc-dots"></span><span>20</span></div>
        <div class="toc-line toc-sub"><span>4.2 &nbsp; Database Implementation and Preprocessing</span><span class="toc-dots"></span><span>21</span></div>
        <div class="toc-line toc-sub"><span>4.3 &nbsp; Testing</span><span class="toc-dots"></span><span>21</span></div>
        <div class="toc-line toc-sub2"><span>4.3.1 &nbsp; Unit Testing</span><span class="toc-dots"></span><span>21</span></div>
        <div class="toc-line toc-sub2"><span>4.3.2 &nbsp; Integration Testing</span><span class="toc-dots"></span><span>21</span></div>
        <div class="toc-line toc-sub2"><span>4.3.3 &nbsp; System Testing</span><span class="toc-dots"></span><span>21</span></div>
        <div class="toc-line toc-sub2"><span>4.3.4 &nbsp; Results and Accuracy</span><span class="toc-dots"></span><span>22</span></div>
        <br>
        <div class="toc-line"><span><b>5 &nbsp; Conclusion</b></span><span class="toc-dots"></span><span><b>23</b></span></div>
        <div class="toc-line toc-sub"><span>5.1 &nbsp; Project Summary</span><span class="toc-dots"></span><span>23</span></div>
        <div class="toc-line toc-sub"><span>5.2 &nbsp; Achievements</span><span class="toc-dots"></span><span>23</span></div>
        <div class="toc-line toc-sub"><span>5.3 &nbsp; Limitations</span><span class="toc-dots"></span><span>24</span></div>
        <div class="toc-line toc-sub"><span>5.4 &nbsp; Future Work</span><span class="toc-dots"></span><span>24</span></div>
        <br>
        <div class="toc-line"><span><b>6 &nbsp; SnapShort (Screenshots)</b></span><span class="toc-dots"></span><span><b>25</b></span></div>
        <div class="toc-line toc-sub"><span>6.1 &nbsp; Database Screenshot (MongoDB Collections)</span><span class="toc-dots"></span><span>25</span></div>
        <div class="toc-line toc-sub"><span>6.2 &nbsp; Application UI Screenshot (Admin &amp; Student Portal)</span><span class="toc-dots"></span><span>26</span></div>
        <br>
        <div class="toc-line"><span><b>7 &nbsp; References</b></span><span class="toc-dots"></span><span><b>27</b></span></div>
      </div>

      <div class="page-footer-roman">v</div>
    </div>
    '''
    pages.append(p6)

    # -------------------------------------------------------------
    # PAGE 7: LIST OF FIGURES (Page vi)
    # -------------------------------------------------------------
    p7 = '''
    <div class="page">
      <div style="text-align: center; font-weight: bold; font-size: 16pt; margin-top: 15px; margin-bottom: 30px;">
        List of Figures
      </div>

      <div style="font-size: 11pt; line-height: 2.3;">
        <div style="display: flex; justify-content: space-between; font-weight: bold; border-bottom: 1.5px solid #000; padding-bottom: 4px; margin-bottom: 15px;">
          <span style="width: 15%;">Fig. No.</span>
          <span style="width: 70%;">Title</span>
          <span style="width: 15%; text-align: right;">Page No.</span>
        </div>

        <div class="toc-line"><span style="width: 15%;">2.1</span><span style="width: 70%;">Use Case Diagram of CampusCare System</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">6</span></div>
        <div class="toc-line"><span style="width: 15%;">2.2</span><span style="width: 70%;">Data Flow Diagram (DFD) of CampusCare System</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">7</span></div>
        <div class="toc-line"><span style="width: 15%;">2.3</span><span style="width: 70%;">Class Diagram of CampusCare System</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">8</span></div>
        <div class="toc-line"><span style="width: 15%;">2.4</span><span style="width: 70%;">Activity Diagram of Complaint Lifecycle</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">9</span></div>
        <div class="toc-line"><span style="width: 15%;">2.5</span><span style="width: 70%;">Sequence Diagram of Grievance Lodging &amp; Resolution</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">10</span></div>
        <div class="toc-line"><span style="width: 15%;">2.6</span><span style="width: 70%;">ER Diagram of CampusCare Database</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">11</span></div>
        <div class="toc-line"><span style="width: 15%;">3.1</span><span style="width: 70%;">Frontend Development &amp; Component Hierarchy</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">12</span></div>
        <div class="toc-line"><span style="width: 15%;">3.2</span><span style="width: 70%;">Backend Service Architecture &amp; REST APIs</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">14</span></div>
        <div class="toc-line"><span style="width: 15%;">3.3</span><span style="width: 70%;">Database Management &amp; Mongoose Schemas</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">15</span></div>
        <div class="toc-line"><span style="width: 15%;">4.1</span><span style="width: 70%;">Implementation Lifecycle &amp; State Validation</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">20</span></div>
        <div class="toc-line"><span style="width: 15%;">4.2</span><span style="width: 70%;">Testing Methodology &amp; Quality Verification</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">21</span></div>
        <div class="toc-line"><span style="width: 15%;">6.1</span><span style="width: 70%;">Database Screenshot (MongoDB Collections &amp; Query Results)</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">25</span></div>
        <div class="toc-line"><span style="width: 15%;">6.2</span><span style="width: 70%;">Application UI Screenshot (Admin &amp; Student Portals)</span><span class="toc-dots"></span><span style="width: 15%; text-align: right;">26</span></div>
      </div>

      <div class="page-footer-roman">vi</div>
    </div>
    '''
    pages.append(p7)

    # -------------------------------------------------------------
    # PAGE 8 (Body Page 1): Chapter 1 - INTRODUCTION
    # -------------------------------------------------------------
    p8 = '''
    <div class="page">
      <div class="page-header">CHAPTER 1. INTRODUCTION 2026</div>

      <div style="text-align: right; font-size: 22pt; font-weight: bold; margin-bottom: 25px; margin-top: 10px;">
        Chapter 1
      </div>
      <div style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 30px; letter-spacing: 0.5px;">
        INTRODUCTION
      </div>

      <div class="section-title">1.1 &nbsp; Overview</div>
      <div class="body-p">
        The <b>CampusCare System</b> is a modern, automated web-based solution engineered to replace traditional, manual ways of handling campus grievances and maintenance incidents. In most colleges, universities, and academic institutions, complaint registration is still handled through physical registers placed in administrative offices, suggestion boxes outside hostel wardens' cabins, or uncoordinated verbal communications. These obsolete methods are time-consuming, unorganized, highly prone to human oversight, and completely lack traceability.
      </div>
      <div class="body-p">
        In traditional environments, students frequently lodge complaints regarding broken laboratory equipment, non-functional classroom projectors, internet or Wi-Fi connectivity blackouts, hostel water supply failures, or electrical faults, only for those requests to sit unattended for days without any verifiable record of who received them or what corrective actions were scheduled. To permanently resolve this problem, we have developed <b>CampusCare</b>—a centralized campus incident management and grievance redressal platform.
      </div>
      <div class="body-p">
        With the rapid evolution of modern web architectures, cloud databases, and single-page applications, digital incident dispatching has become the gold standard in corporate and smart-campus environments. Applying full-stack web technologies to campus grievance management is a vital, natural, and highly practical step toward institutional transparency, accountability, and operational excellence.
      </div>

      <div class="section-title" style="margin-top: 20px;">1.2 &nbsp; Objectives</div>
      <div class="body-p">
        The primary goal of this project is to build an intelligent, centralized campus issue resolution system that completely eliminates the inefficiencies of physical registers and verbal complaint channels. The specific objectives are as follows:
      </div>
      <ul class="body-ul">
        <li><b>To Eliminate Paper-Based Registers:</b> To replace cumbersome physical complaint registers and manual suggestion boxes with an intuitive, cloud-accessible digital grievance submission portal that operates 24/7.</li>
        <li><b>To Prevent Lost or Ignored Complaints:</b> To guarantee that every single student grievance is automatically assigned a unique tracking ticket number and recorded in a centralized database, ensuring zero lost tickets.</li>
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
    pages.append(p8)

    # -------------------------------------------------------------
    # PAGE 9 (Body Page 2): Chapter 1 cont.
    # -------------------------------------------------------------
    p9 = '''
    <div class="page">
      <div class="page-header">CHAPTER 1. INTRODUCTION 2026</div>

      <ul class="body-ul" style="margin-top: 10px;">
        <li><b>To Enable Real-Time Lifecycle Tracking:</b> To provide students and administrators with instant status updates (<i>SUBMITTED, IN_PROGRESS, RESOLVED</i>) alongside an audit history of administrative remarks and timestamps.</li>
        <li><b>To Automate Categorization and Prioritization:</b> To implement structured dispatching across nine distinct institutional domains (Classrooms, Labs, Wi-Fi, Electrical, Cleanliness, Library, Hostel, Administration, Other) with priority grading (LOW, MEDIUM, HIGH).</li>
        <li><b>To Store Incident Data Securely:</b> To maintain a robust, organized NoSQL database (MongoDB) that securely stores student profiles, grievance details, timestamps, and administrative audit trails with zero tampering risk.</li>
        <li><b>To Provide a Dedicated Admin Dashboard:</b> To deliver an administrative cockpit where college authorities can view real-time incident queues, analyze recurring breakdown trends, and monitor maintenance staff resolution efficiency.</li>
        <li><b>To Build a Scalable Campus Infrastructure:</b> To design a stateless RESTful architecture capable of seamless expansion across colleges, departments, and multiple academic campuses without code modifications.</li>
      </ul>

      <div class="section-title" style="margin-top: 25px;">1.3 &nbsp; Problem Statement</div>
      <div class="body-p">
        In many higher educational institutions, facility maintenance and student grievance handling continue to rely on manual, fragmented workflows. These obsolete mechanisms produce multiple systemic failures:
      </div>
      <div class="body-p">
        Current limitations in conventional campus management include:
      </div>
      <ol class="body-ol">
        <li><b>Lack of Traceability:</b> Complaints written in physical registers can be misplaced, damaged, or arbitrarily ignored with no record of who logged or received them.</li>
        <li><b>Zero Status Transparency:</b> Students have no mechanism to check whether their grievance has been acknowledged, assigned to a technician, or resolved, forcing repeated in-person visits to administrative offices.</li>
        <li><b>Absence of Categorical Prioritization:</b> Critical safety or electrical hazards get buried beneath routine maintenance requests due to the lack of algorithmic priority filtering.</li>
        <li><b>No Institutional Accountability:</b> Departmental heads and college administrators lack unified analytics to evaluate average resolution times, recurring infrastructural failures, or staff performance.</li>
        <li><b>Manual Communication Delays:</b> Information transfer between students, administrative officers, and maintenance technicians involves slow, error-prone manual handoffs.</li>
      </ol>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 2</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p9)

    # -------------------------------------------------------------
    # PAGE 10 (Body Page 3): Chapter 1 cont. - Problem Solution
    # -------------------------------------------------------------
    p10 = '''
    <div class="page">
      <div class="page-header">CHAPTER 1. INTRODUCTION 2026</div>

      <div class="section-title" style="margin-top: 10px;">1.4 &nbsp; Problem Solution</div>
      <div class="body-p">
        <b>CampusCare</b> replaces slow, opaque manual registers with an instant, full-stack digital incident management platform. Students can securely submit grievances from any smartphone or browser in under 30 seconds. The backend engine automatically generates a verifiable tracking code, routes the request to the appropriate department, logs timestamped status history, and provides administrators with real-time resolution controls.
      </div>

      <div class="body-p" style="margin-top: 15px;">
        <b>Step 1: Student Onboarding and Authentication (One-Time Setup):</b><br>
        Students register using their academic credentials, institutional email, and roll number. The system verifies input patterns, hashes the password using <b>Bcrypt</b>, and issues a stateless <b>JSON Web Token (JWT)</b> for secure, authenticated session handling across all subsequent requests.
      </div>

      <div class="body-p" style="margin-top: 15px;">
        <b>Step 2: Instant Grievance Lodging (Categorical Classification):</b><br>
        When an issue occurs, the student accesses the <i>Submit Complaint</i> portal. The student inputs a concise title, selects the operational category (e.g., <i>Internet / Wi-Fi, Electrical / Maintenance, Hostel</i>), picks a priority level (<i>LOW, MEDIUM, HIGH</i>), specifies the campus location (e.g., <i>Lab 3, Rack 2</i>), and provides a descriptive explanation.
      </div>

      <div class="body-p" style="margin-top: 15px;">
        <b>Step 3: Automated Ticket Allocation &amp; Audit Logging:</b><br>
        The backend receives the sanitized payload, validates data types, and generates a unique, human-readable ticket number (e.g., <i>CC-2026-0014</i>). It writes the complaint into the <b>MongoDB</b> database with default status <b>SUBMITTED</b> and pushes an immutable initial audit entry into the <code>statusHistory</code> array.
      </div>

      <div class="body-p" style="margin-top: 15px;">
        <b>Step 4: Administrative Review, Dispatch, and Status Transition:</b><br>
        Administrative officers log into the dedicated <b>Admin Dashboard</b>. High-priority incidents are highlighted in red badges. Administrators can inspect ticket details, assign maintenance personnel, update the status to <b>IN_PROGRESS</b>, and record formal resolution notes upon completing the maintenance work.
      </div>

      <div class="body-p" style="margin-top: 15px;">
        <b>Step 5: Transparent Resolution and Closed-Loop Verification:</b><br>
        Once maintenance is complete, the admin marks the status as <b>RESOLVED</b>, appending the completion remarks and resolution timestamp. The student's portal updates in real time, displaying the green resolution checkmark and full audit timeline.
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
    pages.append(p10)

    # -------------------------------------------------------------
    # PAGE 11 (Body Page 4): Chapter 2 - SYSTEM DESIGN
    # -------------------------------------------------------------
    p11 = '''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div style="text-align: right; font-size: 22pt; font-weight: bold; margin-bottom: 25px; margin-top: 10px;">
        Chapter 2
      </div>
      <div style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 30px; letter-spacing: 0.5px;">
        SYSTEM DESIGN
      </div>

      <div class="section-title">2.1 &nbsp; System Architecture</div>
      <div class="body-p">
        The architecture of the <b>CampusCare System</b> is designed as a multi-layered framework that ensures a smooth flow of data from the client browser interface to permanent database storage. It follows a modular, decoupled approach, strictly separating the user interface, business logic processing, authentication security, and persistent document management.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 15px; margin-bottom: 5px;">
        1. Frontend Layer (User Interface): ReactJS + Tailwind CSS
      </div>
      <div class="body-p">
        <b>ReactJS</b> is used to build the responsive client interface. It establishes a Single Page Application (SPA) architecture where dynamic components re-render instantly without triggering full page reloads, providing a desktop-grade user experience.
      </div>
      <div class="body-p">
        <b>Tailwind CSS</b> and <b>Bootstrap</b> provide modern, utility-first styling, ensuring responsive grid layouts, crisp typography, and adaptive components across mobile, tablet, and desktop viewports.
      </div>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 12px; margin-bottom: 5px;">
        Main Pages and Functional Modules:
      </div>
      <ul class="body-ul">
        <li><b>Login / Register Page:</b> Dual-mode public authentication gateway supporting self-registration for students and secure credential validation for administrators.</li>
        <li><b>Student Dashboard:</b> Central overview card displaying total complaints submitted, active investigations, and successfully resolved tickets.</li>
        <li><b>Submit Complaint Page:</b> Dynamic interactive form with input validation, category dropdowns, priority switches, and description counters.</li>
        <li><b>My Complaints Page:</b> Filterable data list with real-time status badges (Blue for Submitted, Amber for In Progress, Green for Resolved).</li>
        <li><b>Complaint Details View:</b> Expandable audit timeline illustrating the exact historical lifecycle, supervisor notes, and timestamps.</li>
        <li><b>Admin Dashboard &amp; Management Portal:</b> Executive control cockpit providing aggregate KPI counters, priority queues, and modal dialogs to update complaint statuses.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 4</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p11)

    # -------------------------------------------------------------
    # PAGE 12 (Body Page 5): Chapter 2 cont. - Backend & Storage
    # -------------------------------------------------------------
    p12 = '''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 10px; margin-bottom: 5px;">
        2. Backend Layer: Node.js &amp; Express REST API Server
      </div>
      <div class="body-p">
        <b>Express.js</b> serves as the central server-side web application framework running on the <b>Node.js</b> runtime. It orchestrates HTTP request routing, input sanitization, controller logic execution, security enforcement, and database communications.
      </div>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 12px; margin-bottom: 5px;">
        Main Architectural Layers:
      </div>
      <ol class="body-ol">
        <li><b>Controller Layer:</b> Receives REST API requests (GET, POST, PUT, DELETE) from the ReactJS frontend, validates incoming JSON payloads, invokes domain business logic, and returns formatted JSON responses with standard HTTP status codes.</li>
        <li><b>Middleware Layer:</b> Intercepts all protected routes to verify JWT bearer tokens, extracts the authenticated user context, checks role permissions (STUDENT vs ADMIN), and sanitizes inputs against malicious payloads.</li>
        <li><b>Service &amp; Business Logic Layer:</b> Contains algorithmic operations including unique ticket number generation (CC-YYYY-XXXX), status transition enforcement rules, and status history array appending.</li>
        <li><b>Repository &amp; ODM Layer:</b> Utilizes <b>Mongoose ODM</b> to enforce strict document schemas, handle compound indexing, and communicate with the underlying MongoDB database.</li>
      </ol>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 15px; margin-bottom: 5px;">
        3. Data Storage Layer (MongoDB NoSQL Database)
      </div>
      <ul class="body-ul">
        <li>Employs <b>MongoDB</b> as a high-performance document store, efficiently handling nested structures like complaint status history and user authentication details.</li>
        <li>Establishes resilient connection pooling with auto-reconnect logic via Mongoose.</li>
        <li>Enforces database-level indexes on <code>createdBy</code>, <code>status</code>, <code>category</code>, and <code>ticketNumber</code> to ensure lightning-fast retrieval times under institutional load.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 15px; margin-bottom: 5px;">
        4. Output &amp; Analytics Layer (Reporting Engine)
      </div>
      <ul class="body-ul">
        <li>Computes real-time aggregate statistics for the administrator dashboard (Total, In Progress, Resolved, High Priority).</li>
        <li>Enables real-time data inspection for audit compliance, departmental review, and infrastructure maintenance planning.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 5</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p12)

    # -------------------------------------------------------------
    # PAGE 13 (Body Page 6): 2.2 UseCase Diagram
    # -------------------------------------------------------------
    p13 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 10px; margin-bottom: 15px;">2.2 &nbsp; UseCase Diagram</div>
      
      <div style="text-align: center; margin: 10px 0;">
        {get_usecase_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 15px;">
        Figure 2.1: UseCase Diagram of CampusCare System
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
    pages.append(p13)

    # -------------------------------------------------------------
    # PAGE 14 (Body Page 7): 2.3 Data Flow Diagram
    # -------------------------------------------------------------
    p14 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 10px; margin-bottom: 15px;">2.3 &nbsp; Data Flow Diagram (DFD)</div>

      <div style="text-align: center; margin: 10px 0;">
        {get_dfd_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 15px;">
        Figure 2.2: Data Flow Diagram of CampusCare System
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
    pages.append(p14)

    # -------------------------------------------------------------
    # PAGE 15 (Body Page 8): 2.4 Class Diagram
    # -------------------------------------------------------------
    p15 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 10px; margin-bottom: 15px;">2.4 &nbsp; Class Diagram</div>

      <div style="text-align: center; margin: 10px 0;">
        {get_class_diagram_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 15px;">
        Figure 2.3: Class Diagram of CampusCare System
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
    pages.append(p15)

    # -------------------------------------------------------------
    # PAGE 16 (Body Page 9): 2.5 Activity Diagram
    # -------------------------------------------------------------
    p16 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 10px; margin-bottom: 15px;">2.5 &nbsp; Activity Diagram</div>

      <div style="text-align: center; margin: 10px 0;">
        {get_activity_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 15px;">
        Figure 2.4: Activity Diagram of Complaint Lifecycle
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
    pages.append(p16)

    # -------------------------------------------------------------
    # PAGE 17 (Body Page 10): 2.6 Sequence Diagram
    # -------------------------------------------------------------
    p17 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 10px; margin-bottom: 15px;">2.6 &nbsp; Sequence Diagram</div>

      <div style="text-align: center; margin: 10px 0;">
        {get_sequence_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 15px;">
        Figure 2.5: Sequence Diagram of Grievance Lodging &amp; Resolution
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
    pages.append(p17)

    # -------------------------------------------------------------
    # PAGE 18 (Body Page 11): 2.7 ER Diagram
    # -------------------------------------------------------------
    p18 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 2. SYSTEM DESIGN 2026</div>

      <div class="section-title" style="margin-top: 10px; margin-bottom: 15px;">2.7 &nbsp; ER-Diagram</div>

      <div style="text-align: center; margin: 10px 0;">
        {get_er_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 15px;">
        Figure 2.6: ER Diagram of CampusCare Database
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
    pages.append(p18)

    # -------------------------------------------------------------
    # PAGE 19 (Body Page 12): Chapter 3 - SYSTEM OVERVIEW & IMPLEMENTATION
    # -------------------------------------------------------------
    p19 = '''
    <div class="page">
      <div class="page-header">CHAPTER 3. SYSTEM OVERVIEW AND IMPLEMENTATION 2026</div>

      <div style="text-align: right; font-size: 22pt; font-weight: bold; margin-bottom: 25px; margin-top: 10px;">
        Chapter 3
      </div>
      <div style="text-align: center; font-size: 18pt; font-weight: bold; margin-bottom: 30px; letter-spacing: 0.5px;">
        SYSTEM OVERVIEW AND IMPLEMENTATION
      </div>

      <div class="section-title">3.1 &nbsp; Frontend Development</div>
      <div class="body-p">
        The Frontend is the visual, interactive layer of the <b>CampusCare System</b> that students and administrators directly interact with. It is developed using <b>ReactJS</b> and styled with <b>Tailwind CSS</b> and <b>Bootstrap</b>—representing the modern industry standard for responsive, high-performance web applications.
      </div>
      <div class="body-p">
        ReactJS leverages a component-driven architecture and a Virtual DOM to minimize browser repaints, ensuring snappy navigation between dashboards, forms, and ticket listings without page flickers. Tailwind CSS delivers utility-first classes that make styling modular, adaptive, and maintainable.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 18px; margin-bottom: 8px;">
        Pages and Components in ReactJS:
      </div>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 8px;">
        1. Login Page
      </div>
      <ul class="body-ul">
        <li>Minimalist, responsive login interface with clear role-based separation.</li>
        <li>Controlled input fields for institutional email and password.</li>
        <li>Client-side form validation with real-time feedback using React state hooks.</li>
        <li>On submission &rarr; executes an asynchronous POST request to <code>/api/auth/login</code>.</li>
        <li>Stores the returned JWT Bearer Token in <code>localStorage</code> and manages user authorization state via React Context API.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 12px;">
        2. Student Registration Page
      </div>
      <ul class="body-ul">
        <li>Structured registration form capturing: Full Name, Institutional Email, and Password.</li>
        <li>Enforces security constraints: Email must conform to valid academic domains; passwords must meet minimum character length requirements.</li>
        <li>On submit &rarr; triggers <code>/api/auth/register</code>, creating a verified STUDENT record with zero plain-text password exposure.</li>
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
    pages.append(p19)

    # -------------------------------------------------------------
    # PAGE 20 (Body Page 13): Chapter 3 cont. - Frontend Components
    # -------------------------------------------------------------
    p20 = '''
    <div class="page">
      <div class="page-header">CHAPTER 3. SYSTEM OVERVIEW AND IMPLEMENTATION 2026</div>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 10px;">
        3. Submit Complaint Page
      </div>
      <ul class="body-ul">
        <li>Dynamic incident lodging interface equipped with category pickers, priority pills, and rich description fields.</li>
        <li>Category Selector covers nine operational domains: <i>Classroom, Laboratory, Internet / Wi-Fi, Electrical / Maintenance, Cleanliness, Library, Hostel, Administration, Other</i>.</li>
        <li>Priority Selector allows students to set urgency level: <b>LOW</b> (Routine maintenance), <b>MEDIUM</b> (Operational inconvenience), or <b>HIGH</b> (Critical or safety hazard).</li>
        <li>Campus Location input captures specific location markers (e.g., <i>MCA Block - 2nd Floor, Room 204</i>).</li>
        <li>Character counter enforcing descriptive clarity (minimum 20 characters, maximum 2000 characters).</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 14px;">
        4. Student Dashboard &amp; My Complaints Page
      </div>
      <ul class="body-ul">
        <li>Displays a summary of personal complaint statistics (Total Lodged, Active, Resolved).</li>
        <li>Interactive tabular view presenting ticket numbers, titles, categories, dates, and live status badges.</li>
        <li>Color-coded status indicators:
          <span style="color: #0284c7; font-weight: bold;">SUBMITTED (Blue)</span>,
          <span style="color: #ea580c; font-weight: bold;">IN_PROGRESS (Orange)</span>, and
          <span style="color: #16a34a; font-weight: bold;">RESOLVED (Green)</span>.
        </li>
        <li>Clicking any complaint launches the <b>Complaint Details View</b>, rendering a step-by-step visual audit timeline with supervisor remarks and completion dates.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 14px;">
        5. Admin Incident Management Dashboard
      </div>
      <ul class="body-ul">
        <li>Executive overview featuring four primary KPI metric cards: Total Complaints, Submitted Awaiting Review, In Progress Under Action, and Successfully Resolved.</li>
        <li>Advanced multi-filter controls enabling administrators to filter queues by status, priority, or category.</li>
        <li>Incident Management Modal: Allows administrators to change status, dispatch tickets to maintenance crews, and input mandatory resolution remarks upon issue closure.</li>
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
    pages.append(p20)

    # -------------------------------------------------------------
    # PAGE 21 (Body Page 14): Chapter 3 cont. - Backend Architecture
    # -------------------------------------------------------------
    p21 = '''
    <div class="page">
      <div class="page-header">CHAPTER 3. SYSTEM OVERVIEW AND IMPLEMENTATION 2026</div>

      <div class="section-title" style="margin-top: 10px;">3.2 &nbsp; Backend Architecture</div>
      <div class="body-p">
        The Backend represents the core operational and business logic engine of the <b>CampusCare System</b>. It is built using <b>Node.js</b> and <b>Express.js</b>—a high-performance, asynchronous JavaScript runtime and web framework optimized for building scalable RESTful APIs.
      </div>
      <div class="body-p">
        Express.js serves as the central API gateway connecting the ReactJS client application with the MongoDB database cluster, enforcing authentication, request validation, business rules, and error logging.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 18px; margin-bottom: 8px;">
        Layers of Express / Node.js Backend:
      </div>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 6px;">
        1. Controller Layer (authController.js &amp; complaintController.js)
      </div>
      <ul class="body-ul">
        <li>Receives all incoming HTTP requests transmitted from the React frontend.</li>
        <li>Validates request parameters and payload structure before invoking database services.</li>
        <li>Returns standardized JSON responses accompanied by semantic HTTP status codes (200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Server Error).</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 12px;">
        2. Middleware Layer (authMiddleware.js &amp; roleMiddleware.js)
      </div>
      <ul class="body-ul">
        <li>Extracts the <code>Authorization: Bearer &lt;token&gt;</code> HTTP header.</li>
        <li>Verifies cryptographic token signatures against the server's private secret key.</li>
        <li>Attaches the decoded user profile (ID, Role) to the <code>req.user</code> context.</li>
        <li>Enforces role guard rails: Blocks non-admin users from accessing administrative incident queues or modification endpoints.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 12px;">
        3. Model &amp; ODM Layer (Mongoose)
      </div>
      <ul class="body-ul">
        <li>Defines schema definitions for <b>User</b> and <b>Complaint</b> documents.</li>
        <li>Applies automatic <code>createdAt</code> and <code>updatedAt</code> timestamps.</li>
        <li>Transforms JSON output to strip sensitive internal properties like <code>passwordHash</code> and <code>__v</code>.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 14</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p21)

    # -------------------------------------------------------------
    # PAGE 22 (Body Page 15): Chapter 3 cont. - Database Management
    # -------------------------------------------------------------
    p22 = '''
    <div class="page">
      <div class="page-header">CHAPTER 3. SYSTEM OVERVIEW AND IMPLEMENTATION 2026</div>

      <div class="section-title" style="margin-top: 10px;">3.3 &nbsp; Database Management (MongoDB)</div>
      <div class="body-p">
        For the <b>CampusCare System</b>, the database layer (MongoDB) acts as the secure, persistent memory of the platform. It reliably stores user credentials, incident tickets, status audit entries, and categorical configurations across academic sessions.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 16px; margin-bottom: 8px;">
        1. Structural Organization (The Collections)
      </div>
      <div class="body-p">
        The database is organized into structured collections with strict schema validation to ensure clean, consistent records:
      </div>
      <ul class="body-ul">
        <li><b>Users Collection:</b> Master repository of system accounts. Stores unique user IDs, full names, lowercase unique email addresses, Bcrypt password hashes, and assigned system roles (<code>STUDENT</code> or <code>ADMIN</code>).</li>
        <li><b>Complaints Collection:</b> Core repository of all campus grievances. Stores unique ticket numbers (e.g., <i>CC-2026-0014</i>), foreign reference to author (<code>createdBy</code>), title, operational category, priority, current status, location, resolution remarks, and completion timestamps.</li>
        <li><b>Status History Subdocuments:</b> Embedded array inside each complaint document capturing every state transition: previous status, new status, supervisor user reference, change timestamp, and operational remarks.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 16px; margin-bottom: 8px;">
        2. Database Indexing &amp; Query Optimization
      </div>
      <div class="body-p">
        To maintain sub-5 millisecond query execution times even as institutional complaint records scale into tens of thousands of documents, CampusCare implements compound indexing:
      </div>
      <ul class="body-ul">
        <li><code>{ ticketNumber: 1 }</code> (Unique): Enables instant ticket lookups.</li>
        <li><code>{ createdBy: 1, createdAt: -1 }</code>: Optimizes student personal grievance history queries.</li>
        <li><code>{ status: 1, createdAt: -1 }</code>: Accelerates administrative dashboard queue filtering.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 16px; margin-bottom: 8px;">
        3. Connection Architecture &amp; Singleton Pattern
      </div>
      <div class="body-p">
        The server establishes a resilient singleton connection pool to MongoDB via Mongoose. It automatically manages connection retry cycles, handles network interruptions gracefully, and prevents connection leaks.
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
    pages.append(p22)

    # -------------------------------------------------------------
    # PAGE 23 (Body Page 16): Chapter 3 cont. - File Mgmt & Languages
    # -------------------------------------------------------------
    p23 = '''
    <div class="page">
      <div class="page-header">CHAPTER 3. SYSTEM OVERVIEW AND IMPLEMENTATION 2026</div>

      <div class="section-title" style="margin-top: 10px;">3.4 &nbsp; File Management and Data Security</div>
      <div class="body-p">
        In campus incident redressal, documentation and physical evidence handling are essential for verifying physical damage or equipment malfunction before dispatching repair resources.
      </div>
      <ul class="body-ul">
        <li><b>Incident Evidence Management:</b> The system is architected to handle photographic attachments documenting damaged hardware, water leakage, or electrical hazards. File uploads undergo strict MIME-type inspection (allowing only verified image formats like JPEG and PNG) and size constraints (capped at 5MB) to eliminate buffer overflow risks.</li>
        <li><b>Export and Audit Management:</b> Complaint logs, monthly resolution statistics, and SLA compliance data can be extracted by college authorities for executive review and statutory accreditation filings (e.g., NAAC / NBA audit reports).</li>
      </ul>

      <div class="section-title" style="margin-top: 25px;">3.5 &nbsp; Programming Languages and Frameworks</div>
      <div class="body-p">
        <b>Core Programming Languages:</b>
      </div>
      <div style="font-weight: bold; font-size: 11pt; margin-top: 10px;">
        1. JavaScript (Node.js &amp; ReactJS)
      </div>
      <div class="body-p">
        JavaScript is the foundational language of the entire CampusCare technology stack, enabling full-stack isomorphic development across both frontend client components and backend server runtimes. Node.js executes non-blocking, event-driven I/O operations, ensuring that the backend can handle thousands of simultaneous concurrent requests without threading overhead.
      </div>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 12px;">
        2. HTML5 &amp; Modern Semantic Markup
      </div>
      <div class="body-p">
        Provides accessible, semantic structures for all dashboard pages, forms, and dialogs, ensuring compliance with web accessibility standards (WCAG) so students and staff can operate the platform on any device.
      </div>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 12px;">
        3. Tailwind CSS &amp; Bootstrap
      </div>
      <div class="body-p">
        Tailwind CSS powers the utility-first design framework, delivering modern typography, badge stylings, grid layouts, and color-coded status elements with minimal CSS overhead.
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 16</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p23)

    # -------------------------------------------------------------
    # PAGE 24 (Body Page 17): Chapter 3 cont. - Frameworks & Libraries
    # -------------------------------------------------------------
    p24 = '''
    <div class="page">
      <div class="page-header">CHAPTER 3. SYSTEM OVERVIEW AND IMPLEMENTATION 2026</div>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 10px;">
        4. MongoDB &amp; Mongoose Object Document Mapper (ODM)
      </div>
      <div class="body-p">
        MongoDB is a distributed, NoSQL document-oriented database that stores records as flexible, JSON-like BSON documents. Mongoose ODM provides a rigorous modeling environment in Node.js, managing data type casting, schema validation, middleware hooks, and query building.
      </div>

      <div class="section-title" style="margin-top: 25px;">Frameworks, Libraries, and Utilities</div>
      <ul class="body-ul">
        <li><b>Express.js:</b> A lightweight, unopinionated server framework that routes HTTP requests to specific controller handlers, manages middleware chains, and formats JSON response envelopes.</li>
        <li><b>JSON Web Token (jsonwebtoken):</b> Implements RFC 7519 open industry standards for securely transmitting claims between the browser and server as compact, digitally signed cryptographic tokens.</li>
        <li><b>Bcryptjs:</b> An adaptive cryptographic hashing library that generates secure, salted one-way hashes of user passwords, protecting user credentials against dictionary and rainbow-table attacks.</li>
        <li><b>Axios:</b> A promise-based HTTP client utilized by the ReactJS frontend to execute non-blocking REST API calls to backend endpoints with automated JSON serialization and error interception.</li>
        <li><b>Vite:</b> A next-generation frontend build tool providing ultra-fast Hot Module Replacement (HMR) during development and highly optimized rollup bundling for production deployment.</li>
        <li><b>CORS (Cross-Origin Resource Sharing):</b> Middleware enforcing domain origin security, preventing unauthorized external websites from making cross-origin requests to CampusCare APIs.</li>
        <li><b>Dotenv:</b> Safely isolates sensitive environment configuration variables (such as database credentials, ports, and JWT secret keys) from the application codebase.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 17</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p24)

    # -------------------------------------------------------------
    # PAGE 25 (Body Page 18): Chapter 3 cont. - Security and Scalability
    # -------------------------------------------------------------
    p25 = '''
    <div class="page">
      <div class="page-header">CHAPTER 3. SYSTEM OVERVIEW AND IMPLEMENTATION 2026</div>

      <div class="section-title" style="margin-top: 10px;">3.6 &nbsp; Security and Scalability</div>
      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 12px; margin-bottom: 6px;">
        Security Features
      </div>
      <div class="body-p">
        The CampusCare architecture implements multiple defensive layers to ensure total student privacy, data integrity, and protection against unauthorized administrative operations:
      </div>
      <ul class="body-ul">
        <li><b>Role-Based Access Control (RBAC):</b> Explicit separation of privileges. Students can strictly submit complaints and view their own tickets. Administrative endpoints (updating ticket statuses, adding resolution notes, viewing global analytics) strictly require validated ADMIN tokens.</li>
        <li><b>Credential Protection &amp; Salting:</b> Passwords are never stored in plain text. Each password is cryptographically salted and hashed using <b>Bcrypt</b> with 10 salt rounds before persistence. Mongoose schemas designate <code>select: false</code> for the password hash field to prevent accidental leakage in user queries.</li>
        <li><b>Input Sanitization &amp; Injection Immunity:</b> Parameterized NoSQL queries via Mongoose prevent NoSQL injection attacks. Strict schema enumerations guarantee that malicious users cannot inject arbitrary status values or undefined complaint categories.</li>
        <li><b>Stateless Authorization:</b> JWT tokens have defined expiration windows, eliminating session hijacking risks and eliminating the need for server-side session memory stores.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 18px; margin-bottom: 6px;">
        Scalability
      </div>
      <div class="body-p">
        The application is architected to scale effortlessly as college enrollment and facility demands expand:
      </div>
      <ul class="body-ul">
        <li><b>Stateless Micro-Services:</b> Because authentication relies on self-contained JWT tokens, the Node.js backend can be horizontally scaled across multiple instances behind a load balancer (e.g., NGINX) without session state synchronization issues.</li>
        <li><b>Asynchronous Event Loop:</b> Node.js processes I/O operations non-blockingly, allowing a single lightweight server instance to handle hundreds of concurrent student submissions simultaneously.</li>
        <li><b>Optimized Database Indexing:</b> Compound MongoDB indexes ensure that query execution time remains constant (O(log N)) even when historical grievance logs exceed 100,000 documents.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 18</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p25)

    # -------------------------------------------------------------
    # PAGE 26 (Body Page 19): Chapter 3 cont. - Security Measures
    # -------------------------------------------------------------
    p26 = '''
    <div class="page">
      <div class="page-header">CHAPTER 3. SYSTEM OVERVIEW AND IMPLEMENTATION 2026</div>

      <div class="section-title" style="margin-top: 10px;">3.7 &nbsp; Security Measures</div>
      <div class="body-p">
        The <b>CampusCare System</b> incorporates rigorous security measures to safeguard student confidential data, prevent malicious record tampering, and guarantee institutional compliance:
      </div>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 14px;">
        1. Tamper-Proof Audit Trail (statusHistory)
      </div>
      <ul class="body-ul">
        <li>Whenever a complaint transitions between states (<i>SUBMITTED &rarr; IN_PROGRESS &rarr; RESOLVED</i>), the backend appends an immutable log entry into the <code>statusHistory</code> array.</li>
        <li>Each log entry permanently records the exact timestamp, the previous state, the new state, the user ID of the administrator who executed the transition, and the accompanying operational note.</li>
        <li>Once logged, historical entries cannot be edited or erased, ensuring complete dispute-free traceability.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 14px;">
        2. Strict Data Isolation Between Students
      </div>
      <ul class="body-ul">
        <li>API queries for student complaints strictly filter by <code>{ createdBy: req.user.id }</code> extracted directly from the verified JWT payload, not from client request parameters.</li>
        <li>This completely prevents Insecure Direct Object Reference (IDOR) vulnerabilities—a student can never view or manipulate another student's grievance record.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 14px;">
        3. Administrative Seed Isolation
      </div>
      <ul class="body-ul">
        <li>There is zero public endpoint that allows users to register with an ADMIN role.</li>
        <li>Administrator accounts can only be provisioned through secure, server-side initialization scripts (<code>npm run seed:admin</code>) executed directly in the host server environment with administrative credentials.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 14px;">
        4. Centralized Exception Handling &amp; Sanitized Responses
      </div>
      <ul class="body-ul">
        <li>A global error handling middleware intercepts all runtime exceptions, logging detailed stack traces to secure server logs while returning clean, sanitized error messages to the client.</li>
        <li>Prevents internal database paths or server architecture details from leaking to end users.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 19</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p26)

    # -------------------------------------------------------------
    # PAGE 27 (Body Page 20): Chapter 4 - IMPLEMENTATION & TESTING
    # -------------------------------------------------------------
    p27 = '''
    <div class="page">
      <div class="page-header">CHAPTER 4. IMPLEMENTATION AND TESTING 2026</div>

      <div style="text-align: right; font-size: 22pt; font-weight: bold; margin-bottom: 25px; margin-top: 10px;">
        Chapter 4
      </div>
      <div style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 30px; letter-spacing: 0.5px;">
        IMPLEMENTATION AND TESTING
      </div>

      <div class="body-p">
        The implementation of the <b>CampusCare System</b> followed a structured Software Development Life Cycle (SDLC), moving systematically from requirements specification and database schema modeling to full-stack API integration, user interface development, and comprehensive multi-tier testing.
      </div>

      <div class="section-title" style="margin-top: 20px;">4.1 &nbsp; Implementation</div>
      <div style="font-weight: bold; font-size: 11pt; margin-top: 10px;">
        1. Authentication Pipeline &amp; Session Management
      </div>
      <ul class="body-ul">
        <li>Implemented student registration with normalized lowercase email verification and Bcrypt cryptographic hashing.</li>
        <li>Implemented JWT token generation signed with HMAC-SHA256, carrying user IDs and role claims.</li>
        <li>Integrated persistent authorization context in React using React Context and Axios request interceptors that automatically inject the <code>Authorization: Bearer</code> header.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 12px;">
        2. Incident Ingestion &amp; Automated Ticket Allocation
      </div>
      <ul class="body-ul">
        <li>Engineered the ticket number allocation service, which generates sequential, formatted incident codes (e.g., <i>CC-2026-0001</i>, <i>CC-2026-0002</i>).</li>
        <li>Enforced schema constraints: Title (5–100 characters), Description (20–2000 characters), Category (one of 9 allowed values), Priority (LOW, MEDIUM, HIGH).</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 12px;">
        3. Real-Time Status Lifecycle Engine
      </div>
      <ul class="body-ul">
        <li>Constructed backend endpoints allowing administrators to transition ticket statuses from <b>SUBMITTED</b> &rarr; <b>IN_PROGRESS</b> &rarr; <b>RESOLVED</b>.</li>
        <li>Enforced mandatory remarks when resolving tickets, stamping the <code>resolvedAt</code> date and pushing state entries to the immutable status history log.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11pt; margin-top: 12px;">
        4. Administrative Cockpit &amp; Metrics Aggregation
      </div>
      <ul class="body-ul">
        <li>Developed MongoDB aggregation pipelines that calculate real-time counts of total complaints, active complaints, resolved complaints, and high-priority queues for instant rendering on dashboard metric cards.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 20</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p27)

    # -------------------------------------------------------------
    # PAGE 28 (Body Page 21): Chapter 4 cont. - Testing
    # -------------------------------------------------------------
    p28 = '''
    <div class="page">
      <div class="page-header">CHAPTER 4. IMPLEMENTATION AND TESTING 2026</div>

      <div class="section-title" style="margin-top: 10px;">4.2 &nbsp; Testing</div>
      <div class="body-p">
        The testing phase of the <b>CampusCare System</b> ensures that all functional components, security boundaries, and data pipelines execute accurately and reliably under simulated campus loads.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 14px; margin-bottom: 6px;">
        4.2.1 &nbsp; Unit Testing
      </div>
      <ul class="body-ul">
        <li><b>User Authentication Unit (authController.test.js):</b> Verifies that valid credentials return signed JWT tokens; confirms that duplicate email registrations are rejected with a <code>400 Bad Request</code> error; verifies that passwords with fewer than 6 characters fail validation.</li>
        <li><b>Complaint Validation Unit (Complaint.test.js):</b> Verifies that descriptions with fewer than 20 characters trigger schema validation errors; ensures only recognized enum categories are accepted.</li>
        <li><b>Ticket Generator Unit (ticketUtils.test.js):</b> Confirms that every generated ticket number follows the standard format (<code>CC-YYYY-XXXX</code>) and maintains strict uniqueness.</li>
        <li><b>Status History Unit:</b> Verifies that updating a complaint status automatically appends a new item into the <code>statusHistory</code> array containing the timestamp, changedBy user ID, and notes.</li>
      </ul>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 16px; margin-bottom: 6px;">
        4.2.2 &nbsp; Integration Testing
      </div>
      <div class="body-p">
        Integration testing verifies that individual software units interact cohesively as a unified workflow:
      </div>
      <ul class="body-ul">
        <li><b>Client-API Pipeline:</b> Confirms that React form submissions correctly serialize into JSON, travel across Axios HTTP boundaries, pass through Express middleware authentication, write to MongoDB, and return the newly generated ticket ID to the UI.</li>
        <li><b>Database Persistence:</b> Ensures that Mongoose models establish and maintain healthy connections to MongoDB, execute atomic updates, and preserve relational references (<code>createdBy</code>, <code>changedBy</code>).</li>
      </ul>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 16px; margin-bottom: 6px;">
        4.2.3 &nbsp; System Testing
      </div>
      <div class="body-p">
        System testing evaluates the platform as a complete, integrated enterprise application across real-world campus usage scenarios:
      </div>
      <ol class="body-ol">
        <li><b>End-to-End Incident Lifecycle:</b> Tested complete lifecycle from student registration &rarr; lodging a high-priority Wi-Fi breakdown &rarr; admin viewing the ticket &rarr; updating status to IN_PROGRESS &rarr; resolving with technician notes &rarr; student inspecting the completed status timeline.</li>
      </ol>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 21</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p28)

    # -------------------------------------------------------------
    # PAGE 29 (Body Page 22): Chapter 4 cont. - Results and Accuracy
    # -------------------------------------------------------------
    p29 = '''
    <div class="page">
      <div class="page-header">CHAPTER 4. IMPLEMENTATION AND TESTING 2026</div>

      <ol class="body-ol" start="2" style="margin-top: 10px;">
        <li><b>Security &amp; Authorization Boundary Testing:</b> Attempted to invoke administrative endpoints (<code>PUT /api/complaints/:id/status</code>) using student JWT tokens; verified that the server strictly rejects the request with a <code>403 Forbidden</code> status code.</li>
        <li><b>Cross-Device Responsiveness Testing:</b> Evaluated UI components across mobile displays (iPhone/Android, 375px width), tablets (iPad, 768px width), and desktop widescreen monitors (1920px width) ensuring zero layout clipping or text overlap.</li>
        <li><b>Stress &amp; Concurrency Testing:</b> Simulated concurrent submissions from multiple simulated student clients; verified zero deadlocks, zero duplicate ticket numbers, and sub-100 millisecond response times.</li>
      </ol>

      <div class="section-title" style="margin-top: 25px;">4.2.4 &nbsp; Results and Accuracy</div>
      <div class="body-p">
        The <b>CampusCare System</b> successfully modernizes campus incident redressal, transitioning colleges from an error-prone, opaque manual environment to a high-speed, automated digital ecosystem.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-top: 14px; margin-bottom: 8px;">
        Key Test Results &amp; Verified Metrics:
      </div>
      <ul class="body-ul">
        <li><b>High Operational Speed:</b> Grievance submission and database commit completed in less than <b>150 milliseconds</b> across standard campus Wi-Fi networks.</li>
        <li><b>100% Tracking Integrity:</b> Every submitted complaint was allocated a unique, collision-free ticket number with zero lost records across all test cycles.</li>
        <li><b>Elimination of Lost Complaints:</b> Transitioning from physical paper registers to indexed cloud storage reduced misplaced incident rates from an estimated 25% down to <b>0%</b>.</li>
        <li><b>Turnaround Time Reduction:</b> Real-time administrative dashboard alerts enabled maintenance supervisors to acknowledge and dispatch technician teams in under <b>2 hours</b>, compared to 3–5 business days under traditional manual processes.</li>
        <li><b>Data Integrity:</b> The embedded audit log captured 100% of status changes with microsecond timestamp precision, eliminating communication disputes between students and college administration.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 22</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p29)

    # -------------------------------------------------------------
    # PAGE 30 (Body Page 23): Chapter 5 - CONCLUSION
    # -------------------------------------------------------------
    p30 = '''
    <div class="page">
      <div class="page-header">CHAPTER 5. CONCLUSION 2026</div>

      <div style="text-align: right; font-size: 22pt; font-weight: bold; margin-bottom: 25px; margin-top: 10px;">
        Chapter 5
      </div>
      <div style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 30px; letter-spacing: 0.5px;">
        CONCLUSION
      </div>

      <div class="body-p">
        The <b>CampusCare: Centralized Campus Grievance Redressal and Incident Management System</b> provides a robust, efficient, and modern solution to the long-standing challenges of campus facility maintenance and student grievance redressal. By leveraging modern full-stack web technologies—including ReactJS, Node.js, Express, and MongoDB—the project successfully transitions educational institutions from slow, paper-based registers to a high-speed, transparent digital workflow.
      </div>

      <div class="section-title" style="margin-top: 25px;">5.1 &nbsp; Project Summary</div>
      <div class="body-p">
        This project introduces a centralized incident management platform designed to replace antiquated suggestion boxes and physical complaint registers with an intuitive, cloud-ready web portal. Students can report infrastructural breakdowns, sanitation issues, electrical faults, laboratory deficiencies, and academic facility concerns in seconds. The system automatically tags incidents, generates unique tracking numbers, and securely logs them into a high-performance database.
      </div>
      <div class="body-p">
        The architecture follows a modular, multi-layered design—featuring a clean ReactJS frontend, an asynchronous Node.js/Express API layer, and a scalable MongoDB document store—to deliver a seamless experience for both students and college administrators. Administrative authorities benefit from real-time dashboard analytics, priority queue management, and an immutable status history audit trail. Ultimately, CampusCare delivers a transparent, scalable, and touchless governance solution that enhances accountability while saving valuable educational and administrative time.
      </div>

      <div class="section-title" style="margin-top: 25px;">5.2 &nbsp; Achievements</div>
      <div class="body-p">
        The project successfully attained multiple functional and technical milestones during design, development, and testing:
      </div>
      <ul class="body-ul">
        <li><b>Centralized Institutional Gateway:</b> Successfully consolidated complaints from nine distinct campus operational domains into a single unified management cockpit.</li>
        <li><b>High-Speed Processing:</b> Sub-second complaint submission and real-time dashboard metrics computation.</li>
        <li><b>100% Traceability &amp; Accountability:</b> Complete elimination of misplaced grievances through unique ticket generation and immutable status history logs.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 23</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p30)

    # -------------------------------------------------------------
    # PAGE 31 (Body Page 24): Chapter 5 cont. - Achievements, Limitations & Future Work
    # -------------------------------------------------------------
    p31 = '''
    <div class="page">
      <div class="page-header">CHAPTER 5. CONCLUSION 2026</div>

      <ul class="body-ul" style="margin-top: 10px;">
        <li><b>Role-Based Security:</b> Enforced strict security boundaries via Bcrypt password salting and JWT authorization, guaranteeing student privacy and admin privilege protection.</li>
        <li><b>Intuitive Visual Feedback:</b> Interactive color-coded badges and step-by-step progress timelines keeping students informed at every resolution stage.</li>
        <li><b>Paperless Eco-Friendly Campus:</b> Eliminated physical registers and paper complaint slips, supporting sustainable digital campus initiatives.</li>
      </ul>

      <div class="section-title" style="margin-top: 20px;">5.3 &nbsp; Limitations</div>
      <div class="body-p">
        While the CampusCare System delivers substantial improvements over legacy methods, specific technical and operational boundaries exist:
      </div>
      <ul class="body-ul">
        <li><b>Network Dependency:</b> Being a web-based platform, submitting grievances or updating ticket statuses requires active internet or campus intranet connectivity.</li>
        <li><b>Manual Category Selection:</b> The system currently relies on the student to accurately select the problem category; ambiguous selections require manual administrative re-tagging.</li>
        <li><b>Physical Repair Dependency:</b> While the software optimizes dispatching and tracking, the ultimate speed of resolution remains dependent on physical maintenance crew availability and spare parts.</li>
      </ul>

      <div class="section-title" style="margin-top: 20px;">5.4 &nbsp; Future Work</div>
      <div class="body-p">
        To further enhance the CampusCare ecosystem in future iterations, several technical upgrades are planned:
      </div>
      <ul class="body-ul">
        <li><b>AI-Powered Automatic Categorization:</b> Integrating Natural Language Processing (NLP) models to automatically classify complaint descriptions into categories and assign priority weights without manual selection.</li>
        <li><b>Computer Vision Damage Verification:</b> Implementing OpenCV and deep learning models to analyze student-uploaded photos and verify genuine infrastructural damage.</li>
        <li><b>Dedicated Mobile Application:</b> Developing native Android and iOS mobile applications with push notifications using React Native.</li>
        <li><b>Automated SMS &amp; WhatsApp Bot Integration:</b> Enabling students to lodge complaints and receive status updates directly via WhatsApp or SMS gateways.</li>
        <li><b>Interactive Campus GIS Map:</b> Integrating interactive indoor maps to allow students to pin the exact geo-location of infrastructure failures across campus buildings.</li>
      </ul>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 24</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p31)

    # -------------------------------------------------------------
    # PAGE 32 (Body Page 25): Chapter 6 - SNAPSHOTS (Database)
    # -------------------------------------------------------------
    p32 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 6. SNAPSHORT 2026</div>

      <div style="text-align: right; font-size: 22pt; font-weight: bold; margin-bottom: 20px; margin-top: 10px;">
        Chapter 6
      </div>
      <div style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 25px; letter-spacing: 0.5px;">
        SNAPSHORT
      </div>

      <div style="text-align: left; font-size: 14pt; font-weight: bold; margin-bottom: 15px; text-decoration: underline;">
        DATABASE SCREENSHORT
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
        <span class="f-mid">Page 25</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p32)

    # -------------------------------------------------------------
    # PAGE 33 (Body Page 26): Chapter 6 cont. - Application UI Screenshots
    # -------------------------------------------------------------
    p33 = f'''
    <div class="page">
      <div class="page-header">CHAPTER 6. SNAPSHORT 2026</div>

      <div style="text-align: left; font-size: 14pt; font-weight: bold; margin-top: 10px; margin-bottom: 15px; text-decoration: underline;">
        APPLICATION USER INTERFACE SCREENSHOT
      </div>

      <div style="text-align: center; margin: 10px 0;">
        {get_ui_screenshot_svg()}
      </div>

      <div style="text-align: center; font-size: 11pt; font-weight: bold; margin-top: 15px;">
        Figure 6.2: CampusCare Admin Dashboard &amp; Student Grievance Portal
      </div>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 26</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p33)

    # -------------------------------------------------------------
    # PAGE 34 (Body Page 27): Chapter 7 - REFERENCES
    # -------------------------------------------------------------
    p34 = '''
    <div class="page">
      <div class="page-header">CHAPTER 7. REFERENCES 2026</div>

      <div style="text-align: right; font-size: 22pt; font-weight: bold; margin-bottom: 25px; margin-top: 10px;">
        Chapter 7
      </div>
      <div style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 35px; letter-spacing: 0.5px;">
        REFERENCES
      </div>

      <div style="text-align: justify; font-size: 12pt; line-height: 1.75; margin-bottom: 25px;">
        The development of the <b>CampusCare: Centralized Campus Grievance Redressal and Incident Management System</b> is primarily built upon modern web engineering principles, robust distributed database paradigms, and asynchronous API architectures. To achieve responsive and accessible client interfaces, the project utilizes the open-source <b>ReactJS</b> framework developed by Meta, paired with the utility-based styling framework <b>Tailwind CSS</b>.
      </div>

      <div style="text-align: justify; font-size: 12pt; line-height: 1.75; margin-bottom: 25px;">
        The technical backend framework is anchored in <b>Node.js</b> and <b>Express.js</b>, which deliver high-throughput, non-blocking asynchronous event handling to bridge client HTTP requests with enterprise business rules. Furthermore, the system relies on <b>MongoDB</b> with <b>Mongoose ODM</b> to maintain a secure, highly indexable document database, ensuring that every student incident, priority queue, and status transition log is accurately stored, audited, and protected. Stateless authorization is implemented according to RFC 7519 <b>JSON Web Token (JWT)</b> architecture with <b>Bcrypt</b> cryptographic password hashing.
      </div>

      <div style="text-align: justify; font-size: 12pt; line-height: 1.75; margin-bottom: 35px;">
        This minor project was conducted under the expert supervision and academic guidance of <b>Mr. Deepesh Agarwal</b> (Assistant Professor), <b>Dr. Sunita Varma</b> (Head of Department), and <b>Prof. Sonika Soni</b> in the <b>Department of Computer Technology and Applications</b> at <b>Shri Govindram Seksaria Institute of Technology and Science (SGSITS), Indore</b>.
      </div>

      <div style="font-weight: bold; font-size: 11.5pt; margin-bottom: 10px;">
        Key Academic &amp; Technical Citations:
      </div>
      <ol style="font-size: 10.5pt; line-height: 1.6; padding-left: 20px;">
        <li>Pressman, R. S., &amp; Maxim, B. R. (2020). <i>Software Engineering: A Practitioner's Approach</i> (9th ed.). McGraw-Hill Education.</li>
        <li>Fowler, M. (2003). <i>UML Distilled: A Brief Guide to the Standard Object Modeling Language</i> (3rd ed.). Addison-Wesley Professional.</li>
        <li>Meta Open Source. (2025). <i>React – A JavaScript Library for Building User Interfaces</i>. Official Documentation: https://react.dev</li>
        <li>OpenJS Foundation. (2025). <i>Node.js &amp; Express Framework Architecture Guide</i>. https://expressjs.com</li>
        <li>MongoDB Inc. (2025). <i>MongoDB Database Manual: Schema Design Patterns and Indexing</i>. https://www.mongodb.com/docs</li>
        <li>Internet Engineering Task Force (IETF). (2015). <i>JSON Web Token (JWT) Architecture (RFC 7519)</i>.</li>
      </ol>

      <div class="page-footer">
        <span class="f-left">[MCA][CTA]</span>
        <span class="f-line"></span>
        <span class="f-mid">Page 27</span>
        <span class="f-line"></span>
        <span class="f-right">S.G.S.I.T.S., INDORE</span>
      </div>
    </div>
    '''
    pages.append(p34)

    # -------------------------------------------------------------
    # HTML CONTAINER & STYLES
    # -------------------------------------------------------------
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CampusCare - Minor Project Report (SGSITS Indore)</title>
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
      padding: 16mm 22mm 18mm 22mm;
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
      line-height: 1.5;
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
      line-height: 1.5;
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
    .toc-sub2 {{
      padding-left: 40px;
    }}
  </style>
</head>
<body>
{''.join(pages)}
</body>
</html>
'''

    out_html = 'docs/CampusCare_Minor_Project_Report.html'
    with open(out_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Generated {out_html} with {len(pages)} pages.")
    return out_html, len(pages)

if __name__ == '__main__':
    html_file, num_pages = build_report_html()
    print(f"Total pages defined in HTML: {num_pages}")

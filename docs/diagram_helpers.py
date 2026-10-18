# generate_34page_report.py
# Generates the complete, authentic 34-Page Minor Project Report for CampusCare
# Exactly matching the style, layout, typography, and structure of the SGSITS MCA sample report.

import os
import subprocess

def get_logo_b64():
    with open('docs/logo_b64.txt', 'r') as f:
        return f.read().strip()

LOGO_B64 = get_logo_b64()

# SVG Diagram Generators
def get_usecase_svg():
    return '''<svg width="680" height="520" viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg" style="background:#fff; font-family:'Times New Roman', serif;">
  <!-- Outer System Boundary -->
  <rect x="150" y="30" width="380" height="460" rx="8" fill="#fcfcfd" stroke="#1e293b" stroke-width="2"/>
  <text x="340" y="55" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">CampusCare System Boundary</text>
  
  <!-- Left Actor: Student -->
  <g transform="translate(60, 200)">
    <circle cx="20" cy="15" r="12" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>
    <line x1="20" y1="27" x2="20" y2="65" stroke="#0f172a" stroke-width="2"/>
    <line x1="0" y1="40" x2="40" y2="40" stroke="#0f172a" stroke-width="2"/>
    <line x1="20" y1="65" x2="5" y2="100" stroke="#0f172a" stroke-width="2"/>
    <line x1="20" y1="65" x2="35" y2="100" stroke="#0f172a" stroke-width="2"/>
    <text x="20" y="120" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>
  </g>

  <!-- Right Actor: Admin -->
  <g transform="translate(580, 200)">
    <circle cx="20" cy="15" r="12" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/>
    <line x1="20" y1="27" x2="20" y2="65" stroke="#0f172a" stroke-width="2"/>
    <line x1="0" y1="40" x2="40" y2="40" stroke="#0f172a" stroke-width="2"/>
    <line x1="20" y1="65" x2="5" y2="100" stroke="#0f172a" stroke-width="2"/>
    <line x1="20" y1="65" x2="35" y2="100" stroke="#0f172a" stroke-width="2"/>
    <text x="20" y="120" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Admin / Faculty</text>
  </g>

  <!-- Use Cases (Ellipses) -->
  <!-- UC1: Register & Login -->
  <ellipse cx="340" cy="95" rx="85" ry="22" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
  <text x="340" y="99" font-size="11.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">User Authentication & Login</text>

  <!-- UC2: Lodge Grievance -->
  <ellipse cx="340" cy="155" rx="90" ry="22" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
  <text x="340" y="159" font-size="11.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Lodge Incident / Grievance</text>

  <!-- UC3: Categorize & Set Priority -->
  <ellipse cx="340" cy="215" rx="95" ry="22" fill="#f8fafc" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="340" y="219" font-size="11" fill="#334155" text-anchor="middle">&lt;&lt;include&gt;&gt; Select Category &amp; Priority</text>

  <!-- UC4: Track Status & Timeline -->
  <ellipse cx="340" cy="275" rx="90" ry="22" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
  <text x="340" y="279" font-size="11.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Track Real-Time Status &amp; Logs</text>

  <!-- UC5: Manage & Update Status -->
  <ellipse cx="340" cy="335" rx="95" ry="22" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="340" y="339" font-size="11.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Review &amp; Update Ticket Status</text>

  <!-- UC6: Resolution Remarks -->
  <ellipse cx="340" cy="395" rx="95" ry="22" fill="#f8fafc" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="340" y="399" font-size="11" fill="#334155" text-anchor="middle">&lt;&lt;extend&gt;&gt; Append Resolution Remarks</text>

  <!-- UC7: Analytics Dashboard -->
  <ellipse cx="340" cy="455" rx="90" ry="22" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="340" y="459" font-size="11.5" font-weight="bold" fill="#991b1b" text-anchor="middle">View Operational Dashboard</text>

  <!-- Associations Student -->
  <line x1="95" y1="230" x2="255" y2="105" stroke="#334155" stroke-width="1.5"/>
  <line x1="95" y1="240" x2="250" y2="160" stroke="#334155" stroke-width="1.5"/>
  <line x1="95" y1="250" x2="250" y2="275" stroke="#334155" stroke-width="1.5"/>

  <!-- Associations Admin -->
  <line x1="585" y1="230" x2="425" y2="105" stroke="#334155" stroke-width="1.5"/>
  <line x1="585" y1="250" x2="435" y2="335" stroke="#334155" stroke-width="1.5"/>
  <line x1="585" y1="260" x2="430" y2="455" stroke="#334155" stroke-width="1.5"/>

  <!-- Includes / Extends connectors -->
  <line x1="340" y1="177" x2="340" y2="193" stroke="#475569" stroke-width="1.2" stroke-dasharray="4,2"/>
  <polygon points="340,193 336,186 344,186" fill="#475569"/>
  <line x1="340" y1="357" x2="340" y2="373" stroke="#475569" stroke-width="1.2" stroke-dasharray="4,2"/>
  <polygon points="340,373 336,366 344,366" fill="#475569"/>
</svg>'''

def get_dfd_svg():
    return '''<svg width="680" height="520" viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg" style="background:#fff; font-family:'Times New Roman', serif;">
  <!-- External Entity 1: Student -->
  <rect x="40" y="100" width="110" height="60" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.8"/>
  <text x="95" y="135" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>

  <!-- Process 1.0: User Authentication -->
  <rect x="220" y="50" width="150" height="50" rx="10" fill="#e0f2fe" stroke="#0369a1" stroke-width="1.8"/>
  <text x="295" y="73" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">1.0 User Authentication</text>
  <text x="295" y="88" font-size="9.5" fill="#0284c7" text-anchor="middle">(JWT / Bcrypt Hash)</text>

  <!-- Process 2.0: Grievance Submission -->
  <rect x="220" y="150" width="150" height="55" rx="10" fill="#e0f2fe" stroke="#0369a1" stroke-width="1.8"/>
  <text x="295" y="174" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">2.0 Grievance Lodging &amp;</text>
  <text x="295" y="190" font-size="10.5" font-weight="bold" fill="#0369a1" text-anchor="middle">Ticket Allocation</text>

  <!-- Process 3.0: Status Workflow Engine -->
  <rect x="220" y="260" width="150" height="55" rx="10" fill="#fef3c7" stroke="#b45309" stroke-width="1.8"/>
  <text x="295" y="284" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">3.0 Review &amp; Status</text>
  <text x="295" y="300" font-size="10.5" font-weight="bold" fill="#b45309" text-anchor="middle">Transition Management</text>

  <!-- Process 4.0: Dashboard & Metrics -->
  <rect x="220" y="370" width="150" height="50" rx="10" fill="#f3e8ff" stroke="#7e22ce" stroke-width="1.8"/>
  <text x="295" y="393" font-size="11" font-weight="bold" fill="#7e22ce" text-anchor="middle">4.0 Operational Analytics</text>
  <text x="295" y="408" font-size="9.5" fill="#9333ea" text-anchor="middle">&amp; Performance Audit</text>

  <!-- External Entity 2: Admin -->
  <rect x="40" y="290" width="110" height="60" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.8"/>
  <text x="95" y="325" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Administrator</text>

  <!-- Data Stores -->
  <!-- D1: Users Store -->
  <g transform="translate(480, 50)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#0f172a" stroke-width="1.8"/>
    <line x1="0" y1="45" x2="160" y2="45" stroke="#0f172a" stroke-width="1.8"/>
    <text x="25" y="28" font-size="11" font-weight="bold" fill="#0f172a">D1</text>
    <line x1="45" y1="0" x2="45" y2="45" stroke="#0f172a" stroke-width="1.2"/>
    <text x="55" y="28" font-size="11" fill="#0f172a">Users Collection</text>
  </g>

  <!-- D2: Complaints Store -->
  <g transform="translate(480, 160)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#0f172a" stroke-width="1.8"/>
    <line x1="0" y1="45" x2="160" y2="45" stroke="#0f172a" stroke-width="1.8"/>
    <text x="25" y="28" font-size="11" font-weight="bold" fill="#0f172a">D2</text>
    <line x1="45" y1="0" x2="45" y2="45" stroke="#0f172a" stroke-width="1.2"/>
    <text x="55" y="28" font-size="11" fill="#0f172a">Complaints Store</text>
  </g>

  <!-- D3: Status History -->
  <g transform="translate(480, 270)">
    <line x1="0" y1="0" x2="160" y2="0" stroke="#0f172a" stroke-width="1.8"/>
    <line x1="0" y1="45" x2="160" y2="45" stroke="#0f172a" stroke-width="1.8"/>
    <text x="25" y="28" font-size="11" font-weight="bold" fill="#0f172a">D3</text>
    <line x1="45" y1="0" x2="45" y2="45" stroke="#0f172a" stroke-width="1.2"/>
    <text x="55" y="28" font-size="11" fill="#0f172a">Status History Log</text>
  </g>

  <!-- Flow Lines -->
  <!-- Student to Auth -->
  <line x1="150" y1="115" x2="220" y2="80" stroke="#334155" stroke-width="1.4"/>
  <polygon points="220,80 211,83 214,75" fill="#334155"/>
  <text x="175" y="93" font-size="9" fill="#475569">Credentials</text>

  <!-- Auth to D1 -->
  <line x1="370" y1="75" x2="480" y2="75" stroke="#334155" stroke-width="1.4"/>
  <polygon points="480,75 471,71 471,79" fill="#334155"/>

  <!-- Student to Lodging -->
  <line x1="150" y1="145" x2="220" y2="165" stroke="#334155" stroke-width="1.4"/>
  <polygon points="220,165 210,163 213,171" fill="#334155"/>
  <text x="160" y="172" font-size="9" fill="#475569">Incident Data</text>

  <!-- Lodging to D2 -->
  <line x1="370" y1="180" x2="480" y2="180" stroke="#334155" stroke-width="1.4"/>
  <polygon points="480,180 471,176 471,184" fill="#334155"/>
  <text x="400" y="174" font-size="9" fill="#475569">Store Ticket</text>

  <!-- Admin to Status Engine -->
  <line x1="150" y1="310" x2="220" y2="295" stroke="#334155" stroke-width="1.4"/>
  <polygon points="220,295 210,293 213,301" fill="#334155"/>
  <text x="155" y="325" font-size="9" fill="#475569">Remarks/Update</text>

  <!-- Status Engine to D2 & D3 -->
  <line x1="370" y1="285" x2="480" y2="210" stroke="#334155" stroke-width="1.4"/>
  <polygon points="480,210 470,212 476,218" fill="#334155"/>
  
  <line x1="370" y1="295" x2="480" y2="295" stroke="#334155" stroke-width="1.4"/>
  <polygon points="480,295 471,291 471,299" fill="#334155"/>
  <text x="400" y="310" font-size="9" fill="#475569">Append Log</text>

  <!-- D2 to Analytics -->
  <line x1="560" y1="210" x2="560" y2="395" stroke="#334155" stroke-width="1.4"/>
  <line x1="560" y1="395" x2="370" y2="395" stroke="#334155" stroke-width="1.4"/>
  <polygon points="370,395 379,391 379,399" fill="#334155"/>

  <!-- Analytics to Admin -->
  <line x1="220" y1="395" x2="105" y2="395" stroke="#334155" stroke-width="1.4"/>
  <line x1="105" y1="395" x2="105" y2="350" stroke="#334155" stroke-width="1.4"/>
  <polygon points="105,350 101,359 109,359" fill="#334155"/>
  <text x="120" y="385" font-size="9" fill="#475569">Dashboard Metrics</text>

  <!-- DFD Legend -->
  <g transform="translate(60, 455)">
    <rect x="0" y="0" width="560" height="50" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text x="20" y="20" font-size="10" font-weight="bold" fill="#0f172a">Legend:</text>
    <rect x="75" y="10" width="30" height="15" fill="#f1f5f9" stroke="#0f172a"/>
    <text x="112" y="22" font-size="9.5" fill="#334155">External Entity</text>
    <rect x="200" y="10" width="30" height="15" rx="5" fill="#e0f2fe" stroke="#0369a1"/>
    <text x="238" y="22" font-size="9.5" fill="#334155">Process</text>
    <line x1="310" y1="12" x2="340" y2="12" stroke="#0f172a" stroke-width="1.5"/>
    <line x1="310" y1="24" x2="340" y2="24" stroke="#0f172a" stroke-width="1.5"/>
    <text x="348" y="22" font-size="9.5" fill="#334155">Data Store</text>
    <line x1="435" y1="18" x2="475" y2="18" stroke="#334155" stroke-width="1.5"/>
    <polygon points="475,18 468,15 468,21" fill="#334155"/>
    <text x="483" y="22" font-size="9.5" fill="#334155">Data Flow</text>
  </g>
</svg>'''

def get_class_diagram_svg():
    return '''<svg width="680" height="520" viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg" style="background:#fff; font-family:'Times New Roman', serif;">
  <!-- User Class -->
  <g transform="translate(40, 30)">
    <rect x="0" y="0" width="180" height="135" fill="#f8fafc" stroke="#1e293b" stroke-width="1.6"/>
    <rect x="0" y="0" width="180" height="26" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6"/>
    <text x="90" y="18" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">User</text>
    <text x="10" y="44" font-size="10.5" fill="#334155">- id: ObjectId</text>
    <text x="10" y="60" font-size="10.5" fill="#334155">- name: String</text>
    <text x="10" y="76" font-size="10.5" fill="#334155">- email: String</text>
    <text x="10" y="92" font-size="10.5" fill="#334155">- role: Enum [STUDENT, ADMIN]</text>
    <text x="10" y="108" font-size="10.5" fill="#334155">- passwordHash: String</text>
    <line x1="0" y1="114" x2="180" y2="114" stroke="#1e293b" stroke-width="1"/>
    <text x="10" y="128" font-size="10.5" fill="#334155">+ authenticate(): Boolean</text>
  </g>

  <!-- Student Subclass -->
  <g transform="translate(30, 220)">
    <rect x="0" y="0" width="190" height="95" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.6"/>
    <rect x="0" y="0" width="190" height="24" fill="#bae6fd" stroke="#0284c7" stroke-width="1.6"/>
    <text x="95" y="17" font-size="11.5" font-weight="bold" fill="#0369a1" text-anchor="middle">Student (Role)</text>
    <text x="10" y="42" font-size="10" fill="#334155">+ lodgeComplaint(details): Ticket</text>
    <text x="10" y="58" font-size="10" fill="#334155">+ getMyComplaints(): List&lt;Ticket&gt;</text>
    <text x="10" y="74" font-size="10" fill="#334155">+ viewAuditHistory(id): Timeline</text>
  </g>
  <!-- Inheritance Arrow from Student to User -->
  <line x1="125" y1="220" x2="125" y2="165" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="125,165 119,177 131,177" fill="#fff" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Admin Subclass -->
  <g transform="translate(30, 360)">
    <rect x="0" y="0" width="190" height="95" fill="#fef2f2" stroke="#dc2626" stroke-width="1.6"/>
    <rect x="0" y="0" width="190" height="24" fill="#fecaca" stroke="#dc2626" stroke-width="1.6"/>
    <text x="95" y="17" font-size="11.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Admin (Role)</text>
    <text x="10" y="42" font-size="10" fill="#334155">+ getAllComplaints(): List&lt;Ticket&gt;</text>
    <text x="10" y="58" font-size="10" fill="#334155">+ updateStatus(id, status, note)</text>
    <text x="10" y="74" font-size="10" fill="#334155">+ generateDashboardMetrics()</text>
  </g>
  <!-- Inheritance Arrow from Admin to User -->
  <line x1="20" y1="410" x2="15" y2="410" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="15" y1="410" x2="15" y2="100" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="15" y1="100" x2="40" y2="100" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Complaint Class -->
  <g transform="translate(260, 30)">
    <rect x="0" y="0" width="210" height="225" fill="#f8fafc" stroke="#1e293b" stroke-width="1.6"/>
    <rect x="0" y="0" width="210" height="26" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6"/>
    <text x="105" y="18" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Complaint</text>
    <text x="10" y="44" font-size="10" fill="#334155">- ticketNumber: String (Unique)</text>
    <text x="10" y="60" font-size="10" fill="#334155">- title: String</text>
    <text x="10" y="76" font-size="10" fill="#334155">- category: Enum [9 Categories]</text>
    <text x="10" y="92" font-size="10" fill="#334155">- description: String</text>
    <text x="10" y="108" font-size="10.5" fill="#334155">- priority: Enum [LOW, MED, HIGH]</text>
    <text x="10" y="124" font-size="10.5" fill="#334155">- status: Enum [SUB, IN_PROG, RES]</text>
    <text x="10" y="140" font-size="10" fill="#334155">- location: String</text>
    <text x="10" y="156" font-size="10" fill="#334155">- createdBy: ObjectId (Ref User)</text>
    <text x="10" y="172" font-size="10" fill="#334155">- resolutionRemarks: String</text>
    <text x="10" y="188" font-size="10" fill="#334155">- resolvedAt: Date</text>
    <line x1="0" y1="195" x2="210" y2="195" stroke="#1e293b" stroke-width="1"/>
    <text x="10" y="212" font-size="10" fill="#334155">+ appendStatusLog(status, note)</text>
  </g>

  <!-- Association User (1) to Complaint (0..*) -->
  <line x1="220" y1="95" x2="260" y2="95" stroke="#1e293b" stroke-width="1.5"/>
  <text x="225" y="88" font-size="10" font-weight="bold">1</text>
  <text x="245" y="88" font-size="10" font-weight="bold">0..*</text>

  <!-- StatusHistory Class -->
  <g transform="translate(260, 310)">
    <rect x="0" y="0" width="210" height="145" fill="#fefce8" stroke="#ca8a04" stroke-width="1.6"/>
    <rect x="0" y="0" width="210" height="26" fill="#fef08a" stroke="#ca8a04" stroke-width="1.6"/>
    <text x="105" y="18" font-size="12" font-weight="bold" fill="#854d0e" text-anchor="middle">StatusHistory (Embedded)</text>
    <text x="10" y="44" font-size="10" fill="#334155">- status: String</text>
    <text x="10" y="60" font-size="10" fill="#334155">- previousStatus: String</text>
    <text x="10" y="76" font-size="10" fill="#334155">- newStatus: String</text>
    <text x="10" y="92" font-size="10" fill="#334155">- changedBy: ObjectId (Ref User)</text>
    <text x="10" y="108" font-size="10" fill="#334155">- changedAt: Date</text>
    <text x="10" y="124" font-size="10" fill="#334155">- note: String (Max 1000)</text>
  </g>
  <!-- Composition Diamond from Complaint to StatusHistory -->
  <line x1="365" y1="255" x2="365" y2="310" stroke="#1e293b" stroke-width="1.5"/>
  <polygon points="365,255 359,265 365,275 371,265" fill="#1e293b"/>
  <text x="372" y="270" font-size="10" font-weight="bold">1</text>
  <text x="372" y="300" font-size="10" font-weight="bold">1..*</text>

  <!-- Controllers Box -->
  <g transform="translate(505, 120)">
    <rect x="0" y="0" width="165" height="110" fill="#fdf4ff" stroke="#a21caf" stroke-width="1.6"/>
    <rect x="0" y="0" width="165" height="24" fill="#f5d0fe" stroke="#a21caf" stroke-width="1.6"/>
    <text x="82" y="17" font-size="11" font-weight="bold" fill="#86198f" text-anchor="middle">&lt;&lt;Control&gt;&gt; ComplaintCtrl</text>
    <text x="8" y="42" font-size="9.5" fill="#334155">+ createComplaint()</text>
    <text x="8" y="58" font-size="9.5" fill="#334155">+ getUserComplaints()</text>
    <text x="8" y="74" font-size="9.5" fill="#334155">+ updateComplaintStatus()</text>
    <text x="8" y="90" font-size="9.5" fill="#334155">+ getDashboardMetrics()</text>
  </g>
  <line x1="470" y1="160" x2="505" y2="160" stroke="#a21caf" stroke-width="1.2" stroke-dasharray="3,3"/>

  <!-- Database Connection Box -->
  <g transform="translate(505, 300)">
    <rect x="0" y="0" width="165" height="85" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.6"/>
    <rect x="0" y="0" width="165" height="24" fill="#bbf7d0" stroke="#16a34a" stroke-width="1.6"/>
    <text x="82" y="17" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">&lt;&lt;Service&gt;&gt; MongoConnection</text>
    <text x="8" y="44" font-size="9.5" fill="#334155">+ connectDB(): Promise</text>
    <text x="8" y="60" font-size="9.5" fill="#334155">+ autoIndex(): Boolean</text>
    <text x="8" y="76" font-size="9.5" fill="#334155">+ connectionPool: Client</text>
  </g>
</svg>'''

def get_activity_svg():
    return '''<svg width="680" height="520" viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg" style="background:#fff; font-family:'Times New Roman', serif;">
  <!-- Start Node -->
  <circle cx="340" cy="25" r="12" fill="#0f172a"/>
  
  <!-- Step 1: Login -->
  <rect x="250" y="55" width="180" height="35" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
  <text x="340" y="77" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Student / Admin Login</text>
  
  <line x1="340" y1="37" x2="340" y2="55" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="340,55 336,47 344,47" fill="#0f172a"/>

  <!-- Step 2: Open Form -->
  <rect x="250" y="110" width="180" height="35" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
  <text x="340" y="132" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Fill Incident Details Form</text>

  <line x1="340" y1="90" x2="340" y2="110" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="340,110 336,102 344,102" fill="#0f172a"/>

  <!-- Decision: Valid Input? -->
  <polygon points="340,165 410,185 340,205 270,185" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
  <text x="340" y="189" font-size="10.5" font-weight="bold" fill="#78350f" text-anchor="middle">Valid Input?</text>

  <line x1="340" y1="145" x2="340" y2="165" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="340,165 336,157 344,157" fill="#0f172a"/>

  <!-- Invalid Input Loopback -->
  <line x1="410" y1="185" x2="470" y2="185" stroke="#b45309" stroke-width="1.4"/>
  <line x1="470" y1="185" x2="470" y2="127" stroke="#b45309" stroke-width="1.4"/>
  <line x1="470" y1="127" x2="430" y2="127" stroke="#b45309" stroke-width="1.4"/>
  <polygon points="430,127 438,123 438,131" fill="#b45309"/>
  <text x="445" y="180" font-size="9.5" fill="#b45309">No (Alert)</text>

  <!-- Valid Input -> Generate Ticket -->
  <text x="350" y="220" font-size="9.5" fill="#15803d">Yes</text>
  <rect x="235" y="230" width="210" height="38" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
  <text x="340" y="247" font-size="10.5" font-weight="bold" fill="#15803d" text-anchor="middle">Generate Unique Ticket ID</text>
  <text x="340" y="260" font-size="9.5" fill="#166534" text-anchor="middle">&amp; Set Status = "SUBMITTED"</text>

  <line x1="340" y1="205" x2="340" y2="230" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="340,230 336,222 344,222" fill="#0f172a"/>

  <!-- Step 4: Admin Queue Review -->
  <rect x="235" y="290" width="210" height="38" rx="10" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="340" y="307" font-size="10.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Admin Reviews Incident Queue</text>
  <text x="340" y="320" font-size="9.5" fill="#b91c1c" text-anchor="middle">&amp; Dispatches to Technician</text>

  <line x1="340" y1="268" x2="340" y2="290" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="340,290 336,282 344,282" fill="#0f172a"/>

  <!-- Step 5: Transition In Progress -->
  <rect x="235" y="350" width="210" height="35" rx="10" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
  <text x="340" y="372" font-size="10.5" font-weight="bold" fill="#c2410c" text-anchor="middle">Update Status = "IN_PROGRESS"</text>

  <line x1="340" y1="328" x2="340" y2="350" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="340,350 336,342 344,342" fill="#0f172a"/>

  <!-- Step 6: Resolve & Add Remarks -->
  <rect x="220" y="405" width="240" height="40" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
  <text x="340" y="423" font-size="10.5" font-weight="bold" fill="#15803d" text-anchor="middle">Issue Resolved &amp; Remarks Appended</text>
  <text x="340" y="437" font-size="9.5" fill="#166534" text-anchor="middle">Set Status = "RESOLVED" (Timestamped)</text>

  <line x1="340" y1="385" x2="340" y2="405" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="340,405 336,397 344,397" fill="#0f172a"/>

  <!-- Final State (Bullseye) -->
  <circle cx="340" cy="485" r="14" fill="#fff" stroke="#0f172a" stroke-width="2"/>
  <circle cx="340" cy="485" r="8" fill="#0f172a"/>

  <line x1="340" y1="445" x2="340" y2="471" stroke="#0f172a" stroke-width="1.5"/>
  <polygon points="340,471 336,463 344,463" fill="#0f172a"/>
</svg>'''

def get_sequence_svg():
    return '''<svg width="680" height="520" viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg" style="background:#fff; font-family:'Times New Roman', serif;">
  <!-- Lifeline Boxes -->
  <!-- Student -->
  <rect x="30" y="20" width="80" height="35" rx="5" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
  <text x="70" y="42" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>
  <line x1="70" y1="55" x2="70" y2="480" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- React UI -->
  <rect x="140" y="20" width="85" height="35" rx="5" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
  <text x="182" y="42" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">React Client</text>
  <line x1="182" y1="55" x2="182" y2="480" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Controller -->
  <rect x="255" y="20" width="95" height="35" rx="5" fill="#fdf4ff" stroke="#a21caf" stroke-width="1.5"/>
  <text x="302" y="42" font-size="11" font-weight="bold" fill="#86198f" text-anchor="middle">Express Server</text>
  <line x1="302" y1="55" x2="302" y2="480" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- DB -->
  <rect x="385" y="20" width="90" height="35" rx="5" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
  <text x="430" y="42" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">MongoDB</text>
  <line x1="430" y1="55" x2="430" y2="480" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Admin -->
  <rect x="520" y="20" width="80" height="35" rx="5" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="560" y="42" font-size="11" font-weight="bold" fill="#991b1b" text-anchor="middle">Admin</text>
  <line x1="560" y1="55" x2="560" y2="480" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Call 1: Submit Form -->
  <line x1="70" y1="85" x2="182" y2="85" stroke="#0f172a" stroke-width="1.3"/>
  <polygon points="182,85 174,81 174,89" fill="#0f172a"/>
  <text x="126" y="78" font-size="9" fill="#1e293b" text-anchor="middle">submitComplaint(form)</text>

  <!-- Call 2: API POST -->
  <line x1="182" y1="115" x2="302" y2="115" stroke="#0f172a" stroke-width="1.3"/>
  <polygon points="302,115 294,111 294,119" fill="#0f172a"/>
  <text x="242" y="108" font-size="9" fill="#1e293b" text-anchor="middle">POST /api/complaints</text>

  <!-- Self-call: Validate JWT -->
  <path d="M 302,130 L 325,130 L 325,150 L 302,150" fill="none" stroke="#a21caf" stroke-width="1.2"/>
  <polygon points="302,150 310,146 310,154" fill="#a21caf"/>
  <text x="330" y="143" font-size="8.5" fill="#86198f">verifyJWT() &amp; genTicket()</text>

  <!-- Call 3: DB Save -->
  <line x1="302" y1="175" x2="430" y2="175" stroke="#0f172a" stroke-width="1.3"/>
  <polygon points="430,175 422,171 422,179" fill="#0f172a"/>
  <text x="366" y="168" font-size="9" fill="#1e293b" text-anchor="middle">Complaint.save()</text>

  <!-- DB Return -->
  <line x1="430" y1="205" x2="302" y2="205" stroke="#16a34a" stroke-width="1.2" stroke-dasharray="3,3"/>
  <polygon points="302,205 310,201 310,209" fill="#16a34a"/>
  <text x="366" y="198" font-size="8.5" fill="#15803d" text-anchor="middle">201 Document Created</text>

  <!-- Server to UI -->
  <line x1="302" y1="230" x2="182" y2="230" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="3,3"/>
  <polygon points="182,230 190,226 190,234" fill="#0284c7"/>
  <text x="242" y="223" font-size="9" fill="#0369a1" text-anchor="middle">return {ticketNumber}</text>

  <!-- UI to Student -->
  <line x1="182" y1="255" x2="70" y2="255" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3,3"/>
  <polygon points="70,255 78,251 78,259" fill="#0f172a"/>
  <text x="126" y="248" font-size="8.5" fill="#1e293b" text-anchor="middle">Show Success Badge</text>

  <!-- Admin Phase -->
  <!-- Admin queries queue -->
  <line x1="560" y1="290" x2="302" y2="290" stroke="#dc2626" stroke-width="1.3"/>
  <polygon points="302,290 310,286 310,294" fill="#dc2626"/>
  <text x="431" y="283" font-size="9" fill="#991b1b" text-anchor="middle">GET /api/complaints?status=SUBMITTED</text>

  <!-- Server queries DB -->
  <line x1="302" y1="315" x2="430" y2="315" stroke="#0f172a" stroke-width="1.3"/>
  <polygon points="430,315 422,311 422,319" fill="#0f172a"/>
  <text x="366" y="308" font-size="8.5" fill="#1e293b" text-anchor="middle">find({status})</text>

  <!-- DB Returns -->
  <line x1="430" y1="340" x2="560" y2="340" stroke="#16a34a" stroke-width="1.2" stroke-dasharray="3,3"/>
  <polygon points="560,340 552,336 552,344" fill="#16a34a"/>
  <text x="495" y="333" font-size="8.5" fill="#15803d" text-anchor="middle">Return Ticket Queue</text>

  <!-- Admin updates status -->
  <line x1="560" y1="380" x2="302" y2="380" stroke="#dc2626" stroke-width="1.3"/>
  <polygon points="302,380 310,376 310,384" fill="#dc2626"/>
  <text x="431" y="373" font-size="9" fill="#991b1b" text-anchor="middle">PUT /api/complaints/:id/status (RESOLVED)</text>

  <!-- Server writes to DB -->
  <line x1="302" y1="410" x2="430" y2="410" stroke="#0f172a" stroke-width="1.3"/>
  <polygon points="430,410 422,406 422,414" fill="#0f172a"/>
  <text x="366" y="403" font-size="8.5" fill="#1e293b" text-anchor="middle">$set status + $push statusHistory</text>

  <!-- Confirmation back to Admin -->
  <line x1="430" y1="440" x2="560" y2="440" stroke="#16a34a" stroke-width="1.2" stroke-dasharray="3,3"/>
  <polygon points="560,440 552,436 552,444" fill="#16a34a"/>
  <text x="495" y="433" font-size="8.5" fill="#15803d" text-anchor="middle">200 Status Updated</text>

  <!-- Realtime UI notification to Student -->
  <line x1="302" y1="465" x2="182" y2="465" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="3,3"/>
  <polygon points="182,465 190,461 190,469" fill="#0284c7"/>
  <text x="242" y="458" font-size="8.5" fill="#0369a1" text-anchor="middle">Notify Status = RESOLVED</text>
</svg>'''

def get_er_svg():
    return '''<svg width="680" height="520" viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg" style="background:#fff; font-family:'Times New Roman', serif;">
  <!-- USERS Table -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="180" height="170" fill="#fff" stroke="#1e293b" stroke-width="1.8"/>
    <rect x="0" y="0" width="180" height="28" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.8"/>
    <text x="90" y="19" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">USERS</text>
    <text x="10" y="48" font-size="10.5" font-weight="bold" fill="#0284c7">PK  _id : ObjectId</text>
    <text x="10" y="68" font-size="10.5" fill="#334155">    name : String</text>
    <text x="10" y="88" font-size="10.5" fill="#334155">    email : String (Unique)</text>
    <text x="10" y="108" font-size="10.5" fill="#334155">    passwordHash : String</text>
    <text x="10" y="128" font-size="10.5" fill="#334155">    role : Enum (STUDENT/ADMIN)</text>
    <text x="10" y="148" font-size="10.5" fill="#334155">    createdAt : Timestamp</text>
    <text x="10" y="164" font-size="10.5" fill="#334155">    updatedAt : Timestamp</text>
  </g>

  <!-- COMPLAINTS Table -->
  <g transform="translate(380, 30)">
    <rect x="0" y="0" width="260" height="250" fill="#fff" stroke="#1e293b" stroke-width="1.8"/>
    <rect x="0" y="0" width="260" height="28" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.8"/>
    <text x="130" y="19" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">COMPLAINTS</text>
    <text x="10" y="48" font-size="10.5" font-weight="bold" fill="#0284c7">PK  _id : ObjectId</text>
    <text x="10" y="68" font-size="10.5" font-weight="bold" fill="#0f172a">    ticketNumber : String (Indexed)</text>
    <text x="10" y="88" font-size="10.5" font-weight="bold" fill="#b45309">FK  createdBy : ObjectId (Ref USERS)</text>
    <text x="10" y="108" font-size="10.5" fill="#334155">    title : String</text>
    <text x="10" y="128" font-size="10.5" fill="#334155">    category : Enum (9 Categories)</text>
    <text x="10" y="148" font-size="10.5" fill="#334155">    description : String (20-2000)</text>
    <text x="10" y="168" font-size="10.5" fill="#334155">    priority : Enum (LOW/MED/HIGH)</text>
    <text x="10" y="188" font-size="10.5" fill="#334155">    status : Enum (SUB/PROG/RES)</text>
    <text x="10" y="208" font-size="10.5" fill="#334155">    location : String</text>
    <text x="10" y="228" font-size="10.5" fill="#334155">    resolutionRemarks : String</text>
    <text x="10" y="244" font-size="10.5" fill="#334155">    resolvedAt : Date</text>
  </g>

  <!-- STATUS_HISTORY (Subdocument / Table) -->
  <g transform="translate(380, 330)">
    <rect x="0" y="0" width="260" height="155" fill="#fff" stroke="#1e293b" stroke-width="1.8"/>
    <rect x="0" y="0" width="260" height="28" fill="#fef08a" stroke="#ca8a04" stroke-width="1.8"/>
    <text x="130" y="19" font-size="12" font-weight="bold" fill="#854d0e" text-anchor="middle">STATUS_HISTORY (Embedded)</text>
    <text x="10" y="48" font-size="10.5" font-weight="bold" fill="#b45309">FK  complaintId : ObjectId</text>
    <text x="10" y="68" font-size="10.5" fill="#334155">    status : Enum (COMPLAINT_STATUSES)</text>
    <text x="10" y="88" font-size="10.5" fill="#334155">    previousStatus : String</text>
    <text x="10" y="108" font-size="10.5" fill="#334155">    newStatus : String</text>
    <text x="10" y="128" font-size="10.5" font-weight="bold" fill="#b45309">FK  changedBy : ObjectId (Ref USERS)</text>
    <text x="10" y="148" font-size="10.5" fill="#334155">    changedAt : Timestamp</text>
  </g>

  <!-- CATEGORIES Reference Table -->
  <g transform="translate(40, 310)">
    <rect x="0" y="0" width="180" height="120" fill="#fff" stroke="#1e293b" stroke-width="1.8"/>
    <rect x="0" y="0" width="180" height="28" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.8"/>
    <text x="90" y="19" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">CATEGORIES_META</text>
    <text x="10" y="48" font-size="10.5" font-weight="bold" fill="#0284c7">PK  code : String</text>
    <text x="10" y="68" font-size="10.5" fill="#334155">    name : String</text>
    <text x="10" y="88" font-size="10.5" fill="#334155">    department : String</text>
    <text x="10" y="108" font-size="10.5" fill="#334155">    slaHours : Integer</text>
  </g>

  <!-- Relationship: USERS to COMPLAINTS (1 to Many) -->
  <line x1="220" y1="120" x2="380" y2="120" stroke="#1e293b" stroke-width="1.6"/>
  <!-- 1 notation on left -->
  <line x1="230" y1="112" x2="230" y2="128" stroke="#1e293b" stroke-width="1.6"/>
  <!-- Crow's foot on right -->
  <line x1="380" y1="120" x2="368" y2="112" stroke="#1e293b" stroke-width="1.6"/>
  <line x1="380" y1="120" x2="368" y2="128" stroke="#1e293b" stroke-width="1.6"/>
  <text x="245" y="112" font-size="10" font-weight="bold">1 (submits)</text>
  <text x="330" y="112" font-size="10" font-weight="bold">N</text>

  <!-- Relationship: COMPLAINTS to STATUS_HISTORY (1 to Many) -->
  <line x1="510" y1="280" x2="510" y2="330" stroke="#1e293b" stroke-width="1.6"/>
  <!-- 1 on top -->
  <line x1="502" y1="290" x2="518" y2="290" stroke="#1e293b" stroke-width="1.6"/>
  <!-- Crow's foot on bottom -->
  <line x1="510" y1="330" x2="502" y2="318" stroke="#1e293b" stroke-width="1.6"/>
  <line x1="510" y1="330" x2="518" y2="318" stroke="#1e293b" stroke-width="1.6"/>
  <text x="520" y="300" font-size="10" font-weight="bold">1</text>
  <text x="520" y="325" font-size="10" font-weight="bold">N</text>

  <!-- Relationship: USERS to STATUS_HISTORY (Admin/User changedBy) -->
  <path d="M 130,220 L 130,470 L 380,470" fill="none" stroke="#64748b" stroke-width="1.4" stroke-dasharray="4,3"/>
  <polygon points="380,470 372,466 372,474" fill="#64748b"/>
  <text x="200" y="465" font-size="9.5" fill="#64748b">changedBy Ref (User)</text>
</svg>'''

def get_db_screenshot_svg():
    return '''<svg width="680" height="520" viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg" style="background:#1e1e1e; font-family:'Courier New', monospace; border-radius:6px;">
  <!-- Window Header Bar -->
  <rect x="0" y="0" width="680" height="30" fill="#2d2d2d" rx="6"/>
  <circle cx="16" cy="15" r="5" fill="#ef4444"/>
  <circle cx="32" cy="15" r="5" fill="#eab308"/>
  <circle cx="48" cy="15" r="5" fill="#22c55e"/>
  <text x="340" y="20" font-size="11" font-weight="bold" fill="#cccccc" text-anchor="middle" font-family="'Times New Roman', serif;">MongoDB Compass — mongodb+srv://cluster.mongodb.net/campuscare</text>

  <!-- Left Sidebar (Databases / Collections) -->
  <rect x="0" y="30" width="160" height="490" fill="#252526"/>
  <text x="15" y="55" font-size="10.5" font-weight="bold" fill="#3b82f6">&gt; campuscare</text>
  <text x="30" y="75" font-size="10" fill="#60a5fa">📄 users (12)</text>
  <text x="30" y="95" font-size="10" fill="#4ade80">📄 complaints (28)</text>
  <text x="30" y="115" font-size="10" fill="#94a3b8">📄 system_logs (142)</text>
  <line x1="160" y1="30" x2="160" y2="520" stroke="#333333" stroke-width="1"/>

  <!-- Top Filter Query Bar -->
  <rect x="170" y="40" width="495" height="32" fill="#1f2430" rx="4" stroke="#3b82f6" stroke-width="1"/>
  <text x="180" y="60" font-size="10" fill="#93c5fd">FILTER: { "status": "SUBMITTED", "priority": "HIGH" } | SORT: { "createdAt": -1 }</text>
  <rect x="615" y="44" width="45" height="24" rx="3" fill="#2563eb"/>
  <text x="637" y="60" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">FIND</text>

  <!-- Query Results Header -->
  <text x="175" y="90" font-size="10" font-weight="bold" fill="#10b981">Query returned 2 documents (Execution Time: 3.4 ms)</text>

  <!-- Document 1 Card -->
  <g transform="translate(170, 100)">
    <rect x="0" y="0" width="495" height="185" fill="#181824" rx="5" stroke="#383850" stroke-width="1"/>
    <text x="15" y="20" font-size="9.5" fill="#e2e8f0">{</text>
    <text x="25" y="38" font-size="9.5" fill="#93c5fd">"_id":</text><text x="75" y="38" font-size="9.5" fill="#fca5a5"> ObjectId("6712ab091f8a91c0e")</text><text x="290" y="38" font-size="9" fill="#64748b">,</text>
    <text x="25" y="56" font-size="9.5" fill="#93c5fd">"ticketNumber":</text><text x="125" y="56" font-size="9.5" fill="#86efac"> "CC-2026-0014"</text><text x="240" y="56" font-size="9" fill="#64748b">,</text>
    <text x="25" y="74" font-size="9.5" fill="#93c5fd">"title":</text><text x="75" y="74" font-size="9.5" fill="#fef08a"> "Server Room Core Switch Power Supply Failure"</text><text x="390" y="74" font-size="9" fill="#64748b">,</text>
    <text x="25" y="92" font-size="9.5" fill="#93c5fd">"category":</text><text x="100" y="92" font-size="9.5" fill="#86efac"> "Internet / Wi-Fi"</text><text x="235" y="92" font-size="9" fill="#64748b">,</text>
    <text x="25" y="110" font-size="9.5" fill="#93c5fd">"priority":</text><text x="95" y="110" font-size="9.5" fill="#f87171"> "HIGH"</text><text x="150" y="110" font-size="9" fill="#64748b">,</text>
    <text x="25" y="128" font-size="9.5" fill="#93c5fd">"status":</text><text x="85" y="128" font-size="9.5" fill="#60a5fa"> "SUBMITTED"</text><text x="180" y="128" font-size="9" fill="#64748b">,</text>
    <text x="25" y="146" font-size="9.5" fill="#93c5fd">"location":</text><text x="95" y="146" font-size="9.5" fill="#fef08a"> "Computer Center - 2nd Floor, Server Rack 4"</text><text x="395" y="146" font-size="9" fill="#64748b">,</text>
    <text x="25" y="164" font-size="9.5" fill="#93c5fd">"createdBy":</text><text x="105" y="164" font-size="9.5" fill="#fca5a5"> ObjectId("671288f21900a3bb8")</text>
    <text x="15" y="180" font-size="9.5" fill="#e2e8f0">}</text>
  </g>

  <!-- Document 2 Card (User Collection Preview) -->
  <g transform="translate(170, 300)">
    <rect x="0" y="0" width="495" height="190" fill="#181824" rx="5" stroke="#383850" stroke-width="1"/>
    <text x="15" y="20" font-size="9.5" fill="#e2e8f0">{</text>
    <text x="25" y="38" font-size="9.5" fill="#93c5fd">"_id":</text><text x="75" y="38" font-size="9.5" fill="#fca5a5"> ObjectId("671288f21900a3bb8")</text><text x="290" y="38" font-size="9" fill="#64748b">,</text>
    <text x="25" y="56" font-size="9.5" fill="#93c5fd">"name":</text><text x="80" y="56" font-size="9.5" fill="#86efac"> "Tanish Jain"</text><text x="180" y="56" font-size="9" fill="#64748b">,</text>
    <text x="25" y="74" font-size="9.5" fill="#93c5fd">"email":</text><text x="85" y="74" font-size="9.5" fill="#86efac"> "tanishjain0502@gmail.com"</text><text x="270" y="74" font-size="9" fill="#64748b">,</text>
    <text x="25" y="92" font-size="9.5" fill="#93c5fd">"role":</text><text x="75" y="92" font-size="9.5" fill="#38bdf8"> "STUDENT"</text><text x="160" y="92" font-size="9" fill="#64748b">,</text>
    <text x="25" y="110" font-size="9.5" fill="#93c5fd">"passwordHash":</text><text x="130" y="110" font-size="9" fill="#94a3b8"> "$2a$10$w8T0M9r1vB7xQ3..." (select: false)</text><text x="420" y="110" font-size="9" fill="#64748b">,</text>
    <text x="25" y="128" font-size="9.5" fill="#93c5fd">"createdAt":</text><text x="110" y="128" font-size="9.5" fill="#fef08a"> ISODate("2026-10-17T11:20:00Z")</text><text x="350" y="128" font-size="9" fill="#64748b">,</text>
    <text x="25" y="146" font-size="9.5" fill="#93c5fd">"updatedAt":</text><text x="110" y="146" font-size="9.5" fill="#fef08a"> ISODate("2026-10-18T10:14:00Z")</text>
    <text x="15" y="170" font-size="9.5" fill="#e2e8f0">}</text>
  </g>
</svg>'''

def get_ui_screenshot_svg():
    return '''<svg width="680" height="520" viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; font-family:'Segoe UI', Arial, sans-serif; border-radius:6px; border:1px solid #cbd5e1;">
  <!-- Navbar -->
  <rect x="0" y="0" width="680" height="42" fill="#0f172a"/>
  <circle cx="25" cy="21" r="10" fill="#3b82f6"/>
  <text x="42" y="26" font-size="13" font-weight="bold" fill="#ffffff">CampusCare</text>
  <text x="130" y="26" font-size="11" fill="#94a3b8">Portal: SGSITS Indore</text>

  <rect x="440" y="9" width="130" height="24" rx="4" fill="#1e293b"/>
  <text x="505" y="25" font-size="10" fill="#e2e8f0" text-anchor="middle">Role: ADMINISTRATOR</text>
  <rect x="585" y="9" width="80" height="24" rx="4" fill="#dc2626"/>
  <text x="625" y="25" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Log Out</text>

  <!-- Metrics Row (4 Cards) -->
  <!-- Card 1 -->
  <g transform="translate(20, 55)">
    <rect x="0" y="0" width="145" height="65" rx="6" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
    <text x="12" y="20" font-size="10" font-weight="bold" fill="#64748b">TOTAL TICKETS</text>
    <text x="12" y="48" font-size="20" font-weight="bold" fill="#0f172a">28</text>
    <text x="60" y="48" font-size="9.5" fill="#16a34a">+12% this week</text>
  </g>
  <!-- Card 2 -->
  <g transform="translate(180, 55)">
    <rect x="0" y="0" width="145" height="65" rx="6" fill="#ffffff" stroke="#bae6fd" stroke-width="1.5"/>
    <text x="12" y="20" font-size="10" font-weight="bold" fill="#0369a1">SUBMITTED</text>
    <text x="12" y="48" font-size="20" font-weight="bold" fill="#0284c7">5</text>
    <text x="45" y="48" font-size="9.5" fill="#0284c7">Awaiting review</text>
  </g>
  <!-- Card 3 -->
  <g transform="translate(340, 55)">
    <rect x="0" y="0" width="145" height="65" rx="6" fill="#ffffff" stroke="#fed7aa" stroke-width="1.5"/>
    <text x="12" y="20" font-size="10" font-weight="bold" fill="#c2410c">IN PROGRESS</text>
    <text x="12" y="48" font-size="20" font-weight="bold" fill="#ea580c">7</text>
    <text x="45" y="48" font-size="9.5" fill="#ea580c">Assigned to staff</text>
  </g>
  <!-- Card 4 -->
  <g transform="translate(500, 55)">
    <rect x="0" y="0" width="155" height="65" rx="6" fill="#ffffff" stroke="#bbf7d0" stroke-width="1.5"/>
    <text x="12" y="20" font-size="10" font-weight="bold" fill="#15803d">RESOLVED</text>
    <text x="12" y="48" font-size="20" font-weight="bold" fill="#16a34a">16</text>
    <text x="50" y="48" font-size="9.5" fill="#16a34a">94% SLA Met</text>
  </g>

  <!-- Section 1: Admin Management Table -->
  <g transform="translate(20, 135)">
    <rect x="0" y="0" width="635" height="175" rx="6" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
    <!-- Table Header -->
    <rect x="0" y="0" width="635" height="30" rx="6" fill="#f1f5f9"/>
    <text x="15" y="20" font-size="10" font-weight="bold" fill="#475569">TICKET</text>
    <text x="110" y="20" font-size="10" font-weight="bold" fill="#475569">TITLE</text>
    <text x="310" y="20" font-size="10" font-weight="bold" fill="#475569">CATEGORY</text>
    <text x="420" y="20" font-size="10" font-weight="bold" fill="#475569">PRIORITY</text>
    <text x="500" y="20" font-size="10" font-weight="bold" fill="#475569">STATUS</text>
    <text x="580" y="20" font-size="10" font-weight="bold" fill="#475569">ACTION</text>

    <!-- Row 1 -->
    <line x1="0" y1="31" x2="635" y2="31" stroke="#e2e8f0"/>
    <text x="15" y="52" font-size="10" font-weight="bold" fill="#2563eb">CC-2026-0014</text>
    <text x="110" y="52" font-size="9.5" fill="#1e293b">Core Switch Power Supply Failure</text>
    <text x="310" y="52" font-size="9.5" fill="#475569">Internet / Wi-Fi</text>
    <rect x="415" y="40" width="45" height="18" rx="3" fill="#fee2e2"/>
    <text x="437" y="53" font-size="9" font-weight="bold" fill="#dc2626" text-anchor="middle">HIGH</text>
    <rect x="495" y="40" width="65" height="18" rx="3" fill="#e0f2fe"/>
    <text x="527" y="53" font-size="9" font-weight="bold" fill="#0284c7" text-anchor="middle">SUBMITTED</text>
    <text x="585" y="53" font-size="9.5" font-weight="bold" fill="#2563eb">Manage &gt;</text>

    <!-- Row 2 -->
    <line x1="0" y1="67" x2="635" y2="67" stroke="#e2e8f0"/>
    <text x="15" y="88" font-size="10" font-weight="bold" fill="#2563eb">CC-2026-0012</text>
    <text x="110" y="88" font-size="9.5" fill="#1e293b">Hostel 3 Geyser Heating Element Damaged</text>
    <text x="310" y="88" font-size="9.5" fill="#475569">Hostel</text>
    <rect x="415" y="76" width="45" height="18" rx="3" fill="#fee2e2"/>
    <text x="437" y="89" font-size="9" font-weight="bold" fill="#dc2626" text-anchor="middle">HIGH</text>
    <rect x="495" y="76" width="65" height="18" rx="3" fill="#ffedd5"/>
    <text x="527" y="89" font-size="9" font-weight="bold" fill="#c2410c" text-anchor="middle">IN PROG</text>
    <text x="585" y="89" font-size="9.5" font-weight="bold" fill="#2563eb">Manage &gt;</text>

    <!-- Row 3 -->
    <line x1="0" y1="103" x2="635" y2="103" stroke="#e2e8f0"/>
    <text x="15" y="124" font-size="10" font-weight="bold" fill="#2563eb">CC-2026-0009</text>
    <text x="110" y="124" font-size="9.5" fill="#1e293b">Classroom 204 Projector HDMI Port Broken</text>
    <text x="310" y="124" font-size="9.5" fill="#475569">Classroom</text>
    <rect x="415" y="112" width="45" height="18" rx="3" fill="#fef3c7"/>
    <text x="437" y="125" font-size="9" font-weight="bold" fill="#b45309" text-anchor="middle">MED</text>
    <rect x="495" y="112" width="65" height="18" rx="3" fill="#dcfce7"/>
    <text x="527" y="125" font-size="9" font-weight="bold" fill="#15803d" text-anchor="middle">RESOLVED</text>
    <text x="585" y="125" font-size="9.5" font-weight="bold" fill="#2563eb">View &gt;</text>

    <!-- Row 4 -->
    <line x1="0" y1="139" x2="635" y2="139" stroke="#e2e8f0"/>
    <text x="15" y="160" font-size="10" font-weight="bold" fill="#2563eb">CC-2026-0005</text>
    <text x="110" y="160" font-size="9.5" fill="#1e293b">Drinking Water Cooler Filter Replacement</text>
    <text x="310" y="160" font-size="9.5" fill="#475569">Cleanliness</text>
    <rect x="415" y="148" width="45" height="18" rx="3" fill="#f1f5f9"/>
    <text x="437" y="161" font-size="9" font-weight="bold" fill="#475569" text-anchor="middle">LOW</text>
    <rect x="495" y="148" width="65" height="18" rx="3" fill="#dcfce7"/>
    <text x="527" y="161" font-size="9" font-weight="bold" fill="#15803d" text-anchor="middle">RESOLVED</text>
    <text x="585" y="161" font-size="9.5" font-weight="bold" fill="#2563eb">View &gt;</text>
  </g>

  <!-- Section 2: Student Ticket Status Lifecycle Timeline -->
  <g transform="translate(20, 325)">
    <rect x="0" y="0" width="635" height="180" rx="6" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
    <text x="18" y="24" font-size="11" font-weight="bold" fill="#0f172a">Student Grievance Timeline View: CC-2026-0012</text>
    <line x1="18" y1="33" x2="615" y2="33" stroke="#f1f5f9"/>

    <!-- Timeline Steps -->
    <!-- Step 1 -->
    <circle cx="50" cy="65" r="12" fill="#22c55e"/>
    <text x="50" y="69" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">✓</text>
    <text x="75" y="62" font-size="10.5" font-weight="bold" fill="#0f172a">Grievance Submitted</text>
    <text x="75" y="75" font-size="9" fill="#64748b">17 Oct 2026, 10:15 AM • Submitted by Tanish Jain (0801CA251139)</text>

    <line x1="50" y1="78" x2="50" y2="105" stroke="#22c55e" stroke-width="2"/>

    <!-- Step 2 -->
    <circle cx="50" cy="115" r="12" fill="#3b82f6"/>
    <text x="50" y="119" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">2</text>
    <text x="75" y="112" font-size="10.5" font-weight="bold" fill="#0f172a">Under Active Resolution (In Progress)</text>
    <text x="75" y="125" font-size="9" fill="#64748b">17 Oct 2026, 02:40 PM • Assigned to Hostel Maintenance Technician Team</text>
    
    <line x1="50" y1="128" x2="50" y2="150" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="3,3"/>

    <!-- Step 3 -->
    <circle cx="50" cy="158" r="10" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
    <text x="75" y="157" font-size="10.5" font-weight="bold" fill="#94a3b8">Resolution &amp; Verification</text>
    <text x="75" y="169" font-size="9" fill="#94a3b8">Pending electrical spare part replacement in Hostel 3</text>
  </g>
</svg>'''

print("Diagram helper functions defined.")

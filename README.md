# 🎓 CampusCare — College Complaint Management System

CampusCare is a full-stack MERN application that allows students to submit college-related complaints and administrators to manage those complaints efficiently.

> **Part 1** implemented the project setup and authentication system.  
> **Part 2** implemented the student complaint submission, tracking, and dashboard module.  
> **Part 3** implements administrative complaint management, status triage, and resolution workflows.  
> **Part 4** implements end-to-end verification, security audits, UI polish, and deployment readiness.

---

## Technology Stack

| Layer     | Technology                                |
|-----------|-------------------------------------------|
| Frontend  | React 18, Vite, Bootstrap 5, React Router, Axios |
| Backend   | Node.js, Express.js                       |
| Database  | MongoDB with Mongoose                     |
| Auth      | JWT (jsonwebtoken), bcryptjs              |
| Env       | dotenv                                    |

---

## Prerequisites

- **Node.js** v18 or higher (`node --version`)
- **npm** v9 or higher (`npm --version`)
- **MongoDB** — local instance or [MongoDB Atlas](https://www.mongodb.com/atlas)

---

## Project Structure

```
campuscare/
├── client/                     # React + Vite frontend
│   ├── src/
│   │   ├── components/         # Navbar, Footer, ProtectedRoute, StatusBadge, PriorityBadge, EmptyState
│   │   ├── constants/          # complaintConstants.js (categories, priorities, statuses)
│   │   ├── context/            # AuthContext (auth state + actions)
│   │   ├── pages/              # HomePage, LoginPage, RegisterPage,
│   │   │                       # StudentDashboard, SubmitComplaintPage, MyComplaintsPage,
│   │   │                       # ComplaintDetailsPage, AdminDashboard, etc.
│   │   ├── services/           # api.js, authService.js, complaintService.js
│   │   ├── App.jsx             # Root component with all routes
│   │   └── main.jsx            # React entry point
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
│
├── server/                     # Express backend
│   ├── src/
│   │   ├── config/             # db.js — MongoDB connection
│   │   ├── constants/          # complaintConstants.js (categories, priorities, statuses)
│   │   ├── controllers/        # authController.js, complaintController.js
│   │   ├── middleware/         # auth.js (protect, restrictTo)
│   │   ├── models/             # User.js, Complaint.js
│   │   ├── routes/             # authRoutes.js, complaintRoutes.js
│   │   ├── scripts/            # seedAdmin.js, testComplaintModule.js
│   │   ├── utils/              # ticketGenerator.js
│   │   ├── app.js              # Express app (CORS, routes, error handling)
│   │   └── server.js           # Entry point
│   ├── .env.example
│   └── package.json
│
├── .gitignore
└── README.md
```

---

## Student Complaint Features (Part 2)

### 1. Complaint Submission (`/student/complaints/new`)
- **Title:** 5–100 characters.
- **Category:** Dropdown of centrally defined campus categories:
  - Classroom, Laboratory, Internet / Wi-Fi, Electrical / Maintenance, Cleanliness, Library, Hostel, Administration, Other.
- **Priority:** LOW, MEDIUM (default), HIGH.
- **Location:** Optional string up to 100 characters (e.g. "Room 302, Tech Block").
- **Description:** 20–2000 characters.
- **Security & Integrity:** Status is locked to `SUBMITTED`, student creator ID is derived strictly from the verified JWT, and administrative parameters are rejected. Double-submit protection prevents duplicate requests.

### 2. My Complaints List (`/student/complaints`)
- Scoped strictly to the logged-in student's complaints.
- Real-time search across ticket number and title.
- Filters by status and category.
- Sorting by newest or oldest.
- Pagination support with metadata.
- View Details link for each ticket.

### 3. Complaint Details (`/student/complaints/:id`)
- Displays ticket number, title, description, category, priority, status, and location.
- Status history timeline tracking all updates.
- Strictly isolated: access to another student's complaint ID returns HTTP 404 to prevent unauthorized data exposure.

### 4. Student Dashboard (`/student/dashboard`)
- Real-time complaint statistics from the database (Total, Submitted, In Progress, Resolved).
- Quick actions for "Submit a Complaint" and "View All Complaints".
- Recent complaints table with live status badges.

---

## Admin Complaint Management Features (Part 3)

### 1. Admin Dashboard (`/admin/dashboard`)
- **Live Statistics:** MongoDB aggregation displaying exact counts for Total Complaints, Pending/Submitted, In Progress, and Resolved.
- **Filter Shortcuts:** Clicking any statistic card directly opens the filtered view in the Complaints table.
- **Recent Complaints Table:** Displays the 5 latest complaints with live ticket numbers, student names, categories, priorities, statuses, and quick action links.
- **Quick Links:** Navigation directly to All Complaints table and filter shortcuts.

### 2. All Complaints Page (`/admin/complaints`)
- **Admin Triage Table:** Displays ticket number, title, student name & email, category, priority, status, created date, and updated date.
- **Multi-Field Search:** Searches across ticket number, complaint title, and student name or email.
- **Multi-Filter System:** Filter simultaneously by status (`SUBMITTED`, `IN_PROGRESS`, `RESOLVED`), category, and priority (`LOW`, `MEDIUM`, `HIGH`).
- **Sorting & Pagination:** Sort by newest or oldest; paginated with configurable limits and page navigation.
- **Empty & Error States:** Graceful display when filters yield no records or network errors occur.

### 3. Complaint Details & Status Workflow (`/admin/complaints/:id`)
- **Complete Information:** Ticket number, full student information (name and email), category, priority, location, created and updated timestamps.
- **Status Transition Workflow:** Allows transitioning status between `SUBMITTED`, `IN_PROGRESS`, and `RESOLVED`.
- **Resolution Remarks Enforcement:** Transitioning to `RESOLVED` strictly requires a resolution remark (minimum 5 characters).
- **Audit History:** Every status transition automatically logs the previous status, new status, acting admin User ID, timestamp, and remark/note.
- **Resolution Lock:** Already resolved complaints are locked against duplicate resolution or arbitrary modification to ensure data integrity.

---

## Complaint Status Definitions

| Status | Description |
| :--- | :--- |
| `SUBMITTED` | Initial state. The complaint has been registered and is pending staff/admin triage. |
| `IN_PROGRESS` | The complaint is actively being investigated or scheduled for maintenance. |
| `RESOLVED` | The concern has been addressed and closed by college staff. |

---

## Installation & Setup

### 1. Install Dependencies

```bash
# Backend dependencies
cd server
npm install

# Frontend dependencies
cd ../client
npm install
```

### 2. Environment Variables

Create `server/.env` based on `server/.env.example`:

```env
PORT=5001
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/campuscare?retryWrites=true&w=majority
JWT_SECRET=your_long_random_jwt_secret_here
JWT_EXPIRES_IN=7d
CLIENT_URL=http://localhost:5173
```

---

## Starting the Application

### Backend (Terminal 1)

```bash
cd server
npm run dev
# Server runs on http://localhost:5001 (or configured PORT)
```

### Frontend (Terminal 2)

```bash
cd client
npm run dev
# Client runs on http://localhost:5173
```

---

## Initializing the First Administrator

```bash
cd server
ADMIN_EMAIL=admin@college.edu ADMIN_PASSWORD=StrongAdminPassword123 npm run seed:admin
```

---

## API Endpoints

### Authentication Endpoints

| Method | Endpoint | Auth? | Role | Description |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/api/health` | No | Public | Server health status |
| `POST` | `/api/auth/register` | No | Public | Register new student (role: STUDENT) |
| `POST` | `/api/auth/login` | No | Public | Authenticate user & receive JWT |
| `GET` | `/api/auth/me` | Yes | All | Get current authenticated user profile |

### Student Complaint Endpoints (Part 2)

| Method | Endpoint | Auth? | Role | Description |
| :--- | :--- | :--- | :--- | :--- |
| `POST` | `/api/complaints` | Yes | STUDENT | Submit a new complaint |
| `GET` | `/api/complaints/mine` | Yes | STUDENT | List complaints owned by current student (supports `search`, `status`, `category`, `sort`, `page`, `limit`) |
| `GET` | `/api/complaints/mine/stats` | Yes | STUDENT | Get complaint counts (total, submitted, inProgress, resolved) |
| `GET` | `/api/complaints/:id` | Yes | STUDENT | View details of a specific complaint owned by current student |

### Admin Complaint Endpoints (Part 3)

| Method | Endpoint | Auth? | Role | Description |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/api/complaints` | Yes | ADMIN | List all complaints with pagination, multi-field search (`search`), and filters (`status`, `category`, `priority`, `sort`, `page`, `limit`) |
| `GET` | `/api/complaints/admin/stats` | Yes | ADMIN | Overall complaint counts for dashboard (total, submitted, inProgress, resolved) |
| `GET` | `/api/complaints/admin/recent` | Yes | ADMIN | Recent complaints list for dashboard (supports `?limit=N`) |
| `GET` | `/api/complaints/admin/:id` | Yes | ADMIN | Complete details for a complaint including student contact info and status history |
| `PATCH` | `/api/complaints/:id/status` | Yes | ADMIN | Update complaint status (`SUBMITTED`, `IN_PROGRESS`, `RESOLVED`). Requires `remarks` (>=5 chars) on `RESOLVED`. Locks already resolved tickets. |

---

## Automated Testing

### Student Complaint Module Tests (Part 2)

```bash
cd server
npm run test:complaints
```

The test suite validates:
1. Student creates a valid complaint with auto-generated ticket number (`CC-YYYYMMDD-XXXXXX`).
2. Input validation rejects invalid title and description lengths.
3. Category and priority validation rejects unrecognized values.
4. Unauthenticated requests are rejected with HTTP 401.
5. ADMIN users cannot use student-only complaint creation routes (HTTP 403).
6. Students can retrieve only their own complaints.
7. Attempting to access another student's complaint returns HTTP 404.
8. Students cannot set status to RESOLVED during submission.
9. Dashboard statistics match real database counts.
10. Search, category filter, status filter, sorting, and pagination work properly.
11. Ticket number uniqueness and format integrity under load.
12. Registration and login functionality continue to function properly.

### Admin Complaint Management Tests (Part 3)

```bash
cd server
npm run test:admin
```

The Part 3 test suite validates:
1. Authenticated students can create complaints (Part 2 creation preserved).
2. Admin can list all complaints across students with pagination.
3. Admin dashboard statistics match real database counts.
4. Admin can update complaint status to `IN_PROGRESS` with audit history.
5. Rejection with HTTP 400 when attempting to resolve without valid remarks (missing or < 5 characters).
6. Admin resolves complaint with remarks, saving `resolvedAt`, `resolutionRemarks`, and admin identity in `statusHistory`.
7. Re-resolving or modifying an already resolved complaint is rejected safely with HTTP 400.
8. Students cannot access admin endpoints (HTTP 403 Forbidden).
9. Unauthenticated requests to admin endpoints return HTTP 401 Unauthorized.
10. Invalid status strings (400) and nonexistent IDs (404) are handled safely.
11. Admin multi-field search and combination filters (status, category, priority) function accurately.
12. Student complaint privacy, isolation, and `/complaints/mine` restrictions remain strictly intact.

### End-to-End Lifecycle & Security Tests (Part 4)

```bash
cd server
npm run test:part4
```

The Part 4 suite executes:
- **10-Step Full Lifecycle Workflow:**
  1. Student registration (`POST /api/auth/register`).
  2. Student login & JWT token issuance (`POST /api/auth/login`).
  3. Student complaint creation (`POST /api/complaints`).
  4. Complaint listing verification in My Complaints (`GET /api/complaints/mine`).
  5. Complaint details inspection (`GET /api/complaints/:id`).
  6. Admin login (`POST /api/auth/login`).
  7. Admin locates complaint via multi-field search (`GET /api/complaints?search=...`).
  8. Admin updates status to `IN_PROGRESS` with audit history (`PATCH /api/complaints/:id/status`).
  9. Admin resolves complaint with remarks (`PATCH /api/complaints/:id/status`).
  10. Student re-login and verification of `RESOLVED` status, remarks banner, and timeline.
- **Security & Robustness Tests:**
  - Missing token rejected with HTTP 401 across all protected routes.
  - Public registration privilege escalation prevention (attempting `{ role: 'ADMIN' }` forces `STUDENT`).
  - Students accessing admin routes rejected with HTTP 403 Forbidden.
  - Cross-student complaint privacy enforced (accessing another student's complaint returns 404).
  - Admin status updates validated (invalid statuses rejected; reopening resolved complaints rejected).
  - Password hashes, salt rounds, and JWT secrets verified absent from all responses.
  - MongoDB queries ReDoS-safe and invalid ObjectIDs handled safely without server errors.

---

## Deployment Readiness

### 1. Production Build

#### Frontend
```bash
cd client
npm run build
# Production assets generated into client/dist/
```

#### Backend Syntax Check
```bash
cd server
node --check src/server.js
node --check src/app.js
```

### 2. Environment Variables Checklist

Ensure the following variables are configured in the hosting environment (e.g. systemd, PM2, Docker, or PaaS environment):

| Variable | Environment | Description | Example |
| :--- | :--- | :--- | :--- |
| `NODE_ENV` | Backend | Runtime mode | `production` |
| `PORT` | Backend | Listening port | `5001` |
| `MONGODB_URI` | Backend | MongoDB Atlas connection string | `mongodb+srv://user:pass@cluster.mongodb.net/campuscare` |
| `JWT_SECRET` | Backend | High-entropy random secret key | (64+ character random string) |
| `JWT_EXPIRES_IN` | Backend | JWT expiration window | `7d` |
| `CLIENT_URL` | Backend | Whitelisted CORS origin for frontend | `https://campuscare.college.edu` |
| `VITE_API_URL` | Frontend | Backend API endpoint base URL | `https://campuscare-api.college.edu/api` |

### 3. Production Deployment Guidelines

- **Frontend Hosting:** Serve `client/dist/` via Nginx, Caddy, Cloudflare Pages, Vercel, or AWS S3 + CloudFront with Single Page Application (SPA) rewrite rules routing all non-asset requests to `index.html`.
- **Backend Hosting:** Run Node.js behind a reverse proxy (e.g. Nginx with SSL/TLS termination) with a process manager like **PM2** (`pm2 start src/server.js --name campuscare-api`).
- **Database:** Use a production-tier MongoDB Atlas cluster with automatic daily backups, IP allowlisting, and TLS enabled.
- **CORS & Domain:** Set `CLIENT_URL` strictly to your production domain to block cross-origin requests.

---

## Security & Architecture Rules

- Passwords hashed with bcrypt (10-12 salt rounds).
- Passwords omitted from all API responses via schema `select: false` and `toJSON` transform.
- Role-based route enforcement on both backend middleware (`protect`, `restrictTo`) and frontend (`ProtectedRoute`).
- Complaint ownership enforced strictly on the server: `createdBy: req.user._id`.
- Ticket numbers generated cryptographically on the server with collision retry.
- Regular expression search inputs sanitized against ReDoS.
- CORS restricted to configured `CLIENT_URL`.
- Sensitive credentials kept in `server/.env` (gitignored).
- Zero external dependencies on SmartAttendee.


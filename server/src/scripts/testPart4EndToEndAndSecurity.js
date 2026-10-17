/**
 * testPart4EndToEndAndSecurity.js
 * Comprehensive automated verification script for CampusCare Part 4:
 * 1. Complete End-to-End functional lifecycle (Steps 1 to 10)
 * 2. Exhaustive Security & Reliability testing
 */

require('dotenv').config({ path: require('path').resolve(__dirname, '../../.env') });
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const http = require('http');

const app = require('../app');
const User = require('../models/User');
const Complaint = require('../models/Complaint');

const runPart4Tests = async () => {
  console.log('===============================================================');
  console.log('🚀 CampusCare — Part 4 E2E Functional & Security Test Suite');
  console.log('===============================================================\n');

  if (!process.env.MONGODB_URI) {
    console.error('❌ MONGODB_URI not configured in .env');
    process.exit(1);
  }

  await mongoose.connect(process.env.MONGODB_URI);
  console.log('Connected to MongoDB.\n');

  const server = http.createServer(app);
  await new Promise((resolve) => server.listen(0, resolve));
  const port = server.address().port;
  const baseUrl = `http://127.0.0.1:${port}/api`;

  const createdUserIds = [];
  const createdComplaintIds = [];

  let testsPassed = 0;
  let totalTests = 0;

  const assertTest = (name, condition, errorMsg = '') => {
    totalTests++;
    if (condition) {
      console.log(`  ✅ PASS: ${name}`);
      testsPassed++;
      return true;
    } else {
      console.error(`  ❌ FAIL: ${name}${errorMsg ? ` - ${errorMsg}` : ''}`);
      return false;
    }
  };

  const apiCall = async (endpoint, options = {}) => {
    const res = await fetch(`${baseUrl}${endpoint}`, options);
    const json = await res.json().catch(() => ({}));
    return { status: res.status, data: json };
  };

  try {
    const timestamp = Date.now();
    const studentPassword = 'SecureStudentPassword123!';
    const adminPassword = 'SecureAdminPassword123!';
    const studentEmail = `student_e2e_${timestamp}@college.edu`;
    const adminEmail = `admin_e2e_${timestamp}@college.edu`;

    // Pre-create an admin user safely for the E2E lifecycle
    const adminPwHash = await bcrypt.hash(adminPassword, 10);
    const adminUser = await User.create({
      name: 'E2E System Admin',
      email: adminEmail,
      passwordHash: adminPwHash,
      role: 'ADMIN',
    });
    createdUserIds.push(adminUser._id);

    console.log('---------------------------------------------------------------');
    console.log('SECTION 1: 10-STEP END-TO-END FUNCTIONAL WORKFLOW');
    console.log('---------------------------------------------------------------\n');

    // STEP 1: Register a student account
    console.log('Step 1: Register a new student account...');
    const registerRes = await apiCall('/auth/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: 'Aarav Sharma',
        email: studentEmail,
        password: studentPassword,
      }),
    });
    const step1Ok =
      registerRes.status === 201 &&
      registerRes.data.success &&
      registerRes.data.user?.role === 'STUDENT' &&
      registerRes.data.token;
    assertTest('Step 1: Student registered successfully with role STUDENT', step1Ok);
    if (registerRes.data.user?.id) {
      createdUserIds.push(registerRes.data.user.id);
    }

    // STEP 2: Log in as the student
    console.log('\nStep 2: Log in as the student...');
    const loginRes = await apiCall('/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: studentEmail,
        password: studentPassword,
      }),
    });
    const step2Ok =
      loginRes.status === 200 &&
      loginRes.data.success &&
      loginRes.data.user?.email === studentEmail &&
      loginRes.data.token;
    assertTest('Step 2: Student logged in and received valid JWT', step2Ok);
    const studentToken = loginRes.data.token;

    // STEP 3: Submit a complaint as student
    console.log('\nStep 3: Student submits a new complaint...');
    const submitRes = await apiCall('/complaints', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${studentToken}`,
      },
      body: JSON.stringify({
        title: 'Water cooler leaking in Block B 3rd Floor',
        category: 'Cleanliness',
        description: 'Water has been pooling around the cooler near room 305 creating slip hazards.',
        priority: 'HIGH',
        location: 'Block B, 3rd Floor Corridor',
      }),
    });
    const createdComplaint = submitRes.data.complaint;
    const step3Ok =
      submitRes.status === 201 &&
      submitRes.data.success &&
      createdComplaint?._id &&
      createdComplaint?.ticketNumber?.startsWith('CC-') &&
      createdComplaint?.status === 'SUBMITTED';
    assertTest('Step 3: Complaint created with valid ticket number & status SUBMITTED', step3Ok);
    if (createdComplaint?._id) {
      createdComplaintIds.push(createdComplaint._id);
    }
    const complaintId = createdComplaint?._id;
    const ticketNumber = createdComplaint?.ticketNumber;

    // STEP 4: Verify complaint appears in My Complaints
    console.log('\nStep 4: Verify complaint appears in My Complaints listing...');
    const myComplaintsRes = await apiCall('/complaints/mine', {
      headers: { Authorization: `Bearer ${studentToken}` },
    });
    const step4Ok =
      myComplaintsRes.status === 200 &&
      myComplaintsRes.data.success &&
      myComplaintsRes.data.complaints.some((c) => c.ticketNumber === ticketNumber);
    assertTest('Step 4: Complaint found in student My Complaints list', step4Ok);

    // STEP 5: Open the complaint details page
    console.log('\nStep 5: Student opens complaint details page...');
    const studentDetailsRes = await apiCall(`/complaints/${complaintId}`, {
      headers: { Authorization: `Bearer ${studentToken}` },
    });
    const step5Ok =
      studentDetailsRes.status === 200 &&
      studentDetailsRes.data.success &&
      studentDetailsRes.data.complaint?.ticketNumber === ticketNumber &&
      studentDetailsRes.data.complaint?.status === 'SUBMITTED';
    assertTest('Step 5: Student views full complaint details', step5Ok);

    // STEP 6: Log in as ADMIN
    console.log('\nStep 6: Log in as ADMIN...');
    const adminLoginRes = await apiCall('/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: adminEmail,
        password: adminPassword,
      }),
    });
    const step6Ok =
      adminLoginRes.status === 200 &&
      adminLoginRes.data.success &&
      adminLoginRes.data.user?.role === 'ADMIN' &&
      adminLoginRes.data.token;
    assertTest('Step 6: Admin logged in with role ADMIN', step6Ok);
    const adminToken = adminLoginRes.data.token;

    // STEP 7: Find the complaint in the admin dashboard / listing
    console.log('\nStep 7: Admin finds complaint in all-complaints listing...');
    const adminListRes = await apiCall(`/complaints?search=${ticketNumber}`, {
      headers: { Authorization: `Bearer ${adminToken}` },
    });
    const step7Ok =
      adminListRes.status === 200 &&
      adminListRes.data.success &&
      adminListRes.data.complaints.some((c) => c.ticketNumber === ticketNumber);
    assertTest('Step 7: Admin located ticket in all-complaints list by search', step7Ok);

    // STEP 8: Change complaint status to IN_PROGRESS
    console.log('\nStep 8: Admin changes status to IN_PROGRESS...');
    const inProgressRes = await apiCall(`/complaints/${complaintId}/status`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${adminToken}`,
      },
      body: JSON.stringify({
        status: 'IN_PROGRESS',
        remarks: 'Maintenance team notified and assigned to inspect plumbing valves.',
      }),
    });
    const step8Ok =
      inProgressRes.status === 200 &&
      inProgressRes.data.success &&
      inProgressRes.data.complaint?.status === 'IN_PROGRESS';
    assertTest('Step 8: Admin transitioned status to IN_PROGRESS with history', step8Ok);

    // STEP 9: Resolve it with a resolution remark
    console.log('\nStep 9: Admin resolves complaint with resolution remark...');
    const resolutionRemarkText =
      'Plumbing seal and pipe joints replaced; floor cleaned and dried. Leak fixed completely.';
    const resolveRes = await apiCall(`/complaints/${complaintId}/status`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${adminToken}`,
      },
      body: JSON.stringify({
        status: 'RESOLVED',
        remarks: resolutionRemarkText,
      }),
    });
    const step9Ok =
      resolveRes.status === 200 &&
      resolveRes.data.success &&
      resolveRes.data.complaint?.status === 'RESOLVED' &&
      resolveRes.data.complaint?.resolutionRemarks === resolutionRemarkText &&
      Boolean(resolveRes.data.complaint?.resolvedAt);
    assertTest('Step 9: Complaint resolved with resolutionRemarks and resolvedAt', step9Ok);

    // STEP 10: Log in again as student and verify the updated status
    console.log('\nStep 10: Student logs in again and verifies updated RESOLVED status...');
    const studentReLoginRes = await apiCall('/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: studentEmail,
        password: studentPassword,
      }),
    });
    const freshStudentToken = studentReLoginRes.data.token;
    const verifiedDetailsRes = await apiCall(`/complaints/${complaintId}`, {
      headers: { Authorization: `Bearer ${freshStudentToken}` },
    });
    const verifiedComplaint = verifiedDetailsRes.data.complaint;
    const step10Ok =
      verifiedDetailsRes.status === 200 &&
      verifiedComplaint?.status === 'RESOLVED' &&
      verifiedComplaint?.resolutionRemarks === resolutionRemarkText &&
      Boolean(verifiedComplaint?.resolvedAt) &&
      verifiedComplaint?.statusHistory?.length >= 3;
    assertTest('Step 10: Student verifies RESOLVED status, remarks, timestamp & timeline', step10Ok);

    console.log('\n---------------------------------------------------------------');
    console.log('SECTION 2: SECURITY & ROBUSTNESS TESTING');
    console.log('---------------------------------------------------------------\n');

    // 2.1 Unauthenticated users cannot access protected APIs
    console.log('Security 2.1: Protected endpoints reject unauthenticated requests...');
    const unauthChecks = await Promise.all([
      apiCall('/auth/me'),
      apiCall('/complaints', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '{}' }),
      apiCall('/complaints/mine'),
      apiCall(`/complaints/${complaintId}`),
      apiCall('/complaints'),
      apiCall('/complaints/admin/stats'),
      apiCall(`/complaints/${complaintId}/status`, { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: '{}' }),
    ]);
    const allUnauth401 = unauthChecks.every((r) => r.status === 401);
    assertTest('2.1 All 7 protected endpoints return HTTP 401 when token is missing', allUnauth401);

    // 2.2 Public registration cannot create an ADMIN account
    console.log('\nSecurity 2.2: Public registration privilege escalation attempt...');
    const exploitRegRes = await apiCall('/auth/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: 'Hacker User',
        email: `hacker_${timestamp}@college.edu`,
        password: 'Password123!',
        role: 'ADMIN', // Privilege escalation attempt
      }),
    });
    const exploitUser = exploitRegRes.data.user;
    if (exploitUser?.id) createdUserIds.push(exploitUser.id);
    const regEscalationBlocked =
      exploitRegRes.status === 201 &&
      exploitUser?.role === 'STUDENT'; // Forced to STUDENT
    assertTest('2.2 Public registration forces role to STUDENT even if ADMIN requested', regEscalationBlocked);

    // 2.3 Students cannot access admin APIs
    console.log('\nSecurity 2.3: Students cannot access admin-only endpoints (403 Forbidden)...');
    const studentAdminChecks = await Promise.all([
      apiCall('/complaints', { headers: { Authorization: `Bearer ${studentToken}` } }),
      apiCall('/complaints/admin/stats', { headers: { Authorization: `Bearer ${studentToken}` } }),
      apiCall('/complaints/admin/recent', { headers: { Authorization: `Bearer ${studentToken}` } }),
      apiCall(`/complaints/${complaintId}/status`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${studentToken}` },
        body: JSON.stringify({ status: 'RESOLVED', remarks: 'Student hacking status' }),
      }),
    ]);
    const allStudentBlocked403 = studentAdminChecks.every((r) => r.status === 403);
    assertTest('2.3 All admin endpoints return HTTP 403 Forbidden for STUDENT tokens', allStudentBlocked403);

    // 2.4 Students cannot view another student's complaint
    console.log('\nSecurity 2.4: Cross-student complaint privacy isolation...');
    // Create Student B
    const studentBEmail = `student_b_${timestamp}@college.edu`;
    const studentBRes = await apiCall('/auth/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: 'Student B',
        email: studentBEmail,
        password: studentPassword,
      }),
    });
    const studentBToken = studentBRes.data.token;
    if (studentBRes.data.user?.id) createdUserIds.push(studentBRes.data.user.id);

    // Student B tries to access Student A's complaint
    const leakAttemptRes = await apiCall(`/complaints/${complaintId}`, {
      headers: { Authorization: `Bearer ${studentBToken}` },
    });
    const privacyPreserved =
      leakAttemptRes.status === 404 &&
      !leakAttemptRes.data.complaint;
    assertTest("2.4 Student B receives 404 when querying Student A's complaint ID", privacyPreserved);

    // 2.5 Admin status updates are validated by backend
    console.log('\nSecurity 2.5: Backend validation on admin status updates...');
    // 2.5.1 Invalid status
    const badStatusRes = await apiCall(`/complaints/${complaintId}/status`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${adminToken}` },
      body: JSON.stringify({ status: 'INVALID_STATUS_FOO' }),
    });
    // 2.5.2 Modification on already resolved complaint
    const reResolveAttempt = await apiCall(`/complaints/${complaintId}/status`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${adminToken}` },
      body: JSON.stringify({ status: 'SUBMITTED', remarks: 'Reopening without workflow' }),
    });
    const statusValidationOk =
      badStatusRes.status === 400 &&
      reResolveAttempt.status === 400;
    assertTest('2.5 Backend rejects invalid statuses & modifications to resolved complaints', statusValidationOk);

    // 2.6 Password hashes and secrets never appear in API responses
    console.log('\nSecurity 2.6: Absence of password hashes and secrets in responses...');
    const responsesToCheck = [
      registerRes.data,
      loginRes.data,
      submitRes.data,
      studentDetailsRes.data,
      adminListRes.data,
      resolveRes.data,
    ];
    let secretLeaked = false;
    for (const obj of responsesToCheck) {
      const serialized = JSON.stringify(obj);
      if (
        serialized.includes('passwordHash') ||
        serialized.includes('$2a$') ||
        serialized.includes('$2b$') ||
        serialized.includes(process.env.JWT_SECRET)
      ) {
        secretLeaked = true;
        break;
      }
    }
    assertTest('2.6 No password hashes or secrets leak into any API response', !secretLeaked);

    // 2.7 MongoDB queries and filters validation (ReDoS and cast errors)
    console.log('\nSecurity 2.7: MongoDB query sanitization and ReDoS safety...');
    // 2.7.1 Special regex characters in search
    const redosTestRes = await apiCall('/complaints/mine?search=.*+?^${}()|[]\\', {
      headers: { Authorization: `Bearer ${studentToken}` },
    });
    // 2.7.2 Invalid ObjectId format handling
    const invalidIdRes = await apiCall('/complaints/not-a-valid-mongodb-id', {
      headers: { Authorization: `Bearer ${studentToken}` },
    });
    const querySafetyOk =
      redosTestRes.status === 200 &&
      (invalidIdRes.status === 400 || invalidIdRes.status === 404);
    assertTest('2.7 Regex search sanitized safely & invalid ObjectIDs handled without crashing', querySafetyOk);

    console.log('\n===============================================================');
    console.log(`PART 4 TEST SUMMARY: ${testsPassed} / ${totalTests} TESTS PASSED`);
    console.log('===============================================================\n');

    if (testsPassed !== totalTests) {
      process.exitCode = 1;
    }
  } catch (error) {
    console.error('Unexpected error in Part 4 test suite:', error);
    process.exitCode = 1;
  } finally {
    console.log('Cleaning up temporary Part 4 test fixtures...');
    if (createdComplaintIds.length > 0) {
      await Complaint.deleteMany({ _id: { $in: createdComplaintIds } });
    }
    if (createdUserIds.length > 0) {
      await User.deleteMany({ _id: { $in: createdUserIds } });
    }
    await mongoose.disconnect();
    server.close();
    console.log('Database cleaned and connections closed.\n');
  }
};

runPart4Tests();

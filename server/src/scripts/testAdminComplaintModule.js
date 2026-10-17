/**
 * testAdminComplaintModule.js
 * Comprehensive automated verification script for Part 3 Admin Complaint Management.
 * Covers all 12 verification test requirements.
 */

require('dotenv').config({ path: require('path').resolve(__dirname, '../../.env') });
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const http = require('http');

const app = require('../app');
const User = require('../models/User');
const Complaint = require('../models/Complaint');

const runTests = async () => {
  console.log('🚀 Starting Part 3 Admin Complaint Module Verification Suite...\n');

  if (!process.env.MONGODB_URI) {
    console.error('❌ MONGODB_URI not set');
    process.exit(1);
  }

  await mongoose.connect(process.env.MONGODB_URI);
  console.log('Connected to MongoDB.\n');

  const server = http.createServer(app);
  await new Promise((resolve) => server.listen(0, resolve));
  const port = server.address().port;
  const baseUrl = `http://127.0.0.1:${port}/api`;

  let student1, student2, adminUser;
  let student1Token, student2Token, adminToken;
  const createdComplaintIds = [];
  const createdUserIds = [];

  try {
    const timestamp = Date.now();
    const pwHash = await bcrypt.hash('TestPassword123', 10);

    // 1. Create Student 1
    student1 = await User.create({
      name: 'Alice Student',
      email: `alice_${timestamp}@college.edu`,
      passwordHash: pwHash,
      role: 'STUDENT',
    });
    createdUserIds.push(student1._id);
    student1Token = jwt.sign(
      { id: student1._id, role: student1.role },
      process.env.JWT_SECRET,
      { expiresIn: '1h' }
    );

    // 2. Create Student 2
    student2 = await User.create({
      name: 'Bob Student',
      email: `bob_${timestamp}@college.edu`,
      passwordHash: pwHash,
      role: 'STUDENT',
    });
    createdUserIds.push(student2._id);
    student2Token = jwt.sign(
      { id: student2._id, role: student2.role },
      process.env.JWT_SECRET,
      { expiresIn: '1h' }
    );

    // 3. Create Admin
    adminUser = await User.create({
      name: 'Carol Admin',
      email: `admin_${timestamp}@college.edu`,
      passwordHash: pwHash,
      role: 'ADMIN',
    });
    createdUserIds.push(adminUser._id);
    adminToken = jwt.sign(
      { id: adminUser._id, role: adminUser.role },
      process.env.JWT_SECRET,
      { expiresIn: '1h' }
    );

    console.log('✅ Test fixtures initialized.\n');

    let passedCount = 0;
    const totalTests = 12;

    const apiCall = async (endpoint, options = {}) => {
      const res = await fetch(`${baseUrl}${endpoint}`, options);
      const json = await res.json().catch(() => ({}));
      return { status: res.status, data: json };
    };

    // -------------------------------------------------------------------------
    // TEST 1: Student creates complaint & existing creation workflow works
    // -------------------------------------------------------------------------
    console.log('Running Test 1: Student creates complaints (Part 2 functionality intact)...');
    const c1Res = await apiCall('/complaints', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${student1Token}`,
      },
      body: JSON.stringify({
        title: 'Projector broken in Lecture Hall 1',
        category: 'Classroom',
        description: 'The overhead HDMI projector flashes red and shuts off after 5 minutes.',
        priority: 'HIGH',
        location: 'LH-101',
      }),
    });

    const c2Res = await apiCall('/complaints', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${student2Token}`,
      },
      body: JSON.stringify({
        title: 'Wi-Fi connection drops in Library',
        category: 'Internet / Wi-Fi',
        description: 'Frequent disconnections on the 2nd floor library study desk area.',
        priority: 'MEDIUM',
        location: 'Central Library 2F',
      }),
    });

    if (
      c1Res.status === 201 &&
      c1Res.data.success &&
      c1Res.data.complaint?._id &&
      c2Res.status === 201 &&
      c2Res.data.success &&
      c2Res.data.complaint?._id
    ) {
      createdComplaintIds.push(c1Res.data.complaint._id);
      createdComplaintIds.push(c2Res.data.complaint._id);
      console.log('  PASS: Both students successfully created complaints.');
      passedCount++;
    } else {
      console.error('  FAIL: Complaint creation failed:', c1Res.data, c2Res.data);
    }

    const complaint1Id = c1Res.data.complaint?._id;
    const complaint2Id = c2Res.data.complaint?._id;

    // -------------------------------------------------------------------------
    // TEST 2: Admin can list all complaints with pagination
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 2: Admin can list all complaints via GET /api/complaints...');
    const listRes = await apiCall('/complaints?page=1&limit=10', {
      headers: { Authorization: `Bearer ${adminToken}` },
    });

    if (
      listRes.status === 200 &&
      listRes.data.success &&
      Array.isArray(listRes.data.complaints) &&
      listRes.data.complaints.length >= 2 &&
      listRes.data.pagination?.total >= 2
    ) {
      console.log(`  PASS: Admin retrieved ${listRes.data.complaints.length} complaints, total: ${listRes.data.pagination.total}.`);
      passedCount++;
    } else {
      console.error('  FAIL: Admin list complaints failed:', listRes.status, listRes.data);
    }

    // -------------------------------------------------------------------------
    // TEST 3: Admin dashboard statistics match real database counts
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 3: Admin dashboard stats GET /api/complaints/admin/stats...');
    const statsRes = await apiCall('/complaints/admin/stats', {
      headers: { Authorization: `Bearer ${adminToken}` },
    });

    const expectedTotal = await Complaint.countDocuments();
    const expectedSubmitted = await Complaint.countDocuments({ status: 'SUBMITTED' });
    const expectedInProgress = await Complaint.countDocuments({ status: 'IN_PROGRESS' });
    const expectedResolved = await Complaint.countDocuments({ status: 'RESOLVED' });

    if (
      statsRes.status === 200 &&
      statsRes.data.success &&
      statsRes.data.stats.total === expectedTotal &&
      statsRes.data.stats.submitted === expectedSubmitted &&
      statsRes.data.stats.inProgress === expectedInProgress &&
      statsRes.data.stats.resolved === expectedResolved
    ) {
      console.log(`  PASS: Live stats matched DB (Total: ${expectedTotal}, Submitted: ${expectedSubmitted}, InProgress: ${expectedInProgress}, Resolved: ${expectedResolved}).`);
      passedCount++;
    } else {
      console.error('  FAIL: Stats mismatch:', statsRes.data, { expectedTotal, expectedSubmitted, expectedInProgress, expectedResolved });
    }

    // -------------------------------------------------------------------------
    // TEST 4: Admin can update status to IN_PROGRESS
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 4: Admin updates complaint status to IN_PROGRESS...');
    const updateProgressRes = await apiCall(`/complaints/${complaint1Id}/status`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${adminToken}`,
      },
      body: JSON.stringify({
        status: 'IN_PROGRESS',
        remarks: 'Technician dispatched to inspect the projector bulb and wiring.',
      }),
    });

    if (
      updateProgressRes.status === 200 &&
      updateProgressRes.data.success &&
      updateProgressRes.data.complaint.status === 'IN_PROGRESS' &&
      updateProgressRes.data.complaint.statusHistory?.length >= 2
    ) {
      console.log('  PASS: Complaint status updated to IN_PROGRESS with history appended.');
      passedCount++;
    } else {
      console.error('  FAIL: Update to IN_PROGRESS failed:', updateProgressRes.status, updateProgressRes.data);
    }

    // -------------------------------------------------------------------------
    // TEST 5: Resolving complaint requires resolution remarks (>=5 chars)
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 5: Rejection when resolving without valid remarks (<5 chars or missing)...');
    const missingRemarksRes = await apiCall(`/complaints/${complaint1Id}/status`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${adminToken}`,
      },
      body: JSON.stringify({
        status: 'RESOLVED',
        remarks: 'done', // Less than 5 characters
      }),
    });

    if (missingRemarksRes.status === 400 && !missingRemarksRes.data.success) {
      console.log(`  PASS: Rejected with 400 when remarks < 5 chars: "${missingRemarksRes.data.message}".`);
      passedCount++;
    } else {
      console.error('  FAIL: Expected 400 for short remarks, got:', missingRemarksRes.status, missingRemarksRes.data);
    }

    // -------------------------------------------------------------------------
    // TEST 6: Resolving complaint succeeds with valid remarks and records history
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 6: Admin resolves complaint with valid remarks and records admin ID & timestamps...');
    const resolveRes = await apiCall(`/complaints/${complaint1Id}/status`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${adminToken}`,
      },
      body: JSON.stringify({
        status: 'RESOLVED',
        remarks: 'Replaced damaged HDMI interface cable and projector lamp. Fully tested.',
      }),
    });

    const latestHistory = resolveRes.data.complaint?.statusHistory?.slice(-1)[0];
    if (
      resolveRes.status === 200 &&
      resolveRes.data.success &&
      resolveRes.data.complaint.status === 'RESOLVED' &&
      resolveRes.data.complaint.resolutionRemarks?.includes('Replaced damaged') &&
      resolveRes.data.complaint.resolvedAt &&
      latestHistory?.newStatus === 'RESOLVED' &&
      latestHistory?.previousStatus === 'IN_PROGRESS' &&
      (latestHistory?.changedBy?._id || latestHistory?.changedBy)?.toString() === adminUser._id.toString()
    ) {
      console.log('  PASS: Complaint resolved with resolutionRemarks, resolvedAt, and statusHistory with admin ID.');
      passedCount++;
    } else {
      console.error('  FAIL: Resolve failed or missing fields:', resolveRes.status, resolveRes.data);
    }

    // -------------------------------------------------------------------------
    // TEST 7: Re-modifying or re-resolving an already resolved complaint is rejected
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 7: Prevent modifying or re-resolving an already RESOLVED complaint...');
    const reResolveRes = await apiCall(`/complaints/${complaint1Id}/status`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${adminToken}`,
      },
      body: JSON.stringify({
        status: 'RESOLVED',
        remarks: 'Trying to resolve again.',
      }),
    });

    if (reResolveRes.status === 400 && !reResolveRes.data.success) {
      console.log(`  PASS: Rejected modification on resolved complaint: "${reResolveRes.data.message}".`);
      passedCount++;
    } else {
      console.error('  FAIL: Re-resolving was not blocked:', reResolveRes.status, reResolveRes.data);
    }

    // -------------------------------------------------------------------------
    // TEST 8: Students cannot access admin endpoints (403 Forbidden)
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 8: Student token rejected on admin endpoints (403 Forbidden)...');
    const sListRes = await apiCall('/complaints', {
      headers: { Authorization: `Bearer ${student1Token}` },
    });
    const sStatsRes = await apiCall('/complaints/admin/stats', {
      headers: { Authorization: `Bearer ${student1Token}` },
    });
    const sPatchRes = await apiCall(`/complaints/${complaint2Id}/status`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${student1Token}`,
      },
      body: JSON.stringify({ status: 'RESOLVED', remarks: 'Student attempting status change' }),
    });

    if (sListRes.status === 403 && sStatsRes.status === 403 && sPatchRes.status === 403) {
      console.log('  PASS: All 3 admin endpoints returned 403 Forbidden for student token.');
      passedCount++;
    } else {
      console.error('  FAIL: Student not blocked with 403:', {
        list: sListRes.status,
        stats: sStatsRes.status,
        patch: sPatchRes.status,
      });
    }

    // -------------------------------------------------------------------------
    // TEST 9: Unauthenticated requests are rejected (401 Unauthorized)
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 9: Unauthenticated requests rejected (401 Unauthorized)...');
    const noAuthListRes = await apiCall('/complaints');
    const noAuthStatsRes = await apiCall('/complaints/admin/stats');
    const noAuthPatchRes = await apiCall(`/complaints/${complaint2Id}/status`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: 'IN_PROGRESS' }),
    });

    if (noAuthListRes.status === 401 && noAuthStatsRes.status === 401 && noAuthPatchRes.status === 401) {
      console.log('  PASS: All 3 admin endpoints returned 401 Unauthorized when missing token.');
      passedCount++;
    } else {
      console.error('  FAIL: Unauthenticated access not rejected with 401:', {
        list: noAuthListRes.status,
        stats: noAuthStatsRes.status,
        patch: noAuthPatchRes.status,
      });
    }

    // -------------------------------------------------------------------------
    // TEST 10: Invalid status and invalid ID handling (400/404)
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 10: Invalid status and nonexistent ID handling...');
    const invalidStatusRes = await apiCall(`/complaints/${complaint2Id}/status`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${adminToken}`,
      },
      body: JSON.stringify({ status: 'INVALID_STATUS_FOO' }),
    });

    const fakeId = new mongoose.Types.ObjectId().toString();
    const notFoundRes = await apiCall(`/complaints/${fakeId}/status`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${adminToken}`,
      },
      body: JSON.stringify({ status: 'IN_PROGRESS' }),
    });

    if (invalidStatusRes.status === 400 && notFoundRes.status === 404) {
      console.log('  PASS: Invalid status rejected with 400, nonexistent ID rejected with 404.');
      passedCount++;
    } else {
      console.error('  FAIL: Status/ID validation failed:', {
        invalidStatus: invalidStatusRes.status,
        notFound: notFoundRes.status,
      });
    }

    // -------------------------------------------------------------------------
    // TEST 11: Search, status/category/priority filtering, and pagination
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 11: Multi-parameter search and filters for admin listing...');
    // Search by student name
    const searchStudentRes = await apiCall(`/complaints?search=Alice`, {
      headers: { Authorization: `Bearer ${adminToken}` },
    });
    // Filter by status
    const filterStatusRes = await apiCall(`/complaints?status=RESOLVED`, {
      headers: { Authorization: `Bearer ${adminToken}` },
    });
    // Filter by category
    const filterCatRes = await apiCall(`/complaints?category=Classroom`, {
      headers: { Authorization: `Bearer ${adminToken}` },
    });
    // Filter by priority
    const filterPriRes = await apiCall(`/complaints?priority=HIGH`, {
      headers: { Authorization: `Bearer ${adminToken}` },
    });

    const aliceMatched = searchStudentRes.data.complaints?.some(
      (c) => c.createdBy?.name === 'Alice Student'
    );
    const resolvedMatched = filterStatusRes.data.complaints?.every(
      (c) => c.status === 'RESOLVED'
    );
    const catMatched = filterCatRes.data.complaints?.every(
      (c) => c.category === 'Classroom'
    );
    const priMatched = filterPriRes.data.complaints?.every(
      (c) => c.priority === 'HIGH'
    );

    if (
      searchStudentRes.status === 200 &&
      aliceMatched &&
      filterStatusRes.status === 200 &&
      resolvedMatched &&
      filterCatRes.status === 200 &&
      catMatched &&
      filterPriRes.status === 200 &&
      priMatched
    ) {
      console.log('  PASS: Search by student name and filters for status, category, and priority all work properly.');
      passedCount++;
    } else {
      console.error('  FAIL: Search/filter validation failed:', {
        aliceMatched,
        resolvedMatched,
        catMatched,
        priMatched,
      });
    }

    // -------------------------------------------------------------------------
    // TEST 12: Student complaint privacy & isolation remain preserved
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 12: Student ownership restrictions remain intact...');
    // Student 1 accesses my complaints
    const myComplaintsRes = await apiCall('/complaints/mine', {
      headers: { Authorization: `Bearer ${student1Token}` },
    });
    // Student 1 tries to access Student 2's complaint
    const forbiddenDetailsRes = await apiCall(`/complaints/${complaint2Id}`, {
      headers: { Authorization: `Bearer ${student1Token}` },
    });

    const onlyStudent1Complaints = myComplaintsRes.data.complaints?.every(
      (c) => c.createdBy === student1._id.toString() || c.createdBy?._id === student1._id.toString()
    );

    if (
      myComplaintsRes.status === 200 &&
      onlyStudent1Complaints &&
      forbiddenDetailsRes.status === 404
    ) {
      console.log('  PASS: Student ownership isolation intact (other student complaint returns 404).');
      passedCount++;
    } else {
      console.error('  FAIL: Student ownership violation:', {
        myStatus: myComplaintsRes.status,
        onlyStudent1Complaints,
        forbiddenStatus: forbiddenDetailsRes.status,
      });
    }

    // -------------------------------------------------------------------------
    // Summary
    // -------------------------------------------------------------------------
    console.log(`\n======================================================`);
    console.log(`TEST RESULTS: ${passedCount} / ${totalTests} PASSED`);
    console.log(`======================================================\n`);

    if (passedCount !== totalTests) {
      process.exitCode = 1;
    }
  } catch (err) {
    console.error('Unexpected error during test suite:', err);
    process.exitCode = 1;
  } finally {
    console.log('Cleaning up test artifacts...');
    if (createdComplaintIds.length > 0) {
      await Complaint.deleteMany({ _id: { $in: createdComplaintIds } });
    }
    if (createdUserIds.length > 0) {
      await User.deleteMany({ _id: { $in: createdUserIds } });
    }
    await mongoose.disconnect();
    server.close();
    console.log('Cleanup finished and database connection closed.\n');
  }
};

runTests();

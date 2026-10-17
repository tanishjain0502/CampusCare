/**
 * testComplaintModule.js
 * Comprehensive automated verification script for Part 2 Student Complaint Module.
 * Covers all 12 required test cases specified in the requirements.
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
  console.log('🚀 Starting Part 2 Verification Test Suite...\n');

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

  let studentA, studentB, adminUser;
  let tokenA, tokenB, adminToken;
  const createdComplaintIds = [];
  const createdUserIds = [];

  try {
    const timestamp = Date.now();
    const pwHash = await bcrypt.hash('TestPassword123', 10);

    // 1. Create Test Student A
    studentA = await User.create({
      name: 'Student A',
      email: `student_a_${timestamp}@college.edu`,
      passwordHash: pwHash,
      role: 'STUDENT',
    });
    createdUserIds.push(studentA._id);
    tokenA = jwt.sign({ id: studentA._id, role: studentA.role }, process.env.JWT_SECRET, { expiresIn: '1h' });

    // 2. Create Test Student B
    studentB = await User.create({
      name: 'Student B',
      email: `student_b_${timestamp}@college.edu`,
      passwordHash: pwHash,
      role: 'STUDENT',
    });
    createdUserIds.push(studentB._id);
    tokenB = jwt.sign({ id: studentB._id, role: studentB.role }, process.env.JWT_SECRET, { expiresIn: '1h' });

    // 3. Create Test Admin
    adminUser = await User.create({
      name: 'Admin Tester',
      email: `admin_${timestamp}@college.edu`,
      passwordHash: pwHash,
      role: 'ADMIN',
    });
    createdUserIds.push(adminUser._id);
    adminToken = jwt.sign({ id: adminUser._id, role: adminUser.role }, process.env.JWT_SECRET, { expiresIn: '1h' });

    console.log('✅ Test fixtures initialized.\n');

    let passedCount = 0;
    const totalTests = 12;

    // Helper fetch wrapper
    const apiCall = async (endpoint, options = {}) => {
      const res = await fetch(`${baseUrl}${endpoint}`, options);
      const json = await res.json().catch(() => ({}));
      return { status: res.status, data: json };
    };

    // -------------------------------------------------------------------------
    // TEST 1: Authenticated student can create a valid complaint
    // -------------------------------------------------------------------------
    console.log('Running Test 1: Authenticated student creates a valid complaint...');
    const t1Res = await apiCall('/complaints', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${tokenA}`,
      },
      body: JSON.stringify({
        title: 'Air conditioning not cooling in Lab 3',
        category: 'Laboratory',
        description: 'The AC unit in Lab 3 has been blowing warm air since yesterday morning.',
        priority: 'MEDIUM',
        location: 'Engineering Building Lab 301',
      }),
    });

    if (
      t1Res.status === 201 &&
      t1Res.data.success &&
      t1Res.data.complaint?.ticketNumber &&
      t1Res.data.complaint.status === 'SUBMITTED'
    ) {
      console.log('✅ Test 1 PASSED: Complaint created with Ticket #:', t1Res.data.complaint.ticketNumber);
      createdComplaintIds.push(t1Res.data.complaint._id);
      passedCount++;
    } else {
      console.error('❌ Test 1 FAILED:', t1Res);
    }

    // -------------------------------------------------------------------------
    // TEST 2: Invalid titles and descriptions are rejected
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 2: Invalid titles and descriptions are rejected...');
    // Short title (< 5)
    const t2a = await apiCall('/complaints', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${tokenA}` },
      body: JSON.stringify({
        title: 'AC',
        category: 'Classroom',
        description: 'Valid description that has more than twenty characters.',
      }),
    });
    // Short description (< 20)
    const t2b = await apiCall('/complaints', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${tokenA}` },
      body: JSON.stringify({
        title: 'Valid Complaint Title',
        category: 'Classroom',
        description: 'Too short',
      }),
    });

    if (t2a.status === 400 && t2b.status === 400) {
      console.log('✅ Test 2 PASSED: Short title and short description properly rejected with HTTP 400.');
      passedCount++;
    } else {
      console.error('❌ Test 2 FAILED:', { t2a, t2b });
    }

    // -------------------------------------------------------------------------
    // TEST 3: Invalid categories and priorities are rejected
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 3: Invalid categories and priorities are rejected...');
    const t3a = await apiCall('/complaints', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${tokenA}` },
      body: JSON.stringify({
        title: 'Valid Complaint Title',
        category: 'NonExistentCategory',
        description: 'Valid description that has more than twenty characters.',
      }),
    });
    const t3b = await apiCall('/complaints', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${tokenA}` },
      body: JSON.stringify({
        title: 'Valid Complaint Title',
        category: 'Classroom',
        description: 'Valid description that has more than twenty characters.',
        priority: 'CRITICAL', // Invalid, allowed: LOW, MEDIUM, HIGH
      }),
    });

    if (t3a.status === 400 && t3b.status === 400) {
      console.log('✅ Test 3 PASSED: Invalid category and priority properly rejected with HTTP 400.');
      passedCount++;
    } else {
      console.error('❌ Test 3 FAILED:', { t3a, t3b });
    }

    // -------------------------------------------------------------------------
    // TEST 4: Requests without valid authentication are rejected
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 4: Requests without valid authentication are rejected...');
    const t4NoToken = await apiCall('/complaints', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: 'Valid Complaint Title',
        category: 'Classroom',
        description: 'Valid description that has more than twenty characters.',
      }),
    });
    const t4BadToken = await apiCall('/complaints', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: 'Bearer bad.token.here' },
      body: JSON.stringify({
        title: 'Valid Complaint Title',
        category: 'Classroom',
        description: 'Valid description that has more than twenty characters.',
      }),
    });

    if (t4NoToken.status === 401 && t4BadToken.status === 401) {
      console.log('✅ Test 4 PASSED: Missing token and invalid token rejected with HTTP 401.');
      passedCount++;
    } else {
      console.error('❌ Test 4 FAILED:', { t4NoToken, t4BadToken });
    }

    // -------------------------------------------------------------------------
    // TEST 5: ADMIN users cannot use student-only complaint creation routes
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 5: ADMIN users cannot use student complaint creation routes...');
    const t5Res = await apiCall('/complaints', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${adminToken}`,
      },
      body: JSON.stringify({
        title: 'Admin Trying To Create Complaint',
        category: 'Classroom',
        description: 'This complaint creation should be blocked for admin role.',
      }),
    });

    if (t5Res.status === 403) {
      console.log('✅ Test 5 PASSED: Admin blocked with HTTP 403 Forbidden.');
      passedCount++;
    } else {
      console.error('❌ Test 5 FAILED:', t5Res);
    }

    // -------------------------------------------------------------------------
    // TEST 6: Students can retrieve only their own complaints
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 6: Students can retrieve only their own complaints...');
    // Create a complaint for Student B
    const t6CompB = await apiCall('/complaints', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${tokenB}` },
      body: JSON.stringify({
        title: 'Broken chair in Library study hall',
        category: 'Library',
        description: 'A study chair in the 2nd floor silent study area has a broken leg.',
      }),
    });
    createdComplaintIds.push(t6CompB.data.complaint._id);

    // Student A requests /complaints/mine
    const t6MineA = await apiCall('/complaints/mine', {
      headers: { Authorization: `Bearer ${tokenA}` },
    });

    const studentAComplaints = t6MineA.data.complaints || [];
    const hasStudentBComplaint = studentAComplaints.some(
      (c) => c._id === t6CompB.data.complaint._id
    );

    if (
      t6MineA.status === 200 &&
      studentAComplaints.length >= 1 &&
      !hasStudentBComplaint
    ) {
      console.log('✅ Test 6 PASSED: Student A sees only their complaints; Student B complaint is isolated.');
      passedCount++;
    } else {
      console.error('❌ Test 6 FAILED:', { length: studentAComplaints.length, hasStudentBComplaint });
    }

    // -------------------------------------------------------------------------
    // TEST 7: One student cannot retrieve another student's complaint by changing ID
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 7: Student A cannot retrieve Student B complaint by ID...');
    const t7Res = await apiCall(`/complaints/${t6CompB.data.complaint._id}`, {
      headers: { Authorization: `Bearer ${tokenA}` },
    });

    if (t7Res.status === 404 && !t7Res.data.complaint) {
      console.log('✅ Test 7 PASSED: ID lookup for another student returns consistent 404 Not Found.');
      passedCount++;
    } else {
      console.error('❌ Test 7 FAILED:', t7Res);
    }

    // -------------------------------------------------------------------------
    // TEST 8: Students cannot set status to RESOLVED during submission
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 8: Students cannot force status to RESOLVED during submission...');
    const t8Res = await apiCall('/complaints', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${tokenA}` },
      body: JSON.stringify({
        title: 'Projector display flickers in Seminar Hall',
        category: 'Classroom',
        description: 'The projector keeps turning off during classes in the seminar hall.',
        status: 'RESOLVED', // Malicious attempt to self-resolve
      }),
    });
    createdComplaintIds.push(t8Res.data.complaint._id);

    if (t8Res.status === 201 && t8Res.data.complaint.status === 'SUBMITTED') {
      console.log('✅ Test 8 PASSED: Client-supplied status was ignored; status set strictly to SUBMITTED.');
      passedCount++;
    } else {
      console.error('❌ Test 8 FAILED:', t8Res);
    }

    // -------------------------------------------------------------------------
    // TEST 9: Student dashboard statistics match database records
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 9: Student dashboard statistics match database records...');
    const t9Stats = await apiCall('/complaints/mine/stats', {
      headers: { Authorization: `Bearer ${tokenA}` },
    });

    const expectedTotal = await Complaint.countDocuments({ createdBy: studentA._id });
    const expectedSubmitted = await Complaint.countDocuments({ createdBy: studentA._id, status: 'SUBMITTED' });

    if (
      t9Stats.status === 200 &&
      t9Stats.data.stats.total === expectedTotal &&
      t9Stats.data.stats.submitted === expectedSubmitted
    ) {
      console.log(`✅ Test 9 PASSED: Stats match DB: Total=${t9Stats.data.stats.total}, Submitted=${t9Stats.data.stats.submitted}`);
      passedCount++;
    } else {
      console.error('❌ Test 9 FAILED:', { t9Stats, expectedTotal, expectedSubmitted });
    }

    // -------------------------------------------------------------------------
    // TEST 10: Search, filtering, sorting and pagination work correctly
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 10: Search, filtering, sorting, and pagination...');
    // Create an electrical complaint for Student A
    const t10Elec = await apiCall('/complaints', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${tokenA}` },
      body: JSON.stringify({
        title: 'Flickering tube lights in corridor',
        category: 'Electrical / Maintenance',
        description: 'The corridor lights outside room 201 are constantly flickering.',
      }),
    });
    createdComplaintIds.push(t10Elec.data.complaint._id);

    // Filter by category
    const catSearch = await apiCall('/complaints/mine?category=Electrical%20%2F%20Maintenance', {
      headers: { Authorization: `Bearer ${tokenA}` },
    });
    const catMatch = catSearch.data.complaints.every((c) => c.category === 'Electrical / Maintenance');

    // Search by keyword
    const kwSearch = await apiCall('/complaints/mine?search=flickering', {
      headers: { Authorization: `Bearer ${tokenA}` },
    });
    const kwMatch = kwSearch.data.complaints.some((c) => c.title.toLowerCase().includes('flickering'));

    // Pagination
    const pageCheck = await apiCall('/complaints/mine?page=1&limit=1', {
      headers: { Authorization: `Bearer ${tokenA}` },
    });
    const pageMatch = pageCheck.data.complaints.length === 1 && pageCheck.data.pagination.limit === 1;

    if (catMatch && kwMatch && pageMatch) {
      console.log('✅ Test 10 PASSED: Category filter, search keyword, and pagination all functional.');
      passedCount++;
    } else {
      console.error('❌ Test 10 FAILED:', { catMatch, kwMatch, pageMatch });
    }

    // -------------------------------------------------------------------------
    // TEST 11: Ticket number uniqueness and safe generation
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 11: Ticket number uniqueness and format...');
    const allStudentA = await apiCall('/complaints/mine?limit=50', {
      headers: { Authorization: `Bearer ${tokenA}` },
    });
    const ticketNumbers = allStudentA.data.complaints.map((c) => c.ticketNumber);
    const uniqueTickets = new Set(ticketNumbers);
    const allMatchFormat = ticketNumbers.every((t) => /^CC-\d{8}-[A-F0-9]{6}$/.test(t));

    if (ticketNumbers.length === uniqueTickets.size && allMatchFormat) {
      console.log(`✅ Test 11 PASSED: All ${ticketNumbers.length} ticket numbers unique and match CC-YYYYMMDD-XXXXXX format.`);
      passedCount++;
    } else {
      console.error('❌ Test 11 FAILED:', { ticketNumbers, allMatchFormat });
    }

    // -------------------------------------------------------------------------
    // TEST 12: Existing registration and login functionality still works
    // -------------------------------------------------------------------------
    console.log('\nRunning Test 12: Existing registration and login still works...');
    const testRegEmail = `reg_check_${Date.now()}@college.edu`;
    const regRes = await apiCall('/auth/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: 'Reg Check Student',
        email: testRegEmail,
        password: 'ValidPassword123',
      }),
    });
    if (regRes.data?.user?.id) {
      createdUserIds.push(regRes.data.user.id);
    }

    const loginRes = await apiCall('/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: testRegEmail,
        password: 'ValidPassword123',
      }),
    });

    if (regRes.status === 201 && loginRes.status === 200 && loginRes.data.token) {
      console.log('✅ Test 12 PASSED: Public registration and login intact and fully working.');
      passedCount++;
    } else {
      console.error('❌ Test 12 FAILED:', { regRes, loginRes });
    }

    // -------------------------------------------------------------------------
    // Results Summary
    // -------------------------------------------------------------------------
    console.log('\n=========================================');
    console.log(`TEST RESULTS: ${passedCount} / ${totalTests} TESTS PASSED`);
    console.log('=========================================\n');

  } catch (err) {
    console.error('Unexpected test execution error:', err);
  } finally {
    // Clean up only the specific documents created for this test run
    console.log('Cleaning up test data...');
    if (createdComplaintIds.length > 0) {
      await Complaint.deleteMany({ _id: { $in: createdComplaintIds } });
    }
    if (createdUserIds.length > 0) {
      await User.deleteMany({ _id: { $in: createdUserIds } });
    }
    await mongoose.disconnect();
    server.close();
    console.log('Cleanup complete. Database restored.');
  }
};

runTests().catch(console.error);

const express = require('express');
const {
  createComplaint,
  getMyComplaints,
  getMyComplaintStats,
  getComplaintById,
  getAllComplaints,
  getAdminComplaintStats,
  getAdminRecentComplaints,
  getAdminComplaintById,
  updateComplaintStatus,
} = require('../controllers/complaintController');
const { protect, restrictTo } = require('../middleware/auth');

const router = express.Router();

// All complaint routes require a valid JWT
router.use(protect);

// ===========================================================================
// ADMIN ROUTES (Must be registered before conflicting dynamic /:id route)
// ===========================================================================

// GET /api/complaints/admin/stats — Overall statistics for admin dashboard
router.get('/admin/stats', restrictTo('ADMIN'), getAdminComplaintStats);

// GET /api/complaints/admin/recent — Recent complaints for admin dashboard
router.get('/admin/recent', restrictTo('ADMIN'), getAdminRecentComplaints);

// GET /api/complaints/admin/:id — Full complaint details for admin
router.get('/admin/:id', restrictTo('ADMIN'), getAdminComplaintById);

// GET /api/complaints — Admin-only endpoint to list all complaints
router.get('/', restrictTo('ADMIN'), getAllComplaints);

// PATCH /api/complaints/:id/status — Admin update complaint status and record remarks
router.patch('/:id/status', restrictTo('ADMIN'), updateComplaintStatus);

// ===========================================================================
// STUDENT ROUTES
// ===========================================================================

// POST /api/complaints — Create a complaint (student only)
router.post('/', restrictTo('STUDENT'), createComplaint);

// GET /api/complaints/mine — Get list of current student's complaints (student only)
router.get('/mine', restrictTo('STUDENT'), getMyComplaints);

// GET /api/complaints/mine/stats — Get statistics for current student's complaints (student only)
router.get('/mine/stats', restrictTo('STUDENT'), getMyComplaintStats);

// GET /api/complaints/:id — View single complaint details
// If called by student, strictly enforces createdBy: req.user._id.
// If called by admin, provides full details via getAdminComplaintById.
router.get('/:id', (req, res, next) => {
  if (req.user.role === 'ADMIN') {
    return getAdminComplaintById(req, res, next);
  }
  return getComplaintById(req, res, next);
});

module.exports = router;

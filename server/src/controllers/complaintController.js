const mongoose = require('mongoose');
const Complaint = require('../models/Complaint');
const User = require('../models/User');
const {
  COMPLAINT_CATEGORIES,
  COMPLAINT_PRIORITIES,
  COMPLAINT_STATUSES,
  DEFAULT_PRIORITY,
  DEFAULT_STATUS,
} = require('../constants/complaintConstants');
const { generateTicketNumber } = require('../utils/ticketGenerator');

// ===========================================================================
// STUDENT CONTROLLERS
// ===========================================================================

// ---------------------------------------------------------------------------
// POST /api/complaints
// Authenticated student submits a new complaint
// ---------------------------------------------------------------------------
const createComplaint = async (req, res) => {
  try {
    const { title, category, description, priority, location } = req.body;

    const errors = [];

    // Title validation
    if (!title || typeof title !== 'string') {
      errors.push('Title is required.');
    } else {
      const trimmedTitle = title.trim();
      if (trimmedTitle.length < 5 || trimmedTitle.length > 100) {
        errors.push('Title must be between 5 and 100 characters.');
      }
    }

    // Category validation
    if (!category || !COMPLAINT_CATEGORIES.includes(category)) {
      errors.push(
        `Category is required and must be one of: ${COMPLAINT_CATEGORIES.join(', ')}.`
      );
    }

    // Description validation
    if (!description || typeof description !== 'string') {
      errors.push('Description is required.');
    } else {
      const trimmedDesc = description.trim();
      if (trimmedDesc.length < 20 || trimmedDesc.length > 2000) {
        errors.push('Description must be between 20 and 2000 characters.');
      }
    }

    // Priority validation (optional, defaults to MEDIUM)
    let assignedPriority = DEFAULT_PRIORITY;
    if (priority !== undefined && priority !== null && priority !== '') {
      if (!COMPLAINT_PRIORITIES.includes(priority)) {
        errors.push(
          `Priority must be one of: ${COMPLAINT_PRIORITIES.join(', ')}.`
        );
      } else {
        assignedPriority = priority;
      }
    }

    // Location validation (optional, max 100 characters)
    let trimmedLocation = '';
    if (location && typeof location === 'string') {
      trimmedLocation = location.trim();
      if (trimmedLocation.length > 100) {
        errors.push('Location must not exceed 100 characters.');
      }
    }

    if (errors.length > 0) {
      return res.status(400).json({
        success: false,
        message: errors.join(' '),
      });
    }

    // Student cannot select status, ticket number, or assignees
    let complaint;
    let attempts = 0;
    const maxAttempts = 3;

    while (attempts < maxAttempts) {
      try {
        const ticketNumber = generateTicketNumber();
        complaint = await Complaint.create({
          ticketNumber,
          createdBy: req.user._id,
          title: title.trim(),
          category,
          description: description.trim(),
          priority: assignedPriority,
          status: DEFAULT_STATUS, // Always SUBMITTED
          location: trimmedLocation,
          statusHistory: [
            {
              status: DEFAULT_STATUS,
              previousStatus: 'NONE',
              newStatus: DEFAULT_STATUS,
              changedBy: req.user._id,
              changedAt: new Date(),
              note: 'Complaint submitted by student',
            },
          ],
        });
        break; // Successfully created
      } catch (err) {
        if (err.code === 11000 && err.keyPattern && err.keyPattern.ticketNumber) {
          attempts += 1;
          if (attempts >= maxAttempts) {
            throw new Error('Failed to generate a unique ticket number. Please try again.');
          }
        } else {
          throw err;
        }
      }
    }

    return res.status(201).json({
      success: true,
      message: 'Complaint submitted successfully.',
      complaint,
    });
  } catch (error) {
    console.error('createComplaint error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error while submitting complaint. Please try again.',
    });
  }
};

// ---------------------------------------------------------------------------
// GET /api/complaints/mine
// Returns complaints submitted by the authenticated student with search & filters
// ---------------------------------------------------------------------------
const getMyComplaints = async (req, res) => {
  try {
    const {
      page = 1,
      limit = 10,
      search = '',
      status,
      category,
      sort = 'newest',
    } = req.query;

    const parsedPage = Math.max(1, parseInt(page, 10) || 1);
    const parsedLimit = Math.min(50, Math.max(1, parseInt(limit, 10) || 10));
    const skip = (parsedPage - 1) * parsedLimit;

    // Filter strictly scoped to the authenticated student
    const filter = {
      createdBy: req.user._id,
    };

    if (status) {
      if (!COMPLAINT_STATUSES.includes(status)) {
        return res.status(400).json({
          success: false,
          message: `Invalid status filter. Allowed values: ${COMPLAINT_STATUSES.join(', ')}.`,
        });
      }
      filter.status = status;
    }

    if (category) {
      if (!COMPLAINT_CATEGORIES.includes(category)) {
        return res.status(400).json({
          success: false,
          message: `Invalid category filter. Allowed values: ${COMPLAINT_CATEGORIES.join(', ')}.`,
        });
      }
      filter.category = category;
    }

    if (search && typeof search === 'string' && search.trim()) {
      const sanitizedSearch = search.trim().replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      filter.$or = [
        { ticketNumber: { $regex: sanitizedSearch, $options: 'i' } },
        { title: { $regex: sanitizedSearch, $options: 'i' } },
      ];
    }

    const sortOption = sort === 'oldest' ? { createdAt: 1 } : { createdAt: -1 };

    const [complaints, total] = await Promise.all([
      Complaint.find(filter)
        .sort(sortOption)
        .skip(skip)
        .limit(parsedLimit)
        .lean(),
      Complaint.countDocuments(filter),
    ]);

    const totalPages = Math.ceil(total / parsedLimit) || 1;

    return res.status(200).json({
      success: true,
      complaints,
      pagination: {
        total,
        page: parsedPage,
        limit: parsedLimit,
        totalPages,
      },
    });
  } catch (error) {
    console.error('getMyComplaints error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error while retrieving complaints.',
    });
  }
};

// ---------------------------------------------------------------------------
// GET /api/complaints/mine/stats
// Return real statistics for the authenticated student's complaints
// ---------------------------------------------------------------------------
const getMyComplaintStats = async (req, res) => {
  try {
    const studentId = req.user._id;

    const [total, submitted, inProgress, resolved] = await Promise.all([
      Complaint.countDocuments({ createdBy: studentId }),
      Complaint.countDocuments({ createdBy: studentId, status: 'SUBMITTED' }),
      Complaint.countDocuments({ createdBy: studentId, status: 'IN_PROGRESS' }),
      Complaint.countDocuments({ createdBy: studentId, status: 'RESOLVED' }),
    ]);

    return res.status(200).json({
      success: true,
      stats: {
        total,
        submitted,
        inProgress,
        resolved,
      },
    });
  } catch (error) {
    console.error('getMyComplaintStats error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error while fetching complaint statistics.',
    });
  }
};

// ---------------------------------------------------------------------------
// GET /api/complaints/:id
// Return a specific complaint owned by the authenticated student
// ---------------------------------------------------------------------------
const getComplaintById = async (req, res) => {
  try {
    const { id } = req.params;

    if (!mongoose.Types.ObjectId.isValid(id)) {
      return res.status(404).json({
        success: false,
        message: 'Complaint not found.',
      });
    }

    // For student access: strictly enforce ownership
    const complaint = await Complaint.findOne({
      _id: id,
      createdBy: req.user._id,
    })
      .populate('createdBy', 'name email role')
      .populate('statusHistory.changedBy', 'name email role');

    if (!complaint) {
      return res.status(404).json({
        success: false,
        message: 'Complaint not found.',
      });
    }

    return res.status(200).json({
      success: true,
      complaint,
    });
  } catch (error) {
    console.error('getComplaintById error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error while retrieving complaint.',
    });
  }
};

// ===========================================================================
// ADMIN CONTROLLERS (Part 3)
// ===========================================================================

// ---------------------------------------------------------------------------
// GET /api/complaints
// Admin-only endpoint to list all complaints with search, filters, pagination
// ---------------------------------------------------------------------------
const getAllComplaints = async (req, res) => {
  try {
    const {
      page = 1,
      limit = 10,
      search = '',
      status,
      category,
      priority,
      sort = 'newest',
    } = req.query;

    const parsedPage = Math.max(1, parseInt(page, 10) || 1);
    const parsedLimit = Math.min(50, Math.max(1, parseInt(limit, 10) || 10));
    const skip = (parsedPage - 1) * parsedLimit;

    const filter = {};

    // Status filter
    if (status) {
      if (!COMPLAINT_STATUSES.includes(status)) {
        return res.status(400).json({
          success: false,
          message: `Invalid status filter. Allowed values: ${COMPLAINT_STATUSES.join(', ')}.`,
        });
      }
      filter.status = status;
    }

    // Category filter
    if (category) {
      if (!COMPLAINT_CATEGORIES.includes(category)) {
        return res.status(400).json({
          success: false,
          message: `Invalid category filter. Allowed values: ${COMPLAINT_CATEGORIES.join(', ')}.`,
        });
      }
      filter.category = category;
    }

    // Priority filter
    if (priority) {
      if (!COMPLAINT_PRIORITIES.includes(priority)) {
        return res.status(400).json({
          success: false,
          message: `Invalid priority filter. Allowed values: ${COMPLAINT_PRIORITIES.join(', ')}.`,
        });
      }
      filter.priority = priority;
    }

    // Search filter across ticketNumber, title, or student name/email
    if (search && typeof search === 'string' && search.trim()) {
      const sanitized = search.trim().replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

      // Find matching users by name or email
      const matchingUsers = await User.find({
        $or: [
          { name: { $regex: sanitized, $options: 'i' } },
          { email: { $regex: sanitized, $options: 'i' } },
        ],
      }).select('_id');

      const userIds = matchingUsers.map((u) => u._id);

      filter.$or = [
        { ticketNumber: { $regex: sanitized, $options: 'i' } },
        { title: { $regex: sanitized, $options: 'i' } },
        { createdBy: { $in: userIds } },
      ];
    }

    const sortOption = sort === 'oldest' ? { createdAt: 1 } : { createdAt: -1 };

    const [complaints, total] = await Promise.all([
      Complaint.find(filter)
        .sort(sortOption)
        .skip(skip)
        .limit(parsedLimit)
        .populate('createdBy', 'name email role')
        .lean(),
      Complaint.countDocuments(filter),
    ]);

    const totalPages = Math.ceil(total / parsedLimit) || 1;

    return res.status(200).json({
      success: true,
      complaints,
      pagination: {
        total,
        page: parsedPage,
        limit: parsedLimit,
        totalPages,
      },
    });
  } catch (error) {
    console.error('getAllComplaints error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error while fetching all complaints.',
    });
  }
};

// ---------------------------------------------------------------------------
// GET /api/complaints/admin/stats
// Admin-only endpoint returning real statistics across all complaints
// ---------------------------------------------------------------------------
const getAdminComplaintStats = async (req, res) => {
  try {
    const [total, submitted, inProgress, resolved] = await Promise.all([
      Complaint.countDocuments({}),
      Complaint.countDocuments({ status: 'SUBMITTED' }),
      Complaint.countDocuments({ status: 'IN_PROGRESS' }),
      Complaint.countDocuments({ status: 'RESOLVED' }),
    ]);

    return res.status(200).json({
      success: true,
      stats: {
        total,
        submitted,
        inProgress,
        resolved,
      },
    });
  } catch (error) {
    console.error('getAdminComplaintStats error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error while fetching admin statistics.',
    });
  }
};

// ---------------------------------------------------------------------------
// GET /api/complaints/admin/recent
// Admin-only endpoint returning limited recent complaints
// ---------------------------------------------------------------------------
const getAdminRecentComplaints = async (req, res) => {
  try {
    const limit = Math.min(20, Math.max(1, parseInt(req.query.limit, 10) || 5));

    const complaints = await Complaint.find({})
      .sort({ createdAt: -1 })
      .limit(limit)
      .populate('createdBy', 'name email role')
      .lean();

    return res.status(200).json({
      success: true,
      complaints,
    });
  } catch (error) {
    console.error('getAdminRecentComplaints error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error while fetching recent complaints.',
    });
  }
};

// ---------------------------------------------------------------------------
// GET /api/complaints/admin/:id
// Admin-only endpoint to get single complaint details with full population
// ---------------------------------------------------------------------------
const getAdminComplaintById = async (req, res) => {
  try {
    const { id } = req.params;

    if (!mongoose.Types.ObjectId.isValid(id)) {
      return res.status(404).json({
        success: false,
        message: 'Complaint not found.',
      });
    }

    const complaint = await Complaint.findById(id)
      .populate('createdBy', 'name email role')
      .populate('statusHistory.changedBy', 'name email role');

    if (!complaint) {
      return res.status(404).json({
        success: false,
        message: 'Complaint not found.',
      });
    }

    return res.status(200).json({
      success: true,
      complaint,
    });
  } catch (error) {
    console.error('getAdminComplaintById error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error while retrieving complaint details.',
    });
  }
};

// ---------------------------------------------------------------------------
// PATCH /api/complaints/:id/status
// Admin-only endpoint to update complaint status and record history
// ---------------------------------------------------------------------------
const updateComplaintStatus = async (req, res) => {
  try {
    const { id } = req.params;
    const { status, remarks, note } = req.body;

    // Validate ID format
    if (!mongoose.Types.ObjectId.isValid(id)) {
      return res.status(404).json({
        success: false,
        message: 'Complaint not found.',
      });
    }

    // Validate status value
    if (!status || !COMPLAINT_STATUSES.includes(status)) {
      return res.status(400).json({
        success: false,
        message: `Invalid status. Permitted values: ${COMPLAINT_STATUSES.join(', ')}.`,
      });
    }

    const complaint = await Complaint.findById(id);
    if (!complaint) {
      return res.status(404).json({
        success: false,
        message: 'Complaint not found.',
      });
    }

    // Prevent duplicate resolution or modifying already resolved complaints
    if (complaint.status === 'RESOLVED') {
      return res.status(400).json({
        success: false,
        message: 'Complaint is already resolved. Status cannot be modified.',
      });
    }

    // Require resolution remarks when resolving
    const providedRemarks = (remarks || note || '').trim();
    if (status === 'RESOLVED') {
      if (!providedRemarks || providedRemarks.length < 5) {
        return res.status(400).json({
          success: false,
          message: 'Resolution remarks are required when resolving a complaint (minimum 5 characters).',
        });
      }
      if (providedRemarks.length > 1000) {
        return res.status(400).json({
          success: false,
          message: 'Resolution remarks cannot exceed 1000 characters.',
        });
      }
    }

    const previousStatus = complaint.status;
    complaint.status = status;

    if (status === 'RESOLVED') {
      complaint.resolutionRemarks = providedRemarks;
      complaint.resolvedAt = new Date();
    }

    // Record status history transition with the authenticated admin
    complaint.statusHistory.push({
      status: status,
      previousStatus: previousStatus,
      newStatus: status,
      changedBy: req.user._id,
      changedAt: new Date(),
      note: status === 'RESOLVED'
        ? providedRemarks
        : (providedRemarks || `Status updated from ${previousStatus} to ${status} by admin`),
    });

    await complaint.save();

    const populatedComplaint = await Complaint.findById(id)
      .populate('createdBy', 'name email role')
      .populate('statusHistory.changedBy', 'name email role');

    return res.status(200).json({
      success: true,
      message: `Complaint status updated to ${status}.`,
      complaint: populatedComplaint,
    });
  } catch (error) {
    console.error('updateComplaintStatus error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error while updating complaint status.',
    });
  }
};

module.exports = {
  // Student controllers
  createComplaint,
  getMyComplaints,
  getMyComplaintStats,
  getComplaintById,
  // Admin controllers (Part 3)
  getAllComplaints,
  getAdminComplaintStats,
  getAdminRecentComplaints,
  getAdminComplaintById,
  updateComplaintStatus,
};

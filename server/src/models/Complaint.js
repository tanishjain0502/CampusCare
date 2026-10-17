const mongoose = require('mongoose');
const {
  COMPLAINT_CATEGORIES,
  COMPLAINT_PRIORITIES,
  COMPLAINT_STATUSES,
  DEFAULT_PRIORITY,
  DEFAULT_STATUS,
} = require('../constants/complaintConstants');

const statusHistorySchema = new mongoose.Schema(
  {
    status: {
      type: String,
      enum: COMPLAINT_STATUSES,
      required: true,
    },
    previousStatus: {
      type: String,
      enum: [...COMPLAINT_STATUSES, 'NONE'],
      default: 'NONE',
    },
    newStatus: {
      type: String,
      enum: COMPLAINT_STATUSES,
    },
    changedBy: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'User',
      default: null,
    },
    changedAt: {
      type: Date,
      default: Date.now,
    },
    note: {
      type: String,
      trim: true,
      maxlength: [1000, 'Status note must not exceed 1000 characters'],
      default: '',
    },
  },
  { _id: false }
);

const complaintSchema = new mongoose.Schema(
  {
    ticketNumber: {
      type: String,
      required: [true, 'Ticket number is required'],
      unique: true,
      trim: true,
      uppercase: true,
      index: true,
    },
    createdBy: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'User',
      required: [true, 'Complaint author is required'],
      index: true,
    },
    title: {
      type: String,
      required: [true, 'Title is required'],
      trim: true,
      minlength: [5, 'Title must be at least 5 characters'],
      maxlength: [100, 'Title must not exceed 100 characters'],
    },
    category: {
      type: String,
      required: [true, 'Category is required'],
      trim: true,
      enum: {
        values: COMPLAINT_CATEGORIES,
        message: 'Invalid category selected',
      },
      index: true,
    },
    description: {
      type: String,
      required: [true, 'Description is required'],
      trim: true,
      minlength: [20, 'Description must be at least 20 characters'],
      maxlength: [2000, 'Description must not exceed 2000 characters'],
    },
    priority: {
      type: String,
      enum: {
        values: COMPLAINT_PRIORITIES,
        message: 'Priority must be LOW, MEDIUM, or HIGH',
      },
      default: DEFAULT_PRIORITY,
      index: true,
    },
    status: {
      type: String,
      enum: {
        values: COMPLAINT_STATUSES,
        message: 'Invalid complaint status',
      },
      default: DEFAULT_STATUS,
      index: true,
    },
    location: {
      type: String,
      trim: true,
      maxlength: [100, 'Location must not exceed 100 characters'],
      default: '',
    },
    resolutionRemarks: {
      type: String,
      trim: true,
      maxlength: [1000, 'Resolution remarks must not exceed 1000 characters'],
      default: '',
    },
    resolvedAt: {
      type: Date,
      default: null,
    },
    statusHistory: {
      type: [statusHistorySchema],
      default: () => [
        {
          status: DEFAULT_STATUS,
          previousStatus: 'NONE',
          newStatus: DEFAULT_STATUS,
          changedBy: null,
          changedAt: new Date(),
          note: 'Complaint submitted by student',
        },
      ],
    },
  },
  {
    timestamps: true,
  }
);

// Indexes for optimal student and admin queries
complaintSchema.index({ createdBy: 1, createdAt: -1 });
complaintSchema.index({ createdBy: 1, status: 1 });
complaintSchema.index({ createdBy: 1, category: 1 });
complaintSchema.index({ createdAt: -1 });
complaintSchema.index({ status: 1, createdAt: -1 });

// Clean toJSON representation
complaintSchema.set('toJSON', {
  transform: (_doc, ret) => {
    delete ret.__v;
    return ret;
  },
});

const Complaint = mongoose.model('Complaint', complaintSchema);

module.exports = Complaint;

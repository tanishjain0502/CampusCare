/**
 * complaintConstants.js
 * Central definitions for complaint categories, priorities, and statuses on the frontend.
 */

export const COMPLAINT_CATEGORIES = [
  'Classroom',
  'Laboratory',
  'Internet / Wi-Fi',
  'Electrical / Maintenance',
  'Cleanliness',
  'Library',
  'Hostel',
  'Administration',
  'Other',
];

export const COMPLAINT_PRIORITIES = ['LOW', 'MEDIUM', 'HIGH'];

export const COMPLAINT_STATUSES = ['SUBMITTED', 'IN_PROGRESS', 'RESOLVED'];

export const STATUS_META = {
  SUBMITTED: {
    label: 'Submitted',
    badgeClass: 'bg-warning text-dark',
    icon: '⏳',
    description: 'Complaint received and pending administrative review.',
  },
  IN_PROGRESS: {
    label: 'In Progress',
    badgeClass: 'bg-info text-dark',
    icon: '🔄',
    description: 'The complaint is currently being investigated or acted upon.',
  },
  RESOLVED: {
    label: 'Resolved',
    badgeClass: 'bg-success',
    icon: '✅',
    description: 'The complaint has been addressed and closed.',
  },
};

export const PRIORITY_META = {
  LOW: {
    label: 'Low',
    badgeClass: 'bg-secondary',
  },
  MEDIUM: {
    label: 'Medium',
    badgeClass: 'bg-primary',
  },
  HIGH: {
    label: 'High',
    badgeClass: 'bg-danger',
  },
};

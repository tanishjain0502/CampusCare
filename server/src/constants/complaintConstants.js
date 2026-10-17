/**
 * complaintConstants.js
 * Centralized constants and categories for the CampusCare complaint module.
 */

const COMPLAINT_CATEGORIES = [
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

const COMPLAINT_PRIORITIES = ['LOW', 'MEDIUM', 'HIGH'];

const COMPLAINT_STATUSES = ['SUBMITTED', 'IN_PROGRESS', 'RESOLVED'];

const DEFAULT_PRIORITY = 'MEDIUM';
const DEFAULT_STATUS = 'SUBMITTED';

module.exports = {
  COMPLAINT_CATEGORIES,
  COMPLAINT_PRIORITIES,
  COMPLAINT_STATUSES,
  DEFAULT_PRIORITY,
  DEFAULT_STATUS,
};

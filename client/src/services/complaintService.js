import api from './api';

/**
 * complaintService.js
 * API client functions for student and admin complaint operations.
 */

// --- Student Operations ---
export const submitComplaint = (data) => api.post('/complaints', data);

export const getMyComplaints = (params) => api.get('/complaints/mine', { params });

export const getMyComplaintStats = () => api.get('/complaints/mine/stats');

export const getComplaintById = (id) => api.get(`/complaints/${id}`);

// --- Admin Operations (Part 3) ---
export const getAllComplaintsAdmin = (params) => api.get('/complaints', { params });

export const getAdminComplaintStats = () => api.get('/complaints/admin/stats');

export const getAdminRecentComplaints = (limit = 5) =>
  api.get('/complaints/admin/recent', { params: { limit } });

export const getAdminComplaintById = (id) => api.get(`/complaints/admin/${id}`);

export const updateComplaintStatus = (id, data) =>
  api.patch(`/complaints/${id}/status`, data);

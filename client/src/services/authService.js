import api from './api';

/**
 * Auth service — thin wrappers around the auth API endpoints.
 * Callers receive the full Axios response; error handling is done in the
 * calling component or context.
 */

export const registerUser = (data) => api.post('/auth/register', data);

export const loginUser = (data) => api.post('/auth/login', data);

export const getProfile = () => api.get('/auth/me');

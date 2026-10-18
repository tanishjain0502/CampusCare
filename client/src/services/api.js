import axios from 'axios';

/**
 * Pre-configured Axios instance for the CampusCare API.
 *
 * Token storage note:
 *   The JWT is stored in localStorage for simplicity in this learning project.
 *   localStorage is accessible by any JavaScript running on the page, which
 *   means it is vulnerable to XSS attacks. In a production system, prefer
 *   storing the token in an HttpOnly cookie so it is inaccessible to scripts.
 */
const rawBaseURL = import.meta.env.VITE_API_URL || 'http://localhost:5001/api';
const trimmedURL = rawBaseURL.trim().replace(/\/+$/, '');
const baseURL = trimmedURL.endsWith('/api') ? trimmedURL : `${trimmedURL}/api`;

const api = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Attach the JWT from localStorage to every outgoing request
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('campuscare_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Centralised response error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired or invalid — clear stored credentials
      localStorage.removeItem('campuscare_token');
      localStorage.removeItem('campuscare_user');
    }
    return Promise.reject(error);
  }
);

export default api;

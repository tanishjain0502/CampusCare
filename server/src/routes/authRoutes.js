const express = require('express');
const { register, login, getMe } = require('../controllers/authController');
const { protect } = require('../middleware/auth');

const router = express.Router();

// POST /api/auth/register — public, creates STUDENT accounts only
router.post('/register', register);

// POST /api/auth/login — public
router.post('/login', login);

// GET /api/auth/me — protected, returns the authenticated user's profile
router.get('/me', protect, getMe);

module.exports = router;

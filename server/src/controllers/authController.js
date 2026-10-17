const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');

// ---------------------------------------------------------------------------
// Helper: sign a JWT for a given user document
// ---------------------------------------------------------------------------
const signToken = (user) => {
  return jwt.sign(
    { id: user._id, role: user.role },
    process.env.JWT_SECRET,
    { expiresIn: process.env.JWT_EXPIRES_IN || '7d' }
  );
};

// ---------------------------------------------------------------------------
// Helper: build a safe user object without the password hash
// ---------------------------------------------------------------------------
const safeUser = (user) => ({
  id: user._id,
  name: user.name,
  email: user.email,
  role: user.role,
  createdAt: user.createdAt,
});

// ---------------------------------------------------------------------------
// POST /api/auth/register
// Public — STUDENT role only. ADMIN accounts must be seeded server-side.
// ---------------------------------------------------------------------------
const register = async (req, res) => {
  try {
    const { name, email, password } = req.body;

    // --- Basic validation ---
    const errors = [];
    if (!name || name.trim().length < 2) {
      errors.push('Name must be at least 2 characters.');
    }
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      errors.push('A valid email address is required.');
    }
    if (!password || password.length < 6) {
      errors.push('Password must be at least 6 characters.');
    }
    if (errors.length > 0) {
      return res.status(400).json({ success: false, message: errors.join(' ') });
    }

    // --- Duplicate check ---
    const existing = await User.findOne({ email: email.toLowerCase().trim() });
    if (existing) {
      return res.status(409).json({
        success: false,
        message: 'An account with this email already exists.',
      });
    }

    // --- Hash password ---
    const saltRounds = 12;
    const passwordHash = await bcrypt.hash(password, saltRounds);

    // --- Create user — role is always STUDENT for public registration ---
    const user = await User.create({
      name: name.trim(),
      email: email.toLowerCase().trim(),
      passwordHash,
      role: 'STUDENT', // Hardcoded — never taken from the request body
    });

    const token = signToken(user);

    return res.status(201).json({
      success: true,
      message: 'Registration successful.',
      token,
      user: safeUser(user),
    });
  } catch (error) {
    // Mongoose duplicate-key error (race condition safety net)
    if (error.code === 11000) {
      return res.status(409).json({
        success: false,
        message: 'An account with this email already exists.',
      });
    }
    console.error('register error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error during registration. Please try again.',
    });
  }
};

// ---------------------------------------------------------------------------
// POST /api/auth/login
// Public — both roles
// ---------------------------------------------------------------------------
const login = async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({
        success: false,
        message: 'Email and password are required.',
      });
    }

    // Fetch the user WITH the passwordHash field (select: false by default)
    const user = await User.findOne({
      email: email.toLowerCase().trim(),
    }).select('+passwordHash');

    if (!user) {
      // Generic message to avoid user enumeration
      return res.status(401).json({
        success: false,
        message: 'Invalid email or password.',
      });
    }

    const isMatch = await bcrypt.compare(password, user.passwordHash);
    if (!isMatch) {
      return res.status(401).json({
        success: false,
        message: 'Invalid email or password.',
      });
    }

    const token = signToken(user);

    return res.status(200).json({
      success: true,
      message: 'Login successful.',
      token,
      user: safeUser(user),
    });
  } catch (error) {
    console.error('login error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error during login. Please try again.',
    });
  }
};

// ---------------------------------------------------------------------------
// GET /api/auth/me
// Protected — requires a valid JWT
// ---------------------------------------------------------------------------
const getMe = async (req, res) => {
  try {
    // req.user is populated by the protect middleware
    return res.status(200).json({
      success: true,
      user: safeUser(req.user),
    });
  } catch (error) {
    console.error('getMe error:', error);
    return res.status(500).json({
      success: false,
      message: 'Server error. Please try again.',
    });
  }
};

module.exports = { register, login, getMe };

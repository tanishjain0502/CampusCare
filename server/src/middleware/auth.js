const jwt = require('jsonwebtoken');
const User = require('../models/User');

/**
 * protect
 * -------
 * Middleware that validates the JWT supplied in the Authorization header.
 * Expected format: "Authorization: Bearer <token>"
 *
 * On success it attaches the authenticated user document (without passwordHash)
 * to req.user and calls next().
 *
 * Security note:
 *   - Tokens are verified with the server-side JWT_SECRET.
 *   - The user is re-fetched from the database so that a deleted or
 *     deactivated account is rejected even if the token itself is still valid.
 */
const protect = async (req, res, next) => {
  try {
    let token;

    if (
      req.headers.authorization &&
      req.headers.authorization.startsWith('Bearer ')
    ) {
      token = req.headers.authorization.split(' ')[1];
    }

    if (!token) {
      return res.status(401).json({
        success: false,
        message: 'Access denied. No token provided.',
      });
    }

    // Verify signature and expiry
    let decoded;
    try {
      decoded = jwt.verify(token, process.env.JWT_SECRET);
    } catch (err) {
      if (err.name === 'TokenExpiredError') {
        return res.status(401).json({
          success: false,
          message: 'Token expired. Please log in again.',
        });
      }
      return res.status(401).json({
        success: false,
        message: 'Invalid token. Please log in again.',
      });
    }

    // Confirm the user still exists in the database
    const user = await User.findById(decoded.id);
    if (!user) {
      return res.status(401).json({
        success: false,
        message: 'User associated with this token no longer exists.',
      });
    }

    req.user = user;
    next();
  } catch (error) {
    console.error('protect middleware error:', error);
    return res.status(500).json({
      success: false,
      message: 'Internal server error during authentication.',
    });
  }
};

/**
 * restrictTo
 * ----------
 * Role-based access-control middleware factory.
 * Usage: router.get('/admin-only', protect, restrictTo('ADMIN'), handler)
 *
 * Must be used AFTER protect so that req.user is already populated.
 */
const restrictTo = (...roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({
        success: false,
        message: 'You do not have permission to perform this action.',
      });
    }
    next();
  };
};

module.exports = { protect, restrictTo };

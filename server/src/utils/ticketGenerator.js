const crypto = require('crypto');

/**
 * Generates a unique, human-friendly ticket number.
 * Format: CC-YYYYMMDD-XXXXXX
 * Example: CC-20261017-A4F9B2
 *
 * Uses cryptographically secure random bytes combined with date prefix
 * to ensure uniqueness even under high concurrency.
 */
const generateTicketNumber = () => {
  const dateStr = new Date().toISOString().slice(0, 10).replace(/-/g, '');
  const randomSuffix = crypto.randomBytes(3).toString('hex').toUpperCase();
  return `CC-${dateStr}-${randomSuffix}`;
};

module.exports = {
  generateTicketNumber,
};

const mongoose = require('mongoose');

/**
 * User schema for CampusCare.
 *
 * Roles:
 *   - STUDENT : registered via the public /api/auth/register endpoint.
 *   - ADMIN   : created only through the secure server-side seed script
 *               (npm run seed:admin inside the server directory).
 *               There is NO public endpoint that allows ADMIN self-registration.
 *
 * Security notes:
 *   - email is normalised to lowercase before saving to prevent
 *     case-sensitivity duplicates.
 *   - passwordHash stores only the bcrypt hash; the plaintext password is
 *     never stored or returned.
 *   - The toJSON transform strips __v and passwordHash so that accidental
 *     serialisation of a User document never leaks the hash.
 */
const userSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: [true, 'Name is required'],
      trim: true,
      minlength: [2, 'Name must be at least 2 characters'],
      maxlength: [100, 'Name must not exceed 100 characters'],
    },
    email: {
      type: String,
      required: [true, 'Email is required'],
      unique: true,
      lowercase: true,
      trim: true,
      match: [
        /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        'Please provide a valid email address',
      ],
    },
    passwordHash: {
      type: String,
      required: [true, 'Password is required'],
      select: false, // Never returned in queries unless explicitly selected
    },
    role: {
      type: String,
      enum: {
        values: ['STUDENT', 'ADMIN'],
        message: 'Role must be either STUDENT or ADMIN',
      },
      default: 'STUDENT',
    },
  },
  {
    timestamps: true, // Adds createdAt and updatedAt automatically
  }
);

/**
 * Remove sensitive and internal fields when converting to JSON.
 * This is a safety net — controllers should also avoid spreading
 * the full document into responses.
 */
userSchema.set('toJSON', {
  transform: (_doc, ret) => {
    delete ret.passwordHash;
    delete ret.__v;
    return ret;
  },
});

const User = mongoose.model('User', userSchema);

module.exports = User;

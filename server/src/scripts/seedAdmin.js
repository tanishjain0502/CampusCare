/**
 * seedAdmin.js
 * ============
 * One-time script to create the initial ADMIN account.
 *
 * Usage (run from the server/ directory):
 *   ADMIN_EMAIL=admin@college.edu ADMIN_PASSWORD=YourStrongPass123 node src/scripts/seedAdmin.js
 *
 * Or set ADMIN_EMAIL and ADMIN_PASSWORD in your .env file before running:
 *   npm run seed:admin
 *
 * Security notes:
 *   - This script is the ONLY way to create an ADMIN account.
 *   - There is no HTTP endpoint that allows public ADMIN registration.
 *   - Run this once, then remove ADMIN_PASSWORD from your .env (or set it blank).
 *   - If the email already exists the script exits without overwriting.
 */

require('dotenv').config({ path: require('path').resolve(__dirname, '../../.env') });
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const User = require('../models/User');

const ADMIN_NAME = process.env.ADMIN_NAME || 'System Administrator';
const ADMIN_EMAIL = process.env.ADMIN_EMAIL;
const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD;

const run = async () => {
  if (!ADMIN_EMAIL || !ADMIN_PASSWORD) {
    console.error(
      '❌  ADMIN_EMAIL and ADMIN_PASSWORD must be set as environment variables.\n' +
      '    Example:\n' +
      '    ADMIN_EMAIL=admin@college.edu ADMIN_PASSWORD=YourStrongPass node src/scripts/seedAdmin.js'
    );
    process.exit(1);
  }

  if (ADMIN_PASSWORD.length < 8) {
    console.error('❌  ADMIN_PASSWORD must be at least 8 characters.');
    process.exit(1);
  }

  await mongoose.connect(process.env.MONGODB_URI);
  console.log('Connected to MongoDB.');

  const existing = await User.findOne({ email: ADMIN_EMAIL.toLowerCase() });
  if (existing) {
    console.log(`ℹ️  A user with email "${ADMIN_EMAIL}" already exists (role: ${existing.role}). No changes made.`);
    await mongoose.disconnect();
    process.exit(0);
  }

  const passwordHash = await bcrypt.hash(ADMIN_PASSWORD, 12);

  const admin = await User.create({
    name: ADMIN_NAME,
    email: ADMIN_EMAIL.toLowerCase().trim(),
    passwordHash,
    role: 'ADMIN',
  });

  console.log(`✅  Admin account created successfully.`);
  console.log(`    Name  : ${admin.name}`);
  console.log(`    Email : ${admin.email}`);
  console.log(`    Role  : ${admin.role}`);
  console.log('\n⚠️  Remove ADMIN_PASSWORD from your .env file now.');

  await mongoose.disconnect();
  process.exit(0);
};

run().catch((err) => {
  console.error('Seed script failed:', err.message);
  process.exit(1);
});

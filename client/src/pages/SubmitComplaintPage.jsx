import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import {
  COMPLAINT_CATEGORIES,
  COMPLAINT_PRIORITIES,
} from '../constants/complaintConstants';
import { submitComplaint } from '../services/complaintService';

const SubmitComplaintPage = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    title: '',
    category: '',
    description: '',
    priority: 'MEDIUM',
    location: '',
  });

  const [errors, setErrors] = useState({});
  const [serverError, setServerError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const [submitting, setSubmitting] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    // Clear field-specific error when user modifies it
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: null }));
    }
    setServerError('');
  };

  const validate = () => {
    const newErrors = {};

    const trimmedTitle = formData.title.trim();
    if (!trimmedTitle) {
      newErrors.title = 'Complaint title is required.';
    } else if (trimmedTitle.length < 5) {
      newErrors.title = 'Title must be at least 5 characters.';
    } else if (trimmedTitle.length > 100) {
      newErrors.title = 'Title cannot exceed 100 characters.';
    }

    if (!formData.category) {
      newErrors.category = 'Please select a complaint category.';
    } else if (!COMPLAINT_CATEGORIES.includes(formData.category)) {
      newErrors.category = 'Please select a valid category from the list.';
    }

    const trimmedDesc = formData.description.trim();
    if (!trimmedDesc) {
      newErrors.description = 'Please provide a detailed description.';
    } else if (trimmedDesc.length < 20) {
      newErrors.description = 'Description must be at least 20 characters.';
    } else if (trimmedDesc.length > 2000) {
      newErrors.description = 'Description cannot exceed 2000 characters.';
    }

    if (formData.location && formData.location.trim().length > 100) {
      newErrors.location = 'Location cannot exceed 100 characters.';
    }

    if (!COMPLAINT_PRIORITIES.includes(formData.priority)) {
      newErrors.priority = 'Invalid priority selected.';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (submitting) return; // Prevent double submission

    if (!validate()) {
      return;
    }

    setSubmitting(true);
    setServerError('');

    try {
      const payload = {
        title: formData.title.trim(),
        category: formData.category,
        description: formData.description.trim(),
        priority: formData.priority,
        location: formData.location.trim(),
      };

      const res = await submitComplaint(payload);
      const createdComplaint = res.data.complaint;

      setSuccessMessage(
        `Complaint registered successfully with Ticket #${createdComplaint.ticketNumber}!`
      );

      // Short delay so the user sees the confirmation before navigating
      setTimeout(() => {
        navigate(`/student/complaints/${createdComplaint._id}`);
      }, 1200);
    } catch (err) {
      const message =
        err.response?.data?.message ||
        'Failed to submit complaint. Please check your inputs and try again.';
      setServerError(message);
      setSubmitting(false);
    }
  };

  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-lg-8">
          {/* Breadcrumb navigation */}
          <nav aria-label="breadcrumb" className="mb-3">
            <ol className="breadcrumb">
              <li className="breadcrumb-item">
                <Link to="/student/dashboard">Dashboard</Link>
              </li>
              <li className="breadcrumb-item">
                <Link to="/student/complaints">My Complaints</Link>
              </li>
              <li className="breadcrumb-item active" aria-current="page">
                Submit Complaint
              </li>
            </ol>
          </nav>

          <div className="card shadow-sm border-0">
            <div className="card-header bg-primary text-white py-3">
              <div className="d-flex align-items-center">
                <span className="fs-3 me-2">📝</span>
                <div>
                  <h4 className="mb-0 fw-bold">Submit a New Complaint</h4>
                  <small className="text-white-50">
                    Provide details about your campus concern for prompt assistance.
                  </small>
                </div>
              </div>
            </div>

            <div className="card-body p-4 p-md-5">
              {serverError && (
                <div className="alert alert-danger d-flex align-items-center mb-4" role="alert">
                  <span className="me-2">⚠️</span>
                  <div>{serverError}</div>
                </div>
              )}

              {successMessage && (
                <div className="alert alert-success d-flex align-items-center mb-4" role="alert">
                  <span className="me-2">✅</span>
                  <div>{successMessage} Redirecting to complaint details...</div>
                </div>
              )}

              <form onSubmit={handleSubmit} noValidate>
                {/* Title */}
                <div className="mb-3">
                  <div className="d-flex justify-content-between align-items-center mb-1">
                    <label htmlFor="title" className="form-label fw-semibold mb-0">
                      Complaint Title <span className="text-danger">*</span>
                    </label>
                    <small className="text-muted">
                      {formData.title.trim().length}/100 chars (min 5)
                    </small>
                  </div>
                  <input
                    id="title"
                    type="text"
                    name="title"
                    className={`form-control ${errors.title ? 'is-invalid' : ''}`}
                    placeholder="e.g. Projector not working in Room 304"
                    value={formData.title}
                    onChange={handleChange}
                    maxLength={100}
                    disabled={submitting}
                    required
                  />
                  {errors.title && (
                    <div className="invalid-feedback">{errors.title}</div>
                  )}
                </div>

                {/* Category & Priority Row */}
                <div className="row g-3 mb-3">
                  <div className="col-md-6">
                    <label htmlFor="category" className="form-label fw-semibold">
                      Category <span className="text-danger">*</span>
                    </label>
                    <select
                      id="category"
                      name="category"
                      className={`form-select ${errors.category ? 'is-invalid' : ''}`}
                      value={formData.category}
                      onChange={handleChange}
                      disabled={submitting}
                      required
                    >
                      <option value="">-- Select a Category --</option>
                      {COMPLAINT_CATEGORIES.map((cat) => (
                        <option key={cat} value={cat}>
                          {cat}
                        </option>
                      ))}
                    </select>
                    {errors.category && (
                      <div className="invalid-feedback">{errors.category}</div>
                    )}
                  </div>

                  <div className="col-md-6">
                    <label htmlFor="priority" className="form-label fw-semibold">
                      Priority Level
                    </label>
                    <select
                      id="priority"
                      name="priority"
                      className={`form-select ${errors.priority ? 'is-invalid' : ''}`}
                      value={formData.priority}
                      onChange={handleChange}
                      disabled={submitting}
                    >
                      <option value="LOW">Low (Informational / Non-urgent)</option>
                      <option value="MEDIUM">Medium (Normal concern - Default)</option>
                      <option value="HIGH">High (Urgent / Hinders academic work)</option>
                    </select>
                    {errors.priority && (
                      <div className="invalid-feedback">{errors.priority}</div>
                    )}
                  </div>
                </div>

                {/* Optional Location */}
                <div className="mb-3">
                  <label htmlFor="location" className="form-label fw-semibold">
                    Specific Location <span className="text-muted fw-normal">(Optional)</span>
                  </label>
                  <input
                    id="location"
                    type="text"
                    name="location"
                    className={`form-control ${errors.location ? 'is-invalid' : ''}`}
                    placeholder="e.g. Block C, 2nd Floor, Room 204 or Girl's Hostel Wing B"
                    value={formData.location}
                    onChange={handleChange}
                    maxLength={100}
                    disabled={submitting}
                  />
                  {errors.location ? (
                    <div className="invalid-feedback">{errors.location}</div>
                  ) : (
                    <small className="form-text text-muted">
                      Help campus maintenance locate the issue quickly.
                    </small>
                  )}
                </div>

                {/* Description */}
                <div className="mb-4">
                  <div className="d-flex justify-content-between align-items-center mb-1">
                    <label htmlFor="description" className="form-label fw-semibold mb-0">
                      Detailed Description <span className="text-danger">*</span>
                    </label>
                    <small className="text-muted">
                      {formData.description.trim().length}/2000 chars (min 20)
                    </small>
                  </div>
                  <textarea
                    id="description"
                    name="description"
                    rows="5"
                    className={`form-control ${errors.description ? 'is-invalid' : ''}`}
                    placeholder="Describe what happened, when you noticed it, and any other relevant details..."
                    value={formData.description}
                    onChange={handleChange}
                    maxLength={2000}
                    disabled={submitting}
                    required
                  />
                  {errors.description && (
                    <div className="invalid-feedback">{errors.description}</div>
                  )}
                </div>

                {/* Submission note */}
                <div className="alert alert-light border small text-muted mb-4">
                  ℹ️ Once submitted, your complaint will be assigned a unique ticket number and
                  reviewed by the administrative team. You will be able to track its progress in your
                  dashboard.
                </div>

                {/* Action buttons */}
                <div className="d-flex gap-3 justify-content-end">
                  <Link
                    to="/student/complaints"
                    className="btn btn-outline-secondary px-4"
                    tabIndex={submitting ? -1 : 0}
                  >
                    Cancel
                  </Link>
                  <button
                    type="submit"
                    className="btn btn-primary px-5 fw-semibold d-flex align-items-center"
                    disabled={submitting}
                  >
                    {submitting ? (
                      <>
                        <span
                          className="spinner-border spinner-border-sm me-2"
                          role="status"
                          aria-hidden="true"
                        />
                        Submitting...
                      </>
                    ) : (
                      'Submit Complaint'
                    )}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SubmitComplaintPage;

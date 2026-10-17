import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import {
  COMPLAINT_STATUSES,
} from '../constants/complaintConstants';
import {
  getAdminComplaintById,
  updateComplaintStatus,
} from '../services/complaintService';
import ComplaintStatusBadge from '../components/ComplaintStatusBadge';
import ComplaintPriorityBadge from '../components/ComplaintPriorityBadge';

const AdminComplaintDetailsPage = () => {
  const { id } = useParams();

  const [complaint, setComplaint] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Status update form state
  const [newStatus, setNewStatus] = useState('');
  const [remarks, setRemarks] = useState('');
  const [statusError, setStatusError] = useState('');
  const [statusSuccess, setStatusSuccess] = useState('');
  const [updating, setUpdating] = useState(false);

  useEffect(() => {
    const fetchDetails = async () => {
      setLoading(true);
      setError('');

      try {
        const res = await getAdminComplaintById(id);
        const data = res.data.complaint;
        setComplaint(data);
        setNewStatus(data.status);
      } catch (err) {
        setError(
          err.response?.data?.message ||
            'Unable to load complaint details. Please check the ID and try again.'
        );
      } finally {
        setLoading(false);
      }
    };

    fetchDetails();
  }, [id]);

  const handleStatusSubmit = async (e) => {
    e.preventDefault();
    setStatusError('');
    setStatusSuccess('');

    if (complaint.status === 'RESOLVED') {
      setStatusError('This complaint is already resolved. Status cannot be modified.');
      return;
    }

    if (!newStatus || !COMPLAINT_STATUSES.includes(newStatus)) {
      setStatusError('Please select a valid target status.');
      return;
    }

    if (newStatus === complaint.status) {
      setStatusError('Please select a different status to update.');
      return;
    }

    // Require remarks when resolving
    if (newStatus === 'RESOLVED') {
      const trimmed = remarks.trim();
      if (!trimmed || trimmed.length < 5) {
        setStatusError('Resolution remarks are required when resolving a complaint (minimum 5 characters).');
        return;
      }
      if (trimmed.length > 1000) {
        setStatusError('Resolution remarks cannot exceed 1000 characters.');
        return;
      }
    }

    setUpdating(true);

    try {
      const res = await updateComplaintStatus(id, {
        status: newStatus,
        remarks: remarks.trim(),
      });

      setComplaint(res.data.complaint);
      setStatusSuccess(`Complaint status updated to ${newStatus} successfully.`);
      setRemarks('');
    } catch (err) {
      setStatusError(
        err.response?.data?.message || 'Failed to update complaint status. Please try again.'
      );
    } finally {
      setUpdating(false);
    }
  };

  if (loading) {
    return (
      <div className="container py-5 text-center">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading complaint...</span>
        </div>
        <p className="text-muted mt-2">Loading ticket details...</p>
      </div>
    );
  }

  if (error || !complaint) {
    return (
      <div className="container py-5">
        <div className="row justify-content-center">
          <div className="col-md-7">
            <div className="card border-0 shadow-sm text-center py-5 px-3">
              <div className="card-body">
                <div style={{ fontSize: '4rem' }} className="mb-3">
                  🔍
                </div>
                <h3 className="fw-bold text-dark mb-2">Complaint Not Found</h3>
                <p className="text-muted mb-4">{error || 'The requested ticket could not be located.'}</p>
                <Link to="/admin/complaints" className="btn btn-primary px-4 fw-semibold">
                  ← Back to All Complaints
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  const isAlreadyResolved = complaint.status === 'RESOLVED';

  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-lg-10">
          {/* Breadcrumb navigation */}
          <nav aria-label="breadcrumb" className="mb-3">
            <ol className="breadcrumb">
              <li className="breadcrumb-item">
                <Link to="/admin/dashboard">Dashboard</Link>
              </li>
              <li className="breadcrumb-item">
                <Link to="/admin/complaints">Complaints</Link>
              </li>
              <li className="breadcrumb-item active" aria-current="page">
                {complaint.ticketNumber}
              </li>
            </ol>
          </nav>

          {/* Main Card */}
          <div className="card border-0 shadow-sm mb-4">
            <div className="card-header bg-white border-bottom py-3 d-flex flex-wrap justify-content-between align-items-center gap-2">
              <div>
                <span className="text-muted small d-block">Complaint Ticket</span>
                <span className="fs-5 fw-bold font-monospace text-primary">
                  {complaint.ticketNumber}
                </span>
              </div>
              <div className="d-flex align-items-center gap-2">
                <ComplaintPriorityBadge priority={complaint.priority} />
                <ComplaintStatusBadge status={complaint.status} />
              </div>
            </div>

            <div className="card-body p-4 p-md-5">
              {/* Title & Student Meta */}
              <h2 className="fw-bold text-dark mb-3">{complaint.title}</h2>

              {/* Information Grid */}
              <div className="row g-3 py-3 border-top border-bottom bg-light rounded-3 mb-4">
                <div className="col-md-3 col-sm-6">
                  <small className="text-muted d-block">Submitted By</small>
                  <strong className="text-dark d-block">
                    {complaint.createdBy?.name || 'Unknown'}
                  </strong>
                  <small className="text-muted">
                    {complaint.createdBy?.email || '—'}
                  </small>
                </div>
                <div className="col-md-3 col-sm-6">
                  <small className="text-muted d-block">Category</small>
                  <strong className="text-dark">{complaint.category}</strong>
                </div>
                <div className="col-md-3 col-sm-6">
                  <small className="text-muted d-block">Location</small>
                  <strong className="text-dark">
                    {complaint.location ? `📍 ${complaint.location}` : 'Not specified'}
                  </strong>
                </div>
                <div className="col-md-3 col-sm-6">
                  <small className="text-muted d-block">Submission Date</small>
                  <strong className="text-dark">
                    {new Date(complaint.createdAt).toLocaleString('en-IN', {
                      dateStyle: 'medium',
                      timeStyle: 'short',
                    })}
                  </strong>
                </div>
              </div>

              {/* Description */}
              <div className="mb-4">
                <h5 className="fw-bold text-primary mb-2">Complaint Description</h5>
                <div
                  className="p-3 bg-white border rounded-3 text-secondary"
                  style={{ whiteSpace: 'pre-wrap', lineHeight: '1.7' }}
                >
                  {complaint.description}
                </div>
              </div>

              {/* Resolution Remarks Banner (if resolved) */}
              {isAlreadyResolved && (
                <div className="alert alert-success border-success mb-4 p-3">
                  <div className="d-flex align-items-center mb-1">
                    <span className="fs-5 me-2">✅</span>
                    <h6 className="fw-bold mb-0 text-success">Complaint Resolved</h6>
                  </div>
                  <p className="mb-1 text-dark">
                    <strong>Remarks:</strong> {complaint.resolutionRemarks || 'Issue addressed.'}
                  </p>
                  {complaint.resolvedAt && (
                    <small className="text-muted">
                      Resolved on:{' '}
                      {new Date(complaint.resolvedAt).toLocaleString('en-IN', {
                        dateStyle: 'medium',
                        timeStyle: 'short',
                      })}
                    </small>
                  )}
                </div>
              )}

              {/* Status Management Form */}
              <div className="card border mb-4 shadow-sm">
                <div className="card-header bg-light fw-bold py-2">
                  ⚙️ Update Complaint Status
                </div>
                <div className="card-body p-4">
                  {statusError && (
                    <div className="alert alert-danger py-2 mb-3 small" role="alert">
                      {statusError}
                    </div>
                  )}
                  {statusSuccess && (
                    <div className="alert alert-success py-2 mb-3 small" role="alert">
                      {statusSuccess}
                    </div>
                  )}

                  {isAlreadyResolved ? (
                    <div className="text-muted small">
                      🔒 <strong>Notice:</strong> This complaint is already marked as{' '}
                      <span className="badge bg-success">RESOLVED</span>. Reopening or further
                      status changes are not permitted in this version.
                    </div>
                  ) : (
                    <form onSubmit={handleStatusSubmit}>
                      <div className="row g-3 align-items-end mb-3">
                        <div className="col-md-5">
                          <label htmlFor="newStatus" className="form-label fw-semibold">
                            New Status <span className="text-danger">*</span>
                          </label>
                          <select
                            id="newStatus"
                            className="form-select"
                            value={newStatus}
                            onChange={(e) => {
                              setNewStatus(e.target.value);
                              setStatusError('');
                            }}
                            disabled={updating}
                          >
                            <option value="SUBMITTED">SUBMITTED (Pending review)</option>
                            <option value="IN_PROGRESS">IN_PROGRESS (Under investigation)</option>
                            <option value="RESOLVED">RESOLVED (Issue addressed & closed)</option>
                          </select>
                        </div>

                        <div className="col-md-7">
                          <label
                            htmlFor="remarks"
                            className="form-label fw-semibold"
                          >
                            {newStatus === 'RESOLVED' ? (
                              <>
                                Resolution Remarks <span className="text-danger">* (Required)</span>
                              </>
                            ) : (
                              'Status Change Note (Optional)'
                            )}
                          </label>
                          <input
                            id="remarks"
                            type="text"
                            className="form-control"
                            placeholder={
                              newStatus === 'RESOLVED'
                                ? 'Describe what was done to fix this issue (min 5 chars)...'
                                : 'e.g. Assigned to campus maintenance team...'
                            }
                            value={remarks}
                            onChange={(e) => {
                              setRemarks(e.target.value);
                              setStatusError('');
                            }}
                            maxLength={1000}
                            disabled={updating}
                          />
                        </div>
                      </div>

                      <div className="text-end">
                        <button
                          type="submit"
                          className="btn btn-primary px-4 fw-semibold"
                          disabled={updating || newStatus === complaint.status}
                        >
                          {updating ? (
                            <>
                              <span
                                className="spinner-border spinner-border-sm me-2"
                                role="status"
                                aria-hidden="true"
                              />
                              Updating...
                            </>
                          ) : (
                            'Confirm Status Update'
                          )}
                        </button>
                      </div>
                    </form>
                  )}
                </div>
              </div>

              {/* Status History Timeline */}
              {complaint.statusHistory && complaint.statusHistory.length > 0 && (
                <div>
                  <h5 className="fw-bold text-primary mb-3">Status Change History</h5>
                  <div className="list-group list-group-flush border rounded-3 overflow-hidden">
                    {complaint.statusHistory.map((step, idx) => (
                      <div
                        key={idx}
                        className="list-group-item p-3 d-flex align-items-start gap-3"
                      >
                        <div className="mt-1">
                          <ComplaintStatusBadge status={step.newStatus || step.status} />
                        </div>
                        <div className="flex-grow-1">
                          <div className="d-flex justify-content-between align-items-center mb-1">
                            <span className="fw-semibold text-dark">
                              {step.note || `Status set to ${step.newStatus || step.status}`}
                            </span>
                            <small className="text-muted">
                              {new Date(step.changedAt).toLocaleString('en-IN', {
                                dateStyle: 'medium',
                                timeStyle: 'short',
                              })}
                            </small>
                          </div>
                          {step.changedBy && (
                            <small className="text-muted d-block">
                              Updated by:{' '}
                              <strong>
                                {step.changedBy.name || 'Admin'}
                              </strong>{' '}
                              ({step.changedBy.email || 'System'})
                            </small>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>

            <div className="card-footer bg-white border-top py-3 d-flex justify-content-between align-items-center">
              <Link to="/admin/complaints" className="btn btn-outline-secondary btn-sm">
                ← Back to All Complaints
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminComplaintDetailsPage;

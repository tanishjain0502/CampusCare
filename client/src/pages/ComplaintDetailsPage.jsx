import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getComplaintById } from '../services/complaintService';
import ComplaintStatusBadge from '../components/ComplaintStatusBadge';
import ComplaintPriorityBadge from '../components/ComplaintPriorityBadge';

const ComplaintDetailsPage = () => {
  const { id } = useParams();

  const [complaint, setComplaint] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchDetails = async () => {
      setLoading(true);
      setError('');

      try {
        const res = await getComplaintById(id);
        setComplaint(res.data.complaint);
      } catch (err) {
        if (err.response?.status === 404) {
          setError('Complaint not found or you do not have permission to view it.');
        } else {
          setError(
            err.response?.data?.message ||
              'Unable to load complaint details. Please try again later.'
          );
        }
      } finally {
        setLoading(false);
      }
    };

    fetchDetails();
  }, [id]);

  if (loading) {
    return (
      <div className="container py-5 text-center">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading details...</span>
        </div>
        <p className="text-muted mt-3">Loading complaint details...</p>
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
                <p className="text-muted mb-4">{error}</p>
                <Link to="/student/complaints" className="btn btn-primary px-4 fw-semibold">
                  ← Back to My Complaints
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-lg-9">
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
                {complaint.ticketNumber}
              </li>
            </ol>
          </nav>

          {/* Main Complaint Card */}
          <div className="card border-0 shadow-sm mb-4">
            <div className="card-header bg-white border-bottom py-3 d-flex flex-wrap justify-content-between align-items-center gap-2">
              <div>
                <span className="text-muted small d-block">Ticket Number</span>
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
              {/* Title */}
              <h2 className="fw-bold text-dark mb-3">{complaint.title}</h2>

              {/* Meta details strip */}
              <div className="row g-3 py-3 border-top border-bottom bg-light rounded-3 mb-4 text-center text-md-start">
                <div className="col-md-3 col-6">
                  <small className="text-muted d-block">Category</small>
                  <strong className="text-dark">{complaint.category}</strong>
                </div>
                <div className="col-md-3 col-6">
                  <small className="text-muted d-block">Location</small>
                  <strong className="text-dark">
                    {complaint.location ? `📍 ${complaint.location}` : 'Not specified'}
                  </strong>
                </div>
                <div className="col-md-3 col-6">
                  <small className="text-muted d-block">Submitted On</small>
                  <strong className="text-dark">
                    {new Date(complaint.createdAt).toLocaleDateString('en-IN', {
                      day: 'numeric',
                      month: 'short',
                      year: 'numeric',
                    })}
                  </strong>
                </div>
                <div className="col-md-3 col-6">
                  <small className="text-muted d-block">Last Updated</small>
                  <strong className="text-dark">
                    {new Date(complaint.updatedAt).toLocaleDateString('en-IN', {
                      day: 'numeric',
                      month: 'short',
                      year: 'numeric',
                    })}
                  </strong>
                </div>
              </div>

              {/* Resolution Banner for Resolved Complaints */}
              {complaint.status === 'RESOLVED' && (
                <div className="alert alert-success border-0 shadow-sm p-4 mb-4 rounded-3">
                  <div className="d-flex align-items-center mb-2">
                    <span className="fs-4 me-2">🎉</span>
                    <h5 className="alert-heading fw-bold mb-0">Complaint Resolved</h5>
                  </div>
                  {complaint.resolutionRemarks ? (
                    <p className="mb-2 text-dark">{complaint.resolutionRemarks}</p>
                  ) : (
                    <p className="mb-2 text-dark">This complaint has been addressed and marked as resolved by the administration.</p>
                  )}
                  {complaint.resolvedAt && (
                    <small className="text-muted d-block">
                      Resolved on{' '}
                      {new Date(complaint.resolvedAt).toLocaleDateString('en-IN', {
                        day: 'numeric',
                        month: 'short',
                        year: 'numeric',
                        hour: '2-digit',
                        minute: '2-digit',
                      })}
                    </small>
                  )}
                </div>
              )}

              {/* Description */}
              <div className="mb-5">
                <h5 className="fw-bold text-primary mb-2">Complaint Description</h5>
                <div
                  className="p-3 bg-white border rounded-3 text-secondary"
                  style={{ whiteSpace: 'pre-wrap', lineHeight: '1.7' }}
                >
                  {complaint.description}
                </div>
              </div>

              {/* Status History Timeline */}
              {complaint.statusHistory && complaint.statusHistory.length > 0 && (
                <div>
                  <h5 className="fw-bold text-primary mb-3">Status Timeline</h5>
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
                          <div className="d-flex justify-content-between align-items-center">
                            <span className="fw-semibold text-dark">
                              {step.note || `Status changed to ${step.newStatus || step.status}`}
                            </span>
                            <small className="text-muted">
                              {new Date(step.changedAt).toLocaleString('en-IN', {
                                dateStyle: 'medium',
                                timeStyle: 'short',
                              })}
                            </small>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>

            <div className="card-footer bg-white border-top py-3 d-flex justify-content-between align-items-center">
              <Link to="/student/complaints" className="btn btn-outline-secondary btn-sm">
                ← Back to My Complaints
              </Link>
              <Link to="/student/complaints/new" className="btn btn-primary btn-sm fw-semibold">
                ➕ Submit Another Complaint
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ComplaintDetailsPage;

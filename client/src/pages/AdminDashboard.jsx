import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import {
  getAdminComplaintStats,
  getAdminRecentComplaints,
} from '../services/complaintService';
import ComplaintStatusBadge from '../components/ComplaintStatusBadge';
import ComplaintPriorityBadge from '../components/ComplaintPriorityBadge';

const AdminDashboard = () => {
  const { user } = useAuth();

  const [stats, setStats] = useState({
    total: 0,
    submitted: 0,
    inProgress: 0,
    resolved: 0,
  });
  const [recentComplaints, setRecentComplaints] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchDashboardData = async () => {
      setLoading(true);
      setError('');

      try {
        const [statsRes, complaintsRes] = await Promise.all([
          getAdminComplaintStats(),
          getAdminRecentComplaints(5),
        ]);

        if (statsRes.data?.stats) {
          setStats(statsRes.data.stats);
        }
        if (complaintsRes.data?.complaints) {
          setRecentComplaints(complaintsRes.data.complaints);
        }
      } catch (err) {
        setError(
          err.response?.data?.message ||
            'Failed to load administrative complaint data. Please try again.'
        );
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  const statCards = [
    {
      label: 'Total Complaints',
      value: stats.total,
      color: 'primary',
      icon: '📋',
      statusFilter: '',
      description: 'All complaints received',
    },
    {
      label: 'Pending / Submitted',
      value: stats.submitted,
      color: 'warning',
      icon: '⏳',
      statusFilter: 'SUBMITTED',
      description: 'Needs initial review',
    },
    {
      label: 'In Progress',
      value: stats.inProgress,
      color: 'info',
      icon: '🔄',
      statusFilter: 'IN_PROGRESS',
      description: 'Currently being handled',
    },
    {
      label: 'Resolved',
      value: stats.resolved,
      color: 'success',
      icon: '✅',
      statusFilter: 'RESOLVED',
      description: 'Addressed and closed',
    },
  ];

  return (
    <div className="container py-5">
      {/* Welcome header */}
      <div className="d-flex flex-wrap justify-content-between align-items-center mb-4 gap-3">
        <div>
          <h1 className="fw-bold text-primary mb-1">Administrator Dashboard</h1>
          <p className="text-muted mb-0">
            Welcome, <strong>{user?.name}</strong>. Monitor, investigate, and resolve college complaints.
          </p>
        </div>
        <div className="d-flex gap-2">
          <Link
            to="/admin/complaints"
            className="btn btn-primary fw-semibold px-4 shadow-sm"
          >
            📋 Manage All Complaints
          </Link>
        </div>
      </div>

      {error && (
        <div className="alert alert-danger py-3 mb-4" role="alert">
          {error}
        </div>
      )}

      {/* Admin Profile & Real Stats Row */}
      <div className="row g-4 mb-4">
        {/* Profile Card */}
        <div className="col-lg-4">
          <div className="card border-0 shadow-sm h-100">
            <div className="card-body p-4">
              <div className="d-flex justify-content-between align-items-start mb-3">
                <h5 className="fw-bold text-primary mb-0">👤 Admin Profile</h5>
                <span className="badge bg-danger">ADMIN</span>
              </div>
              <dl className="mb-0 small">
                <dt className="text-muted">Name</dt>
                <dd className="fw-semibold mb-2">{user?.name}</dd>
                <dt className="text-muted">Email</dt>
                <dd className="fw-semibold mb-2">{user?.email}</dd>
                <dt className="text-muted">System Role</dt>
                <dd className="fw-semibold mb-0">Campus Administrator</dd>
              </dl>
              <hr className="my-3" />
              <div className="d-grid gap-2">
                <Link
                  to="/admin/complaints?status=SUBMITTED"
                  className="btn btn-outline-warning btn-sm text-start"
                >
                  ⏳ Review Submitted Complaints ({stats.submitted})
                </Link>
                <Link
                  to="/admin/complaints?status=IN_PROGRESS"
                  className="btn btn-outline-info btn-sm text-start"
                >
                  🔄 Active In-Progress Tickets ({stats.inProgress})
                </Link>
              </div>
            </div>
          </div>
        </div>

        {/* Live Metrics Grid */}
        <div className="col-lg-8">
          <div className="row g-3">
            {statCards.map(({ label, value, color, icon, statusFilter, description }) => (
              <div key={label} className="col-sm-6">
                <Link
                  to={statusFilter ? `/admin/complaints?status=${statusFilter}` : '/admin/complaints'}
                  className="text-decoration-none"
                >
                  <div
                    className={`card border-0 shadow-sm border-start border-${color} border-4 h-100 card-hover`}
                    title={`Click to view ${label.toLowerCase()}`}
                  >
                    <div className="card-body p-3 d-flex justify-content-between align-items-center">
                      <div>
                        <div className="text-muted small fw-semibold text-uppercase">
                          {label}
                        </div>
                        <div className={`fs-2 fw-bold text-${color}`}>
                          {loading ? (
                            <span
                              className="spinner-border spinner-border-sm text-secondary"
                              role="status"
                            />
                          ) : (
                            value
                          )}
                        </div>
                        <small className="text-muted">{description}</small>
                      </div>
                      <div style={{ fontSize: '2.4rem' }}>{icon}</div>
                    </div>
                  </div>
                </Link>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Recent Complaints Section */}
      <div className="card border-0 shadow-sm">
        <div className="card-header bg-white border-bottom py-3 d-flex justify-content-between align-items-center">
          <h5 className="mb-0 fw-bold text-dark">Recent Submissions</h5>
          <Link
            to="/admin/complaints"
            className="text-primary fw-semibold small text-decoration-none"
          >
            View All Complaints →
          </Link>
        </div>

        <div className="card-body p-0">
          {loading ? (
            <div className="text-center py-5">
              <div className="spinner-border text-primary" role="status">
                <span className="visually-hidden">Loading recent complaints...</span>
              </div>
            </div>
          ) : recentComplaints.length === 0 ? (
            <div className="text-center py-5 px-3">
              <div style={{ fontSize: '3rem' }} className="mb-2">
                📂
              </div>
              <h6 className="fw-bold text-dark">No complaints logged yet</h6>
              <p className="text-muted small mb-0">
                When students submit issues, they will appear here for review.
              </p>
            </div>
          ) : (
            <div className="table-responsive">
              <table className="table table-hover align-middle mb-0">
                <thead className="table-light">
                  <tr className="small text-muted text-uppercase">
                    <th scope="col">Ticket #</th>
                    <th scope="col">Title</th>
                    <th scope="col">Student</th>
                    <th scope="col">Category</th>
                    <th scope="col">Priority</th>
                    <th scope="col">Status</th>
                    <th scope="col">Submitted</th>
                    <th scope="col" className="text-end">Action</th>
                  </tr>
                </thead>
                <tbody>
                  {recentComplaints.map((c) => (
                    <tr key={c._id}>
                      <td>
                        <span className="fw-bold font-monospace text-primary">
                          {c.ticketNumber}
                        </span>
                      </td>
                      <td>
                        <span
                          className="fw-semibold text-dark text-truncate d-inline-block"
                          style={{ maxWidth: '240px' }}
                        >
                          {c.title}
                        </span>
                        {c.location && (
                          <small className="text-muted d-block">
                            📍 {c.location}
                          </small>
                        )}
                      </td>
                      <td>
                        <div className="fw-semibold text-dark small">
                          {c.createdBy?.name || 'Unknown Student'}
                        </div>
                        <small className="text-muted">
                          {c.createdBy?.email || '—'}
                        </small>
                      </td>
                      <td>
                        <span className="badge bg-light text-dark border">
                          {c.category}
                        </span>
                      </td>
                      <td>
                        <ComplaintPriorityBadge priority={c.priority} />
                      </td>
                      <td>
                        <ComplaintStatusBadge status={c.status} />
                      </td>
                      <td className="small text-muted">
                        {new Date(c.createdAt).toLocaleDateString('en-IN', {
                          day: '2-digit',
                          month: 'short',
                        })}
                      </td>
                      <td className="text-end">
                        <Link
                          to={`/admin/complaints/${c._id}`}
                          className="btn btn-outline-primary btn-sm fw-semibold"
                        >
                          Manage
                        </Link>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;

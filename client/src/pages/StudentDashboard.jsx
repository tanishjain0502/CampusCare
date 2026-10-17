import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { getMyComplaintStats, getMyComplaints } from '../services/complaintService';
import ComplaintStatusBadge from '../components/ComplaintStatusBadge';
import ComplaintPriorityBadge from '../components/ComplaintPriorityBadge';

const StudentDashboard = () => {
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
          getMyComplaintStats(),
          getMyComplaints({ limit: 5, sort: 'newest' }),
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
            'Unable to load complaint data. Please try refreshing.'
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
      description: 'Submitted across all categories',
    },
    {
      label: 'Pending',
      value: stats.submitted,
      color: 'warning',
      icon: '⏳',
      description: 'Awaiting admin review',
    },
    {
      label: 'In Progress',
      value: stats.inProgress,
      color: 'info',
      icon: '🔄',
      description: 'Under investigation',
    },
    {
      label: 'Resolved',
      value: stats.resolved,
      color: 'success',
      icon: '✅',
      description: 'Addressed and closed',
    },
  ];

  return (
    <div className="container py-5">
      {/* Welcome header + Prominent Action */}
      <div className="d-flex flex-wrap justify-content-between align-items-center mb-4 gap-3">
        <div>
          <h1 className="fw-bold text-primary mb-1">Student Dashboard</h1>
          <p className="text-muted mb-0">
            Welcome back, <strong>{user?.name}</strong>! Submit and track your campus concerns.
          </p>
        </div>
        <Link
          to="/student/complaints/new"
          className="btn btn-primary btn-lg fw-semibold px-4 shadow-sm"
        >
          ➕ Submit a Complaint
        </Link>
      </div>

      {error && (
        <div className="alert alert-danger py-3 mb-4" role="alert">
          {error}
        </div>
      )}

      {/* Profile & Live Stats Row */}
      <div className="row g-4 mb-4">
        {/* Profile Card */}
        <div className="col-lg-4">
          <div className="card border-0 shadow-sm h-100">
            <div className="card-body p-4">
              <h5 className="fw-bold text-primary mb-3">👤 My Profile</h5>
              <dl className="mb-0 small">
                <dt className="text-muted">Name</dt>
                <dd className="fw-semibold mb-2">{user?.name}</dd>
                <dt className="text-muted">Email</dt>
                <dd className="fw-semibold mb-2">{user?.email}</dd>
                <dt className="text-muted">Role</dt>
                <dd className="mb-2">
                  <span className="badge bg-primary">{user?.role}</span>
                </dd>
                <dt className="text-muted">Member since</dt>
                <dd className="fw-semibold mb-0">
                  {user?.createdAt
                    ? new Date(user.createdAt).toLocaleDateString('en-IN', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric',
                      })
                    : '—'}
                </dd>
              </dl>
              <hr className="my-3" />
              <Link to="/student/complaints" className="btn btn-outline-primary btn-sm w-100 fw-semibold">
                View All My Complaints →
              </Link>
            </div>
          </div>
        </div>

        {/* Live Statistics Cards */}
        <div className="col-lg-8">
          <div className="row g-3">
            {statCards.map(({ label, value, color, icon }) => (
              <div key={label} className="col-sm-6">
                <div className={`card border-0 shadow-sm border-start border-${color} border-4 h-100`}>
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
                    </div>
                    <div style={{ fontSize: '2.2rem' }}>{icon}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Recent Complaints Section */}
      <div className="card border-0 shadow-sm">
        <div className="card-header bg-white border-bottom py-3 d-flex justify-content-between align-items-center">
          <h5 className="mb-0 fw-bold text-dark">📋 Recent Complaints</h5>
          <Link to="/student/complaints" className="text-primary fw-semibold small text-decoration-none">
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
              <h6 className="fw-bold text-dark">No complaints submitted yet</h6>
              <p className="text-muted small mb-3">
                Need help with a classroom, lab, or hostel issue? Let administrators know.
              </p>
              <Link to="/student/complaints/new" className="btn btn-primary btn-sm px-4">
                Submit Your First Complaint
              </Link>
            </div>
          ) : (
            <div className="table-responsive">
              <table className="table table-hover align-middle mb-0">
                <thead className="table-light">
                  <tr className="small text-muted text-uppercase">
                    <th scope="col">Ticket #</th>
                    <th scope="col">Title</th>
                    <th scope="col">Category</th>
                    <th scope="col">Priority</th>
                    <th scope="col">Status</th>
                    <th scope="col">Date</th>
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
                        <span className="fw-semibold text-dark text-truncate d-inline-block" style={{ maxWidth: '250px' }}>
                          {c.title}
                        </span>
                        {c.location && (
                          <small className="text-muted d-block">
                            📍 {c.location}
                          </small>
                        )}
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
                          to={`/student/complaints/${c._id}`}
                          className="btn btn-outline-primary btn-sm fw-semibold"
                        >
                          View
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

export default StudentDashboard;

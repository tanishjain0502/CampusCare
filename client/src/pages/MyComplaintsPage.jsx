import { useState, useEffect, useCallback } from 'react';
import { Link } from 'react-router-dom';
import {
  COMPLAINT_CATEGORIES,
  COMPLAINT_STATUSES,
} from '../constants/complaintConstants';
import { getMyComplaints } from '../services/complaintService';
import ComplaintStatusBadge from '../components/ComplaintStatusBadge';
import ComplaintPriorityBadge from '../components/ComplaintPriorityBadge';
import EmptyState from '../components/EmptyState';

const MyComplaintsPage = () => {
  const [complaints, setComplaints] = useState([]);
  const [pagination, setPagination] = useState({
    page: 1,
    limit: 10,
    total: 0,
    totalPages: 1,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Filters state
  const [searchTerm, setSearchTerm] = useState('');
  const [statusFilter, setStatusFilter] = useState('');
  const [categoryFilter, setCategoryFilter] = useState('');
  const [sortBy, setSortBy] = useState('newest');
  const [page, setPage] = useState(1);

  const fetchComplaints = useCallback(async () => {
    setLoading(true);
    setError('');

    try {
      const params = {
        page,
        limit: 10,
        sort: sortBy,
      };

      if (searchTerm.trim()) {
        params.search = searchTerm.trim();
      }
      if (statusFilter) {
        params.status = statusFilter;
      }
      if (categoryFilter) {
        params.category = categoryFilter;
      }

      const res = await getMyComplaints(params);
      setComplaints(res.data.complaints || []);
      setPagination(res.data.pagination || { page: 1, limit: 10, total: 0, totalPages: 1 });
    } catch (err) {
      setError(
        err.response?.data?.message ||
          'Failed to load complaints. Please refresh the page.'
      );
    } finally {
      setLoading(false);
    }
  }, [page, sortBy, statusFilter, categoryFilter, searchTerm]);

  useEffect(() => {
    fetchComplaints();
  }, [fetchComplaints]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    setPage(1); // Reset to first page on search
    fetchComplaints();
  };

  const handleResetFilters = () => {
    setSearchTerm('');
    setStatusFilter('');
    setCategoryFilter('');
    setSortBy('newest');
    setPage(1);
  };

  const isFiltered = searchTerm || statusFilter || categoryFilter || sortBy !== 'newest';

  return (
    <div className="container py-5">
      {/* Header with Title and Submit CTA */}
      <div className="d-flex flex-wrap justify-content-between align-items-center mb-4 gap-3">
        <div>
          <h1 className="fw-bold text-primary mb-1">My Complaints</h1>
          <p className="text-muted mb-0">
            Track and monitor the progress of all your submitted complaints.
          </p>
        </div>
        <Link to="/student/complaints/new" className="btn btn-primary fw-semibold px-4 py-2">
          ➕ Submit New Complaint
        </Link>
      </div>

      {/* Filter and Search Bar */}
      <div className="card border-0 shadow-sm mb-4">
        <div className="card-body p-3 p-md-4">
          <form onSubmit={handleSearchSubmit}>
            <div className="row g-3 align-items-end">
              {/* Search */}
              <div className="col-lg-4 col-md-6">
                <label htmlFor="search" className="form-label small fw-semibold text-muted mb-1">
                  Search
                </label>
                <div className="input-group">
                  <span className="input-group-text bg-white border-end-0">🔍</span>
                  <input
                    id="search"
                    type="text"
                    className="form-control border-start-0"
                    placeholder="Search by ticket # or title..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                  />
                </div>
              </div>

              {/* Status Filter */}
              <div className="col-lg-2 col-md-3 col-6">
                <label htmlFor="status" className="form-label small fw-semibold text-muted mb-1">
                  Status
                </label>
                <select
                  id="status"
                  className="form-select"
                  value={statusFilter}
                  onChange={(e) => {
                    setStatusFilter(e.target.value);
                    setPage(1);
                  }}
                >
                  <option value="">All Statuses</option>
                  {COMPLAINT_STATUSES.map((st) => (
                    <option key={st} value={st}>
                      {st.replace('_', ' ')}
                    </option>
                  ))}
                </select>
              </div>

              {/* Category Filter */}
              <div className="col-lg-3 col-md-3 col-6">
                <label htmlFor="category" className="form-label small fw-semibold text-muted mb-1">
                  Category
                </label>
                <select
                  id="category"
                  className="form-select"
                  value={categoryFilter}
                  onChange={(e) => {
                    setCategoryFilter(e.target.value);
                    setPage(1);
                  }}
                >
                  <option value="">All Categories</option>
                  {COMPLAINT_CATEGORIES.map((cat) => (
                    <option key={cat} value={cat}>
                      {cat}
                    </option>
                  ))}
                </select>
              </div>

              {/* Sort Order */}
              <div className="col-lg-2 col-md-6 col-6">
                <label htmlFor="sort" className="form-label small fw-semibold text-muted mb-1">
                  Sort By
                </label>
                <select
                  id="sort"
                  className="form-select"
                  value={sortBy}
                  onChange={(e) => {
                    setSortBy(e.target.value);
                    setPage(1);
                  }}
                >
                  <option value="newest">Newest First</option>
                  <option value="oldest">Oldest First</option>
                </select>
              </div>

              {/* Reset Button */}
              <div className="col-lg-1 col-md-6 col-6 text-end">
                {isFiltered && (
                  <button
                    type="button"
                    className="btn btn-outline-secondary w-100"
                    onClick={handleResetFilters}
                    title="Reset all filters"
                  >
                    Reset
                  </button>
                )}
              </div>
            </div>
          </form>
        </div>
      </div>

      {/* Error alert */}
      {error && (
        <div className="alert alert-danger py-3 mb-4" role="alert">
          {error}
        </div>
      )}

      {/* Loading state */}
      {loading ? (
        <div className="text-center py-5">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading complaints...</span>
          </div>
          <p className="text-muted mt-2">Loading your complaints...</p>
        </div>
      ) : complaints.length === 0 ? (
        isFiltered ? (
          <EmptyState
            icon="🔎"
            title="No Matching Complaints"
            message="No complaints found matching your search or filter criteria. Try adjusting or resetting filters."
            actionText="Clear All Filters"
            onActionClick={handleResetFilters}
          />
        ) : (
          <EmptyState
            icon="📝"
            title="No Complaints Submitted Yet"
            message="You haven't submitted any complaints yet. If you have an issue on campus, let us know!"
            actionText="Submit Your First Complaint"
            actionLink="/student/complaints/new"
          />
        )
      ) : (
        <>
          {/* Complaints Table (Desktop) / Cards (Mobile) */}
          <div className="card border-0 shadow-sm mb-4">
            <div className="table-responsive">
              <table className="table table-hover align-middle mb-0">
                <thead className="table-light">
                  <tr className="small text-muted text-uppercase">
                    <th scope="col" style={{ width: '16%' }}>Ticket #</th>
                    <th scope="col" style={{ width: '28%' }}>Title</th>
                    <th scope="col" style={{ width: '15%' }}>Category</th>
                    <th scope="col" style={{ width: '10%' }}>Priority</th>
                    <th scope="col" style={{ width: '13%' }}>Status</th>
                    <th scope="col" style={{ width: '10%' }}>Submitted</th>
                    <th scope="col" className="text-end" style={{ width: '8%' }}>Action</th>
                  </tr>
                </thead>
                <tbody>
                  {complaints.map((c) => (
                    <tr key={c._id}>
                      <td>
                        <span className="fw-bold font-monospace text-primary">
                          {c.ticketNumber}
                        </span>
                      </td>
                      <td>
                        <div className="fw-semibold text-dark text-truncate" style={{ maxWidth: '300px' }}>
                          {c.title}
                        </div>
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
                          year: 'numeric',
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

            {/* Pagination footer */}
            <div className="card-footer bg-white border-0 py-3 d-flex flex-wrap justify-content-between align-items-center gap-2">
              <small className="text-muted">
                Showing {complaints.length} of {pagination.total} complaints (Page {pagination.page} of {pagination.totalPages})
              </small>

              {pagination.totalPages > 1 && (
                <nav aria-label="Complaint navigation">
                  <ul className="pagination pagination-sm mb-0">
                    <li className={`page-item ${pagination.page <= 1 ? 'disabled' : ''}`}>
                      <button
                        className="page-link"
                        onClick={() => setPage((p) => Math.max(1, p - 1))}
                        disabled={pagination.page <= 1}
                      >
                        Previous
                      </button>
                    </li>
                    {Array.from({ length: pagination.totalPages }, (_, i) => i + 1).map((p) => (
                      <li
                        key={p}
                        className={`page-item ${p === pagination.page ? 'active' : ''}`}
                      >
                        <button className="page-link" onClick={() => setPage(p)}>
                          {p}
                        </button>
                      </li>
                    ))}
                    <li
                      className={`page-item ${
                        pagination.page >= pagination.totalPages ? 'disabled' : ''
                      }`}
                    >
                      <button
                        className="page-link"
                        onClick={() => setPage((p) => Math.min(pagination.totalPages, p + 1))}
                        disabled={pagination.page >= pagination.totalPages}
                      >
                        Next
                      </button>
                    </li>
                  </ul>
                </nav>
              )}
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default MyComplaintsPage;

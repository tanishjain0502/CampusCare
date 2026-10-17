import { useState, useEffect, useCallback } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import {
  COMPLAINT_CATEGORIES,
  COMPLAINT_STATUSES,
  COMPLAINT_PRIORITIES,
} from '../constants/complaintConstants';
import { getAllComplaintsAdmin } from '../services/complaintService';
import ComplaintStatusBadge from '../components/ComplaintStatusBadge';
import ComplaintPriorityBadge from '../components/ComplaintPriorityBadge';
import EmptyState from '../components/EmptyState';

const AdminComplaintsPage = () => {
  const [searchParams, setSearchParams] = useSearchParams();

  const [complaints, setComplaints] = useState([]);
  const [pagination, setPagination] = useState({
    page: 1,
    limit: 10,
    total: 0,
    totalPages: 1,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Filters state initialized from URL query params if present
  const [searchTerm, setSearchTerm] = useState(searchParams.get('search') || '');
  const [statusFilter, setStatusFilter] = useState(searchParams.get('status') || '');
  const [categoryFilter, setCategoryFilter] = useState(searchParams.get('category') || '');
  const [priorityFilter, setPriorityFilter] = useState(searchParams.get('priority') || '');
  const [sortBy, setSortBy] = useState(searchParams.get('sort') || 'newest');
  const [page, setPage] = useState(parseInt(searchParams.get('page'), 10) || 1);

  const fetchComplaints = useCallback(async () => {
    setLoading(true);
    setError('');

    try {
      const params = {
        page,
        limit: 10,
        sort: sortBy,
      };

      if (searchTerm.trim()) params.search = searchTerm.trim();
      if (statusFilter) params.status = statusFilter;
      if (categoryFilter) params.category = categoryFilter;
      if (priorityFilter) params.priority = priorityFilter;

      const res = await getAllComplaintsAdmin(params);
      setComplaints(res.data.complaints || []);
      setPagination(
        res.data.pagination || { page: 1, limit: 10, total: 0, totalPages: 1 }
      );

      // Keep URL search params in sync
      const newParams = {};
      if (searchTerm.trim()) newParams.search = searchTerm.trim();
      if (statusFilter) newParams.status = statusFilter;
      if (categoryFilter) newParams.category = categoryFilter;
      if (priorityFilter) newParams.priority = priorityFilter;
      if (sortBy !== 'newest') newParams.sort = sortBy;
      if (page > 1) newParams.page = page;
      setSearchParams(newParams, { replace: true });
    } catch (err) {
      setError(
        err.response?.data?.message ||
          'Failed to load complaints. Please refresh the page.'
      );
    } finally {
      setLoading(false);
    }
  }, [page, sortBy, statusFilter, categoryFilter, priorityFilter, searchTerm, setSearchParams]);

  useEffect(() => {
    fetchComplaints();
  }, [fetchComplaints]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    setPage(1);
    fetchComplaints();
  };

  const handleResetFilters = () => {
    setSearchTerm('');
    setStatusFilter('');
    setCategoryFilter('');
    setPriorityFilter('');
    setSortBy('newest');
    setPage(1);
    setSearchParams({}, { replace: true });
  };

  const isFiltered =
    searchTerm || statusFilter || categoryFilter || priorityFilter || sortBy !== 'newest';

  return (
    <div className="container py-5">
      {/* Header */}
      <div className="d-flex flex-wrap justify-content-between align-items-center mb-4 gap-3">
        <div>
          <h1 className="fw-bold text-primary mb-1">Complaint Management</h1>
          <p className="text-muted mb-0">
            Review, investigate, assign, and resolve student complaints across campus.
          </p>
        </div>
        <Link to="/admin/dashboard" className="btn btn-outline-secondary fw-semibold">
          ← Back to Dashboard
        </Link>
      </div>

      {/* Filter and Search Bar */}
      <div className="card border-0 shadow-sm mb-4">
        <div className="card-body p-3 p-md-4">
          <form onSubmit={handleSearchSubmit}>
            <div className="row g-3 align-items-end">
              {/* Keyword Search */}
              <div className="col-lg-3 col-md-6">
                <label htmlFor="search" className="form-label small fw-semibold text-muted mb-1">
                  Search
                </label>
                <div className="input-group">
                  <span className="input-group-text bg-white border-end-0">🔍</span>
                  <input
                    id="search"
                    type="text"
                    className="form-control border-start-0"
                    placeholder="Ticket #, title, or student..."
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

              {/* Priority Filter */}
              <div className="col-lg-2 col-md-4 col-6">
                <label htmlFor="priority" className="form-label small fw-semibold text-muted mb-1">
                  Priority
                </label>
                <select
                  id="priority"
                  className="form-select"
                  value={priorityFilter}
                  onChange={(e) => {
                    setPriorityFilter(e.target.value);
                    setPage(1);
                  }}
                >
                  <option value="">All Priorities</option>
                  {COMPLAINT_PRIORITIES.map((pr) => (
                    <option key={pr} value={pr}>
                      {pr}
                    </option>
                  ))}
                </select>
              </div>

              {/* Sort Order */}
              <div className="col-lg-1 col-md-4 col-6">
                <label htmlFor="sort" className="form-label small fw-semibold text-muted mb-1">
                  Sort
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
                  <option value="newest">New</option>
                  <option value="oldest">Old</option>
                </select>
              </div>

              {/* Reset Action */}
              <div className="col-lg-1 col-md-4 col-12 text-end">
                {isFiltered && (
                  <button
                    type="button"
                    className="btn btn-outline-secondary w-100"
                    onClick={handleResetFilters}
                    title="Clear all filters"
                  >
                    Reset
                  </button>
                )}
              </div>
            </div>
          </form>
        </div>
      </div>

      {error && (
        <div className="alert alert-danger py-3 mb-4" role="alert">
          {error}
        </div>
      )}

      {/* Complaints List Table */}
      {loading ? (
        <div className="text-center py-5">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading complaints...</span>
          </div>
          <p className="text-muted mt-2">Loading complaints database...</p>
        </div>
      ) : complaints.length === 0 ? (
        <EmptyState
          icon={isFiltered ? '🔎' : '📂'}
          title={isFiltered ? 'No Matching Complaints' : 'No Complaints Recorded'}
          message={
            isFiltered
              ? 'No complaints found matching the selected search or filter criteria.'
              : 'There are currently no complaints in the system.'
          }
          actionText={isFiltered ? 'Clear Filters' : undefined}
          onActionClick={isFiltered ? handleResetFilters : undefined}
        />
      ) : (
        <div className="card border-0 shadow-sm mb-4">
          <div className="table-responsive">
            <table className="table table-hover align-middle mb-0">
              <thead className="table-light">
                <tr className="small text-muted text-uppercase">
                  <th scope="col" style={{ width: '15%' }}>Ticket #</th>
                  <th scope="col" style={{ width: '23%' }}>Title</th>
                  <th scope="col" style={{ width: '18%' }}>Student Info</th>
                  <th scope="col" style={{ width: '13%' }}>Category</th>
                  <th scope="col" style={{ width: '9%' }}>Priority</th>
                  <th scope="col" style={{ width: '11%' }}>Status</th>
                  <th scope="col" style={{ width: '11%' }}>Dates</th>
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
                      <div className="fw-semibold text-dark text-truncate" style={{ maxWidth: '240px' }}>
                        {c.title}
                      </div>
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
                      <small className="text-muted text-truncate d-block" style={{ maxWidth: '170px' }}>
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
                      <div>
                        <strong>Sub:</strong>{' '}
                        {new Date(c.createdAt).toLocaleDateString('en-IN', {
                          day: '2-digit',
                          month: 'short',
                        })}
                      </div>
                      <div>
                        <strong>Upd:</strong>{' '}
                        {new Date(c.updatedAt).toLocaleDateString('en-IN', {
                          day: '2-digit',
                          month: 'short',
                        })}
                      </div>
                    </td>
                    <td className="text-end">
                      <Link
                        to={`/admin/complaints/${c._id}`}
                        className="btn btn-primary btn-sm fw-semibold"
                      >
                        Manage
                      </Link>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {/* Pagination Footer */}
          <div className="card-footer bg-white border-0 py-3 d-flex flex-wrap justify-content-between align-items-center gap-2">
            <small className="text-muted">
              Showing {complaints.length} of {pagination.total} complaints (Page {pagination.page} of {pagination.totalPages})
            </small>

            {pagination.totalPages > 1 && (
              <nav aria-label="Complaints pagination">
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
      )}
    </div>
  );
};

export default AdminComplaintsPage;

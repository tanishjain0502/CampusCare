import { Link } from 'react-router-dom';

const UnauthorizedPage = () => {
  return (
    <div className="container py-5 text-center">
      <div style={{ fontSize: '5rem' }} className="mb-3">🚫</div>
      <h1 className="fw-bold text-danger mb-2">Access Denied</h1>
      <p className="text-muted lead mb-4">
        You do not have permission to view this page.
      </p>
      <div className="d-flex gap-3 justify-content-center">
        <Link to="/" className="btn btn-primary">
          Go to Home
        </Link>
        <Link to="/login" className="btn btn-outline-secondary">
          Login with a Different Account
        </Link>
      </div>
    </div>
  );
};

export default UnauthorizedPage;

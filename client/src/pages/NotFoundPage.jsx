import { Link } from 'react-router-dom';

const NotFoundPage = () => {
  return (
    <div className="container py-5 text-center">
      <div style={{ fontSize: '5rem' }} className="mb-3">🔍</div>
      <h1 className="fw-bold text-primary mb-2">404 — Page Not Found</h1>
      <p className="text-muted lead mb-4">
        The page you are looking for does not exist or has been moved.
      </p>
      <Link to="/" className="btn btn-primary px-4">
        Back to Home
      </Link>
    </div>
  );
};

export default NotFoundPage;

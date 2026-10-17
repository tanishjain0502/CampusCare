import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

/**
 * ProtectedRoute
 * --------------
 * Guards a route that requires:
 *   1. The user to be authenticated.
 *   2. (Optionally) the user to have a specific role.
 *
 * Props:
 *   children  — the component(s) to render if access is granted
 *   role      — (optional) required role string, e.g. 'ADMIN' or 'STUDENT'
 *
 * Security note:
 *   This is a UX convenience that prevents unnecessary navigation.
 *   All sensitive data must ALSO be protected at the backend level with
 *   the protect and restrictTo middleware, because client-side guards
 *   can be bypassed by manipulating the browser.
 */
const ProtectedRoute = ({ children, role }) => {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center" style={{ minHeight: '60vh' }}>
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading…</span>
        </div>
      </div>
    );
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  if (role && user.role !== role) {
    return <Navigate to="/unauthorized" replace />;
  }

  return children;
};

export default ProtectedRoute;

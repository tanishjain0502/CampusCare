import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const HomePage = () => {
  const { user } = useAuth();

  return (
    <>
      {/* Hero section */}
      <section className="bg-primary text-white py-5">
        <div className="container py-4">
          <div className="row align-items-center">
            <div className="col-lg-7">
              <h1 className="display-4 fw-bold mb-3">
                Welcome to CampusCare
              </h1>
              <p className="lead mb-4">
                A streamlined complaint management system for students and administrators.
                Submit, track and resolve college-related concerns — all in one place.
              </p>
              {user ? (
                <Link
                  to={user.role === 'ADMIN' ? '/admin/dashboard' : '/student/dashboard'}
                  className="btn btn-light btn-lg fw-semibold text-primary"
                >
                  Go to Dashboard →
                </Link>
              ) : (
                <div className="d-flex gap-3 flex-wrap">
                  <Link to="/register" className="btn btn-light btn-lg fw-semibold text-primary">
                    Get Started
                  </Link>
                  <Link to="/login" className="btn btn-outline-light btn-lg">
                    Login
                  </Link>
                </div>
              )}
            </div>
            <div className="col-lg-5 text-center mt-4 mt-lg-0">
              <div style={{ fontSize: '8rem', lineHeight: 1 }}>🎓</div>
            </div>
          </div>
        </div>
      </section>

      {/* Features section */}
      <section className="py-5 bg-light">
        <div className="container">
          <h2 className="text-center fw-bold mb-5 text-primary">How It Works</h2>
          <div className="row g-4">
            {[
              {
                icon: '📝',
                title: 'Submit a Complaint',
                text: 'Students can easily submit complaints about academic, infrastructure or other campus issues.',
              },
              {
                icon: '🔍',
                title: 'Track Progress',
                text: 'Monitor the status of your complaints in real time through your personal dashboard.',
              },
              {
                icon: '✅',
                title: 'Get it Resolved',
                text: 'Administrators review, act on and close complaints efficiently, keeping students informed.',
              },
            ].map(({ icon, title, text }) => (
              <div key={title} className="col-md-4">
                <div className="card h-100 border-0 shadow-sm text-center p-4">
                  <div style={{ fontSize: '3rem' }} className="mb-3">{icon}</div>
                  <h5 className="fw-bold text-primary">{title}</h5>
                  <p className="text-muted mb-0">{text}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA section */}
      {!user && (
        <section className="py-5">
          <div className="container text-center">
            <h2 className="fw-bold mb-3">Ready to get started?</h2>
            <p className="text-muted mb-4">
              Create your student account today and take control of your campus experience.
            </p>
            <Link to="/register" className="btn btn-primary btn-lg px-5">
              Register as a Student
            </Link>
          </div>
        </section>
      )}
    </>
  );
};

export default HomePage;

import { Link } from 'react-router-dom';

const EmptyState = ({
  icon = '📋',
  title = 'No Complaints Found',
  message = 'You have not submitted any complaints yet.',
  actionText,
  actionLink,
  onActionClick,
}) => {
  return (
    <div className="card border-0 shadow-sm text-center py-5 px-3">
      <div className="card-body">
        <div style={{ fontSize: '3.5rem' }} className="mb-3">
          {icon}
        </div>
        <h4 className="fw-bold text-dark mb-2">{title}</h4>
        <p className="text-muted mx-auto mb-4" style={{ maxWidth: '450px' }}>
          {message}
        </p>
        {actionLink && actionText && (
          <Link to={actionLink} className="btn btn-primary fw-semibold px-4">
            {actionText}
          </Link>
        )}
        {onActionClick && actionText && !actionLink && (
          <button
            type="button"
            className="btn btn-outline-primary fw-semibold px-4"
            onClick={onActionClick}
          >
            {actionText}
          </button>
        )}
      </div>
    </div>
  );
};

export default EmptyState;

import { STATUS_META } from '../constants/complaintConstants';

const ComplaintStatusBadge = ({ status }) => {
  const meta = STATUS_META[status] || {
    label: status || 'Unknown',
    badgeClass: 'bg-secondary',
  };

  return (
    <span className={`badge ${meta.badgeClass} px-2 py-1 fw-semibold`}>
      {meta.icon && <span className="me-1">{meta.icon}</span>}
      {meta.label}
    </span>
  );
};

export default ComplaintStatusBadge;

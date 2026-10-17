import { PRIORITY_META } from '../constants/complaintConstants';

const ComplaintPriorityBadge = ({ priority }) => {
  const meta = PRIORITY_META[priority] || {
    label: priority || 'Medium',
    badgeClass: 'bg-secondary',
  };

  return (
    <span className={`badge ${meta.badgeClass} px-2 py-1`}>
      {meta.label}
    </span>
  );
};

export default ComplaintPriorityBadge;

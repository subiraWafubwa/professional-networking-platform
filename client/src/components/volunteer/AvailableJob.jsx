import "../../index.css";

export default function AvailableJob({
  title,
  description,
  date,
  maxHoursRequired,
  status,
}) {
  return (
    <div className="job-card">
      <div className="job-header">
        <p className="job-title">{title}</p>
        <button className="status-btn">{status}</button>
      </div>
      <p className="job-description">{description}</p>
      <p className="job-details">
        <span>Date: {date}</span> •{" "}
        <span>Maximum Hours required: {maxHoursRequired}</span>
      </p>
    </div>
  );
}

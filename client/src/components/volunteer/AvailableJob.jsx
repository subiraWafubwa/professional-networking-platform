import "../../index.css";

export default function AvailableJob({
  title,
  description,
  date,
  maxHoursRequired,
  status,
}) {
  const isPending = true;

  return (
    <div className="job-card">
      <div className="job-header">
        <p className="job-title">{title}</p>
      </div>
      <p className="job-description">{description}</p>
      <p className="job-details">
        <span>Date: {date}</span> •{" "}
        <span>Maximum Hours required: {maxHoursRequired}</span>
      </p>
      <button
        className="approve-btn"
        disabled={isPending}
        style={{ backgroundColor: "darkgray", color: "white", width: "150px" }}
      >
        {status}
      </button>
    </div>
  );
}

import "../../index.css";

export default function JobApplication({
  title,
  description,
  date,
  hoursRequired,
}) {
  return (
    <div className="job-card">
      <p className="job-title">{title}</p>
      <p className="job-description">{description}</p>
      <p className="job-details">
        Date: {date} •{" "}
        <span className="job-hours">
          Maximum Hours required: {hoursRequired}
        </span>
      </p>
      <div className="button-group">
        <button className="mark-completed-btn">Mark Completed</button>
        <button className="delete-btn">DELETE</button>
      </div>
    </div>
  );
}

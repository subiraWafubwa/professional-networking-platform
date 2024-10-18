import "../../index.css";

export default function ApprovedJob({
  title,
  description,
  date,
  hoursWorked,
  hoursRequired,
}) {
  return (
    <div className="job-card">
      <p className="job-title">{title}</p>
      <p className="job-description">{description}</p>
      <p className="job-details">
        <span>Date: {date}</span> •{" "}
        <span>
          Hours Worked: {hoursWorked}/{hoursRequired}
        </span>
      </p>
      <button className="approve-btn">Append Hours</button>
    </div>
  );
}

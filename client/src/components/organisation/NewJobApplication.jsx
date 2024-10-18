import "../../index.css";

export default function NewJobApplication({
  applicantName,
  jobTitle,
  date,
  rating,
}) {
  return (
    <div className="new-job-card">
      <p className="applicant-name">{applicantName}</p>
      <p className="job-apply-for">
        <strong>Job applying for:</strong> {jobTitle}
      </p>
      <p className="job-details">
        Date: {date} •{" "}
        <span className="job-rating">Overall Rating: {rating}</span>
      </p>
      <div className="button-group">
        <button className="approve-btn">APPROVE</button>
        <button className="reject-btn">REJECT</button>
      </div>
    </div>
  );
}

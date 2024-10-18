import "../../index.css";
import up from "../../../assets/up.png";
import down from "../../../assets/down.png";
import JobApplication from "../organisation/JobApplication";
import AccountContext from "../context/AccountContext";
import { useContext } from "react";
import NewJobApplication from "../organisation/NewJobApplication";
import ApprovedJob from "../volunteer/ApprovedJob";
import AvailableJob from "../volunteer/AvailableJob";

export default function Toggle({
  setState,
  state,
  pValue,
  list,
  listCount,
  object,
}) {
  const accountType = useContext(AccountContext);

  return (
    <div className="book-section">
      <button className="toggle-button" onClick={() => setState(!state)}>
        <p>
          {pValue} ({listCount})
        </p>
        <img src={state ? up : down} />
      </button>

      {state && (
        <div className="list-container">
          {list.length > 0 && accountType == "volunteer" ? (
            list.map((item) => {
              item;
            })
          ) : accountType == "organization" && object == "JobCreated" ? (
            <JobApplication
              title="Product/process development scientist"
              description="Represent focus yourself assume always enjoy. Crime talk people. Star stay rise time."
              date="today"
              hoursRequired="6"
            />
          ) : accountType == "organization" && object == "NewJobApplication" ? (
            <NewJobApplication
              applicantName="John"
              jobTitle="mechanic"
              date="today"
              rating="5"
            />
          ) : accountType == "volunteer" && object == "ApprovedJob" ? (
            <ApprovedJob
              title="Title"
              description="fgjfjf"
              date="today"
              hoursWorked="5"
              hoursRequired="7"
            />
          ) : accountType == "volunteer" && object == "AvailableJob" ? (
            <AvailableJob
              title="availablejob"
              description="desi"
              date="today"
              maxHoursRequired="89"
              status="Pending"
            />
          ) : null}
        </div>
      )}
    </div>
  );
}

import "../../index.css";
import up from "../../../assets/up.png";
import down from "../../../assets/down.png";
import JobApplication from "../organisation/JobApplication";
import AccountContext from "../context/AccountContext";
import { useContext } from "react";
import NewJobApplication from "../organisation/NewJobApplication";
import ApprovedJob from "../volunteer/ApprovedJob";
import AvailableJob from "../volunteer/AvailableJob";

export default function Toggle({ setState, state, pValue, list, listCount }) {
  const { accountType } = useContext(AccountContext);

  return (
    <div className="book-section">
      <button className="toggle-button" onClick={() => setState(!state)}>
        <p>
          {pValue} ({listCount})
        </p>
        <img src={state ? up : down} alt="toggle arrow" />
      </button>

      {state && (
        <div className="list-container">
          {list.length > 0 && accountType === "Volunteer" ? (
            list.map((item) => <div key={item.id}>{item.title}</div>)
          ) : accountType === "Organization" && object === "JobCreated" ? (
            <JobApplication
              title="Product/process development scientist"
              description="Represent focus yourself assume always enjoy. Crime talk people. Star stay rise time."
              date="today"
              hoursRequired="6"
            />
          ) : accountType === "Organization" &&
            object === "NewJobApplication" ? (
            <NewJobApplication
              applicantName="John"
              jobTitle="mechanic"
              date="today"
              rating="5"
            />
          ) : accountType === "Volunteer" && object === "ApprovedJob" ? (
            <ApprovedJob
              title="Title"
              description="fgjfjf"
              date="today"
              hoursWorked="5"
              hoursRequired="7"
            />
          ) : accountType === "Volunteer" && object === "AvailableJob" ? (
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

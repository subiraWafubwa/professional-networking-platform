import React, { useState, useContext } from "react";
import add from "../../../assets/add.png";
import "../../index.css";
import Toggle from "./Toggle";
import AccountContext from "../context/AccountContext";
import UserToggle from "./Toggle";

export default function RightSection() {
  const accountType = useContext(AccountContext);

  const [showApprovedJobs, setShowApprovedJobs] = useState(true);
  const [showJobs, setShowJobs] = useState(true);
  const [showRejectedJobs, setShowRejectedJobs] = useState(true);

  const approvedJobs = [];
  const jobs = [];
  const rejectedJobs = [];

  const approvedJobCount = 2;
  const jobCount = 8;
  const rejectedJobCount = 3;

  return (
    <div className="right-section">
      {accountType == "volunteer" ? (
        <div className="right-section-main">
          <Toggle
            state={showApprovedJobs}
            setState={setShowApprovedJobs}
            pValue="Approved Jobs"
            list={approvedJobs}
            listCount={approvedJobCount}
            object="ApprovedJob"
          />
          <Toggle
            state={showJobs}
            setState={setShowJobs}
            pValue="Available Jobs"
            list={jobs}
            listCount={jobCount}
          />
          <Toggle
            state={showRejectedJobs}
            setState={setShowRejectedJobs}
            pValue="Rejected Jobs"
            list={rejectedJobs}
            listCount={rejectedJobCount}
          />
        </div>
      ) : accountType == "organization" ? (
        <div className="right-section-main">
          <Toggle
            state={showApprovedJobs}
            setState={setShowApprovedJobs}
            pValue="Jobs Created"
            list={approvedJobs}
            listCount={approvedJobCount}
            object="JobCreated"
          />
          <Toggle
            state={showApprovedJobs}
            setState={setShowApprovedJobs}
            pValue="Jobs Created"
            list={approvedJobs}
            listCount={approvedJobCount}
            object="NewJobApplication"
          />
        </div>
      ) : null}
      <button id="modal">
        <img src={add} alt="plus image" />
      </button>
    </div>
  );
}

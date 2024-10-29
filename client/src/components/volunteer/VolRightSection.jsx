import React, { useState } from "react";
import add from "../../../assets/add.png";
import "../../index.css";
import Toggle from "../common/Toggle";

export default function VolRightSection() {
  const [showJobsCreated, setShowJobsCreated] = useState(true);
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
          pValue="New Job Applications"
          list={approvedJobs}
          listCount={approvedJobCount}
          object="NewJobApplication"
        />
      </div>
      <button id="modal">
        <img src={add} alt="plus image" />
      </button>
    </div>
  );
}

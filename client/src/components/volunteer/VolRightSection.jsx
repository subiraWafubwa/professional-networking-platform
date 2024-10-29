import React, { useState } from "react";
import add from "../../../assets/add.png";
import "../../index.css";
import Toggle from "../common/Toggle";

export default function VolRightSection({
  availableJobs,
  approvedJobs,
  rejectedJobs,
}) {
  const [showApprovedJobs, setShowApprovedJobs] = useState(true);
  const [showJobs, setShowJobs] = useState(true);
  const [showRejectedJobs, setShowRejectedJobs] = useState(true);

  return (
    <div className="right-section">
      <div className="right-section-main">
        <Toggle
          state={showApprovedJobs}
          setState={setShowApprovedJobs}
          pValue="Jobs Created"
          list={approvedJobs}
          listCount={approvedJobs.length}
          object="JobCreated"
        />
        <Toggle
          state={showJobs}
          setState={setShowJobs}
          pValue="New Job Applications"
          list={availableJobs}
          listCount={availableJobs.length}
          object="NewJobApplication"
        />
        <Toggle
          state={showRejectedJobs}
          setState={setShowRejectedJobs}
          pValue="Rejected jobs"
          list={rejectedJobs}
          listCount={rejectedJobs.length}
          object="JobCreated"
        />
      </div>
      <button id="modal">
        <img src={add} alt="plus image" />
      </button>
    </div>
  );
}

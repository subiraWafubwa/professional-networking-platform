import Toggle from "../common/Toggle";

export default function OrganizationBody() {
  return (
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
        state={showApprovedJobs} // Consider changing the state for different Toggles
        setState={setShowApprovedJobs}
        pValue="New Job Applications"
        list={approvedJobs}
        listCount={approvedJobCount}
        object="NewJobApplication"
      />
    </div>
  );
}

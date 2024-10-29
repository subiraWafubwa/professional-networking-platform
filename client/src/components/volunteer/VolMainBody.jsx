import React, { useEffect, useState } from "react";
import VolLeftSection from "./VolLeftSection";
import VolRightSection from "./VolRightSection";
import { useLocation } from "react-router-dom";

export default function VolMainBody() {
  const location = useLocation();
  const { id } = location.state || {};
  const [volunteer, setVolunteer] = useState(null);
  const [certificates, setCertificates] = useState([]);
  const [approvedJobs, setApprovedJobs] = useState([]);
  const [rejectedJobs, setRejectedJobs] = useState([]);
  const [availableJobs, setAvailableJobs] = useState([]);

  useEffect(() => {
    if (id) {
      fetchVolunteer(id);
      fetchCertificates(id);
      fetchApprovedJobs(id);
      fetchRejectedJobs(id);
      fetchAvailableJobs(id);
    }
  }, [id]);

  async function fetchVolunteer(id) {
    try {
      const response = await fetch(`http://127.0.0.1:5555/volunteers/${id}`);
      const data = await response.json();

      if (response.ok) {
        setVolunteer(data.volunteer);
      } else {
        console.error("Failed to fetch volunteer data:", data.message);
      }
    } catch (error) {
      console.error("An error occurred while fetching volunteer data:", error);
    }
  }

  async function fetchCertificates(volunteerId) {
    try {
      const response = await fetch(
        `http://127.0.0.1:5555/certificates/${volunteerId}`
      );
      const data = await response.json();

      if (response.ok) {
        setCertificates(data.certificates);
      } else {
        console.error("Failed to fetch certificates:", data.message);
      }
    } catch (error) {
      console.error("An error occurred while fetching certificates:", error);
    }
  }

  async function fetchApprovedJobs(volunteerId) {
    try {
      const response = await fetch(
        `http://127.0.0.1:5555/job-applications/approved/${volunteerId}`
      );
      const data = await response.json();

      if (response.ok) {
        setApprovedJobs(data.approved_jobs);
      } else {
        console.error("Failed to fetch approved jobs:", data.message);
      }
    } catch (error) {
      console.error("An error occurred while fetching approved jobs:", error);
    }
  }

  async function fetchRejectedJobs(volunteerId) {
    try {
      const response = await fetch(
        `http://127.0.0.1:5555/job-applications/rejected/${volunteerId}`
      );
      const data = await response.json();

      if (response.ok) {
        setRejectedJobs(data.rejected_jobs);
      } else {
        console.error("Failed to fetch rejected jobs:", data.message);
      }
    } catch (error) {
      console.error("An error occurred while fetching rejected jobs:", error);
    }
  }

  async function fetchAvailableJobs(volunteerId) {
    try {
      const response = await fetch(`http://127.0.0.1:5555/jobs/${volunteerId}`);
      const data = await response.json();

      if (response.ok) {
        setAvailableJobs(data.jobs);
      } else {
        console.error("Failed to fetch available jobs:", data.message);
      }
    } catch (error) {
      console.error("An error occurred while fetching available jobs:", error);
    }
  }

  if (!volunteer) return <p>Loading...</p>;

  return (
    <div className="main-body">
      <VolLeftSection volunteer={volunteer} certificates={certificates} />
      <VolRightSection
        approvedJobs={approvedJobs}
        rejectedJobs={rejectedJobs}
        availableJobs={availableJobs}
      />
    </div>
  );
}

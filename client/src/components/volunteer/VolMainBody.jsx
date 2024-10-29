import React, { useEffect, useState } from "react";
import VolLeftSection from "./VolLeftSection";
import VolRightSection from "./VolRightSection";
import { useLocation } from "react-router-dom";

export default function VolMainBody() {
  const location = useLocation();
  const { id } = location.state || {};
  const [volunteer, setVolunteer] = useState(null);

  useEffect(() => {
    if (id) {
      fetchVolunteer(id);
    }
  });

  async function fetchVolunteer(id) {
    try {
      const response = await fetch(`http://127.0.0.1:5555/volunteers/${id}`);
      const data = await response.json();

      if (response.ok) {
        setVolunteer(data.volunteer);
        console.log(`Volunteer set: ${id}`);
      } else {
        console.error("Failed to fetch volunteer data:", data.message);
      }
    } catch (error) {
      console.error("An error occurred while fetching volunteer data:", error);
    }
  }

  // Remove
  if (!volunteer) return <p>Loading...</p>;

  return (
    <div className="main-body">
      <VolLeftSection volunteer={volunteer} />
      <VolRightSection />
    </div>
  );
}

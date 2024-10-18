import React from "react";
import "../../index.css";
import organizationAvatar from "../../../assets/organization.png";

export default function OrganizationProfile() {
  return (
    <div className="profile" style={{ flex: 3 }}>
      <div className="profile-avatar">
        <img
          src={organizationAvatar}
          alt="Organization Icon"
          className="avatar-img"
          style={{ float: "left" }}
        />
        <div
          style={{
            height: "60px",
            display: "flex",
            justifyContent: "center",
            alignItems: "start",
            flexDirection: "column",
          }}
        >
          <h3 className="username">Mcgee, Myers and...</h3>
          <p className="email">shawphyllis@example.com</p>
        </div>
      </div>
      <div className="profile-info">
        <p className="website">
          <strong>Website:</strong> jimenez.com
        </p>
      </div>
      <div className="profile-actions">
        <button className="button logout-btn">LOGOUT</button>
        <button className="button delete-btn">DELETE</button>
      </div>
    </div>
  );
}

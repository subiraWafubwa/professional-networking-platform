import React from "react";
import "../../index.css";
import userAvatar from "../../../assets/user.png";

export default function UserProfile({ volunteer }) {
  return (
    <div className="profile">
      <div className="profile-avatar">
        <img
          src={userAvatar}
          alt="User Avatar"
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
          <h3 className="username">{volunteer.username}</h3>
          <p className="email">{volunteer.email}</p>
        </div>
      </div>
      <div className="profile-info">
        <p className="joined-date">
          <strong>Joined:</strong> 15th October 2024
        </p>
        <p className="jobs-done">
          <strong>Jobs Done:</strong> 11
        </p>
        <p className="overall-rating">
          <strong>Overall Rating:</strong> 4.4
        </p>
      </div>
      <div className="profile-actions">
        <button className="button logout-btn">LOGOUT</button>
        <button className="button delete-btn">DELETE</button>
      </div>
    </div>
  );
}

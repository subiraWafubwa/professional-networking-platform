import React from "react";

function VolunteerSignup() {
  return (
    <div className="volunteer-sign-up">
      <h3>Sign Up as Volunteer</h3>
      <form>
        <div className="form-group">
          <input
            type="text"
            className="form-control"
            placeholder="Enter username"
          />
        </div>
        <div className="form-group">
          <input
            type="email"
            className="form-control"
            placeholder="Enter email"
          />
        </div>
        <div className="form-group">
          <input
            type="password"
            className="form-control"
            placeholder="Enter password"
          />
        </div>
        <button type=" submit" className="button">
          SignUp
        </button>
      </form>
    </div>
  );
}
export default VolunteerSignup;

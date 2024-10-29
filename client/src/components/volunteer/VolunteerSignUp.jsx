import React from "react";
import { Link } from "react-router-dom";
import logo from "../../../assets/logo.png";

function VolunteerSignup() {
  return (
    <div className="auth">
      <div className="modal-div">
        <div>
          <img
            src={logo}
            alt="logo"
            style={{
              float: "left",
              width: "30px",
              margin: "0px 10px 20px 0px",
            }}
          />
          <h2 style={{ float: "left" }}>VolunteerMS</h2>
        </div>
        <h3>Sign Up as Volunteer</h3>
        <form>
          <div className="form-group">
            <input type="text" id="input" placeholder="Enter username" />
          </div>
          <div className="form-group">
            <input type="email" id="input" placeholder="Enter email" />
          </div>
          <div className="form-group">
            <input type="password" id="input" placeholder="Enter password" />
          </div>
          <p style={{ marginTop: "25px" }}>
            <Link to="/" className="custom-link">
              Log In Instead
            </Link>{" "}
            ·{" "}
            <Link to="/organization_signup" className="custom-link">
              Sign up as organization
            </Link>
          </p>
          <button type=" submit" className="button">
            SignUp
          </button>
        </form>
      </div>
    </div>
  );
}
export default VolunteerSignup;

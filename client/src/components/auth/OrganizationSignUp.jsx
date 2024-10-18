import React from "react";
import { Link } from "react-router-dom";
import logo from "../../../assets/logo.png";

export default function OrganisationSignup() {
  return (
    <div className="auth">
      <div className="modal-div" style={{ height: "520px" }}>
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
        <h3>Sign Up as Organisation</h3>
        <form>
          <div>
            <input
              type="text"
              id="input"
              placeholder="Enter organization name"
            />
          </div>
          <div>
            <input type="email" id="input" placeholder="Enter email" />
          </div>
          <div>
            <input type="password" id="input" placeholder="Enter password" />
          </div>
          <div>
            <input type="text" id="input" placeholder="Enter website url" />
          </div>
          <p style={{ marginTop: "25px" }}>
            <Link to="/" className="custom-link">
              Log In Instead
            </Link>{" "}
            ·{" "}
            <Link to="/volunteer_signup" className="custom-link">
              Sign up as volunteer
            </Link>
          </p>
          <button type="submit" className="button">
            SignUp
          </button>
        </form>
      </div>
    </div>
  );
}

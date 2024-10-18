import React from "react";
import { Link } from "react-router-dom";
import "../../index.css";
import logo from "../../../assets/logo.png";

function Login() {
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
        <h3>Log in as Volunteer or Organisation</h3>
        <form>
          <div>
            <input
              type="text"
              id="input"
              placeholder="Enter username,organisation name or email"
            />
          </div>
          <div>
            <input type="text" id="input" placeholder="Enter password" />
          </div>
          <p style={{ marginTop: "25px" }}>
            Sign up as{" "}
            <Link to="/organization_signup" className="custom-link">
              organisation
            </Link>{" "}
            or{" "}
            <Link to="/volunteer_signup" className="custom-link">
              {" "}
              volunteer
            </Link>
          </p>
          <button
            type=" submit"
            className="button"
            style={{ marginTop: "30px" }}
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
}
export default Login;

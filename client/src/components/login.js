import React from "react";
import { Link } from "react-router-dom";

function Login() {
  return (
    <div className="login">
      <h3>Log in as Volunteer or Organisation</h3>
      <form>
        <div>
          <input
            type="text"
            className="form-control"
            placeholder="Enter username,organisation name or email"
          />
        </div>
        <div>
          <input
            type="text"
            className="form-control"
            placeholder="Enter password"
          />
        </div>
        <button type=" submit" className="button">
          Login
        </button>
      </form>
      <div>
        <p>
          Sign up as? <Link to="/organisation_signup">organisation</Link>{" "}
        </p>
        or <Link to="/volunteer_signup"> volunteer</Link>
      </div>
    </div>
  );
}
export default Login;

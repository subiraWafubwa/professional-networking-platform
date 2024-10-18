import React from "react";
import { NavLink } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  return (
    <nav>
      <ul>
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        <li>
          <NavLink to="/VolunteerCertificate">Volunteer Certificate</NavLink>
        </li>
        <li>
          <NavLink to="/GiveCertificate">Give Certificate</NavLink>
        </li>
      </ul>
    </nav>
  );
}
export default Navbar;

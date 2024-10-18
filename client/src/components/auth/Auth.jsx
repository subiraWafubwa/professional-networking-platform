import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./Login";
import OrganizationSignUp from "./OrganizationSignUp";
import VolunteerSignUp from "./VolunteerSignUp";

export default function Auth() {
  return (
    <div>
      <BrowserRouter>
        <div>
          <Routes>
            <Route path="/" element={<Login />} />
            <Route
              path="/organization_signup"
              element={<OrganizationSignUp />}
            />
            <Route path="/volunteer_signup" element={<VolunteerSignUp />} />
          </Routes>
        </div>
      </BrowserRouter>
    </div>
  );
}

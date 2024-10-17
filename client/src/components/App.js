import React, { useEffect, useState } from "react";
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import Login from "./login";
import OrganisationSignup from "./organisation_signup";
import VolunteerSignup from "./volunteer_signup";
import Navbar from "./Navbar";

function App() {
  return (
    <div>
      <BrowserRouter >
        <div>
          <Navbar />
          <Routes>
            <Route path="/" element={<Login />} />
            <Route
              path="/organisation_signup"
              element={<OrganisationSignup />}
            />
            <Route path="/volunteer_signup" element={<VolunteerSignup />} />
          </Routes>
        </div>
      {/* <OrganisationSignup />
      <VolunteerSignup /> */}
      </BrowserRouter>
      
    </div>
  );
}
export default App;

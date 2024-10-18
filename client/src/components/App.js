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
import GiveCertificate from "./GiveCertificate";
import VolunteerCertificate from "./VolunteerCertificate";

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
            <Route path="/VolunteerCertificate" element={<VolunteerCertificate/>} />
            <Route path="/GiveCertificate" element={<GiveCertificate/>} />
          </Routes>
        </div>
        
      </BrowserRouter>
      <div>
        
      </div>
    </div>
    
  );
}
export default App;

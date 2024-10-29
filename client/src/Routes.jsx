import React, { useContext } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./components/auth/Login";
import OrganizationSignUp from "./components/auth/OrganizationSignUp";
import VolunteerSignUp from "./components/auth/VolunteerSignUp";
import VolunteerBody from "./components/volunteer/VolMainBody";
import OrganizationBody from "./components/organisation/OrganizationBody";
import AccountContext from "./components/context/AccountContext";

function AppRoutes() {
  const { accountType } = useContext(AccountContext);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/organization_signup" element={<OrganizationSignUp />} />
        <Route path="/volunteer_signup" element={<VolunteerSignUp />} />
        <Route
          path="/dashboard"
          element={
            accountType === "organization" ? (
              <Navigate to="/organization" />
            ) : accountType === "volunteer" ? (
              <Navigate to="/volunteer" />
            ) : (
              <Navigate to="/" />
            )
          }
        />
        <Route path="/organization" element={<OrganizationBody />} />
        <Route path="/volunteer" element={<VolunteerBody />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;

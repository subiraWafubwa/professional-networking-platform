import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Login from "./login";
import OrganisationSignup from "./organisation_signup";
import VolunteerSignup from "./volunteer_signup";

function App() {
  return(
    <div>
       <h1>Project Client</h1>
       <Login />
       <OrganisationSignup />
       <VolunteerSignup />
    </div>
  )


}

export default App;

import React from "react";

function OrganisationSignup() {
    return(
        <div classname = 'Organisation sign up'>
            <h1>Sign Up as Organisation</h1>
            <form>
                <div>
                    <label>Username</label>
                    <input type="text"  placeholder="Enter username" />
                </div>
                <div >
                    <label>Email</label>
                    <input type="email" placeholder="Enter email" />
                </div>
                <div>
                    <label>Password</label>
                    <input type="password"  placeholder="Enter password" />
                </div>
                <div className="form-group">
                    <label>Confirm Password</label>
                    <input type="password"  placeholder="Confirm password" />
                </div>
                </form>
        </div>
    )
}
export default OrganisationSignup
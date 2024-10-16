import React from "react";

    function VolunteerSignup() {
        return (
            <div classname ="volunteer sign up">
                <h1>Sign Up as Volunteer</h1>
                <form>
                    <div className="form-group">
                        <label>Username</label>
                        <input type="text" className="form-control" placeholder="Enter username" />
                    </div>
                    <div className="form-group">
                        <label>Email</label>
                        <input type="email" className="form-control" placeholder="Enter email" />
                    </div>
                    <div className="form-group">
                        <label>Password</label>
                        <input type="password" className="form-control" placeholder="Enter password" />
                    </div>
                    <div className="form-group">
                        <label>Confirm Password</label>
                        <input type="password" className="form-control" placeholder="Confirm password" />
                    </div>
                    </form>
            </div>
        )
    }

    export default VolunteerSignup
     
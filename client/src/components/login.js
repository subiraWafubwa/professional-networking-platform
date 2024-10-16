import React from "react";

function Login(){
    return (
        <div classname = 'login'>
            <h1>Log in as Volunteer or Organisation</h1>
            <form>
                <div>
                    <label>username,organisation name or email</label>
                    <input type = "text" placeholder="Enter username,organisation name or email" />
                </div>
                <div>
                    <label> Password</label>
                    <input type = "text" placeholder = "Enter password"/>
                </div>
                <div>
                    <label>Confirm Password</label>
                    <input type = "text" placeholder = "Enter password"/>
                </div>
            </form>
        </div>
    )
}
export default Login
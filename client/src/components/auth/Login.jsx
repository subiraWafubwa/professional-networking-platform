import React, { useState, useContext } from "react";
import { Link, useNavigate } from "react-router-dom"; // useNavigate instead of useHistory
import "../../index.css";
import logo from "../../../assets/logo.png";
import SignUpContext from "../context/SignUp"; // Import context

function Login() {
  const [usernameOrEmail, setUsernameOrEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const { setIsLoggedIn } = useContext(SignUpContext);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:5555/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          usernameororganizationnameoremail: usernameOrEmail,
          password: password,
        }),
      });

      const data = await response.json();

      if (response.status === 200) {
        alert("Login successful");
        setIsLoggedIn(true);
        navigate("/");
      } else {
        alert(data.message);
      }
    } catch (error) {
      alert("An error occurred. Please try again.");
      console.error("Error:", error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="auth">
      <div className="modal-div">
        <div>
          <img
            src={logo}
            alt="logo"
            style={{
              float: "left",
              width: "30px",
              margin: "0px 10px 20px 0px",
            }}
          />
          <h2 style={{ float: "left" }}>VolunteerMS</h2>
        </div>
        <h3>Log in as Volunteer or Organization</h3>
        <form onSubmit={handleLogin}>
          <div>
            <input
              type="text"
              id="input"
              placeholder="Enter username, organisation name or email"
              value={usernameOrEmail}
              onChange={(e) => setUsernameOrEmail(e.target.value)} // Update state
              required
            />
          </div>
          <div>
            <input
              type="password" // Should be password type for security
              id="input"
              placeholder="Enter password"
              value={password}
              onChange={(e) => setPassword(e.target.value)} // Update state
              required
            />
          </div>
          <p style={{ marginTop: "25px" }}>
            Sign up as{" "}
            <Link to="/organization_signup" className="custom-link">
              organization
            </Link>{" "}
            or{" "}
            <Link to="/volunteer_signup" className="custom-link">
              {" "}
              volunteer
            </Link>
          </p>
          <button
            type="submit"
            className="button"
            style={{ marginTop: "30px" }}
            disabled={isLoading} // Disable the button while loading
          >
            {isLoading ? "Logging in..." : "Login"} {/* Show loading state */}
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;

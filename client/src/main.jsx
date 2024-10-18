import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import Auth from "./components/auth/Auth.jsx";

const isLoggedIn = true;

createRoot(document.getElementById("root")).render(
  <StrictMode>{!isLoggedIn ? <Auth /> : <App />}</StrictMode>
);

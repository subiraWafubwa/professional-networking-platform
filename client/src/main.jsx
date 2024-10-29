import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import { AccountProvider } from "./components/context/AccountContext.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <AccountProvider>
      <App />
    </AccountProvider>
  </StrictMode>
);

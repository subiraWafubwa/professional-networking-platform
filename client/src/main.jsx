import { StrictMode, useContext } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import Auth from "./components/auth/Auth.jsx";
import { SignUpProvider } from "./components/context/SignUp.jsx";
import SignUpContext from "./components/context/SignUp.jsx";

const RootComponent = () => {
  const { isLoggedIn } = useContext(SignUpContext);

  return isLoggedIn ? <App /> : <Auth />;
};

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <SignUpProvider>
      <RootComponent />
    </SignUpProvider>
  </StrictMode>
);

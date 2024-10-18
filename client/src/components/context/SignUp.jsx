import { createContext, useState } from "react";

const SignUpContext = createContext({
  isLoggedIn: false,
  setIsLoggedIn: () => {},
});

export const SignUpProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <SignUpContext.Provider value={{ isLoggedIn, setIsLoggedIn }}>
      {children}
    </SignUpContext.Provider>
  );
};

export default SignUpContext;

import React, { createContext, useContext, useState } from "react";

const AccountContext = createContext();

export const AccountProvider = ({ children }) => {
  const [accountType, setAccountType] = useState(null); // null, 'volunteer', or 'organization'

  return (
    <AccountContext.Provider value={{ accountType, setAccountType }}>
      {children}
    </AccountContext.Provider>
  );
};

export const useAccountContext = () => {
  return useContext(AccountContext);
};

export default AccountContext;

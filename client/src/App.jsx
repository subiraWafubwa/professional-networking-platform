import React, { useEffect, useState } from "react";
import "./index.css";
import MainBody from "./components/common/MainBody";
import Modal from "./components/common/Modal";
import AccountContext from "./components/context/AccountContext";

function App() {
  const [accountType, setAccountType] = useState("volunteer");
  const hasModal = false;

  return (
    <>
      <AccountContext.Provider value={accountType}>
        {hasModal ? <Modal /> : null}
        <div className="whole-app">
          <MainBody />
        </div>
      </AccountContext.Provider>
    </>
  );
}

export default App;

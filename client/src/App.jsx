import React, { useContext } from "react";
import "./index.css";
import Modal from "./components/common/Modal";
import AppRoutes from "./Routes";

export default function App() {
  const hasModal = false;

  return (
    <>
      {hasModal && <Modal />}
      <div className="whole-app">
        <AppRoutes />
      </div>
    </>
  );
}

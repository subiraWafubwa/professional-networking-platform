import React from "react";
import LeftSection from "../common/LeftSection";
import RightSection from "./RightSection";
import OrgLeftSection from "./OrgLeftSection";

export default function OrgMainBody() {
  return (
    <div className="main-body">
      <OrgLeftSection />
      <RightSection />
    </div>
  );
}

import "../../index.css";
import OtherDetails from "./OtherDetails";
import UserProfile from "../volunteer/UserProfile";
import OrganizationProfile from "../organisation/OrganizationProfile";
import AccountContext from "../context/AccountContext";
import { useContext } from "react";

export default function LeftSection() {
  const accountType = useContext(AccountContext);

  return (
    <div className="left-section">
      {accountType == "volunteer" ? (
        <UserProfile />
      ) : accountType == "organization" ? (
        <OrganizationProfile />
      ) : null}
      <OtherDetails />
    </div>
  );
}

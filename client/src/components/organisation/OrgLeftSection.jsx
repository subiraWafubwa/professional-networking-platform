import "../../index.css";
import OtherDetails from "./OtherDetails";
import OrganizationProfile from "../organisation/OrganizationProfile";

export default function OrgLeftSection() {
  return (
    <div className="left-section">
      <OrganizationProfile />
      <OtherDetails />
    </div>
  );
}

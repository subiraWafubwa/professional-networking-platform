import "../../index.css";
import VolProfile from "./VolProfile";
import VolDetails from "./VolDetails";

export default function VolLeftSection({ volunteer }) {
  return (
    <div className="left-section">
      <VolProfile volunteer={volunteer} />
      <VolDetails />
    </div>
  );
}

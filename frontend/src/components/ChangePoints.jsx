import { useEffect, useState } from "react";
import { fetchChangePoints } from "../api";

export default function ChangePoints() {
  const [points, setPoints] = useState([]);

  useEffect(() => {
    fetchChangePoints().then(setPoints);
  }, []);

  return (
    <div>
      <h2>Detected Change Points</h2>
      <pre>{JSON.stringify(points, null, 2)}</pre>
    </div>
  );
}

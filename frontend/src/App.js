import { useEffect, useState } from "react";
import { fetchPrices, fetchEvents, fetchChangePoints } from "./api";
import PriceChart from "./components/PriceChart";
import EventTimeline from "./components/EventTimeline";
import ChangePointSummary from "./components/ChangePointSummary";

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [cp, setCp] = useState(null);

  useEffect(() => {
    fetchPrices().then(res => setPrices(res.data));
    fetchEvents().then(res => setEvents(res.data));
    fetchChangePoints().then(res => setCp(res.data));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Brent Oil Price Analysis Dashboard</h1>

      <h2>Historical Prices</h2>
      <PriceChart data={prices} />

      <h2>Key Market Events</h2>
      <EventTimeline events={events} />

      <h2>Bayesian Change Point Result</h2>
      <ChangePointSummary cp={cp} />
    </div>
  );
}

export default App;

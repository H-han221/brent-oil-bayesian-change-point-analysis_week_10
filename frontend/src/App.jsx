import PriceChart from "./components/PriceChart";
import EventsList from "./components/EventsList";
import ChangePoints from "./components/ChangePoints";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Brent Oil Bayesian Change Point Dashboard</h1>

  
      <PriceChart />
      <EventsList />
      <ChangePoints />
    </div>
  );
}

export default App;

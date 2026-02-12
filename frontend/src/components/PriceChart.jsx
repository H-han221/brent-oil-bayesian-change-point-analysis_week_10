import { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import { fetchPrices } from "../api";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
} from "chart.js";

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement);

export default function PriceChart() {
  const [prices, setPrices] = useState([]);

  useEffect(() => {
    fetchPrices().then(data => setPrices(data.slice(0, 500)));
  }, []);

  const data = {
    labels: prices.map(p => p.date),
    datasets: [
      {
        label: "Brent Oil Price",
        data: prices.map(p => p.price),
      },
    ],
  };

  return (
    <div>
      <h2>Brent Oil Price Trend</h2>
      <Line data={data} />
    </div>
  );
}

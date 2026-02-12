const BASE_URL = "http://127.0.0.1:5000/api";

export async function fetchPrices() {
  const res = await fetch(`${BASE_URL}/prices`);
  return res.json();
}

export async function fetchEvents() {
  const res = await fetch(`${BASE_URL}/events`);
  return res.json();
}

export async function fetchChangePoints() {
  const res = await fetch(`${BASE_URL}/change-points`);
  return res.json();
}

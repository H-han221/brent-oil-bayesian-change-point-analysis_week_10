import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000/api",
});

export const fetchPrices = () => API.get("/prices");
export const fetchEvents = () => API.get("/events");
export const fetchChangePoints = () => API.get("/change-points");

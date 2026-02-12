import { useEffect, useState } from "react";
import { fetchEvents } from "../api";

export default function EventsList() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetchEvents().then(setEvents);
  }, []);

  return (
    <div>
      <h2>Market Events</h2>
      <ul>
        {events.map((event, index) => (
          <li key={index}>
            {event.date} - {event.event}
          </li>
        ))}
      </ul>
    </div>
  );
}

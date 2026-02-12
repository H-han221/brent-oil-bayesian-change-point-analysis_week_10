const EventTimeline = ({ events }) => (
  <ul>
    {events.map((e, idx) => (
      <li key={idx}>
        <strong>{e.date}</strong> – {e.event} ({e.category})
      </li>
    ))}
  </ul>
);

export default EventTimeline;

const ChangePointSummary = ({ cp }) => {
  if (!cp) return null;

  return (
    <div>
      <h3>Detected Change Point</h3>
      <p><strong>Date:</strong> {cp.change_point_date}</p>
      <p><strong>Mean Before:</strong> {cp.mean_before}</p>
      <p><strong>Mean After:</strong> {cp.mean_after}</p>
      <p><em>{cp.interpretation}</em></p>
    </div>
  );
};

export default ChangePointSummary;

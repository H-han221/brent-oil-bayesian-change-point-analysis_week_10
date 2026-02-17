from typing import Dict
import numpy as np
import pandas as pd


def detect_change_point(series: pd.Series) -> Dict[str, float]:
    """
    Detect a structural change point in a time series
    using mean shift comparison.
    """

    if len(series) < 10:
        raise ValueError("Series too short to detect change point")

    best_index = 0
    best_score = 0

    for i in range(5, len(series) - 5):
        mean_before = series[:i].mean()
        mean_after = series[i:].mean()

        score = abs(mean_after - mean_before)

        if score > best_score:
            best_score = score
            best_index = i

    return {
        "change_point_index": int(best_index),
        "mean_before": float(series[:best_index].mean()),
        "mean_after": float(series[best_index:].mean()),
        "score": float(best_score)
    }

from typing import Dict


def evaluate_change_point(result: Dict[str, float]) -> bool:
    """
    Simple evaluation:
    Returns True if mean difference is significant.
    """

    mean_before = result["mean_before"]
    mean_after = result["mean_after"]

    return abs(mean_after - mean_before) > 0.01

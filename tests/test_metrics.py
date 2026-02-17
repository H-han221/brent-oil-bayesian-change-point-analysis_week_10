from src.evaluation.metrics import evaluate_change_point


def test_evaluate_change_point_true():
    result = {
        "mean_before": 0.0,
        "mean_after": 1.0
    }

    assert evaluate_change_point(result) is True


def test_evaluate_change_point_false():
    result = {
        "mean_before": 1.0,
        "mean_after": 1.005
    }

    assert evaluate_change_point(result) is False

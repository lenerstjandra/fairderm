from fairderm_eval.calib.ece import expected_calibration_error
from fairderm_eval.signals.confusion import GroupCounts, count_binary, rates
from fairderm_eval.signals.fairness import (
    equalized_odds_gap_pp,
    fnr_disparity_pp,
    worst_group_ratio,
)


def test_confusion_rates() -> None:
    counts = count_binary([1, 1, 0, 0], [1, 0, 1, 0])
    assert counts == GroupCounts(tp=1, fp=1, tn=1, fn=1)
    bundle = rates(counts)
    assert bundle.sensitivity == 0.5
    assert bundle.specificity == 0.5


def test_fairness_gaps() -> None:
    light = GroupCounts(tp=9, fp=1, tn=9, fn=1)
    dark = GroupCounts(tp=7, fp=2, tn=8, fn=3)
    assert round(fnr_disparity_pp(light, dark), 3) == 20.0
    assert equalized_odds_gap_pp(light, dark) >= 20.0
    assert round(worst_group_ratio({"l": light, "d": dark}), 3) == 0.778


def test_ece() -> None:
    value = expected_calibration_error([1, 0, 1, 0], [0.9, 0.1, 0.6, 0.4], bins=2)
    assert 0.0 <= value <= 1.0

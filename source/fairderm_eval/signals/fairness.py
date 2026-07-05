from collections.abc import Mapping, Sequence

from fairderm_eval.signals.confusion import rates, safe_div
from fairderm_eval.typing import GroupCounts, MetricBundle


def group_metrics(groups: Mapping[str, GroupCounts]) -> dict[str, MetricBundle]:
    return {name: rates(counts) for name, counts in groups.items()}


def fnr_disparity_pp(light: GroupCounts, dark: GroupCounts) -> float:
    lr = rates(light)
    dr = rates(dark)
    return abs(dr.false_negative_rate - lr.false_negative_rate) * 100.0


def sensitivity_gap_pp(light: GroupCounts, dark: GroupCounts) -> float:
    lr = rates(light)
    dr = rates(dark)
    return abs(lr.sensitivity - dr.sensitivity) * 100.0


def specificity_gap_pp(light: GroupCounts, dark: GroupCounts) -> float:
    lr = rates(light)
    dr = rates(dark)
    return abs(lr.specificity - dr.specificity) * 100.0


def equalized_odds_gap_pp(light: GroupCounts, dark: GroupCounts) -> float:
    lr = rates(light)
    dr = rates(dark)
    return (
        max(
            abs(lr.false_negative_rate - dr.false_negative_rate),
            abs(lr.false_positive_rate - dr.false_positive_rate),
        )
        * 100.0
    )


def demographic_parity_difference_pp(light: GroupCounts, dark: GroupCounts) -> float:
    lr = rates(light)
    dr = rates(dark)
    return abs(lr.positive_rate - dr.positive_rate) * 100.0


def worst_group_ratio(groups: Mapping[str, GroupCounts]) -> float:
    sens = [rates(counts).sensitivity for counts in groups.values()]
    if not sens or max(sens) == 0:
        return 0.0
    return min(sens) / max(sens)


def accuracy_worst_group_ratio(groups: Mapping[str, GroupCounts]) -> float:
    acc = [rates(counts).accuracy for counts in groups.values()]
    if not acc or max(acc) == 0:
        return 0.0
    return min(acc) / max(acc)


def auc_gap_pp(auc_by_group: Mapping[str, float]) -> float:
    values = list(auc_by_group.values())
    if not values:
        return 0.0
    return (max(values) - min(values)) * 100.0


def melanoma_wgr(sensitivity_light: float, sensitivity_dark: float) -> float:
    return safe_div(sensitivity_dark, sensitivity_light)


def clinical_success(fnr_gap_pp_value: float, wgr_value: float) -> bool:
    return fnr_gap_pp_value <= 10.0 and wgr_value >= 0.85


def median(values: Sequence[float]) -> float:
    ordered = sorted(values)
    n = len(ordered)
    if n == 0:
        raise ValueError("median needs at least one value")
    mid = n // 2
    if n % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2.0


def category_summary(rows: Sequence[Mapping[str, float]], key: str) -> float:
    return median([float(row[key]) for row in rows])

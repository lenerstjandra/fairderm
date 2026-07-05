from collections.abc import Sequence


def expected_calibration_error(
    labels: Sequence[int], scores: Sequence[float], bins: int = 10
) -> float:
    if len(labels) != len(scores):
        raise ValueError("labels and scores length mismatch")
    if bins <= 0:
        raise ValueError("bins must be positive")
    n = len(labels)
    if n == 0:
        return 0.0
    total = 0.0
    for index in range(bins):
        lo = index / bins
        hi = (index + 1) / bins
        members = [
            i
            for i, score in enumerate(scores)
            if (score >= lo and (score < hi or index == bins - 1 and score <= hi))
        ]
        if members:
            conf = sum(scores[i] for i in members) / len(members)
            acc = sum(1 for i in members if (scores[i] >= 0.5) == bool(labels[i])) / len(members)
            total += len(members) / n * abs(acc - conf)
    return total


def calibration_disparity_pp(light_ece: float, dark_ece: float) -> float:
    return abs(dark_ece - light_ece) * 100.0


def per_group_ece(
    labels: Sequence[int], scores: Sequence[float], groups: Sequence[str], bins: int = 10
) -> dict[str, float]:
    values: dict[str, float] = {}
    for group in sorted(set(groups)):
        idx = [i for i, item in enumerate(groups) if item == group]
        values[group] = expected_calibration_error(
            [labels[i] for i in idx], [scores[i] for i in idx], bins
        )
    return values


def temperature_scale(scores: Sequence[float], temperature: float) -> list[float]:
    import math

    if temperature <= 0:
        raise ValueError("temperature must be positive")
    out: list[float] = []
    for score in scores:
        clipped = min(max(score, 1e-6), 1.0 - 1e-6)
        logit = math.log(clipped / (1.0 - clipped)) / temperature
        out.append(1.0 / (1.0 + math.exp(-logit)))
    return out

def faithfulness_fairness_lower_bound(
    faithfulness_gap: float, alpha: float, tone_noise: float
) -> float:
    value = alpha * faithfulness_gap - tone_noise
    return value if value > 0.0 else 0.0


def necessary_condition_met(faithfulness_gap: float, tolerance: float) -> bool:
    return abs(faithfulness_gap) <= tolerance


def bound_report(
    faithfulness_light: float, faithfulness_dark: float, alpha: float = 1.0, tone_noise: float = 0.0
) -> dict[str, float | bool]:
    gap = faithfulness_light - faithfulness_dark
    lower = faithfulness_fairness_lower_bound(gap, alpha, tone_noise)
    return {
        "faithfulness_gap": gap,
        "fnr_lower_bound": lower,
        "tone_invariant_ready": necessary_condition_met(gap, 0.01),
    }

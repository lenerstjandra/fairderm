from fairderm_eval.signals.skin_tone import (
    fitzpatrick_from_ita,
    grouped_fst,
    validate_fst_agreement,
)
from fairderm_eval.stats.fairness_bound import bound_report
from fairderm_eval.stats.intervals import bootstrap_ci, mcnemar_stat, spearman_rho, wald_ci


def test_skin_tone_mapping() -> None:
    assert grouped_fst(fitzpatrick_from_ita(60.0)) == "I-II"
    assert grouped_fst(6) == "V-VI"
    stats = validate_fst_agreement([1, 2, 4], [1, 3, 4])
    assert stats["within_one"] == 1.0


def test_stats() -> None:
    lo, hi = bootstrap_ci([1.0, 2.0, 3.0], repeats=10, seed=1)
    assert lo <= hi
    assert wald_ci(5, 10)[0] >= 0.0
    assert round(spearman_rho([1.0, 2.0, 3.0], [3.0, 2.0, 1.0]), 6) == -1.0
    assert mcnemar_stat(10, 2) > 0.0
    assert bound_report(0.8, 0.6)["fnr_lower_bound"] == 0.20000000000000007

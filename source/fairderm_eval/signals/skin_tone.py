from fairderm_eval.typing import ToneGroup


def ita_angle(l_star: float, b_star: float) -> float:
    import math

    if b_star == 0:
        return 90.0 if l_star >= 50.0 else -90.0
    return math.degrees(math.atan((l_star - 50.0) / b_star))


def fitzpatrick_from_ita(ita: float) -> int:
    if ita > 55.0:
        return 1
    if ita > 41.0:
        return 2
    if ita > 28.0:
        return 3
    if ita > 10.0:
        return 4
    if ita > -30.0:
        return 5
    return 6


def grouped_fst(fst: int) -> ToneGroup:
    if fst in (1, 2):
        return "I-II"
    if fst in (3, 4):
        return "III-IV"
    if fst in (5, 6):
        return "V-VI"
    raise ValueError("FST must be in 1..6")


def grouped_midas(fst: int) -> ToneGroup:
    if fst in (1, 2):
        return "I-II"
    if fst in (3, 4, 5, 6):
        return "III+"
    raise ValueError("FST must be in 1..6")


def validate_fst_agreement(predicted: list[int], expert: list[int]) -> dict[str, float]:
    if len(predicted) != len(expert):
        raise ValueError("length mismatch")
    n = len(predicted)
    exact = sum(1 for a, b in zip(predicted, expert, strict=True) if a == b)
    within = sum(1 for a, b in zip(predicted, expert, strict=True) if abs(a - b) <= 1)
    mae = sum(abs(a - b) for a, b in zip(predicted, expert, strict=True)) / n if n else 0.0
    return {"exact": exact / n if n else 0.0, "within_one": within / n if n else 0.0, "mae": mae}

import math
import random
from collections.abc import Callable, Sequence


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def percentile(values: Sequence[float], q: float) -> float:
    if not values:
        raise ValueError("empty sequence")
    ordered = sorted(values)
    pos = (len(ordered) - 1) * q
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return ordered[int(pos)]
    weight = pos - lo
    return ordered[lo] * (1.0 - weight) + ordered[hi] * weight


def bootstrap_ci(values: Sequence[float], repeats: int, seed: int = 0) -> tuple[float, float]:
    if not values:
        raise ValueError("empty sequence")
    rng = random.Random(seed)
    samples: list[float] = []
    for _ in range(repeats):
        draw = [values[rng.randrange(len(values))] for _ in values]
        samples.append(mean(draw))
    return percentile(samples, 0.025), percentile(samples, 0.975)


def wald_ci(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if total <= 0:
        return 0.0, 0.0
    p = successes / total
    se = math.sqrt(p * (1.0 - p) / total)
    return max(0.0, p - z * se), min(1.0, p + z * se)


def spearman_rho(x: Sequence[float], y: Sequence[float]) -> float:
    if len(x) != len(y):
        raise ValueError("length mismatch")
    return pearson(rank(x), rank(y))


def rank(values: Sequence[float]) -> list[float]:
    ordered = sorted((value, idx) for idx, value in enumerate(values))
    ranks = [0.0] * len(values)
    i = 0
    while i < len(ordered):
        j = i
        while j + 1 < len(ordered) and ordered[j + 1][0] == ordered[i][0]:
            j += 1
        r = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[ordered[k][1]] = r
        i = j + 1
    return ranks


def pearson(x: Sequence[float], y: Sequence[float]) -> float:
    if len(x) != len(y):
        raise ValueError("length mismatch")
    mx = mean(x)
    my = mean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y, strict=True))
    dx = math.sqrt(sum((a - mx) ** 2 for a in x))
    dy = math.sqrt(sum((b - my) ** 2 for b in y))
    if dx == 0 or dy == 0:
        return 0.0
    return num / (dx * dy)


def mcnemar_stat(b: int, c: int) -> float:
    if b + c == 0:
        return 0.0
    return (abs(b - c) - 1.0) ** 2 / (b + c)


def signed_rank_stat(differences: Sequence[float]) -> float:
    nonzero = [d for d in differences if d != 0.0]
    ranks = rank([abs(d) for d in nonzero])
    positive = sum(r for r, d in zip(ranks, nonzero, strict=True) if d > 0)
    negative = sum(r for r, d in zip(ranks, nonzero, strict=True) if d < 0)
    return min(positive, negative)


def paired_delta(
    a: Sequence[float], b: Sequence[float], fn: Callable[[float, float], float] | None = None
) -> list[float]:
    if len(a) != len(b):
        raise ValueError("length mismatch")
    op = fn or (lambda x, y: y - x)
    return [op(x, y) for x, y in zip(a, b, strict=True)]

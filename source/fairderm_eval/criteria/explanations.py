from collections.abc import Iterable, Mapping, Sequence

ABCDE_TERMS: dict[str, tuple[str, ...]] = {
    "A": ("asymmetry", "asymmetric", "symmetry"),
    "B": ("border", "irregular", "margin"),
    "C": ("colour", "color", "pigment", "variegated"),
    "D": ("diameter", "size", "millimeter", "mm"),
    "E": ("evolution", "evolving", "elevated", "change"),
}

HALLUCINATION_TERMS = ("network", "ulceration", "bleeding", "blue-white", "streaks", "regression")


def mentioned_criteria(text: str) -> set[str]:
    lower = text.lower()
    found: set[str] = set()
    for key, terms in ABCDE_TERMS.items():
        if any(term in lower for term in terms):
            found.add(key)
    return found


def abcde_alignment(text: str, expected: Iterable[str]) -> float:
    expected_set = set(expected)
    if not expected_set:
        return 0.0
    return len(mentioned_criteria(text) & expected_set) / len(expected_set)


def hallucination_rate(claims: Sequence[str], supported_terms: Sequence[str]) -> float:
    if not claims:
        return 0.0
    supported = {term.lower() for term in supported_terms}
    false_count = 0
    for claim in claims:
        lower = claim.lower()
        marker = any(term in lower for term in HALLUCINATION_TERMS)
        supported_hit = any(term in lower for term in supported)
        if marker and not supported_hit:
            false_count += 1
    return false_count / len(claims)


def token_overlap(a: str, b: str) -> float:
    aa = {part.strip(".,;:()[]").lower() for part in a.split() if part.strip(".,;:()[]")}
    bb = {part.strip(".,;:()[]").lower() for part in b.split() if part.strip(".,;:()[]")}
    if not aa or not bb:
        return 0.0
    return len(aa & bb) / len(aa | bb)


def faithfulness_score(claims: Sequence[str], references: Sequence[str]) -> float:
    if not claims or not references:
        return 0.0
    scores: list[float] = []
    for claim in claims:
        scores.append(max(token_overlap(claim, ref) for ref in references))
    return sum(scores) / len(scores)


def explanation_equity(light_score: float, dark_score: float) -> float:
    return light_score - dark_score


def parse_claims(text: str) -> list[str]:
    raw = text.replace(";", ".").split(".")
    return [part.strip() for part in raw if part.strip()]


def batch_explanation_scores(
    rows: Sequence[Mapping[str, str]], expected: Iterable[str]
) -> dict[str, float]:
    alignments = [abcde_alignment(row["explanation"], expected) for row in rows]
    faith = [faithfulness_score(parse_claims(row["explanation"]), list(expected)) for row in rows]
    if not alignments:
        return {"alignment": 0.0, "faithfulness": 0.0}
    return {"alignment": sum(alignments) / len(alignments), "faithfulness": sum(faith) / len(faith)}

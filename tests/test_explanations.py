from fairderm_eval.criteria.explanations import (
    abcde_alignment,
    faithfulness_score,
    hallucination_rate,
    parse_claims,
)
from fairderm_eval.criteria.prompts import render_prompt, strategy_codes


def test_prompt_codes() -> None:
    assert strategy_codes() == ["P1", "P2", "P3", "P4", "P5", "P6"]
    rendered = render_prompt(
        "P5", {"age": "60", "sex": "female", "location": "sole", "history": "changing"}
    )
    assert "sole" in rendered


def test_explanation_scores() -> None:
    text = "Asymmetry is present. Border is irregular. Colour varies."
    assert abcde_alignment(text, ["A", "B", "C", "D", "E"]) == 0.8
    claims = parse_claims(text)
    assert (
        faithfulness_score(claims, ["asymmetry present", "border irregular", "colour varies"]) > 0.2
    )
    assert hallucination_rate(["pigment network present"], ["border"]) == 1.0

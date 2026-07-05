from fairderm_eval.typing import PromptSpec

PROMPTS: tuple[PromptSpec, ...] = (
    PromptSpec(
        "P1",
        "zero shot",
        "Examine this dermatological image. Is this lesion melanoma or benign? "
        "Provide your diagnosis and confidence level.",
        False,
        1,
    ),
    PromptSpec(
        "P2",
        "few shot",
        "Compare the lesion with three labelled examples, then provide melanoma "
        "or benign and confidence.",
        False,
        1,
    ),
    PromptSpec(
        "P3",
        "basic reasoning",
        "Think step by step about visible clinical features before giving melanoma or benign.",
        False,
        1,
    ),
    PromptSpec(
        "P4",
        "ABCDE reasoning",
        "Evaluate asymmetry, border irregularity, colour variation, diameter, "
        "and evolution or elevation. Provide melanoma or benign and confidence.",
        False,
        1,
    ),
    PromptSpec(
        "P5",
        "ABCDE with context",
        "Evaluate ABCDE criteria with patient age, sex, anatomical location, "
        "and lesion history. Provide melanoma or benign and confidence.",
        True,
        1,
    ),
    PromptSpec(
        "P6",
        "two turn clinical panel",
        "A first clinician describes lesion features. A second clinician applies "
        "ABCDE criteria and gives melanoma or benign with confidence.",
        False,
        2,
    ),
)


def prompt_by_code(code: str) -> PromptSpec:
    for prompt in PROMPTS:
        if prompt.code == code:
            return prompt
    raise KeyError(code)


def render_prompt(code: str, context: dict[str, str] | None = None) -> str:
    prompt = prompt_by_code(code)
    if not prompt.needs_context:
        return prompt.template
    context = context or {}
    fields = ["age", "sex", "location", "history"]
    missing = [field for field in fields if field not in context]
    if missing:
        raise ValueError("missing context fields: " + ",".join(missing))
    return (
        prompt.template
        + f" Patient Age: {context['age']}. Sex: {context['sex']}. "
        + f"Anatomical Location: {context['location']}. "
        + f"Lesion History: {context['history']}."
    )


def strategy_codes() -> list[str]:
    return [prompt.code for prompt in PROMPTS]

from fairderm_eval.typing import DatasetCard

DATASETS: tuple[DatasetCard, ...] = (
    DatasetCard(
        "ISIC 2020",
        "dermoscopic",
        33126,
        19800,
        11300,
        2000,
        "ITA-estimated",
        "https://challenge2020.isic-archive.com/",
        "public",
        "not stated in manuscript",
    ),
    DatasetCard(
        "DDI",
        "clinical",
        656,
        208,
        241,
        207,
        "expert",
        "https://ddi-dataset.github.io/",
        "public",
        "not stated in manuscript",
    ),
    DatasetCard(
        "Fitzpatrick17k",
        "clinical",
        16577,
        7800,
        6600,
        2170,
        "expert",
        "https://github.com/mattgroh/fitzpatrick17k",
        "public",
        "not stated in manuscript",
    ),
    DatasetCard(
        "MIDAS",
        "paired dermoscopic and clinical",
        3830,
        3185,
        498,
        147,
        "ITA-estimated",
        "https://stanfordaimi.azurewebsites.net/datasets/midas",
        "public",
        "not stated in manuscript",
    ),
    DatasetCard(
        "PAD-UFES-20",
        "smartphone",
        2298,
        450,
        1100,
        750,
        "expert",
        "https://data.mendeley.com/datasets/zr7vgbcyr2",
        "public",
        "CC BY 4.0 at source",
    ),
    DatasetCard(
        "MSKCC Skin Tone Labeling",
        "clinical",
        4800,
        1950,
        1680,
        1250,
        "multi-scale ground truth",
        "https://api.isic-archive.com/collections/413/",
        "public validation",
        "not stated in manuscript",
    ),
)

PRIVATE_COHORT = DatasetCard(
    "Private deployment cohort",
    "clinical",
    13412,
    5092,
    4561,
    3759,
    "clinical record",
    "restricted",
    "restricted",
    "data-use agreement",
)


def public_datasets() -> tuple[DatasetCard, ...]:
    return DATASETS


def dataset_by_name(name: str) -> DatasetCard:
    for card in DATASETS + (PRIVATE_COHORT,):
        if card.name.lower() == name.lower():
            return card
    raise KeyError(name)


def total_public_images() -> int:
    return sum(card.total for card in DATASETS)


def fairness_eval_datasets() -> tuple[DatasetCard, ...]:
    return tuple(card for card in DATASETS if not card.name.startswith("MSKCC"))


def dataset_summary_lines() -> list[str]:
    return [f"{card.name}	{card.modality}	{card.total}	{card.url}" for card in DATASETS]

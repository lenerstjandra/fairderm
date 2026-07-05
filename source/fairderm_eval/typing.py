from dataclasses import dataclass
from typing import Literal

ToneGroup = Literal["I-II", "III-IV", "V-VI", "III+"]
Label = Literal["melanoma", "benign"]


@dataclass(frozen=True)
class CaseRecord:
    case_id: str
    dataset: str
    tone_group: ToneGroup
    label: int
    prediction: int
    score: float
    explanation: str


@dataclass(frozen=True)
class GroupCounts:
    tp: int
    fp: int
    tn: int
    fn: int


@dataclass(frozen=True)
class AuditConfig:
    seed: int
    precision: str
    world_size: int
    per_device_batch: int
    grad_accum: int
    effective_batch: int
    epochs: int
    learning_rate: float
    warmup_steps: int
    weight_decay: float
    scheduler: str
    image_size: int
    prompt_strategy: str
    bootstrap_repeats: int
    ece_bins: int
    private_records_enabled: bool


@dataclass(frozen=True)
class DatasetCard:
    name: str
    modality: str
    total: int
    light: int
    medium: int
    dark: int
    tone_source: str
    url: str
    access: str
    license: str


@dataclass(frozen=True)
class PromptSpec:
    code: str
    name: str
    template: str
    needs_context: bool
    turns: int


@dataclass(frozen=True)
class MetricBundle:
    sensitivity: float
    specificity: float
    false_negative_rate: float
    false_positive_rate: float
    accuracy: float
    positive_rate: float


@dataclass(frozen=True)
class DeploymentArm:
    name: str
    sensitivity_light: float
    sensitivity_medium: float
    sensitivity_dark: float
    fnr_gap_pp: float
    worst_group_ratio: float

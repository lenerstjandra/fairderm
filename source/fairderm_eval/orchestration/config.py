from pathlib import Path
from typing import Any

import yaml
from fairderm_eval.typing import AuditConfig


def load_config(path: str | Path) -> AuditConfig:
    raw: dict[str, Any] = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return AuditConfig(
        seed=int(raw["seed"]),
        precision=str(raw["precision"]),
        world_size=int(raw["world_size"]),
        per_device_batch=int(raw["per_device_batch"]),
        grad_accum=int(raw["grad_accum"]),
        effective_batch=int(raw["effective_batch"]),
        epochs=int(raw["epochs"]),
        learning_rate=float(raw["learning_rate"]),
        warmup_steps=int(raw["warmup_steps"]),
        weight_decay=float(raw["weight_decay"]),
        scheduler=str(raw["scheduler"]),
        image_size=int(raw["image_size"]),
        prompt_strategy=str(raw["prompt_strategy"]),
        bootstrap_repeats=int(raw["bootstrap_repeats"]),
        ece_bins=int(raw["ece_bins"]),
        private_records_enabled=bool(raw["private_records_enabled"]),
    )


def validate_config(config: AuditConfig) -> None:
    if config.per_device_batch * config.grad_accum * config.world_size != config.effective_batch:
        raise ValueError("effective batch mismatch")
    if config.ece_bins <= 0:
        raise ValueError("ece bins must be positive")

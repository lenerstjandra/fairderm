import os
from pathlib import Path
from typing import Any

import torch


def atomic_save(obj: dict[str, Any], path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    torch.save(obj, tmp)
    os.replace(tmp, target)


def load_checkpoint(path: str | Path) -> dict[str, Any]:
    value = torch.load(Path(path), map_location="cpu")
    if not isinstance(value, dict):
        raise TypeError("checkpoint must contain a dictionary")
    return value

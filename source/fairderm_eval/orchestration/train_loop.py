import random
from dataclasses import dataclass

import torch
from fairderm_eval.baselines.nets import build_baseline
from fairderm_eval.baselines.synthetic import synthetic_batch
from fairderm_eval.typing import AuditConfig
from torch import nn


@dataclass(frozen=True)
class TrainResult:
    losses: list[float]
    seed: int


def set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def run_two_step(config: AuditConfig) -> TrainResult:
    set_seed(config.seed)
    model = build_baseline("resnet50", image_size=config.image_size)
    opt = torch.optim.SGD(model.parameters(), lr=config.learning_rate)
    loss_fn = nn.CrossEntropyLoss()
    losses: list[float] = []
    steps = 2
    for _step in range(steps):
        x, y = synthetic_batch(config.per_device_batch, config.image_size, config.seed)
        opt.zero_grad(set_to_none=True)
        logits = model(x)
        loss = loss_fn(logits, y)
        loss.backward()
        opt.step()
        losses.append(float(loss.detach().cpu()))
    return TrainResult(losses=losses, seed=config.seed)

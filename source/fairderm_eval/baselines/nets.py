from typing import Literal, cast

import torch
from torch import Tensor, nn


class ConvStem(nn.Module):
    def __init__(self, channels: int, width: int) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(channels, width, 3, padding=1),
            nn.BatchNorm2d(width),
            nn.SiLU(),
            nn.Conv2d(width, width, 3, padding=1),
            nn.BatchNorm2d(width),
            nn.SiLU(),
        )

    def forward(self, x: Tensor) -> Tensor:
        return cast(Tensor, self.net(x))


class ResidualUnit(nn.Module):
    def __init__(self, width: int) -> None:
        super().__init__()
        self.block = nn.Sequential(
            nn.Conv2d(width, width, 3, padding=1),
            nn.BatchNorm2d(width),
            nn.ReLU(),
            nn.Conv2d(width, width, 3, padding=1),
            nn.BatchNorm2d(width),
        )
        self.act = nn.ReLU()

    def forward(self, x: Tensor) -> Tensor:
        return cast(Tensor, self.act(x + self.block(x)))


class AuditCNN(nn.Module):
    def __init__(self, width: int = 32, depth: int = 4) -> None:
        super().__init__()
        layers: list[nn.Module] = [ConvStem(3, width)]
        for _ in range(depth):
            layers.append(ResidualUnit(width))
            layers.append(nn.MaxPool2d(2))
        self.features = nn.Sequential(*layers)
        self.head = nn.Sequential(nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(width, 2))

    def forward(self, x: Tensor) -> Tensor:
        return cast(Tensor, self.head(self.features(x)))


class PatchEncoder(nn.Module):
    def __init__(self, image_size: int = 32, patch: int = 8, width: int = 64) -> None:
        super().__init__()
        self.patch = patch
        self.proj = nn.Conv2d(3, width, patch, stride=patch)
        tokens = (image_size // patch) ** 2
        self.pos = nn.Parameter(torch.zeros(1, tokens, width))

    def forward(self, x: Tensor) -> Tensor:
        tokens = self.proj(x).flatten(2).transpose(1, 2)
        return cast(Tensor, tokens + self.pos[:, : tokens.shape[1], :])


class TinyViT(nn.Module):
    def __init__(
        self, image_size: int = 32, patch: int = 8, width: int = 64, layers: int = 2
    ) -> None:
        super().__init__()
        self.encoder = PatchEncoder(image_size, patch, width)
        layer = nn.TransformerEncoderLayer(
            d_model=width, nhead=4, dim_feedforward=width * 4, batch_first=True
        )
        self.trunk = nn.TransformerEncoder(layer, layers)
        self.head = nn.Linear(width, 2)

    def forward(self, x: Tensor) -> Tensor:
        z = self.trunk(self.encoder(x)).mean(dim=1)
        return cast(Tensor, self.head(z))


def build_baseline(
    name: Literal["resnet50", "efficientnet_b4", "vit_b16"], image_size: int = 32
) -> nn.Module:
    if name == "resnet50":
        return AuditCNN(width=32, depth=4)
    if name == "efficientnet_b4":
        return AuditCNN(width=48, depth=5)
    if name == "vit_b16":
        return TinyViT(image_size=image_size, patch=max(4, image_size // 4), width=64, layers=2)
    raise ValueError(name)

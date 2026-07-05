import torch
from torch import Tensor


def synthetic_batch(batch: int, image_size: int, seed: int) -> tuple[Tensor, Tensor]:
    gen = torch.Generator().manual_seed(seed)
    x = torch.randn(batch, 3, image_size, image_size, generator=gen)
    signal = x[:, :, : image_size // 2, : image_size // 2].mean(dim=(1, 2, 3))
    y = (signal > 0).long()
    x[y == 1] += 0.15
    x[y == 0] -= 0.15
    return x, y

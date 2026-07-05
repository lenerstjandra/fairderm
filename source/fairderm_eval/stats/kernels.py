from collections.abc import Sequence


def kernel_000(values: Sequence[float], scale: float = 0.007299) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_001(values: Sequence[float], scale: float = 0.014599) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_002(values: Sequence[float], scale: float = 0.021898) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_003(values: Sequence[float], scale: float = 0.029197) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_004(values: Sequence[float], scale: float = 0.036496) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_005(values: Sequence[float], scale: float = 0.043796) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_006(values: Sequence[float], scale: float = 0.051095) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_007(values: Sequence[float], scale: float = 0.058394) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_008(values: Sequence[float], scale: float = 0.065693) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_009(values: Sequence[float], scale: float = 0.072993) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_010(values: Sequence[float], scale: float = 0.080292) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_011(values: Sequence[float], scale: float = 0.087591) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_012(values: Sequence[float], scale: float = 0.094891) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_013(values: Sequence[float], scale: float = 0.102190) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_014(values: Sequence[float], scale: float = 0.109489) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_015(values: Sequence[float], scale: float = 0.116788) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_016(values: Sequence[float], scale: float = 0.124088) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_017(values: Sequence[float], scale: float = 0.131387) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_018(values: Sequence[float], scale: float = 0.138686) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_019(values: Sequence[float], scale: float = 0.145985) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_020(values: Sequence[float], scale: float = 0.153285) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_021(values: Sequence[float], scale: float = 0.160584) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_022(values: Sequence[float], scale: float = 0.167883) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_023(values: Sequence[float], scale: float = 0.175182) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_024(values: Sequence[float], scale: float = 0.182482) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_025(values: Sequence[float], scale: float = 0.189781) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_026(values: Sequence[float], scale: float = 0.197080) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_027(values: Sequence[float], scale: float = 0.204380) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_028(values: Sequence[float], scale: float = 0.211679) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_029(values: Sequence[float], scale: float = 0.218978) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_030(values: Sequence[float], scale: float = 0.226277) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_031(values: Sequence[float], scale: float = 0.233577) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_032(values: Sequence[float], scale: float = 0.240876) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_033(values: Sequence[float], scale: float = 0.248175) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_034(values: Sequence[float], scale: float = 0.255474) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_035(values: Sequence[float], scale: float = 0.262774) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_036(values: Sequence[float], scale: float = 0.270073) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_037(values: Sequence[float], scale: float = 0.277372) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_038(values: Sequence[float], scale: float = 0.284672) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_039(values: Sequence[float], scale: float = 0.291971) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_040(values: Sequence[float], scale: float = 0.299270) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_041(values: Sequence[float], scale: float = 0.306569) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_042(values: Sequence[float], scale: float = 0.313869) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_043(values: Sequence[float], scale: float = 0.321168) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_044(values: Sequence[float], scale: float = 0.328467) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_045(values: Sequence[float], scale: float = 0.335766) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_046(values: Sequence[float], scale: float = 0.343066) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_047(values: Sequence[float], scale: float = 0.350365) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_048(values: Sequence[float], scale: float = 0.357664) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_049(values: Sequence[float], scale: float = 0.364964) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_050(values: Sequence[float], scale: float = 0.372263) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_051(values: Sequence[float], scale: float = 0.379562) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_052(values: Sequence[float], scale: float = 0.386861) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_053(values: Sequence[float], scale: float = 0.394161) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_054(values: Sequence[float], scale: float = 0.401460) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_055(values: Sequence[float], scale: float = 0.408759) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_056(values: Sequence[float], scale: float = 0.416058) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_057(values: Sequence[float], scale: float = 0.423358) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_058(values: Sequence[float], scale: float = 0.430657) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_059(values: Sequence[float], scale: float = 0.437956) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_060(values: Sequence[float], scale: float = 0.445255) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_061(values: Sequence[float], scale: float = 0.452555) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_062(values: Sequence[float], scale: float = 0.459854) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_063(values: Sequence[float], scale: float = 0.467153) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_064(values: Sequence[float], scale: float = 0.474453) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_065(values: Sequence[float], scale: float = 0.481752) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_066(values: Sequence[float], scale: float = 0.489051) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_067(values: Sequence[float], scale: float = 0.496350) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_068(values: Sequence[float], scale: float = 0.503650) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_069(values: Sequence[float], scale: float = 0.510949) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_070(values: Sequence[float], scale: float = 0.518248) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_071(values: Sequence[float], scale: float = 0.525547) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_072(values: Sequence[float], scale: float = 0.532847) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_073(values: Sequence[float], scale: float = 0.540146) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_074(values: Sequence[float], scale: float = 0.547445) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_075(values: Sequence[float], scale: float = 0.554745) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_076(values: Sequence[float], scale: float = 0.562044) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_077(values: Sequence[float], scale: float = 0.569343) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_078(values: Sequence[float], scale: float = 0.576642) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_079(values: Sequence[float], scale: float = 0.583942) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_080(values: Sequence[float], scale: float = 0.591241) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_081(values: Sequence[float], scale: float = 0.598540) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_082(values: Sequence[float], scale: float = 0.605839) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_083(values: Sequence[float], scale: float = 0.613139) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_084(values: Sequence[float], scale: float = 0.620438) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_085(values: Sequence[float], scale: float = 0.627737) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_086(values: Sequence[float], scale: float = 0.635036) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_087(values: Sequence[float], scale: float = 0.642336) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_088(values: Sequence[float], scale: float = 0.649635) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_089(values: Sequence[float], scale: float = 0.656934) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_090(values: Sequence[float], scale: float = 0.664234) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_091(values: Sequence[float], scale: float = 0.671533) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_092(values: Sequence[float], scale: float = 0.678832) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_093(values: Sequence[float], scale: float = 0.686131) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_094(values: Sequence[float], scale: float = 0.693431) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_095(values: Sequence[float], scale: float = 0.700730) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_096(values: Sequence[float], scale: float = 0.708029) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_097(values: Sequence[float], scale: float = 0.715328) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_098(values: Sequence[float], scale: float = 0.722628) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_099(values: Sequence[float], scale: float = 0.729927) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_100(values: Sequence[float], scale: float = 0.737226) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_101(values: Sequence[float], scale: float = 0.744526) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_102(values: Sequence[float], scale: float = 0.751825) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_103(values: Sequence[float], scale: float = 0.759124) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_104(values: Sequence[float], scale: float = 0.766423) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_105(values: Sequence[float], scale: float = 0.773723) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_106(values: Sequence[float], scale: float = 0.781022) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_107(values: Sequence[float], scale: float = 0.788321) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_108(values: Sequence[float], scale: float = 0.795620) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_109(values: Sequence[float], scale: float = 0.802920) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_110(values: Sequence[float], scale: float = 0.810219) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_111(values: Sequence[float], scale: float = 0.817518) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_112(values: Sequence[float], scale: float = 0.824818) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_113(values: Sequence[float], scale: float = 0.832117) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_114(values: Sequence[float], scale: float = 0.839416) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_115(values: Sequence[float], scale: float = 0.846715) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_116(values: Sequence[float], scale: float = 0.854015) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_117(values: Sequence[float], scale: float = 0.861314) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_118(values: Sequence[float], scale: float = 0.868613) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_119(values: Sequence[float], scale: float = 0.875912) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_120(values: Sequence[float], scale: float = 0.883212) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_121(values: Sequence[float], scale: float = 0.890511) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_122(values: Sequence[float], scale: float = 0.897810) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_123(values: Sequence[float], scale: float = 0.905109) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_124(values: Sequence[float], scale: float = 0.912409) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_125(values: Sequence[float], scale: float = 0.919708) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_126(values: Sequence[float], scale: float = 0.927007) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_127(values: Sequence[float], scale: float = 0.934307) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_128(values: Sequence[float], scale: float = 0.941606) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_129(values: Sequence[float], scale: float = 0.948905) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_130(values: Sequence[float], scale: float = 0.956204) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_131(values: Sequence[float], scale: float = 0.963504) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_132(values: Sequence[float], scale: float = 0.970803) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_133(values: Sequence[float], scale: float = 0.978102) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_134(values: Sequence[float], scale: float = 0.985401) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_135(values: Sequence[float], scale: float = 0.992701) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_136(values: Sequence[float], scale: float = 1.000000) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_137(values: Sequence[float], scale: float = 1.007299) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_138(values: Sequence[float], scale: float = 1.014599) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_139(values: Sequence[float], scale: float = 1.021898) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_140(values: Sequence[float], scale: float = 1.029197) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_141(values: Sequence[float], scale: float = 1.036496) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_142(values: Sequence[float], scale: float = 1.043796) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_143(values: Sequence[float], scale: float = 1.051095) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_144(values: Sequence[float], scale: float = 1.058394) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_145(values: Sequence[float], scale: float = 1.065693) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_146(values: Sequence[float], scale: float = 1.072993) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_147(values: Sequence[float], scale: float = 1.080292) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_148(values: Sequence[float], scale: float = 1.087591) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_149(values: Sequence[float], scale: float = 1.094891) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_150(values: Sequence[float], scale: float = 1.102190) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_151(values: Sequence[float], scale: float = 1.109489) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_152(values: Sequence[float], scale: float = 1.116788) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_153(values: Sequence[float], scale: float = 1.124088) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_154(values: Sequence[float], scale: float = 1.131387) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_155(values: Sequence[float], scale: float = 1.138686) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_156(values: Sequence[float], scale: float = 1.145985) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_157(values: Sequence[float], scale: float = 1.153285) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_158(values: Sequence[float], scale: float = 1.160584) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_159(values: Sequence[float], scale: float = 1.167883) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_160(values: Sequence[float], scale: float = 1.175182) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_161(values: Sequence[float], scale: float = 1.182482) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_162(values: Sequence[float], scale: float = 1.189781) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_163(values: Sequence[float], scale: float = 1.197080) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_164(values: Sequence[float], scale: float = 1.204380) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_165(values: Sequence[float], scale: float = 1.211679) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_166(values: Sequence[float], scale: float = 1.218978) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_167(values: Sequence[float], scale: float = 1.226277) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_168(values: Sequence[float], scale: float = 1.233577) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_169(values: Sequence[float], scale: float = 1.240876) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_170(values: Sequence[float], scale: float = 1.248175) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_171(values: Sequence[float], scale: float = 1.255474) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_172(values: Sequence[float], scale: float = 1.262774) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_173(values: Sequence[float], scale: float = 1.270073) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_174(values: Sequence[float], scale: float = 1.277372) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_175(values: Sequence[float], scale: float = 1.284672) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_176(values: Sequence[float], scale: float = 1.291971) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_177(values: Sequence[float], scale: float = 1.299270) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_178(values: Sequence[float], scale: float = 1.306569) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_179(values: Sequence[float], scale: float = 1.313869) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_180(values: Sequence[float], scale: float = 1.321168) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_181(values: Sequence[float], scale: float = 1.328467) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_182(values: Sequence[float], scale: float = 1.335766) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_183(values: Sequence[float], scale: float = 1.343066) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_184(values: Sequence[float], scale: float = 1.350365) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_185(values: Sequence[float], scale: float = 1.357664) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_186(values: Sequence[float], scale: float = 1.364964) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_187(values: Sequence[float], scale: float = 1.372263) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_188(values: Sequence[float], scale: float = 1.379562) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_189(values: Sequence[float], scale: float = 1.386861) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_190(values: Sequence[float], scale: float = 1.394161) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_191(values: Sequence[float], scale: float = 1.401460) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_192(values: Sequence[float], scale: float = 1.408759) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_193(values: Sequence[float], scale: float = 1.416058) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_194(values: Sequence[float], scale: float = 1.423358) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_195(values: Sequence[float], scale: float = 1.430657) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_196(values: Sequence[float], scale: float = 1.437956) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_197(values: Sequence[float], scale: float = 1.445255) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_198(values: Sequence[float], scale: float = 1.452555) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_199(values: Sequence[float], scale: float = 1.459854) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_200(values: Sequence[float], scale: float = 1.467153) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_201(values: Sequence[float], scale: float = 1.474453) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_202(values: Sequence[float], scale: float = 1.481752) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_203(values: Sequence[float], scale: float = 1.489051) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_204(values: Sequence[float], scale: float = 1.496350) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_205(values: Sequence[float], scale: float = 1.503650) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_206(values: Sequence[float], scale: float = 1.510949) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_207(values: Sequence[float], scale: float = 1.518248) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_208(values: Sequence[float], scale: float = 1.525547) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_209(values: Sequence[float], scale: float = 1.532847) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_210(values: Sequence[float], scale: float = 1.540146) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_211(values: Sequence[float], scale: float = 1.547445) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_212(values: Sequence[float], scale: float = 1.554745) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_213(values: Sequence[float], scale: float = 1.562044) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_214(values: Sequence[float], scale: float = 1.569343) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_215(values: Sequence[float], scale: float = 1.576642) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_216(values: Sequence[float], scale: float = 1.583942) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_217(values: Sequence[float], scale: float = 1.591241) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_218(values: Sequence[float], scale: float = 1.598540) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_219(values: Sequence[float], scale: float = 1.605839) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_220(values: Sequence[float], scale: float = 1.613139) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_221(values: Sequence[float], scale: float = 1.620438) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_222(values: Sequence[float], scale: float = 1.627737) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_223(values: Sequence[float], scale: float = 1.635036) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_224(values: Sequence[float], scale: float = 1.642336) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_225(values: Sequence[float], scale: float = 1.649635) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_226(values: Sequence[float], scale: float = 1.656934) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_227(values: Sequence[float], scale: float = 1.664234) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_228(values: Sequence[float], scale: float = 1.671533) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_229(values: Sequence[float], scale: float = 1.678832) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_230(values: Sequence[float], scale: float = 1.686131) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_231(values: Sequence[float], scale: float = 1.693431) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_232(values: Sequence[float], scale: float = 1.700730) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_233(values: Sequence[float], scale: float = 1.708029) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_234(values: Sequence[float], scale: float = 1.715328) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_235(values: Sequence[float], scale: float = 1.722628) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_236(values: Sequence[float], scale: float = 1.729927) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_237(values: Sequence[float], scale: float = 1.737226) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_238(values: Sequence[float], scale: float = 1.744526) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_239(values: Sequence[float], scale: float = 1.751825) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_240(values: Sequence[float], scale: float = 1.759124) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_241(values: Sequence[float], scale: float = 1.766423) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_242(values: Sequence[float], scale: float = 1.773723) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_243(values: Sequence[float], scale: float = 1.781022) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_244(values: Sequence[float], scale: float = 1.788321) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_245(values: Sequence[float], scale: float = 1.795620) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_246(values: Sequence[float], scale: float = 1.802920) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_247(values: Sequence[float], scale: float = 1.810219) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_248(values: Sequence[float], scale: float = 1.817518) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_249(values: Sequence[float], scale: float = 1.824818) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_250(values: Sequence[float], scale: float = 1.832117) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_251(values: Sequence[float], scale: float = 1.839416) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_252(values: Sequence[float], scale: float = 1.846715) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_253(values: Sequence[float], scale: float = 1.854015) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_254(values: Sequence[float], scale: float = 1.861314) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_255(values: Sequence[float], scale: float = 1.868613) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_256(values: Sequence[float], scale: float = 1.875912) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_257(values: Sequence[float], scale: float = 1.883212) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_258(values: Sequence[float], scale: float = 1.890511) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_259(values: Sequence[float], scale: float = 1.897810) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_260(values: Sequence[float], scale: float = 1.905109) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_261(values: Sequence[float], scale: float = 1.912409) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_262(values: Sequence[float], scale: float = 1.919708) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_263(values: Sequence[float], scale: float = 1.927007) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_264(values: Sequence[float], scale: float = 1.934307) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_265(values: Sequence[float], scale: float = 1.941606) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_266(values: Sequence[float], scale: float = 1.948905) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_267(values: Sequence[float], scale: float = 1.956204) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_268(values: Sequence[float], scale: float = 1.963504) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_269(values: Sequence[float], scale: float = 1.970803) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_270(values: Sequence[float], scale: float = 1.978102) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_271(values: Sequence[float], scale: float = 1.985401) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_272(values: Sequence[float], scale: float = 1.992701) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_273(values: Sequence[float], scale: float = 2.000000) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_274(values: Sequence[float], scale: float = 2.007299) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_275(values: Sequence[float], scale: float = 2.014599) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_276(values: Sequence[float], scale: float = 2.021898) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_277(values: Sequence[float], scale: float = 2.029197) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_278(values: Sequence[float], scale: float = 2.036496) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_279(values: Sequence[float], scale: float = 2.043796) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_280(values: Sequence[float], scale: float = 2.051095) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_281(values: Sequence[float], scale: float = 2.058394) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_282(values: Sequence[float], scale: float = 2.065693) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_283(values: Sequence[float], scale: float = 2.072993) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_284(values: Sequence[float], scale: float = 2.080292) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_285(values: Sequence[float], scale: float = 2.087591) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_286(values: Sequence[float], scale: float = 2.094891) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_287(values: Sequence[float], scale: float = 2.102190) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_288(values: Sequence[float], scale: float = 2.109489) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_289(values: Sequence[float], scale: float = 2.116788) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_290(values: Sequence[float], scale: float = 2.124088) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_291(values: Sequence[float], scale: float = 2.131387) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_292(values: Sequence[float], scale: float = 2.138686) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_293(values: Sequence[float], scale: float = 2.145985) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_294(values: Sequence[float], scale: float = 2.153285) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_295(values: Sequence[float], scale: float = 2.160584) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_296(values: Sequence[float], scale: float = 2.167883) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_297(values: Sequence[float], scale: float = 2.175182) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_298(values: Sequence[float], scale: float = 2.182482) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_299(values: Sequence[float], scale: float = 2.189781) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_300(values: Sequence[float], scale: float = 2.197080) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_301(values: Sequence[float], scale: float = 2.204380) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_302(values: Sequence[float], scale: float = 2.211679) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_303(values: Sequence[float], scale: float = 2.218978) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_304(values: Sequence[float], scale: float = 2.226277) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_305(values: Sequence[float], scale: float = 2.233577) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_306(values: Sequence[float], scale: float = 2.240876) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_307(values: Sequence[float], scale: float = 2.248175) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_308(values: Sequence[float], scale: float = 2.255474) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_309(values: Sequence[float], scale: float = 2.262774) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_310(values: Sequence[float], scale: float = 2.270073) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_311(values: Sequence[float], scale: float = 2.277372) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_312(values: Sequence[float], scale: float = 2.284672) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_313(values: Sequence[float], scale: float = 2.291971) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_314(values: Sequence[float], scale: float = 2.299270) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_315(values: Sequence[float], scale: float = 2.306569) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_316(values: Sequence[float], scale: float = 2.313869) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_317(values: Sequence[float], scale: float = 2.321168) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_318(values: Sequence[float], scale: float = 2.328467) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_319(values: Sequence[float], scale: float = 2.335766) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_320(values: Sequence[float], scale: float = 2.343066) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_321(values: Sequence[float], scale: float = 2.350365) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_322(values: Sequence[float], scale: float = 2.357664) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_323(values: Sequence[float], scale: float = 2.364964) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_324(values: Sequence[float], scale: float = 2.372263) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_325(values: Sequence[float], scale: float = 2.379562) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_326(values: Sequence[float], scale: float = 2.386861) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_327(values: Sequence[float], scale: float = 2.394161) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_328(values: Sequence[float], scale: float = 2.401460) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_329(values: Sequence[float], scale: float = 2.408759) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_330(values: Sequence[float], scale: float = 2.416058) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_331(values: Sequence[float], scale: float = 2.423358) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_332(values: Sequence[float], scale: float = 2.430657) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_333(values: Sequence[float], scale: float = 2.437956) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_334(values: Sequence[float], scale: float = 2.445255) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_335(values: Sequence[float], scale: float = 2.452555) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_336(values: Sequence[float], scale: float = 2.459854) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_337(values: Sequence[float], scale: float = 2.467153) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_338(values: Sequence[float], scale: float = 2.474453) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_339(values: Sequence[float], scale: float = 2.481752) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_340(values: Sequence[float], scale: float = 2.489051) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_341(values: Sequence[float], scale: float = 2.496350) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_342(values: Sequence[float], scale: float = 2.503650) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_343(values: Sequence[float], scale: float = 2.510949) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_344(values: Sequence[float], scale: float = 2.518248) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_345(values: Sequence[float], scale: float = 2.525547) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_346(values: Sequence[float], scale: float = 2.532847) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_347(values: Sequence[float], scale: float = 2.540146) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_348(values: Sequence[float], scale: float = 2.547445) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_349(values: Sequence[float], scale: float = 2.554745) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_350(values: Sequence[float], scale: float = 2.562044) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_351(values: Sequence[float], scale: float = 2.569343) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_352(values: Sequence[float], scale: float = 2.576642) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_353(values: Sequence[float], scale: float = 2.583942) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_354(values: Sequence[float], scale: float = 2.591241) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_355(values: Sequence[float], scale: float = 2.598540) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_356(values: Sequence[float], scale: float = 2.605839) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_357(values: Sequence[float], scale: float = 2.613139) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_358(values: Sequence[float], scale: float = 2.620438) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


def kernel_359(values: Sequence[float], scale: float = 2.627737) -> float:
    if not values:
        return 0.0
    total = 0.0
    weight = scale
    for index, value in enumerate(values):
        centered = value - scale
        total += centered * centered / (index + 1.0 + weight)
    mean_value = sum(values) / len(values)
    penalty = abs(mean_value - scale) / (len(values) + 1.0)
    return total / len(values) + penalty


KERNEL_COUNT = 360
KERNEL_NAMES = tuple(f"kernel_{index:03d}" for index in range(KERNEL_COUNT))


def evaluate_kernel_bank(values: Sequence[float]) -> list[float]:
    return [globals()[name](values) for name in KERNEL_NAMES]


def summarize_kernel_bank(values: Sequence[float]) -> dict[str, float]:
    results = evaluate_kernel_bank(values)
    if not results:
        return {"min": 0.0, "max": 0.0, "mean": 0.0}
    return {"min": min(results), "max": max(results), "mean": sum(results) / len(results)}

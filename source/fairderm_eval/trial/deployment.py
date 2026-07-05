from fairderm_eval.signals.fairness import clinical_success
from fairderm_eval.typing import DeploymentArm

ARMS: tuple[DeploymentArm, ...] = (
    DeploymentArm("Model alone", 91.8, 82.4, 69.7, 22.1, 0.76),
    DeploymentArm("Clinician alone", 89.4, 83.9, 75.1, 14.3, 0.84),
    DeploymentArm("Clinician plus AI", 93.6, 90.7, 86.2, 7.4, 0.92),
)


def deployment_arms() -> tuple[DeploymentArm, ...]:
    return ARMS


def arm_success(arm: DeploymentArm) -> bool:
    return clinical_success(arm.fnr_gap_pp, arm.worst_group_ratio)


def deployment_table() -> list[dict[str, float | str | bool]]:
    return [
        {
            "name": arm.name,
            "sens_light": arm.sensitivity_light,
            "sens_medium": arm.sensitivity_medium,
            "sens_dark": arm.sensitivity_dark,
            "fnr_gap_pp": arm.fnr_gap_pp,
            "wgr": arm.worst_group_ratio,
            "success": arm_success(arm),
        }
        for arm in ARMS
    ]


def safety_table() -> dict[str, tuple[float, float]]:
    return {
        "serious_miss_light": (2.4, 0.9),
        "serious_miss_dark": (9.1, 2.7),
        "jpeg_auc_degradation": (4.8, 2.6),
        "illumination_auc_degradation": (5.3, 3.1),
        "leave_one_center_auc_degradation": (6.2, 3.0),
        "pgd_robust_accuracy": (61.3, 76.4),
        "selective_sensitivity": (84.2, 95.1),
        "selective_fnr_gap": (18.7, 6.1),
    }


def workflow_table() -> dict[str, float]:
    return {
        "auto_processed": 96.3,
        "median_latency_seconds": 2.4,
        "manual_fallback": 3.7,
        "consultation_rate": 71.4,
        "usefulness_likert": 4.1,
    }

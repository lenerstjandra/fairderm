from fairderm_eval.calib.ece import calibration_disparity_pp
from fairderm_eval.criteria.explanations import explanation_equity
from fairderm_eval.ledger.datasets import total_public_images
from fairderm_eval.signals.fairness import clinical_success


def headline_audit() -> dict[str, float | int | bool]:
    gpt5_fnr = 18.2
    gpt5_auc = 5.6
    team_fnr = 7.4
    team_wgr = 0.92
    return {
        "public_images": total_public_images(),
        "gpt5_fnr_gap_pp": gpt5_fnr,
        "gpt5_auc_gap_pp": gpt5_auc,
        "deployment_fnr_gap_pp": team_fnr,
        "deployment_wgr": team_wgr,
        "deployment_success": clinical_success(team_fnr, team_wgr),
    }


def combine_axes(
    fnr_gap_pp: float,
    auc_gap_pp: float,
    ece_light: float,
    ece_dark: float,
    faith_light: float,
    faith_dark: float,
) -> dict[str, float]:
    return {
        "diagnostic_gap": (fnr_gap_pp + auc_gap_pp) / 2.0,
        "calibration_gap": calibration_disparity_pp(ece_light, ece_dark),
        "explanation_gap": explanation_equity(faith_light, faith_dark),
    }

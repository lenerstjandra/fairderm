from fairderm_eval.orchestration.config import load_config, validate_config
from fairderm_eval.orchestration.train_loop import run_two_step


def test_two_step_training_runs() -> None:
    config = load_config("settings/testonly/two_step.yaml")
    validate_config(config)
    result = run_two_step(config)
    assert len(result.losses) == 2
    assert result.losses[-1] <= result.losses[0] + 0.5

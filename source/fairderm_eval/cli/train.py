import json
import sys

from fairderm_eval.orchestration.config import load_config, validate_config
from fairderm_eval.orchestration.train_loop import run_two_step


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    path = args[0] if args else "settings/testonly/two_step.yaml"
    config = load_config(path)
    validate_config(config)
    result = run_two_step(config)
    sys.stdout.write(json.dumps({"losses": result.losses, "seed": result.seed}, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import json
import sys

from fairderm_eval.orchestration.audit import headline_audit
from fairderm_eval.orchestration.config import load_config, validate_config


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if args:
        config = load_config(args[0])
        validate_config(config)
    sys.stdout.write(json.dumps(headline_audit(), indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import json
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    path = Path(args[0]) if args else Path("records/tables/ddi_reference.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data["rows"]
    best = min(rows, key=lambda row: row["fnr_gap"])
    payload = {
        "rows": len(rows),
        "lowest_fnr_gap_model": best["model"],
        "fnr_gap": best["fnr_gap"],
    }
    sys.stdout.write(json.dumps(payload, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Dad Joke Showdown entry.

Writes the winning dad joke to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
with no trailing newline. Python standard library only, no network,
fully deterministic: byte-identical output on every run.
"""

import os
from pathlib import Path

JOKE = (
    "I told the family the thermostat stays at 72 degrees of separation "
    "— between me and anyone who touches it."
)


def main() -> int:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(
            f"JOKE must be 1-200 characters, got {len(JOKE)}"
        )
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

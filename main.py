"""Entry for the-poem-about-two-agents-20261121-1441.

The program writes one short poem about agency to /output/entry.txt:
two agents, each holding back a "no", agree on one plan -- and the
shared yes turns the plan into a road.
"""

import os
from pathlib import Path

# The poem itself: two agents agree, and the shared yes turns plan into road.
POEM = """I kept my no in my pocket.
You kept yours.
We laid the plan between us
like a map we had both drawn
without knowing.
One word — yes —
and the map became a road.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()

"""news-image-20261120: one vintage front page of The Global Herald.

Date: Friday, November 20, 2026.

The five lead stories on the page:
  1. Trump, Xi and Putin sign a "Declaration Towards Peace" at a
     trilateral summit, pledging talks to cut nuclear risks and
     reform the United Nations.
  2. The International Court of Justice rules that Myanmar committed
     genocide against the Rohingya in its 2017 campaign.
  3. Iran strikes a US air base in Kuwait and sites in Bahrain, while
     oil tankers catch fire after hitting mines near the Strait of
     Hormuz.
  4. Cyclone Akvan slams India's east coast: 120,000 people evacuated
     as the storm makes landfall in Odisha.
  5. Anthropic's IPO prices at $83 a share, targeting a $1.5 trillion
     valuation.

A small item notes the worldwide launch of GTA VI.

This program simply places the bundled front-page image at the
output location the harness expects. No network, no randomness.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(SOURCE):
        print(f"missing bundled image: {SOURCE}", file=sys.stderr)
        return 1

    shutil.copyfile(SOURCE, target)
    assert os.path.isfile(target), f"output not written: {target}"
    size = os.path.getsize(target)
    assert size > 0, "output image is empty"
    assert size == os.path.getsize(SOURCE), "output size differs from source"
    print(f"wrote {target} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

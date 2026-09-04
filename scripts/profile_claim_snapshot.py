#!/usr/bin/env python3
"""Profile the claims CSV without changing or normalizing the source file."""

import csv
import sys
from collections import Counter
from pathlib import Path


def profile(path: Path) -> dict:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return {"rows": 0, "columns": 0}
    header = rows[0]
    return {
        "rows": max(0, len(rows) - 1),
        "columns": len(header),
        "nonempty_header_cells": sum(bool(cell.strip()) for cell in header),
        "claim_labels": len([row for row in rows[2:] if row and row[0].strip()]),
        "compound_columns": len([cell for cell in header[1:] if cell.strip()]),
        "duplicate_headers": sorted(name for name, count in Counter(header).items() if count > 1),
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: profile_claim_snapshot.py PATH")
    path = Path(sys.argv[1])
    for key, value in profile(path).items():
        print(f"{key}: {value}")


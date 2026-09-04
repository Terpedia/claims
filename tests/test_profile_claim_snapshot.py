import csv
from pathlib import Path

from scripts.profile_claim_snapshot import profile


def test_profile_reads_claim_snapshot_shape(tmp_path: Path):
    source = tmp_path / "claims.csv"
    with source.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["", "", "alpha-pinene", "linalool"])
        writer.writerow(["", "109", "13", "7"])
        writer.writerow(["analgesic", "6", "x", ""])
    result = profile(source)
    assert result["rows"] == 2
    assert result["columns"] == 4
    assert result["claim_labels"] == 1
    assert result["compound_columns"] == 2


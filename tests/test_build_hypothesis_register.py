import csv
from pathlib import Path

from scripts.build_hypothesis_register import build_hypotheses


def test_promotional_rows_become_hypotheses(tmp_path: Path):
    claims = tmp_path / "claims.csv"
    claims.write_text(",,linalool,alpha-pinene\n,1,1,1\nanti-anxiety,1,x,\n")
    evidence = tmp_path / "evidence.csv"
    with evidence.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["compound", "receptor_gene", "evidence_status"])
        writer.writeheader()
        writer.writerow({"compound": "linalool", "receptor_gene": "GABRA/GABRB", "evidence_status": "candidate"})
    result = build_hypotheses(claims, evidence)
    assert len(result) == 1
    assert result[0]["effect_hypothesis"] == "anti-anxiety"
    assert result[0]["receptor_mechanism_status"] == "evidence_linked"
    assert result[0]["effect_support_status"] == "unresolved"


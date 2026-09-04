import csv
from pathlib import Path

from scripts.build_claims_terpene_matrix import build_matrix


def test_matrix_preserves_evidence_boundary(tmp_path: Path):
    hypotheses = tmp_path / "hypotheses.csv"
    hypotheses.write_text("hypothesis_id,effect_hypothesis,compound,promotional_source_count,receptor_mechanism_status,effect_support_status,claim_boundary,interpretation\nH0001,analgesic,linalool,1,evidence_linked,unresolved,boundary,linked\n")
    receptor_map = tmp_path / "receptors.csv"
    with receptor_map.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["compound", "candidate_receptor_or_family", "evidence_tier", "primary_source", "pmid", "doi", "terpedia_interpretation"])
        writer.writeheader()
        writer.writerow({"compound": "linalool", "candidate_receptor_or_family": "GABAA", "evidence_tier": "direct", "primary_source": "url", "pmid": "28680877", "doi": "doi", "terpedia_interpretation": "mechanism only"})
    result = build_matrix(hypotheses, receptor_map)
    assert result[0]["candidate_receptor_or_family"] == "GABAA"
    assert result[0]["pmid"] == "28680877"
    assert result[0]["effect_support_status"] == "unresolved"
    assert result[0]["uncertainty_boundary"] == "boundary"


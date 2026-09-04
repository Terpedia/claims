#!/usr/bin/env python3
"""Join the claim hypotheses to the compound-level receptor evidence map."""

import csv
import sys
from pathlib import Path


def build_matrix(hypotheses_path: Path, receptor_map_path: Path) -> list[dict[str, str]]:
    with hypotheses_path.open(newline="", encoding="utf-8-sig") as handle:
        hypotheses = list(csv.DictReader(handle))
    with receptor_map_path.open(newline="", encoding="utf-8-sig") as handle:
        receptor_map = {row["compound"].casefold(): row for row in csv.DictReader(handle)}
    rows = []
    for hypothesis in hypotheses:
        evidence = receptor_map.get(hypothesis["compound"].casefold(), {})
        rows.append({
            "hypothesis_id": hypothesis["hypothesis_id"],
            "effect_hypothesis": hypothesis["effect_hypothesis"],
            "compound": hypothesis["compound"],
            "promotional_source_count": hypothesis["promotional_source_count"],
            "candidate_receptor_or_family": evidence.get("candidate_receptor_or_family", "unresolved"),
            "receptor_evidence_tier": evidence.get("evidence_tier", "no compound-specific receptor evidence"),
            "primary_source": evidence.get("primary_source", ""),
            "pmid": evidence.get("pmid", ""),
            "doi": evidence.get("doi", ""),
            "receptor_mechanism_status": hypothesis["receptor_mechanism_status"],
            "effect_support_status": hypothesis["effect_support_status"],
            "uncertainty_boundary": hypothesis["claim_boundary"],
            "interpretation": evidence.get("terpedia_interpretation", hypothesis["interpretation"]),
        })
    return rows


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("usage: build_claims_terpene_matrix.py HYPOTHESES_CSV RECEPTOR_MAP_CSV OUTPUT_CSV")
    rows = build_matrix(Path(sys.argv[1]), Path(sys.argv[2]))
    output = Path(sys.argv[3])
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else ["hypothesis_id"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} claim–terpene matrix rows")


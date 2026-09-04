#!/usr/bin/env python3
"""Turn the promotional matrix into auditable, evidence-qualified hypotheses."""

import csv
import sys
from pathlib import Path


def load_receptor_evidence(path: Path) -> dict[str, list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        evidence = csv.DictReader(handle)
        result: dict[str, list[dict[str, str]]] = {}
        for row in evidence:
            result.setdefault(row["compound"].strip().casefold(), []).append(row)
        return result


def build_hypotheses(claims_path: Path, evidence_path: Path) -> list[dict[str, str]]:
    with claims_path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.reader(handle))
    if len(rows) < 3:
        return []

    compounds = [cell.strip() for cell in rows[0][2:] if cell.strip()]
    receptor_evidence = load_receptor_evidence(evidence_path)
    output = []
    number = 0
    for row in rows[2:]:
        effect = row[0].strip() if row else ""
        if not effect:
            continue
        for offset, compound in enumerate(compounds, start=2):
            if offset >= len(row) or row[offset].strip().casefold() != "x":
                continue
            number += 1
            matches = receptor_evidence.get(compound.casefold(), [])
            statuses = sorted({match.get("evidence_status", "").strip() for match in matches if match.get("evidence_status")})
            ids = sorted({match.get("receptor_gene", "").strip() for match in matches if match.get("receptor_gene")})
            output.append({
                "hypothesis_id": f"H{number:04d}",
                "effect_hypothesis": effect,
                "compound": compound,
                "promotional_source_count": row[1].strip() if len(row) > 1 else "",
                "receptor_evidence_rows": str(len(matches)),
                "receptor_genes": ";".join(ids),
                "receptor_evidence_statuses": ";".join(statuses),
                "receptor_mechanism_status": "evidence_linked" if matches else "unresolved",
                "effect_support_status": "unresolved",
                "interpretation": (
                    "Terpedia receptor evidence is linked to the compound; it does not establish this effect hypothesis."
                    if matches else
                    "No receptor evidence is linked in the current local Terpedia evidence set; this is not biological absence."
                ),
                "claim_boundary": "Promotional claim treated as a hypothesis; receptor association does not establish efficacy, causality, dose-response, or human relevance.",
            })
    return output


def write_register(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else ["hypothesis_id"]
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("usage: build_hypothesis_register.py CLAIMS_CSV RECEPTOR_EVIDENCE_CSV OUTPUT_CSV")
    register = build_hypotheses(Path(sys.argv[1]), Path(sys.argv[2]))
    write_register(register, Path(sys.argv[3]))
    print(f"wrote {len(register)} hypotheses")


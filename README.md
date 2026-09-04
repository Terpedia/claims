# Terpedia claims investigation

This repository is a focused workspace for investigating the newly added
Terpedia claims tables, especially whether compound-level claims can be
associated with protein receptors. Promotional rows are treated as hypotheses,
not established effects.

The central rule is: a claim-to-protein join is an evidence association, not
proof of binding, activation, inhibition, physiological effect, or human
relevance. Exact chemical identity, receptor identity, assay semantics,
provenance, and negative-result boundaries must remain visible.

## Current state

The local BigQuery project is `terpedia-489015`. Authentication is required
before running live queries. The claims table name is intentionally left as a
configuration value until the inventory query identifies the exact newly added
tables. Existing receptor-oriented tables include:

- `terpedia_raw.sair_protein_terpene_interactions`
- `terpedia_raw.sair_structures`
- `terpedia_core.chemical_identifier_map`

The source snapshot that motivated the work is maintained at
`../kb-source/sources/terpedia-google-sheet-claims-2026-06-26.csv`.

## Hypothesis register

Build a local register from the promotional matrix and the existing Terpedia
receptor evidence map:

```sh
python3 scripts/build_hypothesis_register.py \
  ../kb-source/sources/terpedia-google-sheet-claims-2026-06-26.csv \
  ../absinthe/data/receptor-interactome.csv \
  outputs/hypothesis-register.csv
```

The register deliberately reports two separate fields: `receptor_mechanism_status`
asks whether the compound has any linked receptor evidence, while
`effect_support_status` remains `unresolved` until the effect itself is
supported by appropriately scoped literature or assay data. This prevents a
receptor association from being promoted into an efficacy claim.

Build the joined, reviewable matrix:

```sh
python3 scripts/build_claims_terpene_matrix.py \
  data/hypothesis-register.csv data/receptor-hypothesis-map.csv \
  data/claims-terpene-matrix.csv
```

`data/claims-terpene-matrix.csv` is the main deliverable: one row per
promotional hypothesis with receptor candidates, evidence tier, PubMed/DOI
fields, effect-support status, and uncertainty boundary.

The prioritized experimental plan is in
[`data/hypotheses-to-test.csv`](data/hypotheses-to-test.csv). It specifies
falsifiable tests, controls, endpoints, and what positive or null results would
actually mean.

## Terpene bioassay review

The GCP-backed claim register is in
[`data/bioassay-claims-and-hypotheses.csv`](data/bioassay-claims-and-hypotheses.csv),
and the assay validation queue is in
[`data/bioassay-hypotheses-to-validate.csv`](data/bioassay-hypotheses-to-validate.csv).
The source snapshot and read-only query are maintained in the sibling
[`bioassay/`](../bioassay/) project. The PubChem BioAssay lookup is a coverage
resource: a nonzero assay count does not establish a positive terpene result,
and a zero count does not establish inactivity.

## First run

```sh
cp .env.example .env
python3 scripts/profile_claim_snapshot.py \
  ../kb-source/sources/terpedia-google-sheet-claims-2026-06-26.csv

# Discover claim-like tables and inspect their schemas.
bq --project_id=terpedia-489015 --use_legacy_sql=false \
  < queries/00_discover_claim_tables.sql
```

After setting `CLAIMS_TABLE` and confirming its schema, substitute the fully
qualified table names in `queries/01_claim_receptor_candidates.sql` and run it
with `bq query`. The query is deliberately a candidate generator: it requires
an identity bridge and carries an explicit evidence boundary into every row.

## Investigation sequence

1. Inventory the new tables and record row counts, timestamps, and schemas.
2. Determine whether claims name a compound, effect, target, source, or only a
   promotional category.
3. Resolve compound identity through stable IDs, InChIKey, or structure; do
   not join on display names alone.
4. Resolve receptors through a stable protein ID and preserve UniProt or
   source-record crosswalks.
5. Separate literature/assay evidence from SAIR interaction projections and
   docking or model predictions.
6. Report unresolved joins as unresolved coverage, never as biological absence.

## Planned outputs

- `notes/table-inventory.md` — live table/schema checkpoint.
- `outputs/claim-receptor-candidates.csv` — evidence-qualified candidate rows.
- `outputs/claim-receptor-summary.csv` — counts by claim, compound, receptor,
  evidence type, and join status.

The initial literature pass is recorded in
[`notes/receptor-research-2026-09.md`](notes/receptor-research-2026-09.md) and
the 17-compound candidate map is in
[`data/receptor-hypothesis-map.csv`](data/receptor-hypothesis-map.csv).

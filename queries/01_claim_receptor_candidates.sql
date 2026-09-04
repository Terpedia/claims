-- Template: replace {{CLAIMS_TABLE}} and the claim compound-ID expression
-- after schema inspection. In the join below, replace c.compound_id if the
-- new table uses a different identity column or a nested field.
-- This is an evidence association query, not a binding or activity claim.

WITH claims AS (
  SELECT * FROM `{{CLAIMS_TABLE}}`
),
protein_interactions AS (
  SELECT protein, SMILES, interaction_count, source_release,
         ingestion_run_id, manifest_uri, content_sha256
  FROM `terpedia-489015.terpedia_raw.sair_protein_terpene_interactions`
),
identifier_map AS (
  SELECT source_id, source_record_id, chebi_id, pubchem_cid, inchikey,
         smiles, mapping_method, mapping_confidence, validation_status
  FROM `terpedia-489015.terpedia_core.chemical_identifier_map`
)
SELECT
  c.*,
  m.source_id,
  m.source_record_id,
  m.chebi_id,
  m.pubchem_cid,
  m.inchikey,
  m.mapping_method,
  m.mapping_confidence,
  p.protein AS protein_id,
  p.interaction_count,
  p.source_release AS interaction_source_release,
  p.ingestion_run_id AS interaction_ingestion_run_id,
  p.manifest_uri AS interaction_manifest_uri,
  p.content_sha256 AS interaction_content_sha256,
  CASE
    WHEN p.protein IS NOT NULL THEN 'structure_or_identifier_join_candidate'
    WHEN m.source_record_id IS NOT NULL THEN 'compound_resolved_no_protein_join'
    ELSE 'compound_identity_unresolved'
  END AS join_status,
  'Candidate association only; does not establish binding, activity, direction, potency, or in-vivo relevance.'
    AS claim_boundary
FROM claims AS c
LEFT JOIN identifier_map AS m
  ON LOWER(CAST(c.compound_id AS STRING)) = LOWER(m.source_record_id)
LEFT JOIN protein_interactions AS p
  ON p.SMILES = m.smiles;

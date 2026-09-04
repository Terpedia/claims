-- Read-only inventory of tables whose names or columns suggest claim data.
-- Run with: bq --project_id=terpedia-489015 --use_legacy_sql=false < this_file

SELECT
  table_schema AS dataset_id,
  table_name,
  table_type,
  creation_time,
  row_count,
  size_bytes
FROM `terpedia-489015`.region-us.INFORMATION_SCHEMA.TABLES
WHERE REGEXP_CONTAINS(LOWER(table_name), r'(claim|assert|statement|evidence|effect|target|interaction)')
ORDER BY creation_time DESC;

SELECT
  table_schema AS dataset_id,
  table_name,
  column_name,
  data_type,
  is_nullable,
  ordinal_position
FROM `terpedia-489015`.region-us.INFORMATION_SCHEMA.COLUMNS
WHERE REGEXP_CONTAINS(LOWER(CONCAT(table_name, ' ', column_name)),
                      r'(claim|assert|statement|evidence|compound|molecule|target|receptor|protein|smiles|inchikey|pubchem|chebi)')
ORDER BY table_schema, table_name, ordinal_position;


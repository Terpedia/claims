# PR&P submission checklist

Source checked: official PR&P author guidelines, 4 September 2026.

## Manuscript

- [x] Title is informative and avoids unexplained abbreviations.
- [x] Abstract, keywords, introduction, methods, results, discussion, and conclusion are present.
- [x] Main text is 2,727 words, within the stated review range of 2,500–5,000 words.
- [x] Word manuscript artifact is generated and render-verified on letter-size pages.
- [x] Running title page includes page, table, figure, reference, section-word, and nonstandard-abbreviation counts.
- [x] References are consistent and linked to PubMed records.
- [x] Supporting data and code are linked.
- [x] No figures are included; the machine-readable Supporting Information Tables S1–S4 are listed in the upload manifest.

## Title page and declarations

- [x] Replace author and affiliation placeholders.
- [x] Add corresponding-author telephone, postal address, and institutional email.
- [ ] Add Susan Trapp’s affiliation, email, postal address, and ORCID.
- [x] Complete funding statement.
- [ ] Confirm Susan Trapp’s competing interests; Daniel’s disclosure is complete.
- [x] Add data availability statement.
- [x] Add ethics and patient-consent statements as not applicable.
- [x] Add permissions and clinical-trial statements as not applicable.
- [ ] Confirm CRediT roles for both authors; Susan Trapp is limited to
  Writing—review and editing unless corrected by the authors.
- [x] Add acknowledgements; author-specific confirmations remain flagged as [TO CONFIRM].

## Editorial package

- [ ] Obtain all-author approval of the final manuscript [TO CONFIRM].
- [ ] Confirm the work is not submitted or under consideration elsewhere [TO CONFIRM].
- [x] Create a cover letter with article rationale and author responsibility; no reviewers are suggested.
- [x] Confirmed that no previously published figures or tables are reproduced; no permissions are required.
- [x] Confirm the destination repository URL: https://github.com/Terpedia/claims (main branch; release version to be tagged before publication).
- [ ] Upload main text, title page, figures/tables, Supporting Information Tables S1–S4, and cover letter through Wiley Research Exchange.

## Scientific release gate

- [x] Corrected scope: 109 marked rows across 16 compounds from 17 source columns.
- [x] Compound-level receptor evidence is separated from effect-level support.
- [x] α-pinene and TRPV1 evidence are explicitly qualified.
- [x] Null database joins are not interpreted as biological absence.
- [x] Prioritized hypotheses include controls, endpoints, and interpretation boundaries.
- [x] Proposed classification is an evidence-based pharmacological perspective; the targeted literature pass is explicitly disclosed rather than presented as a systematic review.

## Automated verification

Run from the repository root:

```sh
python3 scripts/verify_submission_package.py
python3 scripts/verify_submission_package.py --strict
```

The first command checks the review-range word count, numbered manuscript
sections, evidence-table invariants, citation order, and presence of the
required package files. The strict command additionally requires the
corresponding-author contact fields to be completed; it should be the final
local gate before upload.

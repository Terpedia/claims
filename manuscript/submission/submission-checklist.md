# PR&P submission checklist

Source checked: official PR&P author guidelines, 4 September 2026.

## Manuscript

- [x] Title is informative and avoids unexplained abbreviations.
- [x] Abstract, keywords, introduction, methods, results, discussion, and conclusion are present.
- [x] Main text is approximately 2,575 words, within the stated review range of 2,500–5,000 words.
- [x] References are consistent and linked to PubMed records.
- [x] Supporting data and code are linked.
- [ ] Final figures/tables and legends are prepared as separate upload files if requested.

## Title page and declarations

- [ ] Replace author and affiliation placeholders.
- [ ] Add corresponding-author postal address, telephone, institutional email, and ORCID.
- [ ] Complete funding statement.
- [ ] Complete conflict-of-interest disclosure.
- [x] Add data availability statement.
- [x] Add ethics and patient-consent statements as not applicable.
- [x] Add permissions and clinical-trial statements as not applicable.
- [ ] Complete CRediT author contributions.

## Editorial package

- [ ] Obtain all-author approval of the final manuscript.
- [ ] Confirm the work is not submitted or under consideration elsewhere.
- [ ] Create a cover letter with article rationale, author responsibility, and suggested reviewers if desired.
- [ ] Confirm permissions for any reproduced material.
- [ ] Confirm the destination repository URL and persistent release/version.
- [ ] Upload main text, title page, figures/tables, supporting information, and cover letter through Wiley Research Exchange.

## Scientific release gate

- [x] Corrected scope: 109 marked rows across 16 compounds from 17 source columns.
- [x] Compound-level receptor evidence is separated from effect-level support.
- [x] α-pinene and TRPV1 evidence are explicitly qualified.
- [x] Null database joins are not interpreted as biological absence.
- [x] Prioritized hypotheses include controls, endpoints, and interpretation boundaries.
- [ ] Complete a systematic literature update if submitting as a full review rather than a perspective.

## Automated verification

Run from the repository root:

```sh
python3 scripts/verify_submission_package.py
```

This checks the review-range word count, numbered manuscript sections, and
presence of the required package files. It intentionally does not approve
author-specific placeholders.

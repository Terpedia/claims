# Submission package

This directory contains the materials needed to submit the manuscript to
*Pharmacology Research & Perspectives*.

The manuscript is positioned as a perspective because the current literature
search is targeted and hypothesis-generating rather than systematic. The
journal accepts perspectives and is interested in new pharmacological
hypotheses, mechanism of action, target identification, translational
pharmacology, and replication. The official author guidelines should be
checked again immediately before upload.

Before submission, complete every unchecked item in
[`submission-checklist.md`](submission-checklist.md), especially author
identity, affiliation, contact details, funding, conflict-of-interest, CRediT,
repository URL, and final all-author approval. Reusable supplied author
metadata is recorded in [`../../author-profile.md`](../../author-profile.md).

The proposed upload set is itemized in
[`upload-manifest.md`](upload-manifest.md). The manuscript is Markdown for
version control, and the generated Word artifact has been rendered and
visually inspected for upload. Rebuild it with
`python3 scripts/build_manuscript_docx.py` after any source edit.

The upload-ready Word title page and cover letter are generated with
`python3 scripts/build_submission_docs.py`; their Markdown counterparts remain
the version-controlled source of truth.

The four CSV artifacts are cited in the manuscript as Supporting Information
Tables S1–S4; [`supporting-information.md`](supporting-information.md) supplies
their upload legends and table descriptions.

#!/usr/bin/env python3
"""Verify objective submission gates, with an optional strict metadata gate."""

import re
import sys
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "manuscript" / "terpene-structure-function-claims.md"
SUBMISSION = ROOT / "manuscript" / "submission"
DATA = ROOT / "data"


def main() -> int:
    text = MAIN.read_text(encoding="utf-8")
    main_text = text.split("## 9. References", 1)[0]
    words = len(re.findall(r"\b[\w’'-]+\b", main_text))
    assert 2500 <= words <= 5000, f"main text word count out of review range: {words}"
    abstract = text.split("## Abstract", 1)[1].split("## 1. Introduction", 1)[0]
    assert len(re.findall(r"\b[\w’'-]+\b", abstract)) <= 250, "abstract exceeds 250 words"
    required_sections = [
        "## Abstract", "## 1. Introduction", "## 2. Materials and methods",
        "## 3. Results", "## 4. Discussion", "## 5. Limitations and next experiments",
        "## 6. Conclusion", "## 7. Data and code", "## 8. Declarations", "## 9. References",
    ]
    assert all(section in text for section in required_sections)
    for filename in (
        "title-page.md", "title-page.docx", "cover-letter.md", "cover-letter.docx",
        "submission-checklist.md",
        "supporting-information.md", "upload-manifest.md",
        "terpene-structure-function-claims.docx",
    ):
        assert (SUBMISSION / filename).exists(), filename
    for filename in ("claims-terpene-matrix.csv", "receptor-hypothesis-map.csv", "hypotheses-to-test.csv", "hypothesis-register.csv"):
        assert (DATA / filename).exists(), filename
    with (DATA / "claims-terpene-matrix.csv").open(newline="", encoding="utf-8") as handle:
        matrix_rows = list(csv.DictReader(handle))
    assert len(matrix_rows) == 109, f"expected 109 matrix rows, found {len(matrix_rows)}"
    assert all(row.get("effect_support_status") == "unresolved" for row in matrix_rows)
    assert "Table 1." in main_text and "summarized in Table 1" in main_text
    assert "Supporting Information Tables S1–S4" in main_text
    citation_numbers = []
    for group in re.findall(r"\[([0-9]+(?:\s*,\s*[0-9]+)*)\]", main_text):
        citation_numbers.extend(int(value) for value in re.split(r"\s*,\s*", group))
    first_seen = []
    for number in citation_numbers:
        if number not in first_seen:
            first_seen.append(number)
    assert first_seen == list(range(1, 14)), f"references are not in first-appearance order: {first_seen}"
    reference_text = text.split("## 9. References", 1)[1]
    assert len(re.findall(r"(?m)^\d+\. ", reference_text)) == 13
    print(f"submission structure audit passed: {words} main-text words")
    placeholder_pattern = re.compile(
        r"\[(?:NAME, POSTAL ADDRESS, TELEPHONE, INSTITUTIONAL EMAIL|"
        r"REPOSITORY URL TO ADD|INSTITUTIONAL EMAIL)\]"
    )
    placeholders = []
    for filename in ("title-page.md", "cover-letter.md"):
        content = (SUBMISSION / filename).read_text(encoding="utf-8")
        if placeholder_pattern.search(content):
            placeholders.append(filename)
    if placeholders and "--strict" in sys.argv:
        raise AssertionError("author-specific placeholders remain in " + ", ".join(placeholders))
    if placeholders:
        print("author-specific placeholders remain in " + ", ".join(placeholders))
    else:
        print("author metadata placeholder audit passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Verify objective submission gates without requiring author-specific values."""

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "manuscript" / "terpene-structure-function-claims.md"
SUBMISSION = ROOT / "manuscript" / "submission"


def main() -> int:
    text = MAIN.read_text(encoding="utf-8")
    main_text = text.split("## 9. References", 1)[0]
    words = len(re.findall(r"\b[\w’'-]+\b", main_text))
    assert 2500 <= words <= 5000, f"main text word count out of review range: {words}"
    required_sections = [
        "## Abstract", "## 1. Introduction", "## 2. Materials and methods",
        "## 3. Results", "## 4. Discussion", "## 5. Limitations and next experiments",
        "## 6. Conclusion", "## 7. Data and code", "## 8. Declarations", "## 9. References",
    ]
    assert all(section in text for section in required_sections)
    for filename in ("title-page.md", "cover-letter.md", "submission-checklist.md"):
        assert (SUBMISSION / filename).exists(), filename
    print(f"submission structure audit passed: {words} main-text words")
    print("author-specific placeholders remain in title-page.md and cover-letter.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())


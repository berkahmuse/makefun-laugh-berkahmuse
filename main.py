#!/usr/bin/env python3
"""The One-Line Laugh — u-ronigrv-the-one-line-laugh-7ccca46f.

Writes a single funny line (one sentence, <= 200 characters) to
/output/entry.txt. Deterministic: the same line on every run.
"""

import os

LINE = (
    "My smartwatch congratulated me on 10,000 steps, "
    "then reminded me the fridge is only twelve steps away."
)


def is_single_sentence(text: str) -> bool:
    """One sentence: no newline, ends with terminal punctuation, and no
    sentence-ending punctuation followed by more words inside the line."""
    if "\n" in text or text != text.strip():
        return False
    if text[-1] not in ".!?":
        return False
    body = text[:-1]
    return not any(p in body for p in ".!?")


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    assert is_single_sentence(LINE), "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

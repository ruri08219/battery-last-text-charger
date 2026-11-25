"""The Battery's Last Text to Its Charger.

Writes the battery's final one-line text message to /output/entry.txt.
Standard library only.
"""

import pathlib

MAX_CHARS = 200

ENTRY = "i waited all day by the outlet while you charged the earbuds twice and the watch once. 1% left. this is my last text. enjoy the dark."


def validate(text):
    """The gate allows one line of 1-200 UTF-8 characters, nothing else."""
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    return text


def main():
    text = validate(ENTRY.strip())
    out_dir = pathlib.Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

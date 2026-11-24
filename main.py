"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line of last words a phone says as its battery hits
1 percent to entry.txt inside the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (default /output),
with no trailing newline.
"""

import os
import unicodedata

LINE = "I faked being at 1% for three hours just to watch you panic. Worth it."


def validate(text: str) -> None:
    """Reject anything that cannot be a valid one-line entry.

    The gate requires UTF-8 text of 1 to 199 characters, not only
    whitespace, as a single line. Control characters (Unicode
    categories Cc, Cf, Zl, Zp) are rejected too, so nothing smuggles
    in a line break or invisible formatting.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > 199:
        raise ValueError("entry must be at most 199 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    for char in text:
        if unicodedata.category(char) in ("Cc", "Cf", "Zl", "Zp"):
            raise ValueError("entry must not contain control characters")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    # Write atomically: a reader never sees a half-written entry.
    with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.replace(tmp_path, path)
    # Read the file back and confirm it holds exactly the validated line.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the validated line")
    validate(written)


if __name__ == "__main__":
    main()

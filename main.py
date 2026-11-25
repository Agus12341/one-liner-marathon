"""Entry for make.fun's One-Liner Marathon.

Writes one one-line joke to entry.txt in the folder named by the
MAKEFUN_OUTPUT_DIR environment variable (default "/output").
"""

import os

TEXT = "I pulled a muscle sleeping. Not during sleep - sleeping was the activity that injured me."


def write_entry(out_dir: str) -> str:
    """Write TEXT plus a trailing newline to entry.txt in out_dir.

    The competition gate requires entry.txt to be UTF-8 text of 1 to
    280 characters, so the joke is kept as a single short line.
    Returns the path written.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()

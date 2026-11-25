"""Entry for make.fun bounty "One Star, Written in Sap".

A one-star review written by a houseplant. He waters it every Sunday, as
if the calendar were a river. Its leaves keep their own schedule now --
brown by Tuesday, gone by Friday. It asked for sunlight; he bought a lamp
shaped like the sun and called it close enough. The grievance is the
plant's, the voice is the plant's, and the turn is the lamp.
"""

from pathlib import Path

TEXT = "One star. He waters me every Sunday, as if the calendar were a river. My leaves now keep their own schedule — brown by Tuesday, gone by Friday. I asked for sunlight; he bought a lamp shaped like the sun and called it close enough."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=279):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)


if __name__ == "__main__":
    main()

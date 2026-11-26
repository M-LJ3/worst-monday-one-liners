"""Write one funny line to /output/entry.txt.

The line is an entry for a one-line joke contest: how awful
Mondays are.
"""

import os


def joke_line():
    """Return one funny line about Mondays."""
    return (
        "Monday is the only day that shows up to work before you do, "
        "drinks your coffee, and still asks why you're late."
    )


def main():
    line = joke_line()
    os.makedirs("/output", exist_ok=True)
    # Write the joke with no trailing newline, exactly as entered.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    # Sanity check: the file must hold exactly the one joke line.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        assert handle.read() == line


if __name__ == "__main__":
    main()

import numpy as np

from aoc23.common.util import get_data_file_name


def _get_patterns(puzzle_input: list[str]) -> list[list[str]]:
    patterns = []
    pattern = []
    for row in puzzle_input:
        row = row.strip()
        if row == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(row)

    return patterns + [pattern]


def find_symmetrical_row(pattern: list[str]) -> int:
    for i in range(1, len(pattern)):
        top = pattern[:i]
        bottom = pattern[i:]
        window_size = min(len(top), len(bottom))

        top = top[-window_size:]
        bottom = reversed(bottom[:window_size])

        if all(t == b for t, b in zip(top, bottom)):
            return i

    return 0


def find_symmetrical_col(pattern: list[str]) -> int:
    transposed = np.transpose([[c for c in row] for row in pattern])
    return find_symmetrical_row(["".join(l) for l in transposed])


def fix_smudge(pattern: list[str]) -> list[str]:
    return pattern


def main():
    p1 = 0
    p2 = 0

    with open(get_data_file_name(13), "r") as fp:
        puzzle_input = [l.replace("\n", "") for l in fp.readlines()]

    patterns = _get_patterns(puzzle_input)

    for pattern in patterns:
        row = find_symmetrical_row(pattern)
        col = find_symmetrical_col(pattern)
        p1 += col + (100 * row)

        fixed_pattern = fix_smudge(pattern)
        row = find_symmetrical_row(fixed_pattern)
        col = find_symmetrical_col(fixed_pattern)
        p2 += col + (100 * row)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

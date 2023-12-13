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


def _rotate_pattern(pattern: list[str]) -> list[str]:
    transposed = np.transpose([[c for c in row] for row in pattern])
    return ["".join(l) for l in transposed]


def string_difference(a: str, b: str) -> int:
    diffs = 0
    for ac, bc in zip(a, b):
        diffs += 0 if ac == bc else 1
    return diffs


def find_symmetrical_row(pattern: list[str], exclude_row: int, max_diffs: int) -> int:
    for i in range(1, len(pattern)):
        if i == exclude_row:
            continue

        differences = 0
        window = 1
        window_limit = min(i, len(pattern) - i)
        is_line_of_symmetry = True

        while window <= window_limit:
            differences += string_difference(pattern[i + window - 1], pattern[i - window])
            is_line_of_symmetry = differences <= max_diffs
            if not is_line_of_symmetry:
                break
            window += 1

        if is_line_of_symmetry:
            return i

    return 0


def find_symmetry_with_differences(pattern: list[str], row: int, col: int, max_diffs: int) -> tuple[int, int]:
    new_row = find_symmetrical_row(pattern, row, max_diffs)
    new_col = 0 if new_row else find_symmetrical_row(_rotate_pattern(pattern), col, max_diffs)
    return (new_row, new_col)


def main():
    with open(get_data_file_name(13), "r") as fp:
        puzzle_input = [l.replace("\n", "") for l in fp.readlines()]

    answers = {0: 0, 1: 0}
    patterns = _get_patterns(puzzle_input)

    for pattern in patterns:
        row = -1
        col = -1
        for i in range(2):
            row, col = find_symmetry_with_differences(pattern, row, col, i)
            answers[i] += row * 100 + col

    for part, answer in answers.items():
        print(f"Part {part + 1}: {answer}")


if __name__ == "__main__":
    main()

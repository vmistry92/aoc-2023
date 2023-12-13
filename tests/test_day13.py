import pytest

from aoc23.solutions.day13 import find_symmetry_with_differences

PATTERNS = [
    [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
    ],
    [
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#",
    ],
]


@pytest.mark.parametrize("pattern,index", [(p, i) for p, i in zip(PATTERNS, [(0, 5), (4, 0)])])
def test_find_symmetry_with_no_differences(pattern, index):
    assert index == find_symmetry_with_differences(pattern, -1, -1, 0)


@pytest.mark.parametrize(
    "pattern,index,exclude_row,exclude_col",
    [(p, i, r, c) for p, i, r, c in zip(PATTERNS, [(3, 0), (1, 0)], [0, 4], [5, 0])],
)
def test_find_symmetry_with_1_difference(pattern, index, exclude_row, exclude_col):
    assert index == find_symmetry_with_differences(pattern, exclude_row, exclude_col, 1)

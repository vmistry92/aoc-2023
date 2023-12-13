from aoc23.solutions.day13 import find_symmetrical_col, find_symmetrical_row


def test_find_symmetrical_row():
    pattern = [
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#",
    ]
    assert 4 == find_symmetrical_row(pattern)


def test_find_symmetrical_col():
    pattern = [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
    ]
    assert 5 == find_symmetrical_col(pattern)

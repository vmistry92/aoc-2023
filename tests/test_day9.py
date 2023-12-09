import pytest

from aoc23.solutions.day9 import find_differences, find_next_value_in_sequence


def test_get_differences():
    assert [3, 3, 3] == find_differences([9, 12, 15, 18])


@pytest.mark.parametrize("expected,sequence", [(28, [1, 3, 6, 10, 15, 21]), (0, [21, 15, 10, 6, 3, 1])])
def test_find_next_value_in_sequence(expected, sequence):
    assert expected == find_next_value_in_sequence(sequence)

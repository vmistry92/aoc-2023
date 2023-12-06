import pytest

from aoc23.solutions.day6 import ways_to_win


@pytest.mark.parametrize("time,distance,ways", [(7, 9, 4), (15, 40, 8), (30, 200, 9)])
def test_ways_to_win(time, distance, ways):
    assert ways == ways_to_win(time, distance)

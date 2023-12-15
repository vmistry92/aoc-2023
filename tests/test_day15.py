import pytest

from aoc23.solutions.day15 import get_string_hash


@pytest.mark.parametrize(
    "item,expected_hash",
    [
        ("rn=1", 30),
        ("cm-", 253),
        ("qp=3", 97),
        ("cm=2", 47),
        ("qp-", 14),
        ("pc=4", 180),
        ("ot=9", 9),
        ("ab=5", 197),
        ("pc-", 48),
        ("pc=6", 214),
        ("ot=7", 231),
    ],
)
def test_get_string_hash(item, expected_hash):
    assert expected_hash == get_string_hash(item)

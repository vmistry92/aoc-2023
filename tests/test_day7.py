import pytest

from aoc23.solutions.day7 import HandType, get_hand_type


@pytest.mark.parametrize(
    "hand,hand_type",
    [
        ("AAAAA", HandType.FIVE_OF_A_KIND),
        ("AAAAK", HandType.FOUR_OF_KIND),
        ("AAAKK", HandType.FULL_HOUSE),
        ("AAAKQ", HandType.THREE_OF_A_KIND),
        ("AAKKQ", HandType.TWO_PAIR),
        ("AAKQJ", HandType.ONE_PAIR),
        ("AKQJ9", HandType.HIGH_CARD),
    ],
)
def test_get_hand_type(hand, hand_type):
    assert hand_type == get_hand_type(hand)

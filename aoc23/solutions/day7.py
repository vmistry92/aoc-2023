from enum import Enum

from aoc23.common.util import get_data_file_name


class HandType:
    FIVE_OF_A_KIND = 0
    FOUR_OF_KIND = 1
    FULL_HOUSE = 2
    THREE_OF_A_KIND = 3
    TWO_PAIR = 4
    ONE_PAIR = 5
    HIGH_CARD = 6


def get_hand_type(hand: str) -> HandType:
    cards = [c for c in hand]
    distinct_cards = {c: cards.count(c) for c in set(cards)}
    distinct_card_count = len(distinct_cards)

    if distinct_card_count == 1:
        return HandType.FIVE_OF_A_KIND

    if distinct_card_count == 2:
        return HandType.FOUR_OF_KIND if distinct_cards[cards[0]] in (1, 4) else HandType.FULL_HOUSE

    if distinct_card_count == 3:
        return HandType.THREE_OF_A_KIND if max(distinct_cards.values()) == 3 else HandType.TWO_PAIR

    return HandType.ONE_PAIR if distinct_card_count == 4 else HandType.HIGH_CARD


def main():
    p1 = 0
    card_ranks = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "1": 0,
    }

    with open(get_data_file_name(7), "r") as fp:
        hands = [line.replace("\n", "").split(" ") for line in fp.readlines()]
        hands = [(hand[0], int(hand[1]), get_hand_type(hand[0])) for hand in hands]
        hands = sorted(
            hands,
            key=lambda x: (
                -x[2],
                card_ranks[x[0][0]],
                card_ranks[x[0][1]],
                card_ranks[x[0][2]],
                card_ranks[x[0][3]],
                card_ranks[x[0][4]],
            ),
        )
        print(f"Part 1: {sum([(i + 1) * hand[1] for i, hand in enumerate(hands)])}")


if __name__ == "__main__":
    main()

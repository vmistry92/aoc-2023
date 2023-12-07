from copy import deepcopy

from aoc23.common.util import get_data_file_name

CARD_RANKS = {
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


class HandType:
    FIVE_OF_A_KIND = 6
    FOUR_OF_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


def get_hand_type(hand: str, j_is_wildcard: bool = False) -> HandType:
    cards = [c for c in hand]
    distinct_cards = {c: cards.count(c) for c in set(cards)}
    distinct_card_count = len(distinct_cards)
    hand_type = None

    if distinct_card_count == 1:
        hand_type = HandType.FIVE_OF_A_KIND
    elif distinct_card_count == 2:
        hand_type = HandType.FOUR_OF_KIND if distinct_cards[cards[0]] in (1, 4) else HandType.FULL_HOUSE
    elif distinct_card_count == 3:
        hand_type = HandType.THREE_OF_A_KIND if max(distinct_cards.values()) == 3 else HandType.TWO_PAIR
    elif distinct_card_count == 4:
        hand_type = HandType.ONE_PAIR
    else:
        hand_type = HandType.HIGH_CARD

    if not j_is_wildcard:
        return hand_type

    wildcards = len([c for c in hand if c == "J"])
    if wildcards == 0:
        return hand_type

    if wildcards >= 4:
        return HandType.FIVE_OF_A_KIND

    if wildcards == 3:
        if hand_type == HandType.THREE_OF_A_KIND:
            return HandType.FOUR_OF_KIND
        else:
            return HandType.FIVE_OF_A_KIND

    if wildcards == 2:
        if hand_type == HandType.FULL_HOUSE:
            return HandType.FIVE_OF_A_KIND
        if hand_type == HandType.TWO_PAIR:
            return HandType.FOUR_OF_KIND
        if hand_type in (HandType.HIGH_CARD, HandType.ONE_PAIR):
            return HandType.THREE_OF_A_KIND

    if wildcards == 1:
        if hand_type == HandType.FOUR_OF_KIND:
            return HandType.FIVE_OF_A_KIND
        if hand_type == HandType.THREE_OF_A_KIND:
            return HandType.FOUR_OF_KIND
        if hand_type == HandType.TWO_PAIR:
            return HandType.FULL_HOUSE
        if hand_type == HandType.ONE_PAIR:
            return HandType.THREE_OF_A_KIND
        if hand_type == HandType.HIGH_CARD:
            return HandType.ONE_PAIR

    raise NotImplementedError()


def part_1_hands_and_ranks(hands: list[str]):
    return [(hand[0], int(hand[1]), get_hand_type(hand[0], False)) for hand in hands], CARD_RANKS


def part_2_hands_and_ranks(hands: list[str]):
    ranks = deepcopy(CARD_RANKS)
    ranks["J"] = -1
    return [(hand[0], int(hand[1]), get_hand_type(hand[0], True)) for hand in hands], ranks


def main():
    with open(get_data_file_name(7), "r") as fp:
        hands = [line.replace("\n", "").split(" ") for line in fp.readlines()]
        for i in range(1, 3):
            hands, ranks = eval(f"part_{i}_hands_and_ranks(hands)")
            hands = sorted(
                hands,
                key=lambda x: (
                    x[2],
                    ranks[x[0][0]],
                    ranks[x[0][1]],
                    ranks[x[0][2]],
                    ranks[x[0][3]],
                    ranks[x[0][4]],
                ),
            )
            print(f"Part {i}: {sum([(i + 1) * hand[1] for i, hand in enumerate(hands)])}")


if __name__ == "__main__":
    main()

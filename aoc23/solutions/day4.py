from aoc23.common.util import get_data_file_name


def main() -> None:
    with open(get_data_file_name(4), "r") as fp:
        cards = fp.readlines()
        cards = [card.replace("\n", "") for card in cards]

    p1 = 0
    p2 = 0

    card_points = {}
    card_copies = {}

    for i, card in enumerate(cards):
        numbers = card.split(":")[1]
        card_numbers, winning_numbers = numbers.split("|")
        card_numbers = set([int(number.strip()) for number in card_numbers.split(" ") if number.strip() != ""])
        winning_numbers = set([int(number.strip()) for number in winning_numbers.split(" ") if number.strip() != ""])

        matched_numbers = card_numbers.intersection(winning_numbers)
        card_points[i] = 2 ** (len(matched_numbers) - 1) if matched_numbers else 0
        card_copies[i] = card_copies.get(i, 0) + 1

        for j in range(len(matched_numbers)):
            card_copies[i + j + 1] = card_copies.get((i + j + 1), 0) + card_copies[i]

    p1 = sum(card_points.values())
    p2 = sum(card_copies.values())

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

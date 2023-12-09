from aoc23.common.util import get_data_file_name


def find_differences(numbers: list[int]) -> list[int]:
    return [n - numbers[i] for i, n in enumerate(numbers[1:])]


def find_next_value_in_sequence(numbers: list[int]) -> int:
    differences = [numbers]
    difference = numbers
    all_zeros = False

    while not all_zeros:
        difference = find_differences(difference)
        differences.append(difference)
        all_zeros = set(difference) == {0}

    differences.reverse()

    for i, d in enumerate(differences[:-1]):
        differences[i + 1].append(d[-1] + differences[i + 1][-1])

    return differences[-1][-1]


def main() -> None:
    p1 = 0
    p2 = 0

    with open(get_data_file_name(9), "r") as fp:
        puzzle_input = [[int(n) for n in l.replace("\n", "").split(" ")] for l in fp.readlines()]

    for numbers in puzzle_input:
        p1 += find_next_value_in_sequence(numbers)
        numbers.reverse()
        p2 += find_next_value_in_sequence(numbers)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

from aoc23.common.util import get_data_file_name


def shift_rocks(
    loose_rocks: list[tuple[int, int]],
    fixed_rocks: list[tuple[int, int]],
    direction: tuple[int, int],
    max_y: int,
    max_x: int,
) -> list[tuple[int, int]]:
    sort_kwargs = {
        (0, -1): {"key": lambda x: x[1], "reverse": False},  # North
        (-1, 0): {"key": lambda x: x[0], "reverse": False},  # West
        (0, 1): {"key": lambda x: x[1], "reverse": True},  # South
        (1, 0): {"key": lambda x: x[0], "reverse": True},  # West
    }

    shifted_rocks = []
    loose_rocks = sorted(loose_rocks, **sort_kwargs[direction])

    for loose_rock in loose_rocks:
        can_move = True
        current_position = loose_rock

        while can_move:
            candidate_position = tuple(map(lambda i, j: i + j, current_position, direction))

            if not (0 <= list(candidate_position)[0] < max_x):
                can_move = False
                continue

            if not (0 <= list(candidate_position)[1] < max_y):
                can_move = False
                continue

            if candidate_position in shifted_rocks or candidate_position in fixed_rocks:
                can_move = False
                continue

            current_position = candidate_position

        shifted_rocks.append(current_position)

    return shifted_rocks


def main() -> None:
    p1 = 0
    p2 = 0

    with open(get_data_file_name(14), "r") as fp:
        puzzle_input = [l.replace("\n", "") for l in fp.readlines()]

    fixed_rocks = []
    loose_rocks = []
    max_y = len(puzzle_input)
    max_x = len(puzzle_input[0])

    for y, row in enumerate(puzzle_input):
        for x, c in enumerate(row):
            if c == ".":
                continue

            if c == "#":
                fixed_rocks.append((x, y))

            if c == "O":
                loose_rocks.append((x, y))

    shifted_rocks = loose_rocks
    rock_shift_strs = []
    cycle_start = -1
    i = 0

    while True:
        for direction in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            shifted_rocks = shift_rocks(shifted_rocks, fixed_rocks, direction, max_y, max_x)

            if i == 0 and direction == (0, -1):
                for shifted_rock in shifted_rocks:
                    p1 += max_y - list(shifted_rock)[1]
                print(f"Part 1: {p1}")

        rock_shift_str = "-".join(str(r) for r in shifted_rocks)

        if rock_shift_str in rock_shift_strs:
            cycle_start = rock_shift_strs.index(rock_shift_str)
            break

        rock_shift_strs.append(rock_shift_str)
        i += 1

    index = ((1000000000 - i) % (i - cycle_start)) + cycle_start - 1
    rock_shift_str = rock_shift_strs[index]
    shifted_rocks = [int(s[1:-1].split(", ")[1]) for s in rock_shift_str.split("-")]

    for shifted_rock in shifted_rocks:
        p2 += max_y - shifted_rock

    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

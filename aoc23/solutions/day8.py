from math import lcm

from aoc23.common.util import get_data_file_name


def steps_to_target(sequence: list[str], start: str, mapping: dict, part_2: bool) -> int:
    steps = 0
    current = start
    solved = False

    while not solved:
        tuple_index = 0 if sequence[steps % len(sequence)] == "L" else 1
        current = mapping[current][tuple_index]
        solved = current.endswith("Z") if part_2 else current == "ZZZ"
        steps += 1

    return steps


def main() -> None:
    with open(get_data_file_name(8), "r") as fp:
        puzzle_input = [l.replace("\n", "") for l in fp.readlines()]
        sequence = [c for c in puzzle_input[0].strip()]
        mapping = {
            puzzle_input[l].split(" = ")[0].strip(): puzzle_input[l].split(" = ")[1].strip()[1:-1].split(", ")
            for l in range(2, len(puzzle_input))
        }

        p1 = steps_to_target(sequence, "AAA", mapping, False)
        current_set = [k for k in mapping.keys() if k.endswith("A")]
        current_set_steps = [steps_to_target(sequence, c, mapping, True) for c in current_set]
        p2 = lcm(*current_set_steps)

        print(f"Part 1: {p1}")
        print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

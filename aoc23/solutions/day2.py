from functools import reduce
from operator import mul

from aoc23.common.util import get_data_file_name


def _get_game_id(game: str) -> int:
    return int(game.split(":")[0].split(" ")[1])


def _is_valid_game_p1(count: int, colour: str) -> bool:
    max_cubes = {"red": 12, "green": 13, "blue": 14}

    return count <= max_cubes[colour]


def main() -> None:
    with open(get_data_file_name(2), "r") as fp:
        games = fp.readlines()

    p1 = 0
    p2 = 0

    for game in games:
        game_id = _get_game_id(game)
        cube_sets = game.split(":")[1].split(";")
        min_colours = {}

        for cube_set in cube_sets:
            for cube in cube_set.split(","):
                count = int(cube.strip().split(" ")[0])
                colour = cube.strip().split(" ")[1]

                p1 += game_id if _is_valid_game_p1(count, colour) else 0

                min_colours[colour] = max(min_colours.get(colour, 0), count)

        p2 += reduce(mul, min_colours.values())

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

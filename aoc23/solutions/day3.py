from aoc23.common.constants import DIGIT_STRINGS
from aoc23.common.util import get_data_file_name


def _get_adjacent_cells(
    x: int, y: int, grid: list[list[str]], exclusion_list: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    max_y = len(grid)
    max_x = len(grid[0])

    adjacent_cells = []
    for yi in range(-1, 2):
        for xi in range(-1, 2):
            if xi == 0 and yi == 0:
                continue

            adjacent_x = x + xi
            adjacent_y = y + yi

            if not (0 <= adjacent_x < max_x):
                continue

            if not (0 <= adjacent_y < max_y):
                continue

            adjacent_cell = (adjacent_x, adjacent_y)
            if adjacent_cell not in exclusion_list:
                adjacent_cells.append(adjacent_cell)

    return adjacent_cells


def main() -> None:
    with open(get_data_file_name(3), "r") as fp:
        schematic = fp.readlines()
        schematic = [row.replace("\n", "") for row in schematic]
        schematic = [[c for c in row] for row in schematic]

        p1 = 0
        p2 = 0
        number_cells: list[tuple[int, list[tuple[int, int]]]] = []
        gear_cells: list[tuple[int, int]] = []
        number = ""

        for y, row in enumerate(schematic):
            for x, char in enumerate(row):
                if char == "*":
                    gear_cells.append((x, y))

                if char in DIGIT_STRINGS:
                    number += char

                end_of_row = x == len(row) - 1

                if char not in DIGIT_STRINGS or end_of_row:
                    if number == "":
                        continue

                    offset = 0 if (end_of_row and char in DIGIT_STRINGS) else -1
                    number_cells.append((int(number), [(xi + offset, y) for xi in range(x, x - len(number), -1)]))
                    number = ""

        cell_numbers = {}
        invalid_numbers = []
        invalid_symbols = ["."] + DIGIT_STRINGS
        for number, cells in number_cells:
            is_valid = False
            adjacent_cells = []
            for x, y in cells:
                adjacent_cells.extend(_get_adjacent_cells(x, y, schematic, cells))
                cell_numbers[(x, y)] = number

            adjacent_cells = set(adjacent_cells)
            for x, y in adjacent_cells:
                if schematic[y][x] not in invalid_symbols:
                    is_valid = True

            p1 += number if is_valid else 0

            if not is_valid:
                invalid_numbers.append((number, cells))

        for x, y in gear_cells:
            adjacent_cells = _get_adjacent_cells(x, y, schematic, [(x, y)])
            adjacent_numbers = list(
                set([cell_numbers[(xa, ya)] for xa, ya in adjacent_cells if (xa, ya) in cell_numbers])
            )

            if len(adjacent_numbers) == 2:
                p2 += adjacent_numbers[0] * adjacent_numbers[1]

        print(f"Part 1: {p1}")
        print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

from aoc23.common.util import get_data_file_name


class Heading:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


CAN_CONNECT = {
    "|": {Heading.NORTH, Heading.SOUTH},
    "-": {Heading.EAST, Heading.WEST},
    "L": {Heading.NORTH, Heading.EAST},
    "J": {Heading.NORTH, Heading.WEST},
    "7": {Heading.WEST, Heading.SOUTH},
    "F": {Heading.EAST, Heading.SOUTH},
    "S": {Heading.NORTH, Heading.SOUTH},
}


def get_opposite_heading(heading: Heading) -> Heading:
    return {
        Heading.NORTH: Heading.SOUTH,
        Heading.SOUTH: Heading.NORTH,
        Heading.EAST: Heading.WEST,
        Heading.WEST: Heading.EAST,
    }[heading]


def get_valid_connections(index: tuple[int, int], grid: list[list[int]]) -> list[tuple]:
    valid_connections = []
    cell_value = grid[index[1]][index[0]]

    if cell_value == ".":
        return valid_connections

    # We cheated we know from the input that S is |
    if cell_value == "S":
        cell_value = "|"

    max_y = len(grid)
    max_x = len(grid[0])

    compass = {
        (0, -1): Heading.NORTH,
        (0, 1): Heading.SOUTH,
        (1, 0): Heading.EAST,
        (-1, 0): Heading.WEST,
    }

    for offset, heading in compass.items():
        if not heading in CAN_CONNECT[cell_value]:
            continue

        # In bounds check
        adjacent_x = index[0] + offset[0]
        adjacent_y = index[1] + offset[1]
        if not (0 <= adjacent_x < max_x):
            continue

        if not (0 <= adjacent_y < max_y):
            continue

        adjacent_cell = grid[adjacent_y][adjacent_x]
        if get_opposite_heading(heading) in CAN_CONNECT[adjacent_cell]:
            valid_connections.append((adjacent_x, adjacent_y))

    return valid_connections


def find_start(grid: list[list[str]]) -> tuple[int, int]:
    starting_index = (-1, -1)
    start_found = False

    for yi, row in enumerate(grid):
        for xi, cell in enumerate(row):
            if cell in ("S"):
                starting_index = (xi, yi)
                start_found = True
                break

        if start_found:
            break

    print(f"Starting Index: {starting_index}")
    return starting_index


def main():
    p1 = 0
    p2 = 0

    with open(get_data_file_name(10), "r") as fp:
        grid = [[c for c in l.replace("\n", "")] for l in fp.readlines()]

    start = find_start(grid)
    visited = {start}
    to_visit = get_valid_connections(start, grid)

    while to_visit:
        p1 += 1
        adjacent_cells = []
        for cell in to_visit:
            visited.add(cell)
            adjacent_cells.extend(get_valid_connections(cell, grid))

        to_visit = [ac for ac in adjacent_cells if ac not in visited]

    # If the number of observed pipes in the row that can connect north and are on the path 
    # is odd then we know anything to the right is inside the loop. The start is a valid north 
    # pipe in the puzzle input as it is a | and |, J, L all have connections to the North.
    for yi, row in enumerate(grid):
        inside = False
        for xi, cell in enumerate(row):
            if (xi, yi) in visited:
                inside = not inside if cell in ("|", "J", "L", "S") else inside
            else:
                p2 += 1 if inside else 0

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

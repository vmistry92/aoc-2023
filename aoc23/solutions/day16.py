from aoc23.common.util import get_data_file_name


class Heading:
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)


def not_visited_with_heading(visited: dict, next_x: int, next_y: int, heading: Heading) -> bool:
    return not heading in visited.get((next_x, next_y), [])


def is_valid_move(current: tuple[int, int], heading: Heading, layout: list[list[str]], visited: dict[list]) -> bool:
    max_y = len(layout)
    max_x = len(layout[0])
    xi, yi = heading
    x, y = current

    in_bounds = 0 <= x + xi < max_x and 0 <= y + yi < max_y
    should_visit = heading not in visited.get((x + xi, y + yi), [])

    return in_bounds and should_visit


def next_directions(current: tuple[int, int], heading: tuple[int, int], layout: list[list[str]]) -> list[Heading]:
    x, y = current
    cell_value = layout[y][x]

    if cell_value == "|" and heading in (Heading.EAST, Heading.WEST):
        return [Heading.NORTH, Heading.SOUTH]
    elif cell_value == "-" and heading in (Heading.NORTH, Heading.SOUTH):
        return [Heading.EAST, Heading.WEST]
    elif cell_value == "/":
        if heading == Heading.NORTH:
            return [Heading.EAST]
        elif heading == Heading.EAST:
            return [Heading.NORTH]
        elif heading == Heading.SOUTH:
            return [Heading.WEST]
        else:
            return [Heading.SOUTH]
    elif cell_value == "\\":
        if heading == Heading.NORTH:
            return [Heading.WEST]
        elif heading == Heading.EAST:
            return [Heading.SOUTH]
        elif heading == Heading.SOUTH:
            return [Heading.EAST]
        else:
            return [Heading.NORTH]
    else:
        return [heading]


def walk_layout(layout: list[list[str]], start: tuple[int, int], heading: Heading) -> int:
    max_y = len(layout)
    max_x = len(layout[0])
    to_visit = [(start, heading)]
    visited = {}

    while to_visit:
        current, heading = to_visit.pop()
        current_x, current_y = current
        visited.update({(current_x, current_y): visited.get((current_x, current_y), []) + [heading]})

        next_headings = next_directions(current, heading, layout)
        for next_heading in next_headings:
            xi, yi = next_heading
            next_x = current_x + xi
            next_y = current_y + yi

            if (
                0 <= next_x < max_x
                and 0 <= next_y < max_y
                and not_visited_with_heading(visited, next_x, next_y, next_heading)
            ):
                to_visit.append(((next_x, next_y), next_heading))

    return len(visited)


def main() -> None:
    p1 = 0
    p2 = 0

    with open(get_data_file_name(16), "r") as fp:
        layout = [[c for c in l.replace("\n", "")] for l in fp.readlines()]

    p1 = walk_layout(layout, (0, 0), Heading.EAST)
    p2 = p1

    max_y = len(layout)
    max_x = len(layout[0])

    top_row = [(x, 0) for x in range(max_x)]
    bottom_row = [(x, max_y - 1) for x in range(max_x)]
    left_col = [(0, y) for y in range(max_y)]
    right_col = [(max_x - 1, y) for y in range(max_y)]

    sides = [top_row, bottom_row, left_col, right_col]
    headings = [Heading.SOUTH, Heading.NORTH, Heading.EAST, Heading.WEST]

    for side, heading in zip(sides, headings):
        for cell in side:
            p2 = max(p2, walk_layout(layout, cell, heading))

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

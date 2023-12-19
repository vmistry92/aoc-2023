from queue import Queue

from aoc23.common.util import get_data_file_name


def get_neighbors(puzzle_input: list[list[str]], current: tuple[int, int]) -> list[tuple[int, int]]:
    neighbors = []
    max_y = len(puzzle_input)
    max_x = len(puzzle_input[0])
    current_x, current_y = current

    for xi in range(-1, 2):
        for yi in range(-1, 2):
            if abs(xi) == abs(yi):
                continue

            next_x = current_x + xi
            next_y = current_y + yi

            if not -1 < next_x < max_x:
                continue

            if not -1 < next_y < max_y:
                continue

            neighbors.append((next_x, next_y))

    return neighbors


def breadth_first_search(puzzle_input: list[list[str]]) -> None:
    start = (0, 0)
    goal = (len(puzzle_input[0]) - 1, len(puzzle_input) - 1)

    frontier = Queue()
    frontier.put(start)

    came_from = dict()
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in get_neighbors(puzzle_input, current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)

    for y, row in enumerate(puzzle_input):
        print_row = ""
        for x, _ in enumerate(row):
            print_row += "#" if (x, y) in path else "."

        print(print_row)

    path_str = str(path.pop())
    for i, n in enumerate(reversed(path)):
        if i > 0 and i % 5 == 0:
            path_str += "\n"
        path_str += f" -> {str(n)}"

    print(path_str)


def main() -> None:
    with open(get_data_file_name(17), "r") as fp:
        puzzle_input = [[int(n) for n in l.replace("\n", "")] for l in fp.readlines()]

    p1 = 0
    p2 = 0

    breadth_first_search(puzzle_input)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

from queue import PriorityQueue

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


def dijkstra(puzzle_input: list[list[str]]) -> None:
    start = (0, 0)
    goal = (len(puzzle_input[0]) - 1, len(puzzle_input) - 1)

    frontier = PriorityQueue()
    frontier.put(start, 0)

    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in get_neighbors(puzzle_input, current):
            next_x, next_y = next
            new_cost = cost_so_far[current] + puzzle_input[next_y][next_x]
            if next not in came_from or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put(next, new_cost)
                came_from[next] = current

    # Trace the path backwards
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)

    # Modify the puzzle input to print
    for y, row in enumerate(puzzle_input):
        print_row = ""
        for x, _ in enumerate(row):
            print_row += "#" if (x, y) in path else "."

        print(print_row)

    # Print the graph and the path
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

    dijkstra(puzzle_input)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

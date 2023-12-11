from aoc23.common.util import get_data_file_name


def galaxy_distance(
    galaxy_a: tuple[int, int],
    galaxy_b: tuple[int, int],
    empty_rows: list[int],
    empty_cols: list[int],
    expansion_factor: int,
) -> int:
    x_offset = 0
    x_coordinates = sorted([galaxy_a[0], galaxy_b[0]])
    for x in range(x_coordinates[0], x_coordinates[1]):
        if x in empty_cols:
            x_offset += max(1, expansion_factor - 1)

    y_offset = 0
    y_coordinates = sorted([galaxy_a[1], galaxy_b[1]])
    for y in range(y_coordinates[0], y_coordinates[1]):
        if y in empty_rows:
            y_offset += max(1, expansion_factor - 1)

    return (x_coordinates[1] - x_coordinates[0]) + (y_coordinates[1] - y_coordinates[0]) + x_offset + y_offset


def get_galaxy_pairs(galaxies: list[tuple[int, int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    if not galaxies:
        return []

    pairs = [(galaxies[0], galaxy) for galaxy in galaxies[1:]]
    return pairs + get_galaxy_pairs(galaxies[1:])


def find_all_galaxies(universe: list[list[str]]) -> list[tuple[int, int]]:
    galaxies = []
    for yi, row in enumerate(universe):
        for xi, cell in enumerate(row):
            if cell == "#":
                galaxies.append((xi, yi))

    return galaxies


def find_empty_cols(grid: list[list[str]]) -> list[int]:
    empty_cols = []
    height = len(grid)  # max Y value
    width = len(grid[0])  # max X value

    for x in range(width):
        col_empty = True
        for y in range(height):
            if grid[y][x] != ".":
                col_empty = False
                break

        if col_empty:
            empty_cols.append(x)

    return empty_cols


def find_empty_rows(grid: list[list[str]]) -> list[int]:
    empty_rows = []
    for yi, row in enumerate(grid):
        if all(cell == "." for cell in row):
            empty_rows.append(yi)

    return empty_rows


def main() -> None:
    with open(get_data_file_name(11), "r") as fp:
        universe = [l.replace("\n", "") for l in fp.readlines()]
        empty_rows = find_empty_rows(universe)
        empty_cols = find_empty_cols(universe)
        galaxies = find_all_galaxies(universe)
        galaxy_pairs = get_galaxy_pairs(galaxies)

        for i, ef in enumerate([1, 1000000]):
            answer = sum(
                [galaxy_distance(galaxy_a, galaxy_b, empty_rows, empty_cols, ef) for galaxy_a, galaxy_b in galaxy_pairs]
            )
            print(f"Part {i + 1}: {answer}")


if __name__ == "__main__":
    main()

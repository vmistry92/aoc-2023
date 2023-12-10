from aoc23.common.util import get_data_file_name


def main() -> None:
    with open(get_data_file_name(11), "r") as fp:
        puzzle_input = [l.replace("\n", "") for l in fp.readlines()]


if __name__ == "__main__":
    main()

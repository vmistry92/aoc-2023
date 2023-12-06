from aoc23.common.util import get_data_file_name


def ways_to_win(time: int, distance: int) -> int:
    lower_bound = 0
    upper_bound = 0

    for i in range(time + 1):
        time_to_move = time - i
        speed = i
        distance_traveled = time_to_move * speed
        if distance_traveled > distance:
            lower_bound = i
            break

    for i in range(time, 0, -1):
        time_to_move = time - i
        speed = i
        distance_traveled = time_to_move * speed
        if distance_traveled > distance:
            upper_bound = i
            break

    return upper_bound - lower_bound + 1


def main():
    p1 = 1

    with open(get_data_file_name(6), "r") as fp:
        document = [line.replace("\n", "") for line in fp.readlines()]

    times = [t.strip() for t in document[0].split(":")[1].strip().split(" ") if not t == ""]
    distances = [d.strip() for d in document[1].split(":")[1].strip().split(" ") if not d == ""]

    p2_time = ""
    p2_distance = ""

    for time, distance in zip(times, distances):
        p2_time += time
        p2_distance += distance
        ways = ways_to_win(int(time), int(distance))
        p1 = p1 * (ways if ways > 0 else 1)

    print(f"Part 1: {p1}")
    print(f"Part 2: {ways_to_win(int(p2_time), int(p2_distance))}")


if __name__ == "__main__":
    main()

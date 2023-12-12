import re
from enum import StrEnum
from functools import cache

from aoc23.common.util import get_data_file_name


class SpringType(StrEnum):
    OPERATIONAL = "."
    DAMAGED = "#"
    UNKNOWN = "?"


def brute_force(record: str, damaged_counts: tuple[int]) -> int:
    permutations = [""]

    def is_valid(r: str, dc: tuple[int]) -> bool:
        to_process = r.replace(SpringType.OPERATIONAL, "A").replace(SpringType.DAMAGED, "B")
        regex = f"^A*{''.join([f'B{{{c}}}A+' for c in dc])}"[:-1] + "*$"
        re_match = re.search(regex, to_process)
        return re_match is not None

    for c in record:
        if c == SpringType.UNKNOWN:
            extended_permutations = []
            for p in permutations:
                extended_permutations.extend(
                    [
                        p + SpringType.DAMAGED,
                        p + SpringType.OPERATIONAL,
                    ]
                )
            permutations = extended_permutations
        else:
            permutations = [p + c for p in permutations]

    valid_permutations = set([p for p in permutations if is_valid(p, damaged_counts)])
    return len(valid_permutations)


@cache
def sliding_window(record: str, damaged_counts: tuple[int]) -> int:
    arrangements = 0
    counts = list(damaged_counts)
    window = counts[0]

    if len(counts) == 1:
        for check in range(len(record) - window + 1):
            end = check + window
            if check > 0 and record[check - 1] == SpringType.DAMAGED:
                break

            if SpringType.OPERATIONAL in record[check:end]:
                continue

            if SpringType.DAMAGED in record[end:]:
                continue

            arrangements += 1
        return arrangements

    for check in range(len(record) - sum(counts) - len(counts) + 2):
        end = check + window
        string_to_check = record[check:end]
        next_string = record[end + 1 :]

        if check > 0 and record[check - 1] == SpringType.DAMAGED:
            break

        if SpringType.OPERATIONAL in string_to_check:
            continue

        if record[end] == SpringType.DAMAGED:
            continue

        if sum(counts[1:]) < next_string.count(SpringType.DAMAGED):
            continue

        arrangements += sliding_window(next_string, tuple(counts[1:]))

    return arrangements


def main() -> None:
    method = sliding_window
    p1 = 0
    p2 = 0

    with open(get_data_file_name(12), "r") as fp:
        puzzle_input = [l.replace("\n", "") for l in fp.readlines()]

    for row in puzzle_input:
        record, damaged_counts = row.split(" ")
        damaged_counts = [int(count) for count in damaged_counts.split(",")]

        p1 += method(record, tuple(damaged_counts))
        p2 += method("?".join(record for _ in range(5)), tuple(damaged_counts) * 5)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

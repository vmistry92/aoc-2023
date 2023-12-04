from aoc23.common.constants import DIGIT_STRINGS, DIGIT_WORD_MAP
from aoc23.common.util import get_data_file_name


def _find_first_digit(line: str) -> str:
    for char in line:
        if char in DIGIT_STRINGS:
            return char
    raise Exception("No Digit Found")


def _find_last_digit(line: str) -> str:
    return _find_first_digit(line[::-1])


def _replace_digits(line: str) -> str:
    return_str = line
    for k, v in DIGIT_WORD_MAP.items():
        insert_index = int(len(k) / 2)
        return_str = return_str.replace(k, f"{k[:insert_index]}{v}{k[insert_index:]}")
    return return_str


def main() -> None:
    with open(get_data_file_name(1), "r") as fp:
        data = fp.readlines()

    p1_calibration_sum = 0
    p2_calibration_sum = 0

    for line in data:
        # Part 1
        p1_calibration_sum += int(f"{_find_first_digit(line)}{_find_last_digit(line)}")

        # Part 2
        p2_line = _replace_digits(line)
        calibration_value = int(f"{_find_first_digit(p2_line)}{_find_last_digit(p2_line)}")
        p2_calibration_sum += calibration_value

    print(f"Part 1: {p1_calibration_sum}")
    print(f"Part 2: {p2_calibration_sum}")


if __name__ == "__main__":
    main()

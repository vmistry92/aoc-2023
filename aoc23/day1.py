import os

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def _find_first_digit(line: str) -> str:
    for char in line:
        if char in digits.values():
            return char
    raise Exception("No Digit Found")


def _find_last_digit(line: str) -> str:
    return _find_first_digit(line[::-1])


def _replace_digits(line: str) -> str:
    return_str = line
    for k, v in digits.items():
        insert_index = int(len(k) / 2)
        return_str = return_str.replace(k, f"{k[:insert_index]}{v}{k[insert_index:]}")
    return return_str


def main() -> None:
    file_directory = os.path.dirname(__file__)
    data_file = os.path.join(file_directory, "../data/day1.txt")
    with open(data_file, "r") as fp:
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

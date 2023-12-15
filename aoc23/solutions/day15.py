from aoc23.common.util import get_data_file_name


def parse_string(item: str) -> tuple[int, str, int | None]:
    operation = "-" if "-" in item else "="
    label, lens = item.split(operation)
    return label, operation, (int(lens) if lens else None)


def get_string_hash(item: str) -> int:
    current_value = 0
    for code in item.encode("ascii"):
        current_value = ((current_value + code) * 17) % 256

    return current_value


def main() -> None:
    p1 = 0
    p2 = 0

    with open(get_data_file_name(15), "r") as fp:
        sequence = fp.readline().split(",")

    boxes: dict[int, dict] = {}

    for item in sequence:
        p1 += get_string_hash(item)
        label, operation, lens = parse_string(item)
        box_key = get_string_hash(label)
        box = boxes.get(box_key, {label: lens})

        if operation == "-" and label in box:
            box.pop(label)

        if operation == "=":
            box[label] = lens

        boxes.update({box_key: box})

    for box_key, box in boxes.items():
        p2 += sum([(box_key + 1) * (slot + 1) * focal_length for slot, focal_length in enumerate(box.values())])

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

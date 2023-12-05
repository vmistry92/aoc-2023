from aoc23.common.util import get_data_file_name


def process_mapping_name(line: str, mapping: dict) -> tuple[dict, dict]:
    name = line.split(" ")[0]
    mapping["name"] = name
    mapping["source"] = name.split("-")[0]
    mapping["destination"] = name.split("-")[2]
    mapping["ranges"] = []
    return mapping


def process_input(almanac: list[str]) -> tuple[list[int], list[dict]]:
    almanac = [line.replace("\n", "") for line in almanac]
    seeds = [int(seed) for seed in almanac[0].split(":")[1].strip().split(" ")]
    mappings = {}
    mapping = {}

    for i in range(2, len(almanac)):
        line = almanac[i]

        if line == "":
            mappings[mapping["name"]] = mapping
            mapping = {}
            continue

        if line.endswith("map:"):
            mapping = process_mapping_name(line, mapping)
            continue

        mapping_ranges = line.split(" ")
        offset = int(mapping_ranges[2]) - 1
        mapping["ranges"].append(
            {
                "destination_start": int(mapping_ranges[0]),
                "destination_end": int(mapping_ranges[0]) + offset,
                "source_start": int(mapping_ranges[1]),
                "source_end": int(mapping_ranges[1]) + offset,
            }
        )

    mappings[mapping["name"]] = mapping
    return seeds, mappings


def get_destination(source: int, ranges: list[dict]) -> int:
    for _range in ranges:
        if _range["source_start"] <= source <= _range["source_end"]:
            offset = _range["destination_start"] - _range["source_start"]
            return source + offset

    return source


def get_seed_location(seed: int, mappings: dict) -> int:
    route = {"seed": seed}
    source = seed

    for _, mapping in mappings.items():
        destination = get_destination(source, mapping["ranges"])
        route[mapping["destination"]] = destination
        source = destination

    return route["location"]


def main() -> None:
    p1 = 0
    p2 = 0

    with open(get_data_file_name(5), "r") as fp:
        almanac = fp.readlines()
        seeds, mappings = process_input(almanac)
        locations = [get_seed_location(seed, mappings) for seed in seeds]

        p1 = min(locations)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

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


def get_destination_ranges(source_range: dict[str, int], ranges: list[dict]) -> list[dict[str, int]]:
    destination_ranges = []
    ranges_to_process = [source_range]

    while ranges_to_process:
        range_to_process = ranges_to_process.pop()
        is_processed = False

        for mapping_range in ranges:
            if not (
                (mapping_range["source_start"] <= range_to_process["range_start"] <= mapping_range["source_end"])
                or (mapping_range["source_start"] <= range_to_process["range_end"] <= mapping_range["source_end"])
            ):
                continue

            offset = mapping_range["destination_start"] - mapping_range["source_start"]

            if (
                range_to_process["range_end"] <= mapping_range["source_end"]
                and range_to_process["range_start"] >= mapping_range["source_start"]
            ):
                offset = mapping_range["destination_start"] - mapping_range["source_start"]
                destination_ranges.append(
                    {
                        "range_start": range_to_process["range_start"] + offset,
                        "range_end": range_to_process["range_end"] + offset,
                    }
                )
                is_processed = True
                break

            if range_to_process["range_start"] < mapping_range["source_start"]:
                destination_ranges.append(
                    {
                        "range_start": mapping_range["destination_start"],
                        "range_end": range_to_process["range_end"] + offset,
                    }
                )
                ranges_to_process.append(
                    {"range_start": range_to_process["range_start"], "range_end": mapping_range["source_start"] - 1}
                )
                is_processed = True
                break

            if range_to_process["range_end"] > mapping_range["source_end"]:
                destination_ranges.append(
                    {
                        "range_start": range_to_process["range_start"] + offset,
                        "range_end": mapping_range["destination_end"],
                    }
                )
                ranges_to_process.append(
                    {"range_start": mapping_range["source_end"] + 1, "range_end": range_to_process["range_end"]}
                )
                is_processed = True
                break

        if not is_processed:
            destination_ranges.append(range_to_process)

    return destination_ranges


def get_seed_range_locations(seed_range: dict[str, int], mappings: dict) -> list:
    route = {"seed": seed_range}
    sources = [seed_range]
    for _, mapping in mappings.items():
        destinations = []
        for _range in sources:
            destinations.extend(get_destination_ranges(_range, mapping["ranges"]))

        route[mapping["destination"]] = destinations
        sources = destinations

    return sources


def main() -> None:
    p1 = 0
    p2 = 0

    with open(get_data_file_name(5), "r") as fp:
        almanac = fp.readlines()
        seeds, mappings = process_input(almanac)
        p1 = min([get_seed_location(seed, mappings) for seed in seeds])

        seed_ranges = [
            {"range_start": int(seeds[i]), "range_end": int(seeds[i]) + int(seeds[i + 1]) - 1}
            for i in range(0, len(seeds), 2)
        ]
        seed_range_locations = []
        for seed_range in seed_ranges:
            seed_range_locations.extend(get_seed_range_locations(seed_range, mappings))
        p2 = min([srl["range_start"] for srl in seed_range_locations])

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

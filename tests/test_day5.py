import pytest

from aoc23.common.util import get_data_file_name
from aoc23.solutions.day5 import get_destination, get_seed_location, process_input, process_mapping_name


@pytest.fixture
def sample_input() -> list[str]:
    with open(get_data_file_name(5, suffix="sample")) as fp:
        return fp.readlines()


def test_process_input_seeds(sample_input):
    seeds, _ = process_input(sample_input)
    assert seeds == [79, 14, 55, 13]


def test_process_mapping_name():
    line = "seed-to-soil map:"
    mapping = process_mapping_name(line, {})
    assert mapping == {
        "name": "seed-to-soil",
        "source": "seed",
        "destination": "soil",
        "ranges": [],
    }


def test_process_input_seed_to_soil_mapping_ranges(sample_input):
    _, mappings = process_input(sample_input)
    seed_to_soil_map = mappings["seed-to-soil"]
    assert seed_to_soil_map["ranges"] == [
        {"destination_start": 50, "destination_end": 51, "source_start": 98, "source_end": 99},
        {"destination_start": 52, "destination_end": 99, "source_start": 50, "source_end": 97},
    ]


@pytest.mark.parametrize("seed,location", [(79, 82), (14, 43), (55, 86), (13, 35)])
def test_get_seed_locations(seed, location, sample_input):
    _, mappings = process_input(sample_input)
    assert location == get_seed_location(seed, mappings)


@pytest.mark.parametrize("seed,soil", [(79, 81), (14, 14), (55, 57), (13, 13), (100, 100)])
def test_get_destinations_seed_to_soil(seed, soil, sample_input):
    _, mappings = process_input(sample_input)
    seed_to_soil_map = mappings["seed-to-soil"]
    assert soil == get_destination(seed, seed_to_soil_map["ranges"])

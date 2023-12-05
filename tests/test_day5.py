import pytest

from aoc23.common.util import get_data_file_name
from aoc23.solutions.day5 import get_destination_ranges, process_input, process_mapping_name


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


@pytest.mark.parametrize(
    "source_range,destination_ranges",
    [
        ({"range_start": 79, "range_end": 93}, [{"range_start": 81, "range_end": 95}]),
        (
            {"range_start": 90, "range_end": 105},
            [
                {"range_start": 92, "range_end": 99},
                {"range_start": 50, "range_end": 51},
                {"range_start": 100, "range_end": 105},
            ],
        ),
    ],
)
def test_get_destination_ranges(source_range, destination_ranges, sample_input):
    _, mappings = process_input(sample_input)
    seed_to_soil_map = mappings["seed-to-soil"]
    assert destination_ranges == get_destination_ranges(source_range, seed_to_soil_map["ranges"])

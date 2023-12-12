import pytest

from aoc23.solutions.day12 import brute_force, sliding_window


@pytest.mark.parametrize("implementation", (brute_force, sliding_window))
@pytest.mark.parametrize(
    "record,counts,arrangements",
    [
        ("???.###", (1, 1, 3), 1),
        (".??..??...?##.", (1, 1, 3), 4),
        ("?#?#?#?#?#?#?#?", (1, 3, 1, 6), 1),
        ("????.#...#...", (4, 1, 1), 1),
        ("????.######..#####.", (1, 6, 5), 4),
        ("?###????????", (3, 2, 1), 10),
    ],
)
def test_implementations_part_1_sample_data(record, counts, arrangements, implementation):
    assert arrangements == implementation(record, counts)


@pytest.mark.parametrize(
    "record,counts,arrangements",
    [
        ("???.###", (1, 1, 3), 1),
        (".??..??...?##.", (1, 1, 3), 16384),
        ("?#?#?#?#?#?#?#?", (1, 3, 1, 6), 1),
        ("????.#...#...", (4, 1, 1), 16),
        ("????.######..#####.", (1, 6, 5), 2500),
        ("?###????????", (3, 2, 1), 506250),
    ],
)
def test_sliding_window_part_2(record, counts, arrangements):
    assert arrangements == sliding_window("?".join([record for _ in range(5)]), counts * 5)

import pytest
from model import Almanac, Map, Seed, Soil


def test_add_section():
    m: Map[Seed, Soil] = Map()
    m.add_section(50, 98, 5)

    assert [r.eval() for r in m.segments.keys()] == [range(98, 103)]
    assert [r.eval() for r in m.segments.values()] == [range(50, 55)]


def test_add_section_2():
    m: Map[Seed, Soil] = Map()
    m.add_section(52, 50, 48)

    assert [r.eval() for r in m.segments.keys()] == [range(50, 98)]
    assert [r.eval() for r in m.segments.values()] == [range(52, 100)]

@pytest.fixture
def test_input():
    return (
        "seeds: 79 14 55 13\n"
        "\n"
        "seed-to-soil map:\n"
        "50 98 2\n"
        "52 50 48\n"
        "\n"
        "soil-to-fertilizer map:\n"
        "0 15 37\n"
        "37 52 2\n"
        "39 0 15\n"
        "\n"
        "fertilizer-to-water map:\n"
        "49 53 8\n"
        "0 11 42\n"
        "42 0 7\n"
        "57 7 4\n"
        "\n"
        "water-to-light map:\n"
        "88 18 7\n"
        "18 25 70\n"
        "\n"
        "light-to-temperature map:\n"
        "45 77 23\n"
        "81 45 19\n"
        "68 64 13\n"
        "\n"
        "temperature-to-humidity map:\n"
        "0 69 1\n"
        "1 0 69\n"
        "\n"
        "humidity-to-location map:\n"
        "60 56 37\n"
        "56 93 4\n"
    )

def test_almanac_seeds_correct_p1(test_input: str):
    almanac = Almanac.load_file_content(test_input, "part1")
    assert list(almanac.seeds) == [79, 14, 55, 13]

def test_seed_count_p1(test_input: str):
    almanac = Almanac.load_file_content(test_input, "part1")
    assert almanac.seed_count == 4
    

def test_almanac_seeds_correct_p2(test_input: str):
    almanac = Almanac.load_file_content(test_input, "part2")
    assert list(almanac.seeds) == [*range(79, 92+1), *range(55, 67+1)]
    

def test_seed_count_p2(test_input: str):
    almanac = Almanac.load_file_content(test_input, "part2")
    assert almanac.seed_count == (93-79)+(68-55)

def test_almanacsegments_lengths_correct(test_input: str):
    almanac = Almanac.load_file_content(test_input, "part1")
    assert [len(thing.eval()) for thing in almanac.seed_to_soil.segments] == [2, 48]
    assert [len(thing.eval()) for thing in almanac.soil_to_fertilizer.segments] == [37, 2, 15]
    assert [len(thing.eval()) for thing in almanac.fertilizer_to_water.segments] == [8, 42, 7, 4]
    assert [len(thing.eval()) for thing in almanac.water_to_light.segments] == [7, 70]
    assert [len(thing.eval()) for thing in almanac.light_to_temperature.segments] == [23, 19, 13]
    assert [len(thing.eval()) for thing in almanac.temperature_to_humidity.segments] == [1, 69]
    assert [len(thing.eval()) for thing in almanac.humidity_to_location.segments] == [37, 4]
    

def test_almanac_seed_to_soil_example(test_input: str):
    almanac = Almanac.load_file_content(test_input, "part1")
    assert almanac.seed_to_soil[0] == 0
    assert almanac.seed_to_soil[1] == 1
    assert almanac.seed_to_soil[48] == 48
    assert almanac.seed_to_soil[49] == 49
    assert almanac.seed_to_soil[50] == 52
    assert almanac.seed_to_soil[51] == 53
    assert almanac.seed_to_soil[96] == 98
    assert almanac.seed_to_soil[97] == 99
    assert almanac.seed_to_soil[98] == 50
    assert almanac.seed_to_soil[99] == 51
    

def test_almanac_seed_to_soil_example2(test_input: str):
    almanac = Almanac.load_file_content(test_input, "part2")
    assert almanac.seed_to_soil[79] == 81
    assert almanac.seed_to_soil[14] == 14
    assert almanac.seed_to_soil[55] == 57
    assert almanac.seed_to_soil[13] == 13
    

def test_almanac_seed_to_location(test_input: str):
    almanac = Almanac.load_file_content(test_input, "part1")
    assert almanac.get_seed_location(79) == 82
    assert almanac.get_seed_location(14) == 43
    assert almanac.get_seed_location(55) == 86
    assert almanac.get_seed_location(13) == 35
    

def test_almanac_closest_seed(test_input: str):
    almanac = Almanac.load_file_content(test_input, "part1")
    assert almanac.lowest_seed_location() == 35

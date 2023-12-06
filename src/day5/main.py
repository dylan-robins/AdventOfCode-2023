from pathlib import Path

from model import Almanac

def part1():
    input_file = Path(__file__).parent / "input.txt"
    print(f"Loading part 1 from {input_file}...")

    almanac = Almanac.load_file_content(input_file.read_text(), "part1")

    result = almanac.lowest_seed_location()
    print("Result:", result)

    print("_" * 80)


def part2():
    input_file = Path(__file__).parent / "input.txt"
    print(f"Loading part 2 from {input_file}...")

    almanac = Almanac.load_file_content(input_file.read_text(), "part2")

    result = almanac.lowest_seed_location()
    print("Result:", result)

    print("_" * 80)


if __name__ == "__main__":
    part1()
    part2()

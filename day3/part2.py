from pathlib import Path
from itertools import groupby
from model import Part, Schematic

from debug import debug


def get_gear_ratios(parts: list[Part]):
    grouped_parts = groupby(parts, key=lambda p: p.coords)
    for k, g in grouped_parts:
        group = list(g)
        if group[0].symbol != '*':
            continue
        
        if len(group) == 2:
            yield group[0].part_number * group[1].part_number


def main():
    input_file = Path(__file__).parent / "input.txt"
    print(f"Loading real data from {input_file}...")

    schematic = Schematic.parse_printout(input_file.read_text())
    gear_ratios = get_gear_ratios(schematic.parts)

    result = sum(gear_ratios)
    print("Result:", result)

    print("_" * 80)


def test():
    example_data = (
        "467..114..\n"
        "...*......\n"
        "..35..633.\n"
        "......#...\n"
        "617*......\n"
        ".....+.58.\n"
        "..592.....\n"
        "......755.\n"
        "...$.*....\n"
        ".664.598..\n"
    )
    print("Example data:")

    schematic = Schematic.parse_printout(example_data)

    gear_ratios = get_gear_ratios(schematic.parts)

    result = sum(gear_ratios)
    expected = 467835
    print(f"{result=} | {expected=}")

    if result == expected:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        exit(1)
    print("_" * 80)


if __name__ == "__main__":
    test()
    main()

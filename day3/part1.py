from pathlib import Path

from model import Schematic


def main():
    input_file = Path(__file__).parent / "input.txt"
    print(f"Loading real data from {input_file}...")

    schematic = Schematic.parse_printout(input_file.read_text())

    result = sum(part.part_number for part in schematic.parts)
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

    for part in schematic.parts:
        print(part)

    result = sum(part.part_number for part in schematic.parts)
    expected = 4361
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

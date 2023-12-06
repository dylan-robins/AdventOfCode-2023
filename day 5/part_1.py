from pathlib import Path

from model import Almanac

def main():
    input_file = Path(__file__).parent / "input.txt"
    print(f"Loading real data from {input_file}...")

    almanac = Almanac.load_file_content(input_file.read_text())

    result = almanac.lowest_seed_location()
    print("Result:", result)

    print("_" * 80)


if __name__ == "__main__":
    main()
from pathlib import Path
from typing import Iterable


def get_first_digit(s: str) -> str:
    for char in s:
        if char.isdigit():
            return char
    raise ValueError(f"No digit was found in the string '{s}'")


def sum_calibration_values(lines: Iterable[str]) -> int:
    sum = 0
    for line in lines:
        calibration_digits = get_first_digit(line) + get_first_digit(line[::-1])
        sum += int(calibration_digits)

    return sum


def test():
    example_data = "1abc2\n" "pqr3stu8vwx\n" "a1b2c3d4e5f\n" "treb7uchet\n"
    print("Example data:")
    print(example_data, end="")

    lines = example_data.splitlines()
    result = sum_calibration_values(lines)
    expected = 142
    print(f"{result=} | {expected=}")

    if result == expected:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        exit(1)
    print("_" * 80)


def main():
    input_file = Path(__file__).parent / "input.txt"
    print(f"Real data from {input_file}:")
    lines = input_file.read_text().splitlines()
    print("Result:", sum_calibration_values(lines))
    print("_" * 80)


if __name__ == "__main__":
    test()
    main()

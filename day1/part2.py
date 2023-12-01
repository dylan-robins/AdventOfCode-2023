from pathlib import Path
from typing import Iterable, Literal, NamedTuple

_DEBUG = False

_ALL_DIGITS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


class MatchedDigit(NamedTuple):
    index: int
    digit: str


def debug(*args, indent=0, **kwargs):
    if _DEBUG:
        prefix = "### Debug:" + "    " * indent
        print(prefix, *args, **kwargs)


def get_first_numeric_digit(s: str, reverse: bool = False) -> MatchedDigit | None:
    if reverse:
        s = s[::-1]

    for index, char in enumerate(s):
        if char.isdigit():
            return MatchedDigit(index, char)

    return None


def get_first_text_digit(s: str, reverse: bool = False) -> MatchedDigit | None:
    if reverse:
        s = s[::-1]

    matches = []

    for digit, substring in enumerate(_ALL_DIGITS, start=1):
        if reverse:
            substring = substring[::-1]

        debug(f"Looking for {substring} in {s}", indent=1)

        if (pos := s.find(substring)) != -1:
            matches.append(MatchedDigit(pos, str(digit)))

    if not matches:
        return None
    return min(matches, key=lambda m: m.index)


def get_calibration_value(line: str, which: Literal["start", "end"] = "start") -> str:
    reverse = which == "end"
    debug(f"Processing line {line} ({reverse=})")

    start_numeric_match = get_first_numeric_digit(line, reverse)
    start_text_match = get_first_text_digit(line, reverse)

    # If both are found: compare indices to find first
    if start_numeric_match is not None and start_text_match is not None:
        if start_numeric_match.index < start_text_match.index:
            return start_numeric_match.digit
        else:
            return start_text_match.digit
    # If only numeric is found, use that
    elif start_numeric_match is not None:
        return start_numeric_match.digit
    # If only text is found, use that
    elif start_text_match is not None:
        return start_text_match.digit
    else:
        raise ValueError(f"No digit was found in the line '{line}'")


def sum_calibration_values(lines: Iterable[str]) -> int:
    sum = 0
    for line in lines:
        first = get_calibration_value(line, "start")
        last = get_calibration_value(line, "end")
        debug(f"{line}: {first=} ... {last=}")
        sum += int(first + last)
    return sum


def main():
    input_file = Path(__file__).parent / "input.txt"
    print(f"Real data from {input_file}:")
    lines = input_file.read_text().splitlines()
    print("Result:", sum_calibration_values(lines))
    print("_" * 80)


def test():
    example_data = (
        "two1nine\n"
        "eightwothree\n"
        "abcone2threexyz\n"
        "xtwone3four\n"
        "4nineeightseven2\n"
        "zoneight234\n"
        "7pqrstsixteen\n"
    )
    print("Example data:")
    print(example_data, end="")

    lines = example_data.splitlines()
    result = sum_calibration_values(lines)
    expected = 281
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

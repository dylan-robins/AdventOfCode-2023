from pathlib import Path

from model import Colour, Game, Handful, debug


def get_smallest_possible_handful(game: Game) -> Handful:
    return Handful(
        red=max(handful.red for handful in game.handfuls),
        green=max(handful.green for handful in game.handfuls),
        blue=max(handful.blue for handful in game.handfuls),
    )


def main():
    input_file = Path(__file__).parent / "input.txt"
    print(f"Loading real data from {input_file}...")

    lines = input_file.read_text().splitlines()
    games = [Game.parse_line(line) for line in lines]

    smallest_handfuls = [get_smallest_possible_handful(game) for game in games]

    print("Powers:", *(f"- {handful.power}" for handful in smallest_handfuls), sep="\n")

    result = sum(handful.power for handful in smallest_handfuls)
    print("Result:", result)

    print("_" * 80)


def test():
    example_data = (
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n"
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n"
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n"
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n"
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n"
    )
    print("Example data:")

    lines = example_data.splitlines()
    games = [Game.parse_line(line) for line in lines]
    for game in games:
        print(game)

    smallest_handfuls = [get_smallest_possible_handful(game) for game in games]

    print("Powers:", *(f"- {handful.power}" for handful in smallest_handfuls), sep="\n")

    result = sum(handful.power for handful in smallest_handfuls)

    expected = 2286
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

from pathlib import Path
from typing import Iterable

from model import Game, Handful


def get_valid_games(games: Iterable[Game], full_hand: Handful) -> Iterable[Game]:
    for game in games:
        is_valid = True
        for handful in game.handfuls:
            if (
                (handful.red > full_hand.red)
                or (handful.green > full_hand.green)
                or (handful.blue > full_hand.blue)
            ):
                is_valid = False
                break
        if is_valid:
            yield game


def main():
    input_file = Path(__file__).parent / "input.txt"
    print(f"Loading real data from {input_file}...")

    lines = input_file.read_text().splitlines()
    games = [Game.parse_line(line) for line in lines]

    full_hand = Handful(12, 13, 14)
    valid_games = list(get_valid_games(games, full_hand))

    print("Valid games:", *(f"- {game.id}" for game in valid_games), sep="\n")

    result = sum(game.id for game in valid_games)
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

    full_hand = Handful(12, 13, 14)
    valid_games = list(get_valid_games(games, full_hand))

    print("Valid games:", *(f"- {game.id}" for game in valid_games), sep="\n")

    result = sum(game.id for game in valid_games)
    expected = 8
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

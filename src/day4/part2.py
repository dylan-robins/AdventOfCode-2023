from pathlib import Path

from model import load_scratchcards, calc_won_card_ids


def main():
    input_file = Path(__file__).parent / "input.txt"
    print(f"Loading real data from {input_file}...")

    scratchcards = list(load_scratchcards(input_file.read_text().splitlines()))

    winnings = [
        [won_card.id for won_card in calc_won_card_ids(scratchcards, sc)]
        for sc in scratchcards
    ]
    flat_winnings = []
    for won_cards in winnings:
        flat_winnings.extend(won_cards)

    result = {sc.id: 1 + flat_winnings.count(sc.id) for sc in scratchcards}
    print("Result:", result)

    final_result = sum(result.values())
    print("Final result:", final_result)

    print("_" * 80)


def test():
    example_data = (
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n"
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n"
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n"
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n"
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n"
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n"
    )
    print("Example data:")

    scratchcards = list(load_scratchcards(example_data.splitlines()))

    winnings = [
        [won_card.id for won_card in calc_won_card_ids(scratchcards, sc)]
        for sc in scratchcards
    ]
    flat_winnings = []
    for won_cards in winnings:
        flat_winnings.extend(won_cards)
    print(flat_winnings)

    result = {sc.id: 1 + flat_winnings.count(sc.id) for sc in scratchcards}
    expected = {
        1: 1,
        2: 2,
        3: 4,
        4: 8,
        5: 14,
        6: 1,
    }
    print(f"{result=} | {expected=}")

    if result == expected:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        exit(1)

    final_result = sum(result.values())
    final_expected = 30

    if final_result == final_expected:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        exit(1)

    print("_" * 80)


if __name__ == "__main__":
    test()
    main()

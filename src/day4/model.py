from dataclasses import dataclass
import re
from typing import Iterable
from typing_extensions import Self


@dataclass
class ScratchCard:
    id: int
    winning: set[int]
    picked: set[int]

    @property
    def number_of_matches(self) -> int:
        return len(self.winning & self.picked)

    @property
    def points(self) -> int:
        return int(2 ** (self.number_of_matches - 1))

    @property
    def won_card_ids(self) -> Iterable[int]:
        for i in range(self.number_of_matches):
            yield self.id + i + 1

    @classmethod
    def from_line(cls, s: str) -> Self:
        mo = re.fullmatch(
            r"^Card\s+(?P<id>\d+):(?P<winning>[^|]+)\|(?P<picked>.*)$",
            s,
        )
        assert mo is not None
        return cls(
            id=int(mo["id"]),
            winning={int(i) for i in mo["winning"].split()},
            picked={int(i) for i in mo["picked"].split()},
        )


def load_scratchcards(lines: list[str]) -> Iterable[ScratchCard]:
    for line in lines:
        yield ScratchCard.from_line(line)


def calc_won_card_ids(all_cards: list[ScratchCard], card: ScratchCard) -> Iterable[int]:
    for won_card in card.won_card_ids:
        yield all_cards[won_card - 1]
        yield from calc_won_card_ids(all_cards, all_cards[won_card - 1])

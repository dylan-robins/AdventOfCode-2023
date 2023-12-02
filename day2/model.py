import re
from dataclasses import dataclass, field
from typing import Literal, TypeAlias, cast

from typing_extensions import Self

Colour: TypeAlias = Literal["red", "green", "blue"]

_DEBUG = False


def debug(*args, indent=0, **kwargs):
    if _DEBUG:
        prefix = "### Debug:" + "    " * indent
        print(prefix, *args, **kwargs)


@dataclass(repr=False)
class Handful:
    red: int
    green: int
    blue: int

    @classmethod
    def parse(cls, s: str) -> Self:
        debug(f"Parsing handful '{s}'", indent=2)
        colour_counts: dict[Colour, int] = {"blue": 0, "green": 0, "red": 0}

        for category in s.split(","):
            # remove spaces at start due to comma seperation and English grammar
            category = category.strip()

            debug(f"Parsing '{category}'", indent=3)
            count, colour_name = category.split(" ", maxsplit=1)

            debug(f"{colour_name=} {count=}", indent=4)
            colour_counts[cast(Colour, colour_name)] = int(count)

        return cls(**colour_counts)

    @property
    def power(self) -> int:
        return self.red * self.green * self.blue

    def __repr__(self) -> str:
        return f"rgb({self.red},{self.green},{self.blue})"


@dataclass
class Game:
    id: int
    handfuls: list[Handful] = field(default_factory=list)

    @classmethod
    def parse_line(cls, line: str) -> Self:
        debug(f"Parsing line '{line}'")
        id_mo = re.fullmatch(r"Game (?P<id>\d+): (?P<game_detail>.*)", line)
        assert id_mo is not None

        debug(f"Parsed id '{id_mo['id']}'", indent=1)
        debug(f"Parsed game_detail '{id_mo['game_detail']}'", indent=1)

        handfuls = [
            Handful.parse(handful) for handful in id_mo["game_detail"].split(";")
        ]

        return cls(int(id_mo["id"]), handfuls)

    def __repr__(self) -> str:
        return f"{self.id}: {'; '.join(repr(h) for h in self.handfuls)}"

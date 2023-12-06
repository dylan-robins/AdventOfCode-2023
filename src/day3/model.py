from dataclasses import dataclass, field
from typing import Iterable, NamedTuple, Self

from debug import debug


class Vec2D(NamedTuple):
    x: int
    y: int


@dataclass
class Part:
    symbol: str
    coords: Vec2D
    part_number: int = None


@dataclass
class Schematic:
    parts: list[Part] = field(default_factory=list)

    @classmethod
    def parse_printout(cls, printout: str) -> Self:
        """Parses the contents of a schematic printout

        Args:
            printout (str): The content of the schematic file

        Returns:
            Schematic: The list of Parts that make up the schematic
        """
        part_list: list[Part] = []
        lines = printout.splitlines()
        instance = cls()
        for y, line in enumerate(lines):
            debug(f"Parsing line {y}: '{line}'")
            for x, char in enumerate(line):
                debug(f"Parsing char {x}: '{char}'", indent=1)
                if not char.isalnum() and char != ".":
                    debug(f"{char} at {x}/{y} is a Part!'", indent=2)
                    part_numbers = set(cls.get_adjascent_numbers(lines, Vec2D(x, y)))
                    part_list.extend(
                        Part(char, Vec2D(x, y), part_number)
                        for part_number in part_numbers
                    )

        return cls(part_list)

    @classmethod
    def get_adjascent_numbers(
        cls, printout_lines: list[str], coords: Vec2D
    ) -> Iterable[int]:
        neighbours = []
        for x_off in [-1, 0, 1]:
            for y_off in [-1, 0, 1]:
                if x_off == 0 and y_off == 0:
                    continue
                neighbours.append(
                    Vec2D(coords.x + x_off, coords.y + y_off),
                )

        for neighbour_coords in neighbours:
            neighbour_value = printout_lines[neighbour_coords.y][neighbour_coords.x]
            if neighbour_value.isdigit():
                yield cls.get_full_number_from_index(
                    printout_lines[neighbour_coords.y], neighbour_coords.x
                )

    @staticmethod
    def get_full_number_from_index(line: str, initial_index: int) -> int:
        start_index = initial_index
        end_index = initial_index
        # move backwards to find start
        while start_index > 0 and line[start_index - 1].isdigit():
            start_index -= 1
        # move forwards to find start
        while end_index < len(line) and line[end_index].isdigit():
            end_index += 1

        return int(line[start_index:end_index])

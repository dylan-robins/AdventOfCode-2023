from dataclasses import dataclass, field
import re
from typing import Generic, Literal, TypeAlias, TypeVar, NewType, cast

Seed: TypeAlias = NewType("Seed", int)
Soil: TypeAlias = NewType("Soil", int)
Fertilizer: TypeAlias = NewType("Fertilizer", int)
Water: TypeAlias = NewType("Water", int)
Light: TypeAlias = NewType("Light", int)
Temperature: TypeAlias = NewType("Temperature", int)
Humidity: TypeAlias = NewType("Humidity", int)
Location: TypeAlias = NewType("Location", int)

U = TypeVar(
    "U",
    Seed,
    Soil,
    Fertilizer,
    Water,
    Light,
    Temperature,
    Humidity,
    Location,
)

V = TypeVar(
    "V",
    Seed,
    Soil,
    Fertilizer,
    Water,
    Light,
    Temperature,
    Humidity,
    Location,
)


class Map(Generic[U, V]):
    def __init__(self) -> None:
        self._map: dict[U, V] = {}

    def add_section(self, dest_start: V, src_start: U, length: int):
        for i in range(length):
            self._map[src_start + i] = dest_start + i

    def __getitem__(self, key: U) -> V:
        if key in self._map:
            return self._map[key]
        # If it's not mapped, the destination is the same!
        return cast(V, key)


State = Literal[
    "scanning",
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


@dataclass
class Almanac:
    seeds: list[Seed] = field(default_factory=list)
    seed_to_soil: Map[Seed, Soil] = field(default_factory=Map)
    soil_to_fertilizer: Map[Soil, Fertilizer] = field(default_factory=Map)
    fertilizer_to_water: Map[Fertilizer, Water] = field(default_factory=Map)
    water_to_light: Map[Water, Light] = field(default_factory=Map)
    light_to_temperature: Map[Light, Temperature] = field(default_factory=Map)
    temperature_to_humidity: Map[Temperature, Humidity] = field(default_factory=Map)
    humidity_to_location: Map[Humidity, Location] = field(default_factory=Map)
    
    def get_seed_location(self, seed: Seed) -> Location:
        soil = self.seed_to_soil[seed]
        fert = self.soil_to_fertilizer[soil]
        water = self.fertilizer_to_water[fert]
        light = self.water_to_light[water]
        temp = self.light_to_temperature[light]
        hum = self.temperature_to_humidity[temp]
        loc = self.humidity_to_location[hum]
        return loc
    
    @property
    def lowest_seed_location(self) -> Seed:
        seed_locations = {seed: self.get_seed_location(seed) for seed in self.seeds}
        return min(seed_locations.values())

    @classmethod
    def load_file_content(cls, file_content: str):
        inst = cls()
        state: State = "scanning"
        for line in file_content.splitlines():
            if line.strip() == "":
                continue

            if line.startswith("seeds:"):
                inst.seeds = [int(i) for i in line.split(":")[1].split()]
                continue
            
            elif (mo := re.fullmatch(r"(?P<state>[\w-]+) map:", line)) is not None:
                state = mo["state"]
                continue

            numbers = [int(i) for i in line.split(maxsplit=3)]
            if state == "seed-to-soil":
                inst.seed_to_soil.add_section(*numbers)
            elif state == "soil-to-fertilizer":
                inst.soil_to_fertilizer.add_section(*numbers)
            elif state == "fertilizer-to-water":
                inst.fertilizer_to_water.add_section(*numbers)
            elif state == "water-to-light":
                inst.water_to_light.add_section(*numbers)
            elif state == "light-to-temperature":
                inst.light_to_temperature.add_section(*numbers)
            elif state == "temperature-to-humidity":
                inst.temperature_to_humidity.add_section(*numbers)
            elif state == "humidity-to-location":
                inst.humidity_to_location.add_section(*numbers)
        return inst

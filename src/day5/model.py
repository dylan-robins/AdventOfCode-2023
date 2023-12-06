from dataclasses import dataclass, field
import re
from typing import Generic, Iterator, Literal, TypeVar, NewType, cast

from tqdm import tqdm


Seed = NewType("Seed", int)
Soil = NewType("Soil", int)
Fertilizer = NewType("Fertilizer", int)
Water = NewType("Water", int)
Light = NewType("Light", int)
Temperature = NewType("Temperature", int)
Humidity = NewType("Humidity", int)
Location = NewType("Location", int)

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


@dataclass
class LazyRange(Generic[U]):
    start: U
    end: U
    
    def eval(self) -> range:
        return range(self.start, self.end)
    
    def get_index(self, val: U) -> int:
        if val not in self:
            raise ValueError(f"Value '{val}' is not in the range {self}")
        return val - self.start
    
    def get_value(self, index: int) -> U:
        return cast(U, self.start + index)
    
    def __repr__(self) -> str:
        return f"[{self.start},{self.end}["
    
    def __hash__(self) -> int:
        return hash(repr(self))
    
    def __contains__(self, val: U) -> bool:
        return self.start <= val < self.end


class Map(Generic[U, V]):
    def __init__(self) -> None:
        self.segments: dict[LazyRange[U], LazyRange[V]] = {}
        
    def add_section(self, dest_start: V, src_start: U, length: int):
        src_end = cast(U, src_start+length)
        dest_end = cast(V, dest_start+length)
        self.segments[LazyRange(src_start, src_end)] = LazyRange(dest_start, dest_end)

    def __getitem__(self, key: U) -> V:
        for src, dest in self.segments.items():
            if key in src:
                return dest.get_value(src.get_index(key))
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
    part: Literal["part1", "part2"]
    seed_to_soil: Map[Seed, Soil] = field(default_factory=Map)
    soil_to_fertilizer: Map[Soil, Fertilizer] = field(default_factory=Map)
    fertilizer_to_water: Map[Fertilizer, Water] = field(default_factory=Map)
    water_to_light: Map[Water, Light] = field(default_factory=Map)
    light_to_temperature: Map[Light, Temperature] = field(default_factory=Map)
    temperature_to_humidity: Map[Temperature, Humidity] = field(default_factory=Map)
    humidity_to_location: Map[Humidity, Location] = field(default_factory=Map)
    
    def __post_init__(self):
        self._seeds_raw: list[int] = []
        if self.part == "part1":
            self._seed_iterator = self.seed_iterator_p1
        else:
            self._seed_iterator = self.seed_iterator_p2
    
    @property
    def seeds(self) -> Iterator[Seed]:
        yield from self._seed_iterator()
    
    @seeds.setter
    def seeds(self, val: str) -> None:
        self._seeds_raw = [int(i) for i in val.split(":")[1].split()]
    
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
    def seed_count(self) -> int:
        if self.part == "part1":
            return len(self._seeds_raw)
        else:
            return sum(length for length in self._seeds_raw[1::2])
            
    
    def lowest_seed_location(self) -> Location | None:
        min_value: Location | None = None
        
        for seed in tqdm(self.seeds, total=self.seed_count, unit="seeds", smoothing=0):
            loc = self.get_seed_location(seed)
            if min_value is None or min_value > loc:
                min_value = loc
        
        return min_value
    
    def seed_iterator_p1(self) -> Iterator[Seed]:
        return iter(self._seeds_raw)
    
    def seed_iterator_p2(self) -> Iterator[Seed]:
        nums = iter(self._seeds_raw)
        for start in nums:
            length = next(nums)
            yield from range(start, start+length)

    @classmethod
    def load_file_content(cls, file_content: str, part: Literal["part1", "part2"]):
        inst = cls(part)
        state: State = "scanning"
        for line in file_content.splitlines():
            if line.strip() == "":
                continue

            if line.startswith("seeds:"):
                inst.seeds = line
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

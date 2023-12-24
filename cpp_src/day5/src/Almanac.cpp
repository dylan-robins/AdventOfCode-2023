#include "Almanac.h"

Location Almanac::get_seed_location(Seed seed) const
{
    auto soil = _seedToSoil[seed];
    auto fert = _soildToFertilizer[soil];
    auto water = _fertilizerToWater[fert];
    auto light = _waterToLight[water];
    auto temp = _lightToTemperature[light];
    auto hum = _temperatureToHumidity[temp];
    auto loc = _humidityToLocation[hum];
    return loc;
}
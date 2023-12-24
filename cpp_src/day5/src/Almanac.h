#pragma once

#include "map.h"

typedef int Seed;
typedef int Soil;
typedef int Fertilizer;
typedef int Water;
typedef int Light;
typedef int Temperature;
typedef int Humidity;
typedef int Location;

// seed_to_soil: Map[Seed, Soil]
// soil_to_fertilizer: Map[Soil, Fertilizer]
// fertilizer_to_water: Map[Fertilizer, Water]
// water_to_light: Map[Water, Light]
// light_to_temperature: Map[Light, Temperature]
// temperature_to_humidity: Map[Temperature, Humidity]
// humidity_to_location: Map[Humidity, Location]


class Almanac
{
private:
    Map _seedToSoil;
    Map _soildToFertilizer;
    Map _fertilizerToWater;
    Map _waterToLight;
    Map _lightToTemperature;
    Map _temperatureToHumidity;
    Map _humidityToLocation;

public:
    Location get_seed_location(Seed seed) const;
};
#pragma once

#include <vector>
#include <tuple>
#include "LazyRange.h"

struct RangeMapping {
    LazyRange src;
    LazyRange dest;
};

class Map
{
public:
    std::vector<RangeMapping> segments;
    void addSection(int srcStart, int destStart, int size);
    
    int operator [](int srcVal) const;
};

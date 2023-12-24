#include "map.h"
#include <stdexcept>

void Map::addSection(int srcStart, int destStart, int size)
{
    const auto srcRange = LazyRange(srcStart, srcStart+size);
    const auto destRange = LazyRange(destStart, destStart+size);

    for (auto &&mapping : segments) {
        if (! srcRange.isDisjoint(destRange))
        {
            throw std::range_error("Source and destination ranges are not disjoint!");
        }
    }
    

    segments.emplace_back(RangeMapping{srcRange, destRange});
}


int Map::operator[](int srcVal) const
{
    for (auto &&segment : segments)
    {
        if (segment.src.contains(srcVal))
        {
            auto index = segment.src.indexOf(srcVal);
            return segment.dest[index];
        }
    }
    // If not in any of the segments, it's a passthrough
    return srcVal;
}
#include "LazyRange.h"

LazyRange::LazyRange(const int start, const int end)
    : start(start), end(end) {
    if (start > end)
    {
        throw std::invalid_argument("End of the range must be greater than the start!");
    }
};

std::set<int> LazyRange::eval() const
{
    auto full_range = std::set<int>();
    for (int i = start; i < end; i++)
    {
        full_range.emplace(i);
    }
    
    return full_range;
}

bool LazyRange::contains(const int val) const
{
    return val >= start && val <= end;
}

int LazyRange::size() const
{
    return end - start + 1;
}

int LazyRange::operator[](const int offset) const
{
    return start + offset;
}

std::ostream &operator<<(std::ostream &stream, const LazyRange &range)
{
    return stream << "[" << range.start << "," << range.end << "]";
}

bool LazyRange::isDisjoint(const LazyRange& other) const
{
    return (this->end < other.start) || (this->start > other.end);
}

int LazyRange::indexOf(const int val) const
{
    return val - start;
}

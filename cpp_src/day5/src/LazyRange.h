#pragma once

#include <set>
#include <iostream>
#include <stdexcept>

class LazyRange
{
public:
    int start;
    int end;

    LazyRange(const int start, const int end);

    std::set<int> eval() const;
    
    bool contains(const int val) const;
    int indexOf(const int val) const;
    
    bool isDisjoint(const LazyRange& other) const;

    int size() const;

    int operator [](const int offset) const;
    friend std::ostream& operator<< (std::ostream& stream, const LazyRange& range);
};

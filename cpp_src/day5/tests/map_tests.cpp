#include <gtest/gtest.h>
#include <iostream>
#include "map.h"
#include <stdexcept>

TEST(map_simple, instanciation){
    auto map = Map();
    map.addSection(0, 100, 10);
    map.addSection(11, 1011, 15);

    EXPECT_EQ(map.segments.size(), 2);
}

TEST(map_simple, overlapping_sections){
    auto map = Map();
    map.addSection(0, 100, 100);

    EXPECT_THROW(
        map.addSection(50, 150, 100),
        std::range_error
    );
}

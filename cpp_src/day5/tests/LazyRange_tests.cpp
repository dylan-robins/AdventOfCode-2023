#include <gtest/gtest.h>
#include <iostream>
#include <sstream>
#include "LazyRange.h"

#include <tuple>

TEST(LazyRange_instanciation, simple){
    auto range = LazyRange(0, 5);
    EXPECT_EQ(range.start, 0);
    EXPECT_EQ(range.end, 5);
}

TEST(LazyRange_instanciation, inverted_dir){
    EXPECT_THROW(
        LazyRange(5, 0),
        std::invalid_argument
    );
}

TEST(LazyRange_size, simple){
    auto range = LazyRange(0, 5);
    EXPECT_EQ(range.size(), 6);
}

TEST(LazyRange_repr, simple){
    auto range = LazyRange(0, 5);
    auto repr = std::stringstream();
    repr << range;

    EXPECT_EQ(repr.str(), "[0,5]");
}

TEST(LazyRange_indexOf, 55){
    auto range = LazyRange(50, 60);
    EXPECT_EQ(range.indexOf(55), 5);
}

TEST(LazyRange_indexOf, 2){
    auto range = LazyRange(0, 5);
    EXPECT_EQ(range.indexOf(2), 2);
}


class LazyRange_disjoint : public ::testing::TestWithParam<std::tuple<LazyRange, LazyRange>> {};

TEST_P(LazyRange_disjoint, disjoint){
    std::tuple<LazyRange, LazyRange> params = GetParam();
    auto first = std::get<0>(params);
    auto second = std::get<1>(params);
    EXPECT_TRUE(first.isDisjoint(second));
}

INSTANTIATE_TEST_CASE_P(passing, LazyRange_disjoint, ::testing::Values(
  std::tuple<LazyRange, LazyRange>{LazyRange(0, 10), LazyRange(11, 50)},
  std::tuple<LazyRange, LazyRange>{LazyRange(50, 60), LazyRange(100, 150)}
));


class LazyRange_not_disjoint : public ::testing::TestWithParam<std::tuple<LazyRange, LazyRange>> {};

TEST_P(LazyRange_not_disjoint, disjoint){
    std::tuple<LazyRange, LazyRange> params = GetParam();
    auto first = std::get<0>(params);
    auto second = std::get<1>(params);
    EXPECT_FALSE(first.isDisjoint(second));
}

INSTANTIATE_TEST_CASE_P(failing, LazyRange_not_disjoint, ::testing::Values(
  std::tuple<LazyRange, LazyRange>{LazyRange(0, 10), LazyRange(9, 50)},
  std::tuple<LazyRange, LazyRange>{LazyRange(50, 60), LazyRange(0, 55)}
));

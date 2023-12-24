cmake_minimum_required(VERSION 3.15)
project(AoC_day5 CXX)
enable_testing()

find_package(GTest REQUIRED)

include_directories(BEFORE src)


add_library(LazyRange src/LazyRange.cpp)
add_library(Map src/map.cpp)

add_executable(AoC_day5 src/main.cpp)
add_dependencies(AoC_day5 GTest::gtest)
target_link_libraries(AoC_day5 GTest::gtest LazyRange)

add_executable(LazyRange_tests tests/LazyRange_tests.cpp)
add_dependencies(LazyRange_tests GTest::gtest)
target_link_libraries(LazyRange_tests GTest::gtest GTest::Main LazyRange)

add_executable(map_tests tests/map_tests.cpp)
add_dependencies(map_tests GTest::gtest)
target_link_libraries(map_tests GTest::gtest GTest::Main Map LazyRange)



install(TARGETS AoC_day5 DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )

add_test(NAME LazyRange_tests WORKING_DIRECTORY ${CMAKE_BINARY_DIR} COMMAND LazyRange_tests)
add_test(NAME map_tests WORKING_DIRECTORY ${CMAKE_BINARY_DIR} COMMAND map_tests)

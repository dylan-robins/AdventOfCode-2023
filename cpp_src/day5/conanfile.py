from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.build import check_max_cppstd, check_min_cppstd

class AoC_day5Recipe(ConanFile):
    name = "aoc_day5"
    version = "0.1"
    package_type = "application"

    # Optional metadata
    license = "MIT"
    author = "Dylan ROBINS dylan.robins@gmail.com"
    url = "https://github.com/dylan-robins/AdventOfCode-2023"
    description = "My solution to day 5 of the AoC 2023"
    topics = ("Advent of Code", "c++", "conan", "cmake")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "tests/*"
    
    def requirements(self):
        self.requires("gtest/1.14.0")

    def validate(self):
        check_min_cppstd(self, "11")
        check_max_cppstd(self, "20")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()
    

    

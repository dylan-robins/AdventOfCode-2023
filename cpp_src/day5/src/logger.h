#pragma once

#include <iostream>

#ifndef NDEBUG
#define DEBUG(x) do { std::cerr << __func__ << ":" << __LINE__ << " - " << x << std::endl; } while (0)
#else
#define DEBUG(x)
#endif

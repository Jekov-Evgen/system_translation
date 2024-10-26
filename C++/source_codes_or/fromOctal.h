#pragma once

#include <string>
#include <sstream>
#include <bitset>
#include <cstring>

extern "C" __declspec(dllexport) const char* octalToBinary(const char*);
extern "C" __declspec(dllexport) const char* octalToDemical(const char*);
extern "C" __declspec(dllexport) const char* octalToHexadecimal(const char*);

#pragma once
#include <string>
#include <sstream>
#include <bitset>
#include <cstring>

extern "C" __declspec(dllexport) const char* fromDecimalToBinary(const char*);
extern "C" __declspec(dllexport) const char* fromDecimalToOctal(const char*);
extern "C" __declspec(dllexport) const char* decimalToHexadecimal(const char*);

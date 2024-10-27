#pragma once
#include <string>
#include <sstream>
#include <cstring>


extern "C" __declspec(dllexport) const char* binaryToDecimal(const char*);
extern "C" __declspec(dllexport) const char* binaryToOctal(const char*);
extern "C" __declspec(dllexport) const char* binaryToHexadecimal(const char*);
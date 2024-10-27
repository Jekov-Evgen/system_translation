#include "pch.h"


extern "C" __declspec(dllexport) const char* octalToBinary(const char* octalNumber) {
    static std::string binary;
    int decimal = std::stoi(octalNumber, nullptr, 8);
    binary = std::bitset<32>(decimal).to_string();
    return binary.c_str();
}

extern "C" __declspec(dllexport) const char* octalToDemical(const char* octalNumber) {
    static std::string decimal_str;
    int decimal = std::stoi(octalNumber, nullptr, 8);
    decimal_str = std::to_string(decimal);
    return decimal_str.c_str();
}

extern "C" __declspec(dllexport) const char* octalToHexadecimal(const char* octalNumber) {
    static std::string hexadecimal_str;
    int decimal = std::stoi(octalNumber, nullptr, 8);
    std::stringstream hexadecimal;
    hexadecimal << std::hex << decimal;
    hexadecimal_str = hexadecimal.str();
    return hexadecimal_str.c_str();
}
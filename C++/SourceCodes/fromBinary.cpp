#include "pch.h"

extern "C" __declspec(dllexport) const char* binaryToDecimal(const char* binaryNumber) {
    int decimal = std::stoi(binaryNumber, nullptr, 2);
    std::string decimal_str = std::to_string(decimal);

    char* result = new char[decimal_str.size() + 1];
    strcpy_s(result, decimal_str.size() + 1, decimal_str.c_str());
    return result;
}

extern "C" __declspec(dllexport)const char* binaryToOctal(const char* binaryNumber) {
    int decimal = std::stoi(binaryNumber, nullptr, 2);
    std::stringstream octal;
    octal << std::oct << decimal;
    std::string octal_str = octal.str();

    char* result = new char[octal_str.size() + 1];
    strcpy_s(result, octal_str.size() + 1, octal_str.c_str()); 
    return result;
}

extern "C" __declspec(dllexport) const char* binaryToHexadecimal(const char* binaryNumber) {
    int decimal = std::stoi(binaryNumber, nullptr, 2);
    std::stringstream hexadecimal;
    hexadecimal << std::hex << decimal;
    std::string hex_str = hexadecimal.str();

    char* result = new char[hex_str.size() + 1];
    strcpy_s(result, hex_str.size() + 1, hex_str.c_str());
    return result;
}
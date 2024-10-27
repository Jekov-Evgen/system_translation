#include "pch.h"


extern "C" __declspec(dllexport) const char* fromDecimalToBinary(const char* decimalNumber) {
    int decimal = std::stoi(decimalNumber);
    std::string binary_str = std::bitset<32>(decimal).to_string();
    binary_str = binary_str.substr(binary_str.find('1')); 

    char* result = new char[binary_str.size() + 1];
    strcpy_s(result, binary_str.size() + 1, binary_str.c_str()); 
    return result;
}

extern "C" __declspec(dllexport) const char* fromDecimalToOctal(const char* decimalNumber) {
    int decimal = std::stoi(decimalNumber);
    std::stringstream octal;
    octal << std::oct << decimal;
    std::string octal_str = octal.str();

    char* result = new char[octal_str.size() + 1];
    strcpy_s(result, octal_str.size() + 1, octal_str.c_str()); 
    return result;
}

extern "C" __declspec(dllexport) const char* decimalToHexadecimal(const char* decimalNumber) {
    int decimal = std::stoi(decimalNumber);
    std::stringstream hexadecimal;
    hexadecimal << std::hex << decimal;
    std::string hex_str = hexadecimal.str();

    char* result = new char[hex_str.size() + 1];
    strcpy_s(result, hex_str.size() + 1, hex_str.c_str());
    return result;
}
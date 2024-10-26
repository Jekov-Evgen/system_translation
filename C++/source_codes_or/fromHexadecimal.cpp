#include "pch.h"


extern "C" __declspec(dllexport) const char* hexadecimalToBinary(const char* hexadecimalNumber) {
    int decimal = std::stoi(hexadecimalNumber, nullptr, 16);
    std::string binary_str = std::bitset<32>(decimal).to_string();
    binary_str = binary_str.substr(binary_str.find('1'));

    char* result = new char[binary_str.size() + 1];
    strcpy_s(result, binary_str.size() + 1, binary_str.c_str());
    return result;
}

extern "C" __declspec(dllexport) const char* hexadecimalToOctal(const char* hexadecimalNumber) {
    int decimal = std::stoi(hexadecimalNumber, nullptr, 16);
    std::stringstream octal;
    octal << std::oct << decimal;
    std::string octal_str = octal.str();

    char* result = new char[octal_str.size() + 1];
    strcpy_s(result, octal_str.size() + 1, octal_str.c_str());
    return result;
}

extern "C" __declspec(dllexport) const char* hexadecimalToDecimal(const char* hexadecimalNumber) {
    int decimal = std::stoi(hexadecimalNumber, nullptr, 16);
    std::string decimal_str = std::to_string(decimal);

    char* result = new char[decimal_str.size() + 1];
    strcpy_s(result, decimal_str.size() + 1, decimal_str.c_str());
    return result;
}
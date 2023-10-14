#include <string>

std::string createPhoneNumber(const int numbers[10]) {
    std::string formattedNumber;
    formattedNumber += "(" + std::to_string(numbers[0]) + std::to_string(numbers[1]) + std::to_string(numbers[2]) + ") ";
    formattedNumber += std::to_string(numbers[3]) + std::to_string(numbers[4]) + std::to_string(numbers[5]) + "-";
    formattedNumber += std::to_string(numbers[6]) + std::to_string(numbers[7]) + std::to_string(numbers[8]) + std::to_string(numbers[9]);

    return formattedNumber;
}

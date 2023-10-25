#include <string>

int solve(const std::string& s) {
    int largestNumber = 0;
    int currentNumber = 0;

    for (char c : s) {
        if (std::isdigit(c)) {
            currentNumber = currentNumber * 10 + (c - '0');
        } else {
            if (currentNumber > largestNumber) {
                largestNumber = currentNumber;
            }
            currentNumber = 0; 
        }
    }
    if (currentNumber > largestNumber) {
        largestNumber = currentNumber;
    }
    return largestNumber;
}
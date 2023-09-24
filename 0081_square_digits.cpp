#include <string>
#include <iostream>
#include <cmath>

int square_digits(int num) {
    std::string ans = "";
    std::string numStr = std::to_string(num);
    for (int i = 0; i < numStr.size(); i++) {
        char digit = numStr[i];
        int squared = (digit - '0') * (digit - '0');  
        ans += std::to_string(squared);
    }
    return std::stoi(ans);
}
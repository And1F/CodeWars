#include <string>
#include <iostream>
#include <sstream>
#include <vector>

std::string highAndLow(const std::string& numbers) {
    std::vector<int> numList;
    std::stringstream ss(numbers);
    int num;

    while (ss >> num) {
        numList.push_back(num);
    }
  
    int max = numList[0];
    int min = numList[0];

    for (int i = 1; i < numList.size(); i++) {
        if (numList[i] > max) {
            max = numList[i];
        }
        if (numList[i] < min) {
            min = numList[i];
        }
    }

    return std::to_string(max) + " " + std::to_string(min);
}
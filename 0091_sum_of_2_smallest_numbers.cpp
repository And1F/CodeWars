#include <iostream>
#include <vector>

long long sumTwoSmallestNumbers(std::vector<int> numbers){
    int min1 = INT_MAX;
    int min2 = INT_MAX;

    for (int num : numbers) {
        if (num < min1) {
            min2 = min1;
            min1 = num;
        } else if (num < min2) {
            min2 = num;
        }
    }
    return static_cast<long long>(min1) + min2;
}
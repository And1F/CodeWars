#include <vector>

std::vector<int> oddOnesOut(const std::vector<int>& numbers) {
    std::vector<int> count(101, 0); 
    for (int num : numbers) {
        count[num]++;
    }
    std::vector<int> result;
    for (int num : numbers) {
        if (count[num] % 2 == 0) {
            result.push_back(num);
        }
    }
    return result;
}

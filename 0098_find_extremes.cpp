#include <vector>

int betweenExtremes(const std::vector<int>& numbers) {
    int min = numbers[0]; 
    int max = numbers[0]; 

    for (int i = 1; i < numbers.size(); i++) {
        if (numbers[i] < min) {
            min = numbers[i];
        }
        if (numbers[i] > max) {
            max = numbers[i];
        }
    }

    return max - min;
}

#include <vector>

int stray(std::vector<int> numbers) {
    for (int i = 1; i < numbers.size() - 1; i++) {
        if (numbers[i] != numbers[i - 1] && numbers[i] != numbers[i + 1]) {
            return numbers[i];
        }
    }
    if (numbers[0] != numbers[1]) {
        return numbers[0];
    }
    return numbers.back();
}

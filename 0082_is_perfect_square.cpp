#include <cmath>

bool is_square(int n) {
    if (n < 0) {
        return false;
    }
    int sqt = static_cast<int>(std::sqrt(n));
    return sqt * sqt == n;
}
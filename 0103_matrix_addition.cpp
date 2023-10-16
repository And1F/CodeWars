#include <iostream>
#include <vector>

std::vector<std::vector<int>> matrixAddition(const std::vector<std::vector<int>>& matrixA, const std::vector<std::vector<int>>& matrixB) {
    int n = matrixA.size();
    std::vector<std::vector<int>> result(n, std::vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = matrixA[i][j] + matrixB[i][j];
        }
    }

    return result;
}
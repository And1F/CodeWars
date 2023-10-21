#include <vector>

template <typename T>
std::vector<T> zorro(const std::vector<std::vector<T>> matrix) {
  if (matrix.size() < 1) {
    return {};
  }
  std::vector<T> ans;
  
  for (int i = 0; i < matrix[0].size(); i++) {
    ans.push_back(matrix[0][i]);
  }

  for (int i = 1; i < matrix[0].size() - 1; i++) {
    ans.push_back(matrix[i][matrix.size() - 1 - i]);
  }

  for (int i = 0; i < matrix[matrix.size() - 1].size(); i++) {
    ans.push_back(matrix[matrix.size() - 1][i]);
  }
  
  return ans;
}
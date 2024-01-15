std::vector<int> L (int n, int L0, int L1, int add){
  std::vector<int> result;
  
  if (n >= 1) result.push_back(L0);
  if (n >= 2) result.push_back(L1);
  for (int i = 2; i < n; ++i) {
    int nextLeonardo = result[i - 1] + result[i - 2] + add;
    result.push_back(nextLeonardo);
    }

    return result;
}
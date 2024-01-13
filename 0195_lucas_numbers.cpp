#include <unordered_map>

std::unordered_map<int, long long int> memo;

long long int lucasnum(int n) {
  if (memo.find(n) != memo.end()) return memo[n];
  long long int result;
  
  if (n == 0) result = 2;
  else if (n == 1) result = 1;
  else if (n > 0) result = lucasnum(n - 1) + lucasnum(n - 2);
  else result = lucasnum(n + 2) - lucasnum(n + 1);

  memo[n] = result;
  return result;
}
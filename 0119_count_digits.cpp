#include <stdint.h>
#include <string>

int digits(uint64_t n) {
  std::string ans = std::to_string(n);
  return ans.size();
}
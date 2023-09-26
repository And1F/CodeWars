#include <string>

int find_short(std::string str) {
  unsigned int ans = str.size(); 
  unsigned int counter = 0;
  
  for (unsigned int i = 0; i < str.size(); i++) { 
    if (str[i] == ' ') { 
      if (counter < ans) { 
        ans = counter;
      }
      counter = 0;
    } 
    else {
      counter += 1;
    }
  }
  if (counter < ans) {
    ans = counter;
  }
  return ans;
}

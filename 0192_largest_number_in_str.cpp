#include <string>

int largest_five_digits(const std::string &digits){
  int ans = 0;
  for(unsigned int i = 0;i<digits.size()-4;i++){
    if(stoi(digits.substr(i,5)) > ans){
      ans = stoi(digits.substr(i,5));
    }
  }
  return ans; 
}
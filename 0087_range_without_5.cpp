#include <cmath>
bool includes5(int number){
  number = std::abs(number);
    while (number > 0) {
        int digit = number % 10; 
        if (digit == 5) {
            return false;  
        }
        number /= 10;  
    }
    return true;  
}

int dontGiveMeFive(int start, int end){
  int ans = 0;
  
  for (unsigned int i = start;i<= end;i++){
    if(includes5(i)){
      ans++;
    }
  }
  return ans;
}


#include <iostream>

long long rowSumOddNumbers(int n){
  long long ans = 0;
  int num = -1;
  for(int row = 1;row < n+1;row++){
    for(int i = 0;i < row;i++){
      num +=2;
      if(row==n){
        ans+=num;
      }
    }
  }
  return ans;
}
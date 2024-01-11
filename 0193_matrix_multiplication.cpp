#include <vector>
using namespace std;
vector<vector<int>> matrix_multiplication(vector<std::vector<int>> &a, vector<vector<int>> &b, size_t n){
  vector<int> l(n,0);
  vector<vector<int>> c(n,l);
  int sum;

  for(unsigned int i = 0;i<n;i++){
    for(unsigned int j = 0;j<n;j++){
      sum = 0;
      for(unsigned int k = 0;k<n;k++){
        sum += a.at(i).at(k)*b.at(k).at(j);
      }
      c.at(i).at(j) = sum;
    } 
  }
  return c;  
}
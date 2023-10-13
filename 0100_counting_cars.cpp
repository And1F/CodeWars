#include <string>

unsigned long long countPhotos(const std::string& road){
  unsigned long long ans = 0;
  int cars = 0;
  for(int i = 0;i < road.size();i++){
    if(road[i] == '>') cars++;
    else if(road[i] == '.')ans += cars;
  }
  
  cars = 0;
  
  for(int i = road.size()-1;i >= 0;i--){
    if(road[i] == '<') cars++;
    else if(road[i] == '.')ans +=cars;
  }
  
  return ans;
}
int solution(int number) {
  if(number<2){
    return 0;
  }
  unsigned int ans = 0;
  int counter = 3;
  while(counter < number){
    if(counter%3==0 || counter%5==0){
      ans+=counter;
    }
  counter++;
  }
  return ans;
}
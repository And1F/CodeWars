namespace Triangle
{
  bool isTriangle(int a, int b, int c){
    if (a<1 || b<1 || c<1){
     return false;
    }
    if (a >= b+c || b >= a+c || c >= a+b){
    return false;
    }
    else{
      return true;
    }
  }
}
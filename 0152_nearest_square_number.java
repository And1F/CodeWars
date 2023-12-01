public class CodeWarsMath {
    public static int nearestSq(final int n){
          int sqrt = (int) Math.sqrt(n);
  
          int lowerSq = sqrt * sqrt;
          int upperSq = (sqrt + 1) * (sqrt + 1);
  
          if (Math.abs(n - lowerSq) <= Math.abs(n - upperSq)) {
              return lowerSq;
          } else {
              return upperSq;
          }
    }
  }
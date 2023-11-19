public class LuckyNumber {
  
    public static boolean isLucky(long n) {
        if (n == 0) return true;
          String str = Long.toString(n); 
          int ans = 0;
          for (int i = 0; i < str.length(); i++) {
              ans += Character.getNumericValue(str.charAt(i));
          }
          return ans % 9 == 0;
      }
  }
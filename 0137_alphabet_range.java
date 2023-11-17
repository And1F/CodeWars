public class Solution{
    public static String gimmeTheLetters(String s){
          char start = s.charAt(0);
          char end = s.charAt(2);
  
          StringBuilder result = new StringBuilder();
          for (char i = start; i <= end; i++) {
              result.append(i);
          }
  
          return result.toString();
      }
  }
  
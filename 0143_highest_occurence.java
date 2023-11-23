import java.util.Arrays;
public class Kata {
  public static int mostFrequentItemCount(int[] collection) {
    if (collection.length == 0) return 0; 
    Arrays.sort(collection);
    int max = 1; 
    int count = 1;
    for (int i = 1; i < collection.length; i++) {
      if (collection[i] == collection[i - 1]) count++;
      else count = 1;
      if (count > max) max = count;
    }
        return max;
  } 
}
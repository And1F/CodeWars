import java.util.List;

class MinMax {
  static int[] getMinMax(List<Integer> list) {
    int min = list.get(0);
    int max = list.get(0);
    for(int e: list){
      if(e<min) min = e;
      else if (e>max) max = e;
    }
  return new int[]{min,max};
  }
}
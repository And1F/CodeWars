public class Ghostbusters {
    public static String ghostBusters(String building) {
        String ans = building.replace(" ", "");
        if (ans.equals(building)) {
            return "You just wanted my autograph didn't you?";
        } else {
            return ans;
        }
    }     
  }
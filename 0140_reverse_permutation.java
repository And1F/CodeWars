public class Kata{
    private static void recursion(String number, StringBuilder result) {
        if (number.length() == 0) {
            return;
        } else if (result.length() % 2 == 0) {
            recursion(number.substring(1), result.append(number.charAt(0)));
        } else {
            recursion(number.substring(0, number.length() - 1), result.append(number.charAt(number.length() - 1)));
        }
    }

    public static String FlipNumber(String n) {
        StringBuilder result = new StringBuilder();
        recursion(n, result);
        return result.toString();
    }
}

public class Homework8 {
  public static void main(String[] args) {
    System.out.println(check(new char[] { 'W', '*', 'R' }, "WoRDLE"));
    System.out.println(check(new char[] { 'W', '*' }, "woRDLE"));
    System.out.println(check(new char[] { 'S', '*', 'G', '*', 'R' }, "SUGAR"));
    System.out.println(check(new char[] {}, ""));
    System.out.println(check(new char[] { '*', '*', '*', '*', '*' }, "PARADIGMS"));
  }

  public static boolean check(char[] correctPositions, String word) {
    int n = correctPositions.length;

    if (n > word.length())
      return false; // according to instructions this will never not be true but just in case

    for (int i = 0; i < n; i++) {
      char c = word.charAt(i);
      if (!Character.isLetter(c))
        return false; // make sure its alphabetic
      if (correctPositions[i] == c)
        continue; // match is good
      if (correctPositions[i] == '*')
        continue; // * means anything is good
      return false;
    }
    return true;
  }
}

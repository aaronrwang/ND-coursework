public class Main {
  public static void main(String[] args) {
    Point p1 = new Point(2, 3);
    Point p2 = new Point(-3, 1);
    Point p3 = new Point(-2, -3);
    System.out.println(p1.equals(p2)); // → false because p1 and p2 are not equally distant to the origin
    System.out.println(p1.equals(p3)); // → true because p1 and p3 are equally distant to the origin
    System.out.println(p1.equals(null)); // → false because non-null rule, an object != null
    System.out.println(p1.equals(p1)); // → true
  }
}

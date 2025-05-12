public class Point {
  private int x;
  private int y;

  // implement the constructor
  public Point(int x, int y) {
    this.x = x;
    this.y = y;
  }

  @Override
  public boolean equals(Object other) {
    // change this implementaion as specified in the question
    // reflexive
    if (other == this)
      return true;
    // non-null
    if (other == null)
      return false;
    // don't even bother! they have different types
    if (getClass() != other.getClass())
      return false;
    Point point = (Point) other; // why do we need this type cast?
    double distance1 = Math.pow(Math.pow(this.x, 2) + Math.pow(this.y, 2), 1 / 2.0);
    double distance2 = Math.pow(Math.pow(point.x, 2) + Math.pow(point.y, 2), 1 / 2.0);
    return distance1 == distance2;
  }

  @Override
  public int hashCode() {
    int hash = 41 + x;
    hash = 41 * hash + y;
    return hash;
  }

}
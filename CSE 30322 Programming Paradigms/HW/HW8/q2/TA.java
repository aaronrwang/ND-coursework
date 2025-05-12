public class TA extends UniversityMember {
  private Course[] coursesAssisting;

  public TA(String name, String id, String email) {
    super(name, id, email);
    this.coursesAssisting = new Course[2];

  }

  @Override
  public String getRole() {
    return "TA";
  }

  public void assignToCourse(Course course) {
    // if course is already assigned ignore
    if (course == this.coursesAssisting[0] || course == this.coursesAssisting[1])
      return;

    if (this.coursesAssisting[0] == null) {
      // if course 1 is empty assign
      this.coursesAssisting[0] = course;
    } else if (this.coursesAssisting[1] == null) {
      // if course 2 is empty assign
      this.coursesAssisting[1] = course;
    }
    // case where both slots are filled
  }

  public Course[] getCoursesAssisting() {
    return this.coursesAssisting;
  }

  @Override
  public String toString() {
    String coursesstr = "";
    if (null == this.coursesAssisting[0] && null == this.coursesAssisting[1]) {
      coursesstr = "None";
    } else if (null != this.coursesAssisting[0] && null != this.coursesAssisting[1]) {
      coursesstr = this.coursesAssisting[1].getCode() + ", " + this.coursesAssisting[1].getCode();
    } else if (null != this.coursesAssisting[0]) {
      coursesstr = this.coursesAssisting[0].getCode();
    } else if (null != this.coursesAssisting[1]) {
      coursesstr = this.coursesAssisting[1].getCode();
    }

    return String.format("%s (%s). TA for courses %s.", getName(), getEmail(), coursesstr);
  }

}

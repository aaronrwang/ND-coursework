public class Student extends UniversityMember {
  private String major;

  public Student(String name, String id, String email, String major) {
    super(name, id, email);
    this.major = major;
  }

  @Override
  public String getRole() {
    return "Student";
  }

  public String getMajor() {
    return this.major;
  }

  @Override
  public String toString() {
    return String.format("%s (%s) - Major: %s", getName(), getEmail(), getMajor());
  }
}

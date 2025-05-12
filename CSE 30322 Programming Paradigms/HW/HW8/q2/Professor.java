public class Professor extends UniversityMember {
  private String department;

  public Professor(String name, String id, String email, String department) {
    super(name, id, email);
    this.department = department;
  }

  @Override
  public String getRole() {
    return "Professor";
  }

  public String getDepartment() {
    return this.department;
  }

  @Override
  public String toString() {
    return String.format("Prof. %s (%s)", getName(), getEmail());
  }
}

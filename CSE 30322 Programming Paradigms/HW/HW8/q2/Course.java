public class Course {
  private String name;
  private String code;
  private Student[] enrolledStudents;
  private Professor instructor;

  public Course(String name, String code, Professor instructor) {
    this.name = name;
    this.enrolledStudents = new Student[50];
    this.code = code;
    this.instructor = instructor;
  }

  // do we need to account for equality?
  public void addStudent(Student student) {
    for (int i = 0; i < 50; i++) {
      if (enrolledStudents[i] == null) {
        enrolledStudents[i] = student;
        return;
      }
    }
  }

  public void removeStudent(Student student) {
    for (int i = 0; i < 50; i++) {
      if (enrolledStudents[i] == student) {
        enrolledStudents[i] = null;
        return;
      }
    }
  }

  public String getName() {
    return this.name;
  }

  public String getCode() {
    return this.code;
  }

  public Student[] getEnrolledStudents() {
    return this.enrolledStudents;
  }

  public Professor getInstructor() {
    return this.instructor;
  }

  // do we need a course str?
  // @Override
  // public String toString() {
  // return String.format("Course %s", name);
  // }
}

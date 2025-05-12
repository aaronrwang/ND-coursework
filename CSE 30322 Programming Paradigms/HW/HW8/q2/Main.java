public class Main {
  public static void main(String[] args) {

    // create paradigms course, prof, ta
    Professor p1 = new Professor("Joanna Cecilia da Silva Santos", "1", "jdasilv2@nd.edu", "Computer Science");
    TA ta1 = new TA("Ella Gerczak", "2", "egerczak@nd.edu");
    TA ta2 = new TA("Kaixiang Zhao", "3", "kzhao5@nd.edu");
    TA ta3 = new TA("Sahil Khandelwal", "4", "skhandel@nd.edu");
    TA ta4 = new TA("Micah Brody", "5", "mbrody@nd.edu");
    Course c1 = new Course("Programming Paradigms", "CSE-30332", p1);
    ta1.assignToCourse(c1);
    ta2.assignToCourse(c1);
    ta3.assignToCourse(c1);
    ta4.assignToCourse(c1);

    // create other course, prof, ta
    Professor p2 = new Professor("Aaron Dingler", "6", "adingler@nd.edu", "Computer Science");
    TA ta5 = new TA("Ella Gerczak", "7", "a@nd.edu");
    Course c2 = new Course("Logic Design", "CSE-20221", p2);
    ta5.assignToCourse(c2);
    ta2.assignToCourse(c2);

    // create 3 students
    Student s1 = new Student("Aaron Wang", "8", "awang27@nd.edu", "Computer Science");
    Student s2 = new Student("Derick Shi", "9", "dshi2@nd.edu", "ACMS");
    Student s3 = new Student("Therese Kim", "10", "tkim24@nd.edu", "Sociology");

    // add students to classes
    c1.addStudent(s1);
    c1.addStudent(s2);
    c1.addStudent(s3);
    c2.addStudent(s1);
    c2.addStudent(s2);
    c2.addStudent(s3);

    // System.out.println(p1);
    // System.out.println(s1);
    // System.out.println(s2);
    // System.out.println(s3);
    // System.out.println(ta2);
  }
}

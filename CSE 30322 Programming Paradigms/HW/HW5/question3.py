from abc import ABC, abstractmethod

class UniversityMember(ABC):
  num_members = 0
  def __init__(self, name, member_id, email):
    self.name = name
    self.member_id = member_id
    self.email = email
    UniversityMember.num_members +=1

  @abstractmethod
  def get_role(self):
    pass

class Student(UniversityMember):
  def __init__(self, name, member_id, email, major):
    self.major = major
    super().__init__(name, member_id, email)

  def get_role(self):
    return "Student"
  
  def __str__(self):
    return f'{self.name} ({self.email}) - Major: {self.major}'
  
class Professor(UniversityMember):
  def __init__(self, name, member_id, email, department):
    self.department = department
    super().__init__(name, member_id, email)

  def get_role(self):
    return "Professor"
  
  def __str__(self):
    return f'Prof. {self.name.split(" ")[-1]} ({self.email})'
  
class TA(UniversityMember):
  def __init__(self, name, member_id, email):
    self.courses_assisting = []
    super().__init__(name, member_id, email)

  def assign_to_course(self, course):
    if course not in self.courses_assisting:
      self.courses_assisting.append(course)  

  def get_role(self):
    return "TA"
  
  def __str__(self):
    return f'{self.name} ({self.email}). TA for courses: {", ".join(self.courses_assisting)}.'
  


class Course:
  def __init__(self, name, code):
    self.name = name
    self.code = code
    self.enrolled_students = []
    self.instructor = None

  def add_student(self, student):
    if student not in self.enrolled_students:
      self.enrolled_students.append(student)

  def remove_student(self, student):
    self.enrolled_students = filter(lambda a: a!= student, self.enrolled_students)

  def add_instructor(self, instructor):
    self.instructor = instructor

  def remove_instructor(self):
    self.instructor = None

  def __str__(self):
    students_str = "\n  ".join(map(str, self.enrolled_students)) if self.enrolled_students else "None"
    return f"Course: {self.name} - {self.code}.\nInstructor: {self.instructor}\nStudents:\n  {students_str}"
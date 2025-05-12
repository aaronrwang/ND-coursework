from question3 import *

if __name__ == "__main__":
  c = Course("Programming Paradigms", "CSE-30332")
  p = Professor("Joanna Cecilia da Silva Santos", 1, "jdasilv2@nd.edu", "Computer Science")
  c.add_instructor(p)

  s1 = Student("Aaron Wang", 7, "awang27@nd.edu", "Computer Science")
  s2 = Student("Derick Shi", 8, "dshi2@nd.edu", "ACMS")
  s3 = Student("Therese Kim", 9, "tkim24@nd.edu", "Sociology")  
  ss = [s1, s2, s3]
  for s in ss:
    c.add_student(s)
  t1 = TA("Ella Gerczak", 2 , "egerczak@nd.edu")
  t2 = TA("Kaixiang Zhao", 3 , "kzhao5@nd.edu")
  t3 = TA("Sahil Khandelwal", 4 , "skhandel@nd.edu")
  t4 = TA("Micah Brody", 5 , "mbrody@nd.edu")
  tas = [t1, t2, t3, t4]
  for ta in tas:
    ta.assign_to_course(c.code)

  l = [p, t1, t2, t3, t4, s1, s2, s3]
  for j in l:
    print(j)
  print()
  print(c)
  print()
  print(UniversityMember.num_members)
  print(s1.get_role(),t1.get_role(),p.get_role())

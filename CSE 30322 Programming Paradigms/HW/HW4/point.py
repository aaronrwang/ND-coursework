class Point:

  # initialize object
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # magic print method
  def __str__(self):
    return f'({self.x},{self.y})'
  
  # magic == method, uses distance formula from origin to points to compare
  def __eq__(self, p):
    return (self.x**2+self.y**2)**.5 == (p.x**2+p.y**2)**.5
  
  # magic > method, uses distance from origin to points to compare; further away is greater
  def __gt__(self, p):
    return (self.x**2+self.y**2)**.5 > (p.x**2+p.y**2)**.5
  
  # magic >= method, uses above methods: >= = > or ==
  def __ge__(self, p):
    return self > p or self == p
  
  # magic <= method, uses above methods: <= = not >
  def __le__(self, p):
    return not (self > p)
  
  # magic >= method, uses above methods: < = not >=
  def __lt__(self, p):
    return not (self >= p)
  

# test cases
p1 = Point(2,3)  
p2 = Point(-3,1) 
p3 = Point(-2,-3)
print(p1 > p2) # prints True because p1 is more distant to the origin than p2
print(p1 == p2) # prints False because p1 and p2 are not equally distant to the origin 
print(p1 < p2) # prints False because p1 is not closer to the origin as compared to p2
print(p1 == p3) # prints True  because p1 and p3 are equally distant to the origin
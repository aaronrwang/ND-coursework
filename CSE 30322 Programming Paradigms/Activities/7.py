import math
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __str__(self):
    return f'({self.x},{self.y})'
  

def distance(p1, p2):
  return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**.5

p1 = Point(3,7)
p2 = Point(-1,-2)
print(p1, p2)
print(distance(p1, p2))
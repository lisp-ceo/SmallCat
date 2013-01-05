"""
  Supplemental game objects
"""
from math import sqrt

class Vector2(object):
  def __init__(self, x=0.0, y=0.0):
    self.x = x
    self.y = y

  def __str___(self):
    return "(%s, %s)" % (self.x, self.y)

  def __add__(self,rhs):
    return Vector2(self.x + rhs.x, self.y + rhs.y)

  @staticmethod
  def from_points(P1,P2):
    return Vector2(P2[0] - P1[0], P2[1] - P1[1])

class Vector3(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, x, y, z):
    return Vector3(self.x+x,self.y+y,self.z+z)
  
  def __eq__(self):
    return x, y, z

  def get_magnitude(self):
    return sqrt(self.x**2 + self.y**2 + self.z**2)

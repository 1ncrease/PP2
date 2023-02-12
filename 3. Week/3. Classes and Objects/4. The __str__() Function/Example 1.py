#The __str__() function controls what should be returned when the class object is represented as a string.
#If the __str__() function is not set, the string representation of the object is returned:

#The string representation of an object WITHOUT the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
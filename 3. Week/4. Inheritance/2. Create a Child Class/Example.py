#Create a class named Student, which will inherit the properties and methods from the Person class:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
class Student(Person):
  pass

#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
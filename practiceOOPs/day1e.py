# concept of single inheritence
# (Create a base class called Person with the following attributes and methods:

# Attributes: name (string), age (integer)
# Method: display_info() that prints the name and age.
# Create a derived class called Student that inherits from Person and has the following additional attribute and method:

# Attribute: student_id (string)
# Method: display_student_info() that prints the name, age, and student_id.
#  Write a Python program to demonstrate the creation of a Student object and display its information using both display_info() and display_student_info() methods.)

class Person:
  def __init__(self,aname,aage):
    self.name=aname
    self.age=aage
  def display_info(self):
    print( f"Name: {self.name}  Age: {self.age}")
  

class Student(Person):
  def __init__(self,aname,aage,astudent_id): 
    # super().__init__(aname,aage)
    Person.__init__(self,aname,aage)
    self.student_id= astudent_id
  def display_student_info(self):
    # self.display_info()  # here the infinite looping is not occurring due to display_info and display_student_info both are different  
    # super().display_info()
    Person.display_info(self)
    print( f"Student_ID: {self.student_id}")
    
  
harry=Student("STUDENT",12,2221)

harry.display_info()
harry.display_student_info()
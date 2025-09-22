# concept of multilevel inheritence

# Create a base class Person with the following attributes and methods:
# Attributes: name (string) and age (integer)
# Method: display_person_info() that prints the name and age.

# Create a derived class Employee that inherits from Person and has the following additional attribute and method:
# Attribute: employee_id (string)
# Method: display_employee_info() that prints the employee_id along with the name and age.

# Create another derived class Manager that inherits from Employee and has the following additional attribute and method:
# Attribute: department (string)
# Method: display_manager_info() that prints the department along with the employee_id, name, and age.
# Write a Python program to demonstrate the creation of a Manager object and display its information using the display_person_info(), display_employee_info(), and display_manager_info() methods.

class Person():
  def __init__(self,aname,aage):
    self.name=aname
    self.age=aage
  def display_person_info(self):
    print(f"Name: {self.name} Age: {self.age}")

class Employee(Person):
  def __init__(self,aname,aage,aemployee_id):
    Person.__init__(self,aname,aage)
    self.employee_id=aemployee_id

  def display_employee_info(self):
    self.display_person_info()
    print(f"Employee_id: {self.employee_id}")

class Manager(Employee):
  def __init__(self,aname,aage,aemployee_id,adepartment):
    Employee.__init__(self,aname,aage,aemployee_id)
    self.department=adepartment
  def display_manager_info(self):
    self.display_employee_info()
    print(f"Department: {self.department}")
manager=Manager("MANAGER",36,"CSE22006","FULL STACK DEVELOPER")
print("1")
manager.display_person_info()
print("2")
manager.display_employee_info()
print("3")
manager.display_manager_info()

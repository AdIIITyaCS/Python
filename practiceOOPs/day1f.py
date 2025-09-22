# concept of multiple inheritence 
# Create two base classes Person and Employee:

# The Person class should have attributes name (string) and age (integer), and a method display_person_info() that prints the name and age.
# The Employee class should have an attribute employee_id (string), and a method display_employee_info() that prints the employee_id.


# Create a derived class Manager that inherits from both Person and Employee, and has an additional attribute department (string). The Manager class should have a method display_manager_info() that prints the name, age, employee_id, and department.

# Write a Python program to demonstrate the creation of a Manager object and display its information using the display_person_info(), display_employee_info(), and display_manager_info() methods.

class Person:
  def __init__(self,aname,aage):
    self.name=aname
    self.age=aage
  def display_person_info(self):
    print(f"Name: {self.name} Age: {self.age}")

class Employee:
  def __init__(self,aemployee_id):
    self.employee_id=aemployee_id
  def display_employee_info(self):
    print(f"Employee_ID: {self.employee_id}")

class Manager(Person,Employee):
  def __init__(self,aname,aage,aemployee_id,adepartment):
    # super().__init__(self,aname,aage)
    # super().__init__(self,aemployee_id)
    # these above lines will create confusion in choosing specific init function of parent class  
    Person.__init__(self,aname,aage) 
    Employee.__init__(self,aemployee_id)
    self.department=adepartment
    
  def display_manager_info(self):
    # Person.display_person_info(self)
    # Employee.display_employee_info(self)
    self.display_person_info()
    self.display_employee_info()
    print(f"Department: {self.department}")


person=Person("PERSON",20)
employee=Employee("EMPLOYEE_ID")
manager=Manager("MANAGER",36,"CSE22006","FULL_STACK_DEVELOPER")

manager.display_person_info()
manager.display_employee_info()
manager.display_manager_info()
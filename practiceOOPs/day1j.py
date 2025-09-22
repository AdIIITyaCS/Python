# concept of abstraction in oops in python
# Create an abstract base class Appliance with the following abstract methods:
# turn_on(): This method should be implemented to turn the appliance on.
# turn_off(): This method should be implemented to turn the appliance off.

# Create two subclasses WashingMachine and Refrigerator that inherit from Appliance and implement the abstract methods.
# Write a Python program to demonstrate the creation of WashingMachine and Refrigerator objects and call their turn_on() and turn_off() methods.

# from abc import ABC, abstractmethod
# class Appliance(ABC):
#   @abstractmethod
#   def turn_on():
#     pass
#   def turn_off():
#     pass

# class WashingMachine(Appliance):
#   def __init__(self,adevice):
#     self.device=adevice
#   def turn_on(self):
#     print(f"TURN ON THE {self.device}")
#   def turn_off(self):
#     print(f"TURN OFF THE {self.device}")

# class Refrigerator(Appliance):
#   def __init__(self,adevice):
#     self.device=adevice
#   def turn_on(self):
#     print(f"TURN ON THE {self.device}")
#   def turn_off(self):
#     print(f"TURN OFF THE {self.device}")

# device1=WashingMachine("WM")
# device2=Refrigerator("RF")

# device1.turn_on()
# device1.turn_off()
# device2.turn_on()
# device2.turn_off()



# Create an abstract base class Employee with the following abstract methods:
# calculate_salary(): This method should be implemented to calculate the salary of the employee.
# get_details(): This method should be implemented to return the details of the employee.

# Create two subclasses FullTimeEmployee and PartTimeEmployee that inherit from Employee and implement the abstract methods.
# The FullTimeEmployee class should have the attributes name (string) and monthly_salary (float). The calculate_salary() method should return the monthly salary, and the get_details() method should return a string containing the name and monthly salary of the employee.
# The PartTimeEmployee class should have the attributes name (string), hourly_wage (float), and hours_worked (float). The calculate_salary() method should return the product of hourly_wage and hours_worked, and the get_details() method should return a string containing the name, hourly wage, and hours worked of the employee.
# Write a Python program to demonstrate the creation of FullTimeEmployee and PartTimeEmployee objects, display their details using the get_details() method, and calculate their salaries using the calculate_salary() method.

from abc import ABC, abstractmethod
class Employee(ABC):
  @abstractmethod
  def calculate_salary():
    pass
  def get_details():
    pass

class FullTimeEmployee(Employee):
  def __init__(self,aname,amonthly_salary):
    self.name=aname
    self.monthly_salary=amonthly_salary
  def calculate_salary(self):
    return self.monthly_salary
  def get_details(self):
    return f"NAME: {self.name} MONTHLY_SALARY: {self.monthly_salary}"

class PartTimeEmployee(Employee):
  def __init__(self,aname, ahourly_wage,ahours_worked):
    self.name=aname
    self.hourly_wage=ahourly_wage
    self.hours_worked=ahours_worked
  def calculate_salary(self):
    return (self.hourly_wage)*(self.hours_worked)
  def get_details(self):
    return f"NAME: {self.name} HOURLY_WAGE={self.hourly_wage} HOURS_WORKED: {self.hours_worked}"
  
person1=FullTimeEmployee("FULLTIME_Worker",120000)
person2=PartTimeEmployee("HALFTIME_Worker",2000,12)

print(person1.get_details())
print(person1.calculate_salary())
print(person2.get_details())
print(person2.calculate_salary())
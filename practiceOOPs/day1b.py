class Employee:
  no_of_leave=8
  pass
harry=Employee()
larry=Employee()
larry.no_of_leave=100
print(harry.no_of_leave)
print(larry.no_of_leave)
Employee.no_of_leave=100000
print(harry.no_of_leave)
print(larry.no_of_leave)
print(harry.__dict__)
print(larry.__dict__)
print(Employee.__dict__)

class Employee:
  no_of_leave=8
  def __init__(self,aname,astd,asection):
    self.section=asection
    self.std=astd
    self.name=aname
  def details(self):
    return f"Name is {self.name}\nStandard is {self.std}\nSection is {self.section}"

  def add(self,a,b):
    return a+b
  def sub(self,a,b):
    return a-b
  
harry=Employee("HARRY",6,"A")
print(harry.details())
print(harry.add(4,5))
print(harry.sub(10,5))

larry=Employee("LARRY",8,"B")
print(larry.details())
print(larry.add(100,5))
print(larry.sub(100,5))
larry.no_of_leave=900
print(larry.no_of_leave)
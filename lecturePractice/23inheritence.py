# # single inheritance
#  class Employee:
#     no_of_leaves=8
#     def __init__(self,aname,asalary,role):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
# class Programmer(Employee):
#     def __init__(self,aname,alanguage,askill):
#         self.name=aname
#         self.language=alanguage
#         self.skill=askill
#     def printdetail(self):
#         return f"{self.name} knows {self.language} and having {self.skill} skill"
# shubham=Programmer("Shubham","PYTHON","Reading")
# print(shubham.printdetail())
  
# # multiple inheritance  
# class Employee:
#     def __init__(self,aname,asalary,arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
# class Player():
#     def __init__(self,aname,agame):
#         self.name=aname
#         self.game=agame
#     def detail(self):
#         return f"Employee name is {self.name} and likes to play {self.game}"
# class Combo(Employee,Player):
#     def __init__(self, aname, agame):
#         Employee.__init__(self, aname,None,None)
#         Player.__init__(self, aname,agame)
# rohan=Employee("Rohan",200000,"CEO")
# shubham=Player("Shubham","Cricket")
# karan=Combo("Karan","Volleyball") 
# print(karan.detail())

# # multilevel inheritance
# class Dad:
#     basketball_goal=1
# class Son(Dad):
#     basketball_goal=22
#     dance=2
#     def isDance(self):
#         return f"Yes I dance {self.dance} no. of times"
# class GrandSon(Son):
#     dance=5
#     def isDance(self):
#         return f"Jackson Yeah!!! I dance {self.dance} times"
# darry=Dad()
# larry=Son()
# harry=GrandSon()
# print(harry.dance)
# print(harry.basketball_goal)

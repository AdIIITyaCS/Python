# l1=["abc","def","ghi"]
# print("USING NORMAL INDICES::")
# for values in l1:
#     print(values)
# print("USING -VE INDICES::")
# print(l1[-1])
# print(l1[-2])
# print(l1[-3])

# mystr="a bc def ghij"
# print("1",mystr[0:])
# print("2",mystr[:])
# print("3",mystr[:200])
# print("4",mystr[::1])
# print("5",mystr[::-1])
# print("6",mystr[::-2])
# print("7",mystr[::-3])
# print("8",mystr[::-4])
# print("9",mystr[::])

# d1={"ab":"AB","cd":"CD","ef":"EF","gh":"GH"}
# for i in d1.keys():
#     print(i)
# for i in d1.values():
#     print(i)
# for i,j in d1.items():
#     print(i,j)
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# print(d1["ab"])
# d1["ij"]="IJ"
# d1.update({"kl":"KL"})
# print(d1.items())

# var1=89
# var2=98
# var3=int(input("enter your no."))
# print("var3 is",var3)
# if var1==var2:
#     print("var1 is equal to var2")
# elif var1>var2:
#     print("var1 is greater than var2")
# else:
#     print("var1 is lesser than var2")
# l2=[5,6,7]
# print(5 in l2)
# print(5 not in l2)
# if 9 in l2:
#     print("5 is present in list:")
# else:
#     print("not present:")

# while(True):
#     var4=int(input("Enter a number:"))
#     if var4==34:
#         print(var4,"is equal to 34")
#     elif var4>34:
#         print(var4,"is greater than 34")
#         print("loop is leaved due to break statement")
#         break
#     else:
#         print(var4,"is lesser than 34")
#         print("loop is continued due to continue statement")
#         continue

# print("yes") if 5>7 else print("no its wrong")
# var="""a bc def ghij
# klmno pqrstu
#                         vwxyz"""
# print(var)

# def add(a,b):
#     """this is a function to add two no:"""
#     return a+b
# print(add.__doc__)
# print(add(7,8))
# add=lambda a,b:a+b
# print(add(9,10))

# a=input("enter a: ")
# b=input("enter b: ")
# try:
#     c=int(a)+int(b)
#     print(c)
# except Exception as e:
#     print(e)

# import random
# random_no1=random.randint(1,20)
# print(random_no1)
# random_no2=random.random()*100
# print(random_no2)
# l3=[1,2,3,4,8]
# l4=["ab","cd","ef","gh"]
# random_no3=random.choice(l3)
# print(random_no3)
# random_no4=random.choice(l4)
# print(random_no4)

# class Employee:
#     no_of_leaves=100
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         print(self.name,"and",self.salary)
# a=Employee("A",100)
# b=Employee("B",200)
# c=Employee("C",300)
# d=Employee("D",400)
# e=Employee("E",500)
# Employee.no_of_leaves=50
# print(Employee.no_of_leaves)


# class Employee:
#     no_of_leaves=100
#     @classmethod
#     def change_leaves(cls,new_leaves):
#         cls.no_of_leaves=new_leaves
# a=Employee()
# a.change_leaves(89)
# print("Employee",Employee.no_of_leaves)
# print("a",Employee.no_of_leaves)

# class Employee:
#     @staticmethod
#     def printgood(st):
#         print("This is good"+st)
#         return 89
# print(Employee.printgood("mango"))

# class Employee:
#     no_of_leaves=100
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         print(self.name , "and" , self.salary)
# class Programmer(Employee):
#     pass
#     def printprog(self):
#         return f"Name is {self.name} and Salary is {self.salary}"
# a=Employee("a",100888)
# b=Programmer("b",270000)
# d=Programmer("c",2000000)
# print(b.printprog())
# print(d.printprog())

class Employee:
    public=100
    _protected=200
    __private=300
    def __init__(self,name,salary,height):
        self.name=name
        self.salary=salary
        self.height=height
        print(self.name , "and" , self.salary, "and", self.height)
class Programmer():
    def __init__(self,langauge,age):
        self.language=langauge
        self.age=age
    def printprog(self):
        return f"Language is {self.language} and Age is {self.age}"
class CollegeEmployee(Programmer,Employee):
    pass
a=Employee("a",100888,67)
b=Programmer("Python",27)
c=CollegeEmployee("c",78)
print("\n")
print(b.printprog())
print(Employee.public)  # Access class variable using class name
print(a._protected)  # Accessing name-mangled protected variable using the correct name
print(a._Employee__private)  

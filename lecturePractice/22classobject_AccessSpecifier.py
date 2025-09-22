# # USE OF CLASS WITH THEIR OBJECT
# class Employee:
#     no_of_leaves=23
#     pass
# harry=Employee()
# rohan=Employee()
# harry.salary=2000
# print(harry.salary)
# print("Class variable is accessible by all objects,class itself")
# print(harry.no_of_leaves)
# print(rohan.no_of_leaves)
# print(Employee.no_of_leaves)
# print("But class Variable is modified by class only:")
# Employee.no_of_leaves=56
# print(Employee.no_of_leaves)
# #this will create a new instance variable in harry object 
# harry.no_of_leaves=569  
# print(harry.__dict__)
# print(Employee.no_of_leaves)

# #if any method is created in class, if brings 'self' in its argument
# class Employee:
#     def printdetail(self):
#         return f"Employee name is {self.name}\nEmployee salary is {self.salary}"
# harry=Employee()
# harry.name="Harry"
# harry.salary=1874
# print(harry.printdetail())        

# # use of constructor
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def printdetail(self):
#         return f"Employee name is {self.name}\nEmployee salary is {self.salary}"
# harry=Employee("Munna",2000)
# print(harry.printdetail())  

# #using (@classmethod and object) we can modify the class variable also
# class Employee:
#     @classmethod
#     def change_no_of_leaves(cls,newleaves):
#         cls.no_of_leaves=newleaves
#     no_of_leaves=23
#     pass
# harry=Employee()
# print("Class variable is accessible by all objects,class itself")
# print("class Variable is modified by class only:")
# print("but using (@classmethod and object) we can modify the class variable also")
# print("initially no of leaves!!!!!")
# print(Employee.no_of_leaves)
# Employee.no_of_leaves=56
# print("After changing no. of leaves by class itself")
# print(Employee.no_of_leaves)
# harry.change_no_of_leaves(365)
# print("After changing no. of leaves by (@classmethod and object)!!!!!")
# print(Employee.no_of_leaves)

# if we don't want any self,cls etc them use @static method
# which is used to print or to perform any operation
# class Employee:
#     @staticmethod
#     def printdetail():
        # print("Mango is good for health")
        # return 108
#         # sum= a+b
#         # return sum
# harry=Employee()
# a = int (input ("Enter first number:"))
# b =int ( input ("enter second number"))
# print(harry.printdetail())

# access specifier 
# public: normal variable,methods of class 
# protected: same as public access specifier with underscore(_name)
# it doesn't mean that they can't be used outside its only a convention by 
#     developer
# private: unlike than above this is used with (__aname) but their accessing 
#     is like <object_name>._<class_name>__(method_name/variable)  

class A:
        public_variable=23
        _protected_variable=34555
        __private_variable=79898
class B(A):
        mango=90
# class C(A,B):
#         pass
object_A=A()
object_B=B()
# object_C=C()
# print(object_A.public_variable)
# print(object_A._protected_variable)
print(object_A._A__private_variable)
# print(object_B.public_variable)
# print(object_B._protected_variable)
# print(object_B._A__private_variable)     
# print(object_C.public_variable)
# print(object_C._protected_variable)
# print(object_C.__private_variable)
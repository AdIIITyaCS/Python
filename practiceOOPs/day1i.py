# Class Calculator:

# Defines a method add that takes three parameters: a, b, and an optional c with a default value of None.
# The method checks if c is None:
# If c is None, it returns the sum of a and b.
# If c is not None, it returns the sum of a, b, and c.
# Creating a Calculator Object:

# An object calc of the Calculator class is created.
# Using the add Method:

# The add method is called with two arguments (10 and 5), which returns their sum (15).
# The add method is called with three arguments (10, 5, and 3), which returns their sum (18).

# class Calculator():
#   def add(self,*args):
#     return sum(args)
# calculator=Calculator()
# print(calculator.add(1,2))
# print(calculator.add(1,2,6))


# Create a base class Animal with the following attributes and methods:
# Attribute: name (string)
# Method: make_sound() that prints "Animal makes a sound".

# Create a derived class Dog that inherits from Animal and overrides the make_sound() method to print "Dog barks".
# Create another derived class Cat that inherits from Animal and overrides the make_sound() method to print "Cat meows".

# Write a Python program to demonstrate the creation of Dog and Cat objects and call their make_sound() methods to show method overriding.

class Animal():
  def __init__(self,aname):
    self.name=aname
  def make_sound(self):
    print( "Animal makes a sound")
class Dog(Animal):
  def make_sound(self):
    print( "Dog barks")
class Cat(Animal):
  def make_sound(self):
    print("Cat meows")

animal=Animal("ANIMAL")
dog=Dog("DOG")
cat=Cat("CAT")
dog.make_sound()
cat.make_sound()

# Create a base class Vehicle with the following attributes and methods:
# Attributes: make (string), model (string), year (integer)
# Method: vehicle_info() that returns a string with the vehicle's make, model, and year.

# Create a derived class Car that inherits from Vehicle and has the following additional attributes and methods:
# Attribute: number_of_doors (integer)
# Method: vehicle_info() that overrides the base class method to include the number of doors.

# Create another derived class Motorcycle that inherits from Vehicle and has the following additional attributes and methods:
# Attribute: type_of_handlebars (string)
# Method: vehicle_info() that overrides the base class method to include the type of handlebars.

# Create an abstract base class Serviceable with the following abstract method:
# Abstract method: service() that does not have an implementation.
# Make the Car and Motorcycle classes inherit from Serviceable and implement the service() method in each.

# Write a Python program to demonstrate the creation of Car and Motorcycle objects, display their information using the vehicle_info() method, and call the service() method to show the implementation of all OOP concepts.


# from abc import ABC, abstractmethod
# class Serviceable(ABC):
#   @abstractmethod
#   def service():
#     pass
# class Vehicle():
#   def __init__(self,amake, amodel, ayear ):
#     self.make=amake
#     self.model=amodel
#     self.year=ayear
#   def vehicle_info(self):
#     print( f"VEHICLE'S MAKE={self.make}\t\tMODEL={self.model}\t\tYEAR={self.year}" )
# class Car(Vehicle,Serviceable):
#   def __init__(self,amake, amodel, ayear,anumber_of_doors):
#     Vehicle.__init__(self,amake, amodel, ayear)
#     self.number_of_doors=anumber_of_doors
#   def vehicle_info(self):
#     Vehicle.vehicle_info(self)
#     print( f"NUMBER_OF_DOORS: {self.number_of_doors}")
#   def service(self):
#     return print("Time to service Car")
  
# class Motorcycle(Vehicle,Serviceable):
#   def __init__(self,amake, amodel, ayear,atype_of_handlebars):
#     Vehicle.__init__(self,amake, amodel, ayear)
#     self.type_of_handlebars=atype_of_handlebars
#   def vehicle_info(self):
#     Vehicle.vehicle_info(self)
#     print (f"TYPE_OF_HANDLEBARS: {self.type_of_handlebars}")
#   def service(self):
#     return print("Time to service Motorcycle")


# car=Car("TOYOTA","CAMRY",2020,50)
# motorcycle= Motorcycle("Harley-Davidson", "Street 750", 2019, "Ape Hangers")

# car.vehicle_info()
# car.service()
# motorcycle.vehicle_info()
# motorcycle.service()
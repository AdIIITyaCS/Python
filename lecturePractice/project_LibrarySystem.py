
# Library Management System Simulation
# Base Class LibraryItem (Abstract Class):
# Attributes:

# title (string): Title of the item.
# identifier (integer): Unique identifier for the item.
# Methods:

# get_details(): Abstract method that returns a string with the details of the item.
# Derived Class Book (Normal Class, inherits from LibraryItem):
# Additional Attribute:

# author (string): Author of the book.
# Methods:

# get_details(): Overrides the base class method to include details of the book (title, author, identifier).
# Derived Class DVD (Normal Class, inherits from LibraryItem):
# Additional Attribute:

# director (string): Director of the DVD.
# Methods:

# get_details(): Overrides the base class method to include details of the DVD (title, director, identifier).
# Class Library (Normal Class):
# Attributes:

# items (list): List to store instances of Book and DVD.
# Methods:

# add_item(item): Adds a new item (either Book or DVD) to the library.
# display_items(): Displays details of all items in the library using their get_details() method.
# Task:
# Write a Python program to implement the above classes and simulate the library system. Demonstrate the following:

# Creation of instances of Book and DVD.
# Adding these instances to a Library object.
# Displaying details of all items in the library using the display_items() method.
# This structure clarifies that LibraryItem is an abstract class (because it has an abstract method) while Book, DVD, and Library are normal classes. This distinction helps in understanding the design and implementation of the library management system.
# finally
# Create instances of Book and DVD.
# Add these instances to a Library object.
# Call the display_items() method to display details of all items in the library.
from abc import ABC, abstractmethod
class LibraryItem(ABC):
  def __init__(self,atitle,aidentifier):
    self.title=atitle
    self.identifier=aidentifier
  @abstractmethod
  def get_details():
    pass
class Book(LibraryItem):
  def __init__(self,atitle,aidentifier,aauthor):
    LibraryItem.__init__(self,atitle,aidentifier)
    self.author=aauthor
  def get_details(self):
    return f"Title(Book): {self.title}\t\tAuthor: {self.author}\t\tIdentifier: {self.identifier}"
class DVD(LibraryItem):
  def __init__(self,atitle,aidentifier,adirector):
    LibraryItem.__init__(self,atitle,aidentifier)
    self.director=adirector
  def get_details(self):
    return f"Title(DVD): {self.title}\t\tDirector: {self.director}\t\tIdentifier: {self.identifier}"
class Library():
  def __init__(self):
    self.items=[]
  def add_item(self,item):
    if isinstance(item,LibraryItem):
      self.items.append(item)
    else:
      print("INVALID INSTANCE!!!..........")
  def display_items(self):
    for item in self.items:
      print(item.get_details())

library = Library()

  # Add initial items to the library
book1 = Book("The Great Gatsby", 1, "F. Scott Fitzgerald")
dvd1 = DVD("Inception", 2, "Christopher Nolan")
library.add_item(book1)
library.add_item(dvd1)

while True:
  # Prompt user for the type of item to add
  item_type = input("Enter the type of item to add (Book/DVD) or 'quit' to exit: ").strip().lower()
  if item_type == 'quit':
      break
  elif item_type == 'book':
      title = input("Enter the book title: ")
      identifier = int(input("Enter the book identifier: "))
      author = input("Enter the book author: ")
      new_item = Book(title, identifier, author)
  elif item_type == 'dvd':
      title = input("Enter the DVD title: ")
      identifier = int(input("Enter the DVD identifier: "))
      director = input("Enter the DVD director: ")
      new_item = DVD(title, identifier, director)
  else:
      print("Invalid item type. Please enter 'Book' or 'DVD'.")
      continue

  # Add the new item to the library
  library.add_item(new_item)

  # Display the updated list of items in the library
  print("\nUpdated Library Items:")
  library.display_items()
  print("\n")
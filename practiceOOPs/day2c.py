# 1. Base Class LibraryItem
# Attributes:

# title (string): Title of the item.
# identifier (integer): Unique identifier for the item.
# available (boolean): Availability status of the item (True if available, False if not).
# Methods:

# get_details(): Abstract method that returns a string with the details of the item. This method is overridden in each derived class (Book, DVD, Magazine).

# check_out(): Method to check out an item by setting its available attribute to False if it's currently available (True). Returns True if successful, False otherwise.

# check_in(): Method to check in an item by setting its available attribute to True if it's currently checked out (False). Returns True if successful, False otherwise.

# 2. Derived Class Book
# Attributes Inherited:

# title, identifier, available.
# Additional Attribute:

# author (string): Author of the book.
# Methods:

# get_details(): Overrides the base class method to include details of the book (title, author, identifier, available).
# 3. Derived Class DVD
# Attributes Inherited:

# title, identifier, available.
# Additional Attribute:

# director (string): Director of the DVD.
# Methods:

# get_details(): Overrides the base class method to include details of the DVD (title, director, identifier, available).
# 4. Derived Class Magazine
# Attributes Inherited:

# title, identifier, available.
# Additional Attribute:

# issue (integer): Issue number of the magazine.
# Methods:

# get_details(): Overrides the base class method to include details of the magazine (title, issue, identifier, available).
# 5. Class LibraryMember
# Attributes:

# member_id (integer): Unique identifier for the library member.
# name (string): Name of the library member.
# Methods:

# get_member_info(): Returns a string with the member's ID and name.
# 6. Class Library
# Attributes:

# items (list): List to store instances of Book, DVD, and Magazine.
# members (list): List to store instances of LibraryMember.
# Methods:

# add_item(item): Adds a new item (either Book, DVD, or Magazine) to the library's items list.

# remove_item(item_id): Removes an item from the library based on its identifier (item_id). Returns True if successful, False otherwise.

# add_member(member): Adds a new LibraryMember to the library's members list.

# remove_member(member_id): Removes a member from the library based on their ID (member_id). Returns True if successful, False otherwise.

# display_items(): Displays details of all items in the library using their get_details() method.

# display_members(): Displays details of all members in the library using their get_member_info() method.

# check_out_item(member_id, item_id): Checks out an item from the library by setting its available status to False. Returns True if successful, False otherwise.

# check_in_item(item_id): Checks in an item to the library by setting its available status to True. Returns True if successful, False otherwise.

# Procedure for Methods:
# LibraryItem Class Methods:
# get_details() Method:

# For Book Class:
# Format and return a string with title, author, identifier, and available status.
# For DVD Class:
# Format and return a string with title, director, identifier, and available status.
# For Magazine Class:
# Format and return a string with title, issue, identifier, and available status.
# check_out() Method:

# Check if the item is available.
# If available (True), set available to False and return True.
# If not available (False), return False.
# check_in() Method:

# Check if the item is not available.
# If not available (False), set available to True and return True.
# If already available (True), return False.
# Book, DVD, Magazine Class Methods:
# get_details() Method:
# Return a formatted string specific to each type (Book, DVD, Magazine) including all relevant attributes (title, author or director, issue for Magazine, identifier, available status).
# LibraryMember Class Methods:
# get_member_info() Method:
# Return a formatted string with member_id and name.
# Library Class Methods:
# add_item(item) Method:

# Append the item (instance of Book, DVD, or Magazine) to the items list.
# remove_item(item_id) Method:

# Iterate through items list to find the item with item_id.
# If found, remove the item from the items list and return True.
# If not found, return False.
# add_member(member) Method:

# Append the member (instance of LibraryMember) to the members list.
# remove_member(member_id) Method:

# Iterate through members list to find the member with member_id.
# If found, remove the member from the members list and return True.
# If not found, return False.
# display_items() Method:

# Iterate through items list and print details using each item's get_details() method.
# display_members() Method:

# Iterate through members list and print details using each member's get_member_info() method.
# check_out_item(member_id, item_id) Method:

# Find the item with item_id in items list.
# If found and check_out() returns True, the item is successfully checked out.
# If not found or already checked out, return False.
# check_in_item(item_id) Method:

# Find the item with item_id in items list.
# If found and check_in() returns True, the item is successfully checked in.
# If not found or already checked in, return False
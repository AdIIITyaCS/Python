# # THIS IS QUITE LENTHY WHEN MORE NO.OF NAMES WOULD BE ADDED
# def name(a, b, c, d):
#     print(a, b, c, d)
# name("ADITYA", "ROHAN", "SHIVAM", "SHREYANSH")

# #
def name(*args):
    for items in args:
        print(items)


list1 = ["ADITYA", "ROHAN", "SHIVAM", "SHREYANSH", "ADARSH"]
name(*list1)
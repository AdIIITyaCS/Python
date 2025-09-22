# copying a function into another one
# def funct1():
#     print("Subscribe Now!!!!!!!")
# funct2=funct1
# del funct1
# funct2()

# # use of decorator @function either use @function or use (2),(3) in the code 
# def dec1(funct1):
#     def nowexec():
#         print("Executing Now!!!")
#         funct1()
#         print("Executed!!!!")
#     return nowexec()
# @dec1  #(1)
# def who_is_harry():
#     print("Harry is good!!!!!!")
# # (2)whose_harry=dec1(who_is_harry)
# # (3)who_is_harry()  
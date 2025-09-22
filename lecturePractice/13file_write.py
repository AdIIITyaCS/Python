# # writing in a file if not present then create that file then write
# f = open("adi.txt", "w")
# f.write("MANGO IS NOT ALWAYS EATEN")
# f.close()


# # print no. of character that we are going to write same as above
# f = open("adi.txt", "a")
# a=f.write("MANGO IS NOT ALWAYS EATEN")
# print(a) # this line will print the no. of characters
# f.close()


# # read and write both in file
# f = open("adi.txt", "r+")
# print(f.read())
# f.write("\nTHANKYOU")
# f.close()

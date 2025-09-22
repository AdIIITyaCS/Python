# # print statement with limited characters
# f = open("file.txt", "rt")
# content = f.read()
# print(content)
# f.close


# # print statement next to next
# f = open("file.txt", "rt")
# content = f.read(3)   # this will read 3 charac
# print(content)
# content = f.read(3)  # this will read next 3 charac
# print(content)
# f.close()


# # print all statements line by line
# f = open("file.txt", "rt")
# for line in f:
#     print(line, end="")
# f.close()


# print single line
# f = open("file.txt", "rt")
# print(f.readline())
# print(f.readline())
# f.close()


# # print all lines
# f = open("file.txt", "rt")
# print(f.readlines())
# f.close()


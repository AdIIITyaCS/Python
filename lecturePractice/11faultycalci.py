D = {"45*3": "555",
     "56+9": "77",
     "56/6": "4"}
n1 = int(input("ENTER 1ST NO.\n"))
op = input("ENTER operator\n")
n2 = int(input("ENTER 2ND NO.\n"))
val = str(n1) + op + str(n2)
if val in D:
    print(D[val])
else:
    print("ANS", eval(val))
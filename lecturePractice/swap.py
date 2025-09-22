a=int(input("start with 1:: "))
while(a!=0):
    n1 = input("ENTER 1ST NUMBER: ")
    n2 = input("ENTER 2ND NO: ")
    print("YOUR GIVEN NO. ARE ",n1,n2)
    print("1.Direct Interchange")
    print("2.USING 3RD VARIABLE")
    i=int(input("ENTER BY WHICH METHOD YOU WANT TO SWAP!!!!!!!! "))
    if i==1:
        (n1 , n2) = (n2 , n1) 
        print(n1,n2)
    elif i==2:
        t = n1
        n1 = n2
        n2 = t
        print(n1,n2)
    print("Do you want to continue swapping? ")
    a=int(input("0 to exit::1 to continue"))

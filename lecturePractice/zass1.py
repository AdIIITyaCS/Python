from functools import reduce
PI = 3.14
def swap(a,b):
    (a,b)=(b,a)
    return print(a, b)
def areaPeri(r):
    area=PI*r*r
    peri=2*PI*r
    return print(area,peri)
def compute():
    n=int(input("Enter no:  "))
    exp=(100*n+10*n+n)+(10*n+n)+n
    return print(exp)
def oddEven():
    n=int(input("Enter no:  "))
    return print(n," is even") if n%2==0 else print(n," is odd")
def averMark():
    l=[]
    for i in range(5):
        m=int(input("Enter your marks(0 < marks < 100): "))
        l.append(m)
    mark=reduce(lambda a,b:a+b ,l)
    avg=mark/len(l)
    if avg>90 and avg<=100:
        return print('Ex')
    elif avg>80 and avg<=90:
        return print('A')
    elif avg>70 and avg<=80:
        return print('B')
    elif avg>60 and avg<=70:
        return print('C')
    elif avg<=60:
        return print('D')
    else:
        return print("Not any grade")

x=9
while x:
    print("1.TO SWAP TWO NO-->>>>>") 
    print("2.TO FIND AREA AND PERIMETER OF CIRCLE-->>>>>")  
    print("3.TO FIND VALUE OF EXPRESSION-->>>>>")  
    print("4.TO DETECT EVEN OR ODD NO-->>>>>") 
    print("5.TO FIND GRADE OF STUDENT-->>>>>") 
    x=int(input("Enter 0 for EXIT (0,1,2,3,4,5):"))
    if x==1:
        print("1.TO SWAP TWO NO-->>>>>") 
        a=int(input("Enter no1: ")) 
        b=int(input("Enter no2: ")) 
        swap(a,b)
    elif x==2:
        print("2.TO FIND AREA AND PERIMETER OF CIRCLE-->>>>>")  
        r=int(input("Enter radius: "))
        areaPeri(r)
    elif x==3:
        print("3.TO FIND VALUE OF EXPRESSION (n+nn+nnn)-->>>>>")  
        compute()
    elif x==4:
        print("4.TO DETECT EVEN OR ODD NO-->>>>>") 
        oddEven()
    elif x==5:
        print("5.TO FIND GRADE OF STUDENT-->>>>>") 
        averMark()





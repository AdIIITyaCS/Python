n1 = 93
n2 = 34
n3 = int(input("enter"))
if (n1 > (n3 + n2)):
    print("n1 is greater")
else:
    print("n3 is king")

while(1):
   n1 = int(input("ENTER YOUR CHOICE\n"))
   if(n1>=5):
        print("NEXT TRY")
        continue
   else:
        print("BEST TRY")
        break

things = [int, float, 23, 67, 2, 88, "HURRY"]
for item in things:
    if str(item).isnumeric() and item > 6:
        print(item) 

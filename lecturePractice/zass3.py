from functools import reduce

dict1={
    "k2":[7,8,6,9,9],
    "k1":[7,8,6,7,7,9],
    "k3":[7,8,6,5,9]
}
s_list=sorted(dict1.items())
print("1.Sorted list: ",s_list)
avr_list=[]
for value in dict1.values():
    a=reduce(lambda a,b:a+b,value)/len(value)
    avr_list.append(a)  
l=len(avr_list)
if l%2==1:
    idx=(l-1)//2
    med=avr_list[idx]
else:
    med=(avr_list[(l/2)-1]+avr_list[l/2])//2
print("2.Median of the averages of each list: ",med)

filt_list=[]
b=[]
for value in dict1.values():
    b=list(filter(lambda a:a<=8,value))
    filt_list.append(b)
print("4.List containing Values<=8:  ",filt_list)
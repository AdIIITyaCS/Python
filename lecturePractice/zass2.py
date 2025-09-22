l1 = [23, 13.2, "IIITK", 23, 52, 52, 52, 52, "iiitk"]
print(l1)
short_l1= set(l1)
l2_int=[]
l2_float=[]
l2_str=[]

add=0
for item in short_l1:
    if isinstance(item, int):
        l2_int.append(item)
        add+=item
    if isinstance(item, float):
        l2_float.append(item)
    if isinstance(item, str):
        l2_str.append(item)
total_list=[l2_str,l2_int,l2_float]
print("1.Sum of INTEGERS from short_list:  ",add)

consecutive_indices = []
i=0
for i in range(len(l1) - 2):
    if l1[i] == l1[i + 1] == l1[i + 2]:
        a=i
        consecutive_indices.append(i)
print("2.list contains 3 or more consecutive same elements corresponding indices: ",(a,a+2))



print("3.frequencies of all the elements in the list: ")
for item in short_l1:
    d1_dict={}
    d1_dict.update({item:l1.count(item)})
    print(d1_dict)
print("5.Sub-lists based on the data types:  ",total_list)


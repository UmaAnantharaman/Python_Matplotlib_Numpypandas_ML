import os
list1 = [1,2,3,4,5]
list2 = [2,2,2,2,2]
list3 = [0,0,0,0,0]
index = 0
len_list1 = len(list1) 
print(len_list1)
for index in range(0,len_list1):
    list3[index] = list1[index] + list2[index]
    index+=1
print(list3)

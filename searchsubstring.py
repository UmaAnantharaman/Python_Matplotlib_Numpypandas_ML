list_1 = ['Conversations with Mother','Mother Teresa of Cats','Nun']
list_2 = ['Late Night Talks with Mother','Godfather','Spiderman']
list_3 = list_1 + list_2
print(list_3)
for index in list_3:
    result = index.find('Mother')
    print(result)
    if result != -1:
        print('contains substring Mother')
    else:
        print('does not contain substring Mother')

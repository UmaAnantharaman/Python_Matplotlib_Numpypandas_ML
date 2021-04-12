from collections import OrderedDict
  
dict1 = {'zavi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}
dict2 = {3:4,1:2,6:8,2:5}
##dict1 = OrderedDict(sorted(dict1.items()))
##dict2 = OrderedDict(sorted(dict2.items()))
dict3=sorted(dict1.items())
dict4=sorted(dict2.items())
print(dict3)
print(dict4)


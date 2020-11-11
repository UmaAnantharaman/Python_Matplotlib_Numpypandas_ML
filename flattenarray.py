def flatten(lst):
    newlst=[]
    [newlst.append(x) if type(x) is int else newlst.extend(x) for x in lst]
    return newlst
print(flatten([1,2,3, [4,5], 6, [7,8], 9]))

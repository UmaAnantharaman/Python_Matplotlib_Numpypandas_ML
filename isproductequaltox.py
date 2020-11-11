def isProduct(arr,n,x):
    for i in arr:
        for j in arr:
            if i*j==x:
                return True
    return False

arr = [10,40,25,4,100]
x = 400
n = len(arr)
if(isProduct(arr,n,x)==True):
    print("Yes")
else:
    print("No")

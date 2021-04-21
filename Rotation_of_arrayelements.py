# Function to reverse arr[] from index start to end
def revarray(arr):
    arr1=arr.copy()
    for i in range(0,len(arr)):
        if i+d<len(arr):
           arr[i]=arr1[i+d]
        if i+d>=len(arr):
           arr[i]=arr1[(i+d)-len(arr1)] 
        print(arr)
def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i])
        
arr = [1, 2, 3, 4, 5, 6, 7]
d=3
revarray(arr)
printArray(arr)


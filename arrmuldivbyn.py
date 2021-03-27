def findremainder(arr, lens, n):
	mul = 1
	for i in arr:
		mul = mul * i 

	return mul % n


# Driver code
arr = [100, 10, 5, 25, 35, 14]
lens = len(arr)
n = 11

print(findremainder(arr, lens, n))



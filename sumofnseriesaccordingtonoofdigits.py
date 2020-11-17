'''Given a natural number  n  (where  1≤n≤9 ), find the sum of the series having  n  number of numbers such that the series is  n,nn,nnn,…nnn…n  times.

Hence, the required sum is

n+nn+nnn+⋯+nnn…n '''

# Python program to sum the given series 
  
def Series(n,m):
    str_n = str(n)
    sums = n
    sum_str = str(n)
    for i in range(1,m):
        sum_str = sum_str + str_n
        sums = sums + int(sum_str)
    return sums

#Driver code
n = 2
m = 2
total = Series(n,m)
print(total)
    


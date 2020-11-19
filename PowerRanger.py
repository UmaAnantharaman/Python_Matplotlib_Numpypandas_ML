'''
PowerRanger
Given 3 inputs n, minimum, & maximum, find the number of values raised to the nth power that lie in the range [minimum, maximum], inclusive.

Constraints:

Remember that the range is inclusive.

a < b will always be true.

Input Format

Three integer value of n, minimum, maximum


Sample Input 1

2, 49, 65
Sample Output 1

2
 
# 2 squares (n^2) lie between 48 and 65, 49 (7^2) and 64 (8^2)'''
import math

def powerranger(n,minimum,maximum):
    count = 0
    raise_to_power = n
    for ans in range(1,maximum):
        value = math.pow(ans,n)
        if value in range(minimum,maximum):
            count = count+1
    return count

if __name__ == '__main__':
    n = int(input())
    minimum = int(input())
    maximum = int(input())
    result = powerranger(n,minimum,maximum)
    print(result)
    
        
    


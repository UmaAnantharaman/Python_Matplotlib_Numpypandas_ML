import os
import sys

input_string = str(input())
for t in input_string:
    count = input_string.count(t)
    if count == 2:
        new_string = input_string.replace(t,"")

print(new_string)
    

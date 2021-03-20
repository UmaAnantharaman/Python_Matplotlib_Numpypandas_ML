# Initializing String  
test_str = "Hello-world"

print("which index do you want to remove?")
i = int(input())

# Printing original string  
print ("The original string is : " + test_str) 
  
# Removing char at pos 3 
# using slice + concatenation 
new_str = test_str[:i-1] +  test_str[i:] 
  
# Printing string after removal   
# removes ele. at 3rd index 
print ("The string after removal of i'th character : " + new_str) 

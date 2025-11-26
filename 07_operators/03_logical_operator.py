c = True 
d = False

# Logical Operators is used to combine conditional statements
print(True and True) # it gives True if both the statements are true otherwise it gives False
print(True and False)
print(False and True)
print(False and False)

print("For Or Operator...")
print(True or True) # it gives True if at least one statement is true otherwise it gives False
print(True or False)
print(False or True)
print(False or False)

print("Not Operator") # it reverses the boolean value
print(not(True) ) 
print(not(False) ) 



# a = 5 and b = 6

# In binary: 5 = 0b0101, 6 = 0b0110
# a & b (bitwise AND)

# AND compares each bit: 0101 & 0110 = 0100
# 0100 in decimal = 4
# So a & b -> 4
# ~b (bitwise NOT / complement)

# Flips all bits in two’s-complement form
# In Python, ~n equals 

a = 5   
b = 6
print(a & b , ~b) 

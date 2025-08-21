def add (a, b):
    x = a + b
    return x
c  = add(3, 7)
print(c)

def add (a, b , c= 9): #because c has a default value
    x = a + b
    return x
c  = add(3, 7)
print(c)

def add (a, b,c):
    x = a + b + c
    return x
c  = add(a = 3 , b = 8 , c = 9)
print(c)


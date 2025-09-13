from functools import reduce
numbers = [44, 32 , 223]
         #[76,223]
         #[299]
def sum (a,b):
    return a +b 

c = reduce(sum, numbers)
print(c)
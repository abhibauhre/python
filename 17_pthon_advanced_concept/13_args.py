def sum(*args):
#args will be tuple of all the value pass to the sum
    total = 0
    for items in args:
        total += items
    return total    

print(sum(3, 2, 22))        

def repeat(n): # this is decorator with argument it is take an argument n
    def decorator(func): # this is a decorator function inside the repeat function
        def wrapper(a): # this is a wrapper function inside the decorator function 
            for i in range (n): # this is a for loop that will run n times
                func(a) # this is call the say_hello function inside the wrapper function
        return wrapper  # this is return the wrapper function inside the decorator function
    return decorator # this is return the decorator function inside the repeat function
@repeat(8) # this is use the repeat function to decorate the say_hello function and passing the argument 8
def say_hello(name): # this is a function that we want to decorate
    print(f"hello {name}") # this is print the name of the person
say_hello("harry")  #this is call the say_hello function and passing the argument harry



#argument is a function that takes an argument and returns a function
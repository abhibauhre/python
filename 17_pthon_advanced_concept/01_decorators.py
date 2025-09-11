#decorators is a function that takes a function , its creates a wrapper
# function inside a body of decorator function and returns the wrapper function
# def decorator(func): # this is a decorator function
#     def wrapper(): # this is a wrapper function
#         print("this is before function execution")
#         func()# this is call the say_hello function inside the wrapper function 
#         print("this is after function execution")
#     return wrapper # this is return the wrapper function 
    
# @decorator # this is use the decorator function to decorate the say_hello function    
# def say_hello(): # this is a function that we want to decorate
#     print("hello world")
        
        
        
# f = decorator(say_hello) # this is call the decorator function and passing the say_hello function as an argument
# f() # this is call the wrapper function inside the decorator function

def decorator(abhi):
    def wrapper():
        print("i am create a file be ready to execute ")
        print("i am executed this function")
        abhi()
        print("hello world i am abhi")
    return wrapper
@decorator
def say_hello():
    print("hello")        

say_hello()    


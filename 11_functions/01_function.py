# A function is a reusable block of code that performs a specific task.
# You define a function using:

# def function_name(parameters):
#     # body
#     return value


# Functions help:

# reduce code repetition

# increase readability

# break big programs into small pieces

# implement logic cleanly

# perform modular programming

# Topics included:

# Normal Functions

# Function Arguments (positional, keyword, default, *args, **kwargs)

# Lambda Functions

# Recursion

# Modules / Custom Modules

# Function Scope (Local, Global, Nonlocal)


# a = 3
# b = 7
# c= 9

# average =(a + b + c) / 3
# print(average)
# a1 = 3
# b2= 7
# c3 = 5

# average =(a1+ b2 + c3) / 3
# print(average)
def average(a,b,c):
    d = (a + b + c )/3
    return d
    # print(d)
a1 =average(3, 7, 9)
a2 =average(5, 7, 9)
print(a1 ,a2)
#conceptual questions
'Q1.What is the fundamental difference between a variable named age and a variable named Age in Python?'
age = 34
Age = 45
print(age)#34
print(Age)#45
#In Python, variable names are case-sensitive. Therefore, 'age' and 'Age' are two distinct variables.

'Q2.What is the primary purpose of the type() function?'
print(type(age))  # <class 'int'>
#The primary purpose of the type() function is to determine the data type of a given variable or value.
#It returns the type as a class object, allowing you to identify whether a variable is an integer, float, string, boolean, etc.

'Q3.Why does the input() function always return a string, even if you enter a number?'
# user_input = input("Enter a number: ")
# print(type(user_input))  # <class 'str'>
#The input() function always returns a string because it is designed to capture user input as text.
'Q4.Can a variable name in Python start with a number? Provide a simple yes or no and explain why based on the rules youve learned.'
#No, a variable name in Python cannot start with a number. This is because variable names must begin with a letter (a-z, A-Z) or an underscore (_), and cannot start with a digit. 
# This rule helps to distinguish variable names from numeric literals and ensures that the syntax of the language remains clear and unambiguous.
'Q5.What is typecasting, and why is it necessary when you take a number as input from a user to perform a mathematical calculation?'
#Typecasting is the process of converting one data type into another. 
# It is necessary when you take a number as input from a user because the input() function returns a string by default.

#Output prediction questions
a = "34"
b = 23
print(a + str(b))
#output is 3423
'Q2.'

pi = 3.14
pi_int = int(pi)
print(pi_int)
print(type(pi_int))
#output is 3 and class int
'Q3.'

name = "Harry"
age = 34
print("My name is " + name + " and my age is " + str(age))
#output is my name is harry and my age is 34

'Q4'

a = "10"
b = "20"
print(int(a) + int(b))
#output is 30
'Q5.'
x = input("Enter a value: ") # User enters 5
y = input("Enter another value: ") # User enters 10
print(x + y)
#output is 15
'CODING QUESTIONS'
'''[Write a Python program that asks for the user's name and then prints a welcome message
, like "Hello, [Name]!".]'''

Name = input("Enter your name")
print("hello" + Name + '!')

'''[Write a program that declares two integer variables, a and b, 
assigns them values, and then prints their sum.]'''

a = int(input("Enter a value "))
b = int(input ("Enter b value "))
print(a + b)
''' Write a program that asks the user for their birth year and
 calculates their approximate age.
'''
birth_year = int(input("Enter a birth year "))
current_year = 2026
current_age = current_year - birth_year
print(current_age)
''' Write a program that takes a floating-point number from the user
 and prints the integer part of that number.'''
num = float(input("enter floating number"))
print(int(num))
'''Create a program that asks for two numbers, converts them to integers,
 and then prints the result of the first number multiplied by the second.'''
num_1 = int(input("enter 1 number"))
num_2 = int(input("enter 2 number"))
print(int(num_1)*int(num_2))
#DEBUGGING QUESTIONS
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print("The sum is: ",result)
#question 2
first_number = 10
second_number = 20
sum = first_number + second_number
print(sum)

#REAL WORLD MINI CHALLENGE
total_bill_amount = float(input("enter total bill amount"))
tip_percentage = float(input("enter tip percentage"))
tip_amount =(total_bill_amount * tip_percentage) / 100
total_bill = total_bill_amount + tip_amount
print("tip amount",total_bill)
print("final total bill",total_bill)


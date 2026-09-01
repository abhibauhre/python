#CONCEPTUAL QUESTION 
#Q1.What is the fundamental difference between a variable named age and a variable named Age in Python?
age = 20
Age = 20 
print(age)
print(Age)
# In Python, variable names are case-sensitive. So, 'age' and 'Age' are two different variables.

#Q2.What is the primary purpose of the type() function?
name = 'abhi'
print(name)
print(type(name))
# The primary purpose of the type() function is to determine the data type of a variable or value. 
# It returns the type of the object passed to it, allowing you to understand 
# what kind of data you are working with in your program.

#Q3.Why does the input() function always return a string, even if you enter a number?
age = input("Enter your age: ")

print(age)
print(type(age))

# The input() function always returns a string because 
# it is designed to capture user input as text.

#Q4.Can a variable name in Python start with a number?
# Provide a simple yes or no and explain why based on the rules you've learned.
#1age = 20 #invalid because variable names cannot start with a number in python


'Q5.What is typecasting, and why is it necessary when you take a number as input from a' 
'user to perform a mathematical calculation?'

# Typecasting is the process of converting one data type to another.
# It is necessary when you take a number as input from a user because the input() function always returns a string.
# To perform mathematical operations, you need to convert the string to a numeric type, such as an integer or a float.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)
#output 1020 

#OUTPUT PREDICTION QUESTION
a = "34"
b = 23
print(a + str(b))
#op-3423

pi = 3.14
pi_int = int(pi)
print(pi_int)
print(type(pi_int))
#op = 3 ,class int 

name = "Harry"
age = 34
print("My name is " + name + " and my age is " + age)
#op = TypeError: can only concatenate str (not "int") to str

a = "10"
b = "20"
print(int(a) + int(b))
#op = 30

x = input("Enter a value: ") # User enters 5
y = input("Enter another value: ") # User enters 10
print(x + y)
#op = 510

#CODING QUESTIONS
'Q1.Write a Python program that asks for the users name '
'and then prints a welcome message, like "Hello, [Name]'
name = input("enter your name")
print("hello," + name + "!")

'Q2.Write a program that declares two integer variables,'
' a and b, assigns them values, and then prints their sum.'
a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
print (a + b)

'Q3. Write a program that asks the user for their birth year '
'and calculates their approximate age'

birth_year = int(input("enter your birth year"))
current_year = 2026

age = current_year - birth_year
print(f'your approximate age is {age}')

'Q4.Write a program that takes a floating-point number from the user '
'and prints the integer part of that number'

num = float(input("enter the number"))
print(int(num))

'Q5.Create a program that asks for two numbers, converts them to integers,'
' and then prints the result of the first number multiplied by the second'
num1 = int(input("enter 1 number"))
num2 = int(input("enter 2 number"))

print(int(num1) * int(num2))

#DEBUGGING QUESTIONS 
'Q1.The following code is supposed to add two numbers provided by the user, '
'but its not working correctly. Find the bug and fix it.'

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# result = num1 + num2
# print("The sum is: " + result)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print("The sum is: " + result)

'Q2.This code has an invalid variable name. '
'Identify it, fix it, and explain why it was wrong.'

# 1st_number = 10
# 2nd_number = 20
# sum = 1st_number + 2nd_number
# print(sum)
first_number = 10
second_number = 20

sum = first_number + second_number

print(sum)
# The variable names '1st_number' and '2nd_number' are invalid 
# because variable names cannot start with a number.

#REAL-WORLD MINI CHALLENGE
# Create a simple "Tip Calculator".

# Ask the user for the total bill amount (e.g., 55.75).
# Ask the user for the tip percentage they'd like to give (e.g., 15).
# Calculate the tip amount.
# Calculate the total bill (bill + tip).
# Print the tip amount and the final total bill for the user.

total_bill = float(input("enter your total bill"))
tip_percentange = float(input("enter tip percentage"))
tip = total_bill *  tip_percentange / 100
real_total_bill = total_bill + tip
print(f'the total tip amount is :{tip},total bill for the user is :{real_total_bill}')
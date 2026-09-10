'Q1.What is the purpose of a single-line comment?'
# The purpose of a single-line comment is to provide explanations or notes within the code that
# are ignored by the interpreter. They help improve code readability and understanding for anyone reading the code, 
# including the original developer and others who may work on it in the future.

'Q2.What is the purpose of triple-quoted text in the examples?'
# The purpose of triple-quoted text in Python is to create multi-line strings or docstrings.
# They can span multiple lines and are often used for documentation purposes, allowing developers 
#to include detailed explanations or descriptions of functions, classes, or modules.
# Triple quotes can also be used for multi-line comments, although they are technically treated as string literals.

'Q3.What does \n do inside a string?'
# The \n is an escape character in Python that represents a newline.

'Q4.What does \t do inside a string?'
# The \t is an escape character in Python that represents a tab space. It is used to insert 
# horizontal spacing within strings, making the output more organized and readable.

'Q5.What is the difference between the sep and end arguments of print()?'
# The sep argument in the print() function specifies the string that is inserted between
#  the values being printed.

#CODING QUESTION 
'Q1.Print your name and age on separate lines using one print() statement.'
print("Abhishek\n20")
'Q2. Print three words separated by `---`.'
print("Hello---World---Python")
'Q3.Ask the user for their name and print Hello, [name]!.'
name = input("Enter your name: ")
print("Hello, " + name + "!")
'Q4.Print a two-line address using `\n` and a tab-separated phone number using `\t`.'
print("Jhansi, Uttar Pradesh\nIndia\t9876543210")
'Q5.Ask the user for two numbers, convert them to integers, and print their sum in this format:'
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)

#Debugging question 
i = 1

while i < 6:
    print(i)
    i += 1

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")    

s = "aabbcdde"

count = {}

# Count each character
for ch in s:
    count[ch] = count.get(ch, 0) + 1

# Find first character with count 1
for ch in s:
    if count[ch] == 1:
        print(ch)
        break

numbers = [10, 5, 20, 8, 20, 15]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)


def length_of_longest_substring(s):
    seen = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1

        seen[s[right]] = right

        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length


print(length_of_longest_substring("abcabcbb"))

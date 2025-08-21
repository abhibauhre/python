# s = "hello world"#strings is immutable
# # s[0]="r"#you can do this
# a = len(s)
# print(a)
# print(s.upper())
# print(s.lower())
# print(s.capitalize())#first letter is capital and others in small
# print(s.title()) #first letter of every word is capital and other letter is smal

# text = " \nhello world "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip()) # Output: "hello world "
# print(text.rstrip()) # Output: " hello world"

# text = "python is fun and fun and fun"
# print(text.find("is"))#The output is 7 because the .find() method in Python returns the index of the first occurrence of the substring you are searching for.
# print(text.replace("is","awesome"))

# text = "apple , banana , cherry"
# #print(text.split(","))  # Output: ['apple ', ' banana ', ' cherry']
# print(",".join(['apple', 'banana', 'cherry']))  # Output: "apple,banana,cherry"
text = "python123"
print(text.isalpha())#output False because it contains numbers
print(text.isdigit()) #output False because it contains letters and numbers
print(text.isalnum()) #output True because it contains both letters and numbers
print(text.isspace())   # Output: False (because of spaces)
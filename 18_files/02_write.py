#write to a file called abhi bauhre.txt
#it should contain data about of abhi bauhre

f = open("abhi bauhre.txt","w")

string = '''hello guys i am abhishek i love coding and i am 18 years old'''

content = f.write(string)
print(content)

f.close()

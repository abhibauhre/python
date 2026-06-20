#sum and multiply all item in list
list = [2,3,4,5]
totalsum = 0 
totalmul = 1
for i in list:
    totalsum += i
    totalmul *= i

print(totalsum,totalmul)    

#program to find words longer than n from a list
words = ["python", "java", "programming", "code", "developer"]
n = 5
result=[]
for word in words:
    if len(word) > n:
        result.append(word)
print("words longer than",n,"is are",result)        

#Program to check whether a number is Fibonacci or not
num = int(input("enter the number"))
a,b = 0,1

while b < num:
    a , b = b, a + b
    
if b == num or num ==0:
    print("fibonacci")
else:
    print("not fibonacci")

#wap to print the number of specified list remove even numbers 

lst = [10, 15, 20, 25, 30, 35]

result=[]
for i in lst:
    if i % 2 !=0:
        result.append(i)
print("List after removing even numbers:", result)



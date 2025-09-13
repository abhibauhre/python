def very_slow_function ():
    print("something")
    print("something")
    print("something")
    print("something")
    print("something")
    return 70
# a = very_slow_function()
if ((a:=very_slow_function())>10):#isme mein direct value store hojati hai is operator ki help se
    print(a)
else:
    print ("it is not greater than 10")   
while(data:=input("Enter the value: ")):
    print(data)
    if data == "q":
        break 
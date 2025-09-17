try :
    a = int(input("enter a first number"))
    b = int(input("enter a second number"))

    print('''what kind of operation do you want to perform .\npress + for addition .\npress - for subtraction.\npress / for division.\npress * for multipication''')
    
    o = input ("enter a operation")

    match o :
        case "+":
            print(f"the result is {a + b}")
        case "-":
            print(f"the result is {a - b}")
        case "/":
            print(f"the result is {a / b}")
        case "*":
            print(f"the result is {a * b}")
        case default :
            print("there was an error")   
except Exception as e :
    print("please input valid operation")                    
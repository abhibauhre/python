# a = int(input("enter a first number :"))
# b = int(input("enter a second number:"))
# try :
#     c = a / b
#     print(c)
    

# except Exception as e:
#     print(e)
# #this is always executed no matter if try completely executed or not
# finally:
#     print ("this is always executed")
def divide(a,b):
    try :
        c = a / b 
        print(c)
        return c
    
    except Exception as e :
        print (e)
        return None
    
    finally:
        print("this is always executed")

a = int(input("enter a first number :"))
b = int(input("enter a second number:"))
divide(a,b)
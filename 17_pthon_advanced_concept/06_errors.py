# while True:# Keep doing this forever, or until you explicitly tell it to stop.
#     try:
#          a = int(input("enter a first number :"))
#          b = int(input("enter a second number:"))

#          print(f"the division is {a / b}")
#     except ValueError:
#          print("please dont perform bad typecast")
#     except ZeroDivisionError:
#          print("dont divide by zero")          

#     except Exception as e:
#          print("some error occured", e) 
# # Try and accept statements are used to handle errors in Python.
a = int(input("enter a first number :"))
b = int(input("enter a second number:"))
if b == 0 :
    raise ValueError("Please dont divide by 0")
print(f"the division is {a / b}")

 

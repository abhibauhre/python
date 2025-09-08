# class employee:
#     def __init__(self, name, salary, bond):
#         self.name = name # instance variable and we are initializing it using constructor
#         self.salary = salary
#         self.bond = bond

#     def getsalary(self): # it is a method of class employy and it is used to return the salary of employee
#         return self.salary

#     def getinfo(self): # method to display employee information
#         print(f"name of employee is {self.name}. the salary of employee is {self.salary}. the bond of employee is {self.bond}")#accessing instance variable using self

# e = employee("harry", 100000, 2)  # object creation and passing values to constructor
# e.getinfo()#calling method to display employee information

class workers:

    def __init__(self, name, salary, bond):
        self.name = name
        self.salary = salary 
        self.bond = bond

    def getsalary(self):
        return self.salary
    
    def getinfo(self):#getinfo is a method to display worker information
        print(f"name of worker is {self.name}. the salary of worker is {self.salary}.bond is {self.bond}")


e = workers("abhi", 100000, 20)
print(e.getsalary())
e.getinfo()

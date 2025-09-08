# class employee:
#     company = "google" #class attribute is not printed using constructor
#     def __init__(self, name, salary, bond, company):
        
#         self.name = name
#         self.salary = salary
#         self.bond = bond
#         self.company = company

#     def getsalary(self):
#         return self.salary

#     def getinfo(self):
#         print(f"name of employee is {self.name}. the salary of employee is {self.salary}. the bond of employee is {self.bond}")

# e = employee("harry", 100000, 2, "asus")  # object creation and passing values to constructor
# print(e.company) # it will print asus because instance variable has more priority than class variable
# print(employee.company) # it will print google because we are accessing class variable using class name

# #object introspection is used to know the attributes and methods of an object
# print(dir(e)) # it will print all the attributes and methods of object e

class workers:
    company = "abhi housing pvt. ltd"

    def __init__(self, name, salary, bond, company):
        self.name = name
        self.salary = salary 
        self.bond = bond
        self.company = company

    def getsalary(self):
        return self.salary
    
    def getinfo(self):#getinfo is a method to display worker information
        print(f"name of worker is {self.name}. the salary of worker is {self.salary}.bond is {self.bond}")


e = workers("abhi", 100000, 20, "asus")
print(e.getsalary())
print(e.company) # it will print asus because instance variable has more priority than class variable
print(workers.company) # it will print abhi housing pvt. ltd because we are accessing class variable using class name
print(dir(e)) # it will print all the attributes and methods of object e
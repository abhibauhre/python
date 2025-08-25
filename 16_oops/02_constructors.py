class employee:
    def __init__(self, name, salary, bond):
        self.name = name # instance variable and we are initializing it using constructor
        self.salary = salary
        self.bond = bond

    def getsalary(self): # it is a method of class employy and it is used to return the salary of employee
        return self.salary

    def getinfo(self): # method to display employee information
        print(f"name of employee is {self.name}. the salary of employee is {self.salary}. the bond of employee is {self.bond}")#accessing instance variable using self

e = employee("harry", 100000, 2)  # object creation and passing values to constructor
e.getinfo()#calling method to display employee information

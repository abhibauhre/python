class employee:
    company = "hp"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def __str__(self):#this method generally use by basic coder
        return f"the name is the employee is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):#this method mostly used by developers
        return f"name: {self.name}\nsalary: {self.salary}"
    def __len__(self):#its tell how the length of the name
        return len(self.name)



e = employee("abhi" , 57477)
print(e.name , e.salary)    
print(str(e))
print(repr(e))
print(len(e))

class employee:
    company = "abhi housing"
    def __init__(self, name , salary):
        self.name = name 
        self.salary = salary
    
    #this is a instance method(default)
    def print_info(self):
        info = f"the name is {self.name} and the salary is {self.salary}"
        print(info)
    @staticmethod #static method is use to dont use {self} in the function
    def sum (a,b):
        return a + b
    #class method 
    @classmethod
    def print_company(cls):
        print(cls.company)
    @classmethod    
    def change_company(cls,new_company):
        cls.company = new_company

    
e1 = employee("ABHI",15555)
e2 = employee("ARYAN",166373)
# e1.print_info()
# e2.print_info()

# print(e2.sum(2,5))
e1.print_company()
e1.change_company("acer")
e1.print_company()




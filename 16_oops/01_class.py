#class is an abstraction of real worlds entities and it is a blueprint of an 
# object e.g form for an exam contains name, roll number, marks etc

#object is a specific instance of a class e.g form which contain the data of a particular student

# class employee:
#     company = "google"  #class variable

#     def getsalary(self):
#         return 100000
    
# e = employee()  #object creation    
# print(e.getsalary())
# print(e.company)  #accessing class variable using object

# e2 = employee() 
# print(e2.getsalary())
# print(e2.company) #accessing class variable using object
# #e and e2 is is a self variable which is used to access the instance variable and method of class object

class workers:
    company = "abhi housing pvt. ltd"
    
    def getsalary(this):#inside a function this is used to access the instance variable and method of class object
        return 100000
    
e = workers()
print(e.getsalary())
print(e.company)
#e is an object of class workers    
# OOP (Object-Oriented Programming) is a programming style where we design programs using classes and objects.

# OOP has 4 pillars:

# Encapsulation — binding data + methods together

# Abstraction — hiding complex details

# Inheritance — child classes inherit features from parent

# Polymorphism — same function name, different behavior
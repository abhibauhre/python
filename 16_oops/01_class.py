#class is an abstraction of real worlds entities and it is a blueprint of an 
# object e.g form for an exam contains name, roll number, marks etc

#object is a specific instance of a class e.g form which contain the data of a particular student

class employee:
    company = "google"  #class variable

    def getsalary(self):
        return 100000
    
e = employee()  #object creation    
print(e.getsalary())
print(e.company)  #accessing class variable using object

e2 = employee()
print(e2.getsalary())
print(e2.company) #accessing class variable using object
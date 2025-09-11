# class Employee:
#     def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary

#     @property
#     def first_name(self):
#         l = self.name.split(" ") 
#         return l[0]
    
#     @first_name.setter
#     def first_name(self, first):
#         l = self.name.split(" ")
#         new_name = f"{first} {l[1]}" 
#         self.name = new_name

# e = Employee("Jack Doe", 34555)
# # print(e.first_name())
# # e.set_first_name("John")
# # print(e.name)

# print(e.first_name)
# e.first_name = "John"
# print(e.name)

class employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @property    #You can access it like an attribute without parentheses.
    def first_name(self):
        l = self.name.split(" ")
        print(l)
        return l[0]
    @first_name.setter #This method allows you to set first_name like this:
    def first_name(self,first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name
e = employee("jack doe",19999)    
# print(e.first_name())
# e.set_first_name("john")
# print(e.name)
print(e.first_name)
e.first_name = "abhi"
print(e.name)

            
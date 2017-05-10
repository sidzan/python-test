#!/bin/python3

class Employee(object):
    empCount = 0
    def __init__ (self,name,salary):
        self.name = name
        self.salary = salary
        self.age = 10
        Employee.empCount+=1

    def displayCount(self):
        print ("Total Employees is " ,Employee.empCount)

    def displayEmployee(self):
        print ("Name ",self.name," salary is ",self.salary, " age is ",self.age);
        try:
            print ("phone",self.phone)
        except :
            print ("no phone")

    def __del__(self):
        print("i will be deleted")    

class Contact(Employee):
    def __init__(self):
        print ("calling child class")

emp1 = Employee("Sijan",40000)
emp1.displayCount()
emp1.displayEmployee()
emp1.salary = 50000 #modify salary
print(getattr(emp1,'name')) # get attribute
print(hasattr(emp1,'phone')) # check if has attribute
if not hasattr(emp1,'phone'): # Check if has attribute, if not add one
    setattr(emp1,'phone',1234)
print(hasattr(emp1,'phone')) 
#emp2.displayCount()
#emp2.displayEmployee()

emp1.displayEmployee()

# print ("Employee.__doc__:", Employee.__doc__)
# print ("Employee.__name__:", Employee.__name__)
# print ("Employee.__module__:", Employee.__module__)
# print ("Employee.__bases__:", Employee.__bases__)
# print ("Employee.__dict__:", Employee.__dict__)

sijan = Contact()

print("is subclass",issubclass(Contact,Employee))
print("is instance",isinstance(emp1,Employee))

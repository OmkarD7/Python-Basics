'''
1. class keyword
2. instance attribute
3. class attributes
4. __init__ method -> constructor
5. self
'''

class Employee:
    salary = 0
    count = 0
    def __init__(self):
        print("In constructor!")
        Employee.count += 1 #Employee.count is a class attribute
    
    def getEmployeeCount(self):
        print("Empoloyee Count: ")
        print(Employee.count)

emp = Employee()
emp.getEmployeeCount()
emp2 = Employee()
emp2.getEmployeeCount()
emp3 = Employee()
emp3.getEmployeeCount()
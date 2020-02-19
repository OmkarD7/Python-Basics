class Employee:
    count = 0
    def __init__(self, name, salary):
        print("In Constuctor!")
        self.name = name
        self.salary = salary
        Employee.count += 1
    def getEmployeeDetails(self):
        print("-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-")
        print("Employee Details: ")
        print("Name: ", self.name)
        print("Salary: ", self.salary)

emp1 = Employee("obb", 8888)
emp2 = Employee("bob", 6666)
emp3 = Employee("tom", 7777)
emp4 = Employee("jerry", 9999)

emp1.getEmployeeDetails()
emp2.getEmployeeDetails()
emp3.getEmployeeDetails()
emp4.getEmployeeDetails()

print("Team count: ", Employee.count)
print("Access instance attributes directly!")
print("emp1 is: ", emp1.name, "his salary: ", emp1.salary)
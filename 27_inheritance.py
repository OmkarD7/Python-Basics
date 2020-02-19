class Employee:
    def __init__(self, fname, lname):
        print("In Employee Constructor!")
        self.fname = fname
        self.lname = lname

    def getFname(self):
        return self.fname

    def getLname(self):
        return self.lname
    
class FullStackEngineer(Employee):
    def __init__(self, fname, lname, tech):
        self.tech = tech
        super().__init__(fname, lname)
    
    def getEmployeeDetails(self):
        return "Name: "+self.fname+ " " +self.lname+ "\nTechnology: " +self.tech

fse1 = FullStackEngineer("Omkar", "Dnyanmote", "Java")
print(fse1.getEmployeeDetails())
print(fse1.getFname())
print(fse1.getLname())

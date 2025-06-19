class Employee:
    company = "ITC"
    def show(self):
        print(f"the name of the emplyoee is {self.name} and the salary is{self.salary}")
class programmer(Employee):
    company="ITC Info"
    def Showlanguage(self):
        print(f"the name iss{self.name} and he is good with {self.language} language")
a=Employee()
b=programmer()
print(a.company,b.company)
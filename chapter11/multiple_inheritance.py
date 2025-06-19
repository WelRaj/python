class Employee:
    company = "ITC"
    name="default"
    def show(self):
        print(f"the name of the emplyoee is {self.name} and the salary is{self.company}")
class coder:
    language="python"
    def printLanguage(self):
        print(f"out of all the language here is your langauge: {self.language}")
class programmer(Employee,coder):
    company="ITC Info"
    def Showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language")
a=Employee()
b=programmer()
b.show()
b.printLanguage()
b.Showlanguage()
class Employee:
    language="python" 
    salary=1400000
    def getInfo(self):
        print(f"the language is {self.language} and salary is {self.salary}")
    @staticmethod
    def geet():
        print("ram is good boy")
harry=Employee()
harry.language="java"
harry.getInfo()
harry.geet()
Employee.getInfo(harry) #the another way to call getinfo function
Employee.geet()
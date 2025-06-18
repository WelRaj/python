class Employee:
    language="python" 
    salary=120000
    
    def __init__(self,name,salary,language):#this is dunder method and which is called automatically called   
             self.name=name
             self.salary=salary
             self.language=language
             print("i am creating a object")
    @staticmethod
    def geet():
        print("ram is good boy")
harry=Employee("harry",130000,"javascript")
harry.name="Harry"
print(harry.name,harry.salary,harry.language)


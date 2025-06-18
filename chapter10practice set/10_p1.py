class Programmer:
    company="microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
p=Programmer("raj","1600000",470001)
print(p.name,p.salary,p.pin,p.company)
p=Programmer("ajay","14550000",47001)
print(p.name,p.salary,p.pin,p.company)
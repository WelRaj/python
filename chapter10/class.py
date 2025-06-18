'''class Employee:
    name ="Raj"
    language="python"
    salary=1200000
harry=Employee()
print(harry.name,harry.language,harry.salary)'''
class Employee:
    language="python" #class attributes
    salary=1400000
harry=Employee()
harry.name="rajkumar" #object attributes or instance attributes
print(harry.name,harry.language,harry.salary)
harry.name="ajay"
print(harry.name,harry.language,harry.salary)
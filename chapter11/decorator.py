class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"the class atribute of a is {cls.a}")
    @property
    def name(self):
        return f"{self.fname}{self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
o=Employee()
o.a=5
o.show()
o.name ="rajkumar rathore"
print(o.fname,o.lname)
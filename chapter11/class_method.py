class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"the class atribute of a is {cls.a}")
o=Employee()
o.a=5
o.show()

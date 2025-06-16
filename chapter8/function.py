
def avg():
    a=int(input("Enter number a:"))
    b=int(input("Enter number b:"))
    c=int(input("Enter number c:"))
    avg=(a+b+c)/3
    print(avg)
avg()
print("thank you")
avg()
print("thank you")

def hello(name,ending):
    print("hi "+name)
    print(ending)
     
hello("raj","thank you")
hello("shyam","thank")
hello("ram","thankyou")
def avg1():
    a=int(input("Enter number a:"))
    b=int(input("Enter number b:"))
    c=int(input("Enter number c:"))
    avg=(a+b+c)/3
    return avg
a=avg1()
print(a)
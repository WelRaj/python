f = open("file.txt")
data = f.read()
print(data)
f.close()
#the same can be open using with
with open("file.txt") as f:
    print(f.read())
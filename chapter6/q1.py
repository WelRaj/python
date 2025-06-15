p1="ram is good boy"
p2="ram is from gwalior"
p3="he is a boy"
p4="click this"
message=input("enter your comment:")
if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("this is spam")
else:
    print("this is not spam")
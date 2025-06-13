marks = {
     "Harry":100,
     "shubam":56,
     "rohan":23
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":99,"ramu":100})
print(marks)
print(marks.get("Harry"))#print none
print(marks["Harry"])#print error
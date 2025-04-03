point = dict(x=2, y=3)
print(point["x"])
point["x"] = 10
print(point["x"])

point["z"] = 20
print(point)

#to find a key in a dictionary similar to list we can use

if "a" in point:
    print("valga")
else:
    print("valarga")

#or

print(point.get("a"))
#This returns as normal key value pair
for i in point:
    print(i, point[i])

#This returns as a tuple
for i in point.items():
    print(i)
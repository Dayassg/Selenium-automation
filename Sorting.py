numbers = [3,2,5,6,7,3,2,1]
numbers.sort() #ascending
print(numbers)
numbers.sort(reverse=False) #descending
print(numbers)

# To create a copy of sorted list
print(sorted(numbers, reverse=False))
print(sorted(numbers, reverse=True))


items = [
    ("product_1", 10),
    ("product_2", 9),
    ("product_3", 11),
]

items.sort(key=lambda item:item[1])
print(items)

list_1 = [1,2,3]
list_2 = [5,6,7]
x = zip(list_1, list_2)
y = list(x)
print(y)

c = zip("abc",list_1, list_2)
z = list(c)
print(z)

x = 12
y = 3

z = x
x = y
y = z

#or

x, y = y, x
letters = ["a","b","c"]
number = list(range(20))
multi = [1] * 5
strgs = list("Hello World")
matrix = [[0,1], [2,3]]


letters[0] = "A"
print(letters[0])
print(letters[0:2])
print(letters[::2])
print(letters[::-1])



number_1 = letters[0]
number_2 = letters[1]
number_3 = letters[2]

#or

number_1, number_2, number_3 = letters

# to get all the other values in the list using unpacking

number_1, number_2, *others = letters
number_1, *others, number_last = letters

print(others)



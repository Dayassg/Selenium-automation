letters = ["a", "b", "c", "b"]
print(letters.index("a"))    #To find index of a value
print(letters.count("b"))    #Used to find total number of occurance of b

for letter in enumerate(letters):
    value = letter
    print(value)



letters.append("d")
print(letters)
letters.insert(0, "1")
print(letters)
letters.pop()    #removes the last one
print(letters)
letters.pop(0)
print(letters)
letters.remove("b")     #it will remove the first occurance of b, loop it remove all b
del letters[0:2]        #pop can be used to remove one and del can be used to remove a range
print(letters)
letters.clear()         #Remove all/clear all value in list

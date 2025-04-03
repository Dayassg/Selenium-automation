try:
    inputs = int(input("Enter a number : "))
    y = inputs/0
    print(inputs)
except:
    print("Exception error")
else:
    print("Its gonna be fine")
finally:
    print("Finally will always be executed")

print("Hola")

with open("Basics.py") as file:
    print("Hello Worlds")
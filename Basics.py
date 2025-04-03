print("Hello World")
print("*" * 10)

first = "dayaln"
last = "suruliappan"
full_name = first+" " + last
full_name_01 = f"{first} {last} {len(first)}"
final_name = full_name_01.title()
print(final_name)

temperatue = 50
if temperatue<40:
    print("Its ok bro")

elif temperatue == 30:
    print("fine")
else:
    print("not fine")

x = 5

for i in range(x):
    i += 1
    print(i*"*")

y = 6

for i in range(1, y):
    print((y-i) * "1")

for i in range(1, 10, 2):
    print(i * "2")

for i in range(1, y):
    print((y-(i+1)) * " " + (i*"*"))

success = True
for i in range(1, y):
    if not success:
        print((y-(i+1)) * " " + (i*"*"))
else:
    print("Else part success")

for i in range(5):
    for j in range(3):
        print(f"({i}, {j})")



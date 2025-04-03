import random
import string
from random import shuffle

from Sorting import numbers

x = random.random()
print(x)
y = random.randint(1, 10)
print(y)
z = random.choice([1,2,3,4,5])
print(z)
f = random.choices([1,2,3,4,5], k=3)
print(f)
k = random.choices("password", k=4)
print("".join(k))
g = random.choices("password", k=4)
print(",".join(k))
j = random.choices(string.ascii_letters + string.digits, k=9)
print("".join(j))

num = [1,2,3,4,5]
random.shuffle(num)
print(num)

num.sort(reverse=True)
print(num)
num.sort()
print(num)
x = num[::-1]
print(x)
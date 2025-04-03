class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self, z, w):
        super().__init__()
        self.z = z
        self.w = w
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


animal = Mammal()
animal.walk()
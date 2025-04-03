from Dictionary import point


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def first_func(self):
        return self.x + self.y

point_instance = Point(2, 5)
print(point_instance.first_func())
class Point:
    color = "Blue"

    @classmethod
    def zero(cls):
        return Point(0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(F"Point ({self.x},{self.y})")

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 13)
other = Point(11, 31)
# print(point == other)
# print(point >= other)
combined = point + other
print(combined.x)

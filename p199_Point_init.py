class Point:
    """ Represents a point with x and y coordinates. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])


p1 = Point(1, 5)
p2 = Point(2, 8)
p3 = (2, 8)
print(p1, p2, p3)

print(p1 + p2)
print(p1 + p3)

class Point:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y
        self.cord = tuple((x, y))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return f'{self.name}{tuple((self.x, self.y))}'

    def invert(self):
        return Point(self.name, self.y, self.x)

    def __invert__(self):
        return self.invert()

    def get_coords(self):
        return tuple((self.x, self.y))

    def __repr__(self):
        return f'Point(\'{self.name}\', {self.x}, {self.y})'

    def __eq__(self, other):
        return self.cord == other.cord and self.name == other.name and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

p_A1 = Point('A', 1, 2)
p_A2 = Point('A', 2, 1)
p_B1 = Point('B', 2, 3)
p_B2 = Point('B', 2, 3)

print(p_A1 == p_A2, p_B1 == p_B2)
print(p_A1 != p_A2, p_B1 != p_B2)
print(p_A1 < p_A2, p_B1 > p_B2)
print(p_A1 >= p_A2, p_B1 <= p_B2)
print(max(p_A1, p_B2, p_A2, p_B2))
print(min(p_A1, p_B2, p_A2, p_B2))

points = [Point('A', 101, 1), Point('B', -1, 0),
          Point('A', 11, 0), Point('A', 111, -11)]
points.sort()
print(', '.join(map(str, points)))
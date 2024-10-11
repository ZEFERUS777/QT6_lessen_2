class Point:
    def __init__(self, name, x, y):
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


class ColoredPoint(Point):
    def __init__(self, name, x, y, color=(0, 0, 0)):
        self.color = tuple(color)
        self.name = name
        self.x = x
        self.y = y
        self.cord = tuple((x, y))
        self.r = tuple(color)[0]
        self.g = tuple(color)[1]
        self.b = tuple(color)[2]

    def get_color(self):
        return self.color

    def __invert__(self):
        return ColoredPoint(self.name, self.y, self.x, tuple((255 - self.r, 255 - self.g, 255 - self.b)))

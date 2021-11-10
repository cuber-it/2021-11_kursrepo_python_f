class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other): # self <- p1, other <- p2
        assert isinstance(other, Point), "Kein Point-Operand"
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

    def __str__(self):
        return f"Point({self.x},{self.y})"

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1+p2) # Das macht python daraus p1.__add__(p2) --> intern wird daraus: __add__(p1, p2)
print(p1 == p2)
print(p1 == p1)
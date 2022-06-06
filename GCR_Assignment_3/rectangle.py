class Rectangle():
    length = 0
    breadth = 0

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.length


r = Rectangle(25, 24)
print(r.area())

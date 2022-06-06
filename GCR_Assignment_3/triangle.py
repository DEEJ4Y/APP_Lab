from cmath import sqrt


class Triangle():
    a = 0,
    b = 0
    c = 0

    def __init__(self, s1, s2, s3):
        self.a = s1
        self.b = s2
        self.c = s3

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c)/2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


trngle = Triangle(2, 3, 2)
print(trngle.perimeter())
print(trngle.area())

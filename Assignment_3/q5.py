class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area =", 3.14 * self.radius * self.radius)

c = Circle(7)
c.area()
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def total_radius(self, other):
        return self.radius + other.radius

    def __add__(self, other):
        return self.radius + other.radius

    def __gt__(self, other):
        return self.radius > other.radius


c1 = Circle(3)
c2 = Circle(5)
total_radius = c1.radius + c2.radius
print(total_radius)  # 8

print(c1.total_radius(c2))  # 8

print(c1 + c2)  # 8

print(c1 > c2)  # True / False

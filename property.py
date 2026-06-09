class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    @property
    def is_square(self):
        return self.width == self.height
    
r = Rectangle(4, 6)

print(r.area)
print(r.perimeter)
print(r.is_square)

r.width = 6
print(r.is_square)
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
circle = Circle(7)
rectangle = Rectangle(10, 5)

print(f"Circle Area (r=7): {circle.area():.2f}")
print(f"Rectangle Area (10x5): {rectangle.area()}")

# ix. Explanation for README:
# Polymorphism is shown because both Circle and Rectangle inherit area() from Shape,
# but each implements it differently. 

# Design an abstract class Shape with an abstract method area(). Then create two derived classes, Rectangle and Circle, 
# that implement the area() method for calculating the area of a rectangle and a circle, respectively. 
# Demonstrate the use of these classes by creating objects and calculating areas.
from abc import ABC, abstractmethod
import math 
class Shape:
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        Area = self.length * self.width
        return print(f"Area of Rectangle is: {Area}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        Area = math.pi * self.radius**2
        return print(f"Area of Circle is: {Area:.2f}")

cir1 = Circle(50)
cir1.area()

rec1 = Rectangle(20,43)
rec1.area()

cir2 = Circle(6.1)
cir2.area()

rec2 = Rectangle(5,3)
rec2.area()
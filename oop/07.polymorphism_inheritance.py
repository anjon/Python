# Polymorphism = Greek word that means to "have many forms of face"
#               Poly = Many 
#               Morphe = Form
# TWO WAY TO ACTIVATE POLMORPHISM:
#       1. Inheritance = An object could be treated of the same time as parent class
#       2. "Duck Typing" = Object must have necessary attributes
# INHERITANCE

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radious):
        self.radious = radious

    def area(self):
        return 3.14 * self.radious ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side 

    def area(self):
        return self.side ** 2 

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 2

class Pizza(Circle):
    def __init__(self, topping, radious):
        super().__init__(radious)
        self.radious = radious

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza('Pepperoni', 15)]

for shape in shapes:
    print(f"{shape.area()}cm2")
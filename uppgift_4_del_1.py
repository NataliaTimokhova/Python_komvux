#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Natalia Timokhova
an area calculator for a number of shapes
"""

import math

# A basic class for all classes
# it doesn't have any specific instance variables to initialize, that is why no __init__ here.
class Formbas:
    def area(self):
        pass


# sub-classes of the 1st level (Formbas ->....)
# In sub-classes we include some variables, that is why we include __init__ in the construction
class Rectangle(Formbas):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Square(Formbas):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (self.side) **2
    

class Triangle(Formbas):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Formbas):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Hexagon(Formbas):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2
 


def main():
    # vi name classes for each variable for getting acces to the class functions later
    square = Square(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 8)
    circle = Circle(2)
    hexagon = Hexagon(4)

    # for calculating the area we call a name of the variable and the function in the relevant class
    print(f"Area of Square: {square.area():.2f}")
    print(f"Area of Rectangle: {rectangle.area():.2f}")
    print(f"Area of Triangle: {triangle.area():.2f}")
    print(f"Area of Circle: {circle.area():.2f}")
    print(f"Area of Hexagon: {hexagon.area():.2f}")

if __name__ == "__main__":
    main()



# breakpoint() is a built-in function that is used for debugging purposes

def main():
    square = Square(5)
    rectangle = Rectangle(4, 6)

    # When the program execution reaches this point, it will pause for debugging in the next lines.
    breakpoint()

    triangle = Triangle(3, 8)
    
    # if we agree with the line 88 we can press in terminal n for the checking the next line
    # or continue for skipping debugging
    circle = Circle(2)
    hexagon = Hexagon(4)
    
    print(f"Area of Square: {square.area()}")
    print(f"Area of Rectangle: {rectangle.area()}")
    print(f"Area of Triangle: {triangle.area():.2f}")
    print(f"Area of Circle: {circle.area():.2f}")
    print(f"Area of Hexagon: {hexagon.area():.2f}")

if __name__ == "__main__":
    main()

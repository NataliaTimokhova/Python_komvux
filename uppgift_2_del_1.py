#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Natalia TImokhova

"""

from geometry import triangle_area, circle_area, parallellogram_area, parallelltrapets_area, circlesector_area


'''
The function takes sets of calculations from the geometry module.
The user is asked to enter the name of the geometric figure and then to give
some values to calculate. If the name or value is misspelled,
the loop will be infinite before the User answers No to continue.
'''

def calculate_area():
    while True:
        try:
            shape = input("\nWhich shape would you like to calculate the area for?\n(triangle/circle/parallelogram/parallelltrapez/circlesector): ")

            if shape == "triangle":
                base = float(input("Enter the base length of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = triangle_area(base, height)
                print("\nArea of the triangle:", area, "\n")
            elif shape == "circle":
                radius = float(input("Enter the radius of the circle: "))
                area, circumference = circle_area(radius)
                print("\nArea of the circle:", area)
                print("\nCircumference of the circle:", circumference, "\n")
            elif shape == "parallelogram":
                base = float(input("Enter the base length of the parallelogram: "))
                height = float(input("Enter the height of the parallelogram: "))
                area = parallellogram_area(base, height)
                print("\nArea of the parallelogram:", area,"\n")
            elif shape == "parallelltrapez":
                base1 = float(input("Enter the length of the first base of the parallell trapezoid: "))
                base2 = float(input("Enter the length of the second base of the parallell trapezoid: "))
                height = float(input("Enter the height of the parallell trapezoid: "))
                area = parallelltrapets_area(height, base1, base2)
                print("\nArea of the parallell trapezoid:", area, "\n")
            elif shape == "circlesector":
                angle = float(input("Enter the angle of the circle sector in degrees: "))
                radius = float(input("Enter the radius of the circle sector: "))
                arc, area = circlesector_area(angle, radius)
                print("\nArc length of the circle sector:", arc, "\n")
                print("\nArea of the circle sector:", area, "\n")
            else:
                raise ValueError("\nInvalid shape entered.")
            
            # in this part we create an endless loop before the User writes No
            choice = input("\nDo you want to calculate the area for another shape? (yes/no): ")
            if choice.lower() == "yes":
                continue
            elif choice.lower() == "no":
                print("Thanks, bye!")
                break
            else:
                raise ValueError("\nYou did not write No, so we continue")
                
        # all errors both values and variables names are catching here
        except ValueError as e:
            print(str(e), "\n\nPlease try again.")

# call the program
calculate_area()



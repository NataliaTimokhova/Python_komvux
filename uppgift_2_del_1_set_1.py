#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Natalia TImokhova

"""

from geometry import triangle_area, circle_area, parallellogram_area, parallelltrapets_area, circlesector_area

       
        
# ger ett värde till varje input-variabel för att räkna area 
base = 5
height = 10
radius = 3
base2 = 4
angle = 45


triangle = triangle_area(base, height)
print("Area of the triangle:", triangle)

circle, circuit = circle_area(radius)
print("Area of the circle:", circle)
print("Circumference of the circle:", circuit)

parallelogram = parallellogram_area(base, height)
print("Area of the parallelogram:", parallelogram)

parallell_trapezoid = parallelltrapets_area(height, base, base2)
print("Area of the parallell trapezoid:", parallell_trapezoid)

arc, circle_sector_area = circlesector_area(angle, radius)
print("Arc length of the circle sector:", arc)
print("Area of the circle sector:", circle_sector_area)



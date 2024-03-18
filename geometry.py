#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Natali Timokhova

"""
import math

'''
The functions calculate area for different types of geometric figures.
Some input variables are needed (base, height, radius, base2, angle).
These functions will exist as a module "geometry".
The functions will be called from some other file in the same directory as
"from geometry import FUNCTION" or "import geometry" and then geometry.FUNCTION
'''

def triangle_area(base, height):
    triangle = round((0.5 * base * height), 2)
    return triangle

def circle_area(radius):
    circle = round((math.pi * radius ** 2), 2)
    circuit = round((2*math.pi*radius),2)
    return circle, circuit

def parallellogram_area(height, base):
    parallellogram = round((base*height),2)
    return parallellogram

def parallelltrapets_area(height, base, base2):
    parallelltrapets = round((0.5*(height*(base+base2))),2)
    return parallelltrapets


def circlesector_area(angle,radius):
    arc = round(((angle/360)*2*math.pi*radius),2)
    circlesector_area = round((0.5*(arc * radius)),2)
    return arc, circlesector_area
    



    
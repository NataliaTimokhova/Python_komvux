#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Natalia Timokhova

Uppgift 4. Del 2. Modulen flaggor

"""

'''
Modulen som innehåller funktioner vilka ritar svenska, danska och norska flaggor. 
Denna module i sin tur använder modulen turtle där vi kan ta funktioner forward, right
eller color t.ex. och rita den bild som vi behöver. 


Modulen ser lite lång ut för att alla flaggor har olika proportioner och man behöver ge
olika koordinater för att måla bilden. 


Jag skulle kunna förkorta programmet genom att ange koordinater separat, men för att jag 
räknade dem manuellt blir det krånglit för användaren att förstå siffror utifrån koden. 
Som det ser ut nu kan användaren förstå att rakt fram 160 sedan till höger 90 grader och neråt 100,
istället för (160,100) någonstans separat. 
'''


import turtle


def svenska_flaggan():
    turtle.clear()  # vi rensar allt innan vi ritar en ny flagga
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    
    # Draw the blue rectangle
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(160)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    
    
    # Draw the yellow cross
    turtle.color("yellow")
    
    # Vertical bar
    turtle.penup()
    turtle.goto(-50, 100)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()


    # Horizontal bar
    turtle.penup()
    turtle.goto(-100, 60)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(160)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()


def danska_flaggan():
    turtle.clear() 
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    
    # Draw the red rectangle
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(160)
        turtle.right(90)
        turtle.forward(121)
        turtle.right(90)
    turtle.end_fill()
    
    
    # Draw the white cross
    turtle.color("white")
    
    # Vertical bar
    turtle.penup()
    turtle.goto(-48, 100)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(17)
        turtle.right(90)
        turtle.forward(121)
        turtle.right(90)
    turtle.end_fill()


    # Horizontal bar
    turtle.penup()
    turtle.goto(-100, 48)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(160)
        turtle.right(90)
        turtle.forward(17)
        turtle.right(90)
    turtle.end_fill()



def norska_flaggan():
    turtle.clear() 
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    
    # Draw the red rectangle
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(160)
        turtle.right(90)
        turtle.forward(117)
        turtle.right(90)
    turtle.end_fill() 

    
    # Draw the WHITE cross
    turtle.color("white")
    
    # Vertical bar
    turtle.penup()
    turtle.goto(-56, 100)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(29)
        turtle.right(90)
        turtle.forward(117)
        turtle.right(90)
    turtle.end_fill()

    # Horizontal bar
    turtle.penup()
    turtle.goto(-100, 56)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(160)
        turtle.right(90)
        turtle.forward(29)
        turtle.right(90)
    turtle.end_fill()   
    
    
    # Draw the BLUE cross
    turtle.color("blue")
    
    # Vertical bar
    turtle.penup()
    turtle.goto(-49, 100)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(117)
        turtle.right(90)
    turtle.end_fill()

    # Horizontal bar
    turtle.penup()
    turtle.goto(-100, 49)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(160)
        turtle.right(90)
        turtle.forward(15)
        turtle.right(90)
    turtle.end_fill()
    
  
    
    
    
    
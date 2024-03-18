#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Natalia Timokhova

"""


'''
This module consists of two functions which 
read the text and write text in a file.
We include try-except code for catching some possible errors
'''


def read_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print("Innehållet i filen: ", file_name, "\n")
            print(content)
    except FileNotFoundError:
        print("Filen hittades inte.")
    # incorrect file name or location
    except IOError:
        print("Ett fel uppstod vid läsning av filen.")


def write_to_file(file_name, text):
    try:
        with open(file_name, "a") as file:
            file.write(text + "\n")
        print("Texten har sparats i filen: ", file_name, "\n")
    except IOError:
        print("Ett fel uppstod vid skrivning till filen.")
        
        
        
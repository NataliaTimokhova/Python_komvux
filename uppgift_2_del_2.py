#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Natalia Timokhova

"""

'''
This function uses module "text" for the writing a text from terminal to a file.
The name of the file is six first letters/signs of the given text.
The same time, the function is reading the context of the file that we just saved
or ends the loop if we leaves an empty row instead of the text. 
'''

from text import write_to_file, read_from_file

def uppgift2():
    
    print("Välkommen!")
    
    # filnamn ska stå före loop som en global variabel
    file_name = ""
    
    while True:
        text = input("\nSkriv en rad text (lämna tom för att avsluta):")
        if text == "":
            break
        
        #Vi sparar ett filnamn som 6 första tecken av den givna texten
        file_name = text[:6] + ".txt"  
        write_to_file(file_name, text)
        read_from_file(file_name)

    print("Tack för idag!")

# anropar programmet
uppgift2()




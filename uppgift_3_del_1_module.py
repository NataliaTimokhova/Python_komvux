#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Natalia Timokhova
Uppgift 3. Del 1. Modul

"""


'''
Modul som består av tre funktioner:
1. En funktion som beräknar moms
2. Den andra funktionen som skriver in resultat i en fil
3. Tredje funktionen visar innehållet ur filen i terminalen
Funktionerna kommer att anropas utifrån andra filer som funktioner ur modulen.
Funktionerna fångar upp möjliga fel vid input av data.
'''


def pris_med_moms():
    while True:
        try:
            pris_exkl_moms = float(input("Ange pris exklusive moms: "))
            moms_procent = float(input("Ange momssats i procent: "))
            break
        except ValueError:
            print("Felaktig inmatning. Ange numeriska värden för priset.")

    moms = pris_exkl_moms * (moms_procent / 100)
    pris_inkl_moms = pris_exkl_moms + moms
    return pris_exkl_moms, moms_procent, pris_inkl_moms


def write_to_file(file_name, text):
    try:
        with open(file_name, "a") as file:
            file.write(text + "\n")
        print("Texten har sparats i filen: ", file_name, "\n")
    except IOError:
        print("Ett fel uppstod vid skrivning till filen.")



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







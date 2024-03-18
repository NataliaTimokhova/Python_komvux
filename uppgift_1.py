#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Natalia Timokhova
Uppgift 1

"""


'''
Del 1.
En funktion som beräknar vad en vara  kostar inklusive moms. 
Som parametrar ska funktionen få dels priset exklusive moms och 
dels momssatsen uttrycket i procent. 
'''


def pris_med_moms():
    
    while True:                             # Felhantering som fångar icke-numeriska input
        try:
            pris_exkl_moms = float(input("Ange pris exklusive moms: "))
            moms = float(input("Ange momssats i procent: "))
            break
        except ValueError:
            print("Felaktig inmatning. Ange numeriska värden för priset.")
    

    moms = pris_exkl_moms * (moms / 100)
    pris_inkl_moms = pris_exkl_moms + moms
    return pris_inkl_moms                   # det som vi ska få när vi kör funktionen


# Kör Del 1 ============================================================

print("Pris inklusive moms:", pris_med_moms())
# ======================================================================



'''
Del 2
En funktion som undersöker hur många små respektive stora bokstäver som finns i en text. 
Resultaten ska ges i en tupel. 
'''


def count_letters(input_text=None, file_path=None): # för att kunna välja en fil eller skriva en text
    number_small_letters = 0
    number_capital_letters = 0
    
    if file_path is not None:               # Väljer en fil i direktoriet
        with open(file_path, 'r') as file:
            text = file.read()
    elif input_text is not None:            # anger egen text när kör funktionen
        text = input_text
    else:
        raise ValueError("Ange antingen parametern 'input_text' eller 'file_path'")


    for letter in text:
        if letter.islower():
            number_small_letters += 1
        elif letter.isupper():
            number_capital_letters += 1

    resultat = (number_small_letters, number_capital_letters)
    return resultat


# Kör Del 2 ============================================================

input_text="En funktion som undersöker hur många SMÅ respektive stora bokstäver som finns i en text."
print("Små bokstäver", count_letters(input_text)[0], "Stora bokstäver", count_letters(input_text)[1])

#file_path = "/Users/Documents/Python/Filen.txt"    # koden för den fil som ska öppnas, ange en pass till direktoriet
#print("Små bokstäver", count_letters(file_path)[0], "Stora bokstäver", count_letters(file_path)[1])

# ======================================================================



'''
Del 3
Ett palindrom är ett ord eller en mening som blir samma sak baklänges. 
Ex: anna, sallad i dallas, ola salo.
Du har tillgång till en funktion som heter som returnerar mening i omvänd ordning. 
Du ska skriva  en funktion som tar emot en mening och 
returnerar True om meningen är ett palindrom, eller False annars.
'''

def palindrom(text):
    letters = [letter.lower() for letter in text if letter.isalpha()] # tar endsat bokstäver
    reverse_order = list(reversed(letters))

    if letters == reverse_order:
        return True
    else:
        return False


# Kör Del 3 ============================================================

print(palindrom("anna"))
print(palindrom("sallad i dallas"))
print(palindrom("ola salo"))
print(palindrom("Python program"))

# ======================================================================


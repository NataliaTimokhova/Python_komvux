#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Natalia Timokhova
Uppgift 3. Del 1
"""


'''
moms_output() är en funktion som beräknar vad en vara  kostar inklusive moms,
skapar en fil output.txt, där skriver in resultatet: 
given pris exkl.moms, given moms i procent och pris inkl.moms. 
Funktionen visar också innehållet av filen i terminalen.
'''

from uppgift_3_del_1_module import pris_med_moms, write_to_file, read_from_file


def moms_output():
    while True:
        # i yttre while-loopen programmet kommer att använda tre funktioner utifrån modulen "uppgift_3_del_1_module"
        # en funktion
        pris_exkl_moms, moms_procent, pris_inkl_moms = pris_med_moms()   
        file_name = "output.txt"
        
        # andra funktion
        write_to_file(file_name, f"Pris exk. moms: {pris_exkl_moms:.2f}, Moms: {moms_procent:.2f} %, Pris inkl. moms: {pris_inkl_moms:.2f}")
        print("Du kan se filens innehåll nedan")
        
        # tredje funktion
        read_from_file(file_name) 
        

        
        while True:
            choice = input("\nVill du fortsätta? (ja/nej): ")
            if choice.lower() == "ja":
                break      
                #bryter bara ut ur den inre while-loopen, inte den yttre while-loopen
                # Detta gör att programmet kan gå tillbaka till början av den yttre loopen och be om mer input.
            
            elif choice.lower() == "nej":
                print("Tack för idag!")
                return
                # avslutar moms_output()-funktionen och avslutar följaktligen programmet
                # när return används utanför en funktion, avslutas hela programmet
                
            else:
                print("\nDu svarade varken ja eller nej, försök igen.")
                # Eftersom detta "else" är den sista delen av loopen, 
                # kommer det automatiskt att fortsätta till nästa iteration utan behov av "continue"

moms_output()



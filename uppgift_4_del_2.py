#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Natalia Timokhova
"""

'''
Programmet ska fråga om vilken flagga som man vill rita om valet är svenska flaggan
då passar man parametrar till funktionen för att rita svenska flaggan. 
'''

import uppgift_4_del_2_module as flaggor


# Huvudprogram
def rita_flaggan():
    while True:
        try:
            land = input("\nVilken flagga vill du rita?\n(svensk, dansk, norsk): ").lower()

            if land == "svensk":
                flaggor.svenska_flaggan()
            elif land == "dansk":
                flaggor.danska_flaggan()
            elif land == "norsk":
                flaggor.norska_flaggan()
            else:
                print("Ogiltigt val")
        
            svar = input("Vill du fortsätta? (ja/nej): ").lower()
            if svar != "ja":
                print("Tack för idag!")
                break
        except KeyboardInterrupt:
            print("\nAvslutar programmet...")
            break
        except:
            print("\nEtt fel uppstod. Försök igen.")

rita_flaggan()


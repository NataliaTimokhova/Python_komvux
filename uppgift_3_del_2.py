#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Natalia Timokhova
Uppgift 3. Del 2
"""

'''
Funktionen som anropar modulen "uppgift_3_del_2_module"
'''

from uppgift_3_del_2_module import find_primes, handle_list, write_to_csv, read_from_csv_and_plot


def main():
    try:
        primes_list = find_primes()
        handle_list(primes_list)

        csv_file = "primes.csv"
        write_to_csv(csv_file, primes_list)

        read_from_csv_and_plot(csv_file)
    except KeyboardInterrupt:
        print("Programmet avslutades av användaren.")
        
        # Jag lägger till detta block, men snarare som ett exempel på ett möjligt fel, 
        # eftersom programmet körs automatiskt utan inmatning och 
        # det finns ingen tid för avbrott av användaren.
        
    except Exception as e:
        print("Ett oväntat fel inträffade:", e)

if __name__ == "__main__":
    main()
    

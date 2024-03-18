#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Natalia Timokhova
Uppgift 3. Del 2

"""

'''
Modul som består av fyra funktioner:
1.En funktion som räkna primtal från 2–200
2.Data ska skicka till en lista. Så skapa funktion som hantera listan.
3.En funktion som lagra data från listan i en CSV fil.
4.En funktion som läsa data från CSV fil och skapa diagram
'''

        
import pandas as pd
import matplotlib.pyplot as plt

# pandas för att hantera csv-filer, matplotlib för att skapa diagram


def find_primes():
    primes = []
    for num in range(2, 201):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def handle_list(data_list):
    print("Listan av primtal:")
    for num in data_list:
        print(num)

def write_to_csv(file_name, data_list):
    try:
        df = pd.DataFrame(data_list, columns=["Primes"])
        df.to_csv(file_name, index=False)
        print("Data har sparats i CSV-filen:", file_name)
    except IOError:
        print("Ett fel uppstod vid skrivning till filen.")

def read_from_csv_and_plot(file_name):
    try:
        df = pd.read_csv(file_name)
        plt.plot(df["Primes"])
        plt.xlabel("Index")
        plt.ylabel("Primtal")
        plt.title("Primtal från CSV-fil")
        plt.show()
        print("Se diagrammet i terminalen")
    except FileNotFoundError:
        print("Filen hittades inte.")
    except IOError:
        print("Ett fel uppstod vid läsning av filen.")


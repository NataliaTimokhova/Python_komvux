#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
***************************************************************************************** 
*****************************************************************************************

Projekt i Programmering 2, uppgift 5

Teoretiska frågor inskrivna som kommentar i koden för att kombinera det med ett exempel. 

*****************************************************************************************
***************************************************************************************** 
"""

import csv       # för att hantera filer av csv-format 
import random    # för att skapa ett nummer för ett bakkonto


"""
-----------------------------------------------------------------------------------------
Klasser innehåller de egenskaper som ett objekt ska ha, 
och metoder som beskriver vad objektet ska kunna göra. 


Basklassen är den grundläggande klassen som innehåller generell funktionalitet, 
medan den driven klassen ärver från basklassen och anpassar funktionaliteten.
-----------------------------------------------------------------------------------------
"""


# Basklass
class Person:
    def __init__(self, name, personnummer, address):
        self.name = name
        self.personnummer = personnummer
        self.address = address

    def information(self):
        print(f"Namn: {self.name}, Personnummer: {self.personnummer}, Adress: {self.address}")

"""
-----------------------------------------------------------------------------------------
Ett objekt innehåller information om tillstånd (namn, personnummer, adress). 
Om vi skapar ett objekt "person" i klass-Person ska detta objekt inkludera ovannämnda tillstånd

Sub klass, Ärv från Person-klass
Sub klass är en klass som ärver attribut och metoder från en basklass
Här nedan vi ser att Kund(Person) uppvisar att Kund är en sub klass till basklassen Person 
-----------------------------------------------------------------------------------------
"""

class Kund(Person):
    
    """
    -----------------------------------------------------------------------------------------
    Klassens konstruktor är en metod som returnerar en instans av klassen
    vanligtvis för att initialisera attribut i objektet med hjälp av __init__(self, name, osv.)
    -----------------------------------------------------------------------------------------
    """
    
    def __init__(self, name, personnummer, address, kundnummer):
        # super() ärver alla metoder från Person klass. Resten är kundnummer
        super().__init__(name, personnummer, address)
        self.kundnummer = kundnummer

    def information(self):
        super().information()
        print(f"Kundnummer: {self.kundnummer}")

"""
-----------------------------------------------------------------------------------------
Polymorfism tillåter olika klasser att ha metoder med samma namn, 
men de kan bete sig olika beroende på klassen som anropar dem.
I vårt fall är det def information(self), som har olika output i basklassen och sub klassen
-----------------------------------------------------------------------------------------
"""


# Sub-klass, Ärv från Kund-klass

class Bankkonto(Kund):
    def __init__(self, name, personnummer, address, kundnummer):
        # super() ärver alla metoder från Kund klass. Resten är kontonummer och saldo
        super().__init__(name, personnummer, address, kundnummer)
        self.kontonummer = self.generera_kontonummer()
        self.saldo = 0  # Saldo är 0 när ett konto skapas


    def generera_kontonummer(self):
        # enligt uppgiften ett random nummer "t.ex. 9855- 0934218"
        return f"{random.randint(0000, 9999)}-{random.randint(0000000, 9999999)}"

    def visa_saldo(self):
        print(f"Kontonummer: {self.kontonummer}, Saldo: {self.saldo}")

    def insattning(self, belopp):
        self.saldo += belopp

    def uttag(self, belopp):
        if belopp <= self.saldo:
            self.saldo -= belopp
        else:
            print("Otillräckligt saldo för uttag.")


# Funktioner, Sparande och läsning från CSV-fil

def spara_kunddata_till_csv(kunddata):
    with open('kunder.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Namn", "Personnummer", "Adress", "Kundnummer", "Kontonummer", "Saldo"])
        for kund in kunddata:
            if isinstance(kund, Bankkonto):
                writer.writerow([kund.name, kund.personnummer, kund.address, kund.kundnummer, kund.kontonummer, kund.saldo])
            else:
                writer.writerow([kund.name, kund.personnummer, kund.address, kund.kundnummer, "", ""])
                

def las_kunddata_från_csv():
    kunddata = []
    try:
        with open('kunder.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if "Kontonummer" in row and "Saldo" in row:
                    kund = Bankkonto(row["Namn"], row["Personnummer"], row["Adress"], row["Kundnummer"])
                    kund.kontonummer = row["Kontonummer"]
                    saldo_str = row["Saldo"]
                    if saldo_str:
                        kund.saldo = float(saldo_str)
                    else:
                        kund.saldo = 0.0
                else:
                    kund = Kund(row["Namn"], row["Personnummer"], row["Adress"], row["Kundnummer"])
                kunddata.append(kund)
    except FileNotFoundError:
        pass
    return kunddata


"""
-----------------------------------------------------------------------------------------
OBS! 
VI görde try-except koden i ovanstående funktionen, men använde det inte i huvudprogrammet
Detta gjordes 
 1) för att förkorta huvudprogrammet, 
 2) om något inte stämmer med kundinformation anropas programmet om och kör vidare
-----------------------------------------------------------------------------------------
"""



"""
-----------------------------------------------------------------------------------------
HUVUDPROGRAM
-----------------------------------------------------------------------------------------

 där vi använder funktioner och klasser som skapades ovanpå
 Vi kunde skriva huvudprogrammet i en separad fil och använda kod med klasser som en module
 Men vi väljer att skriva allt i en fil. 
-----------------------------------------------------------------------------------------
"""


def main():
    kunddata = las_kunddata_från_csv()
    #  kontrollera att filen med kod och filen med kunder ligger i samma mapp

    while True:
        print("\nVälkommen till banken!")
        print("1. Skapa en ny kund")
        print("2. Ändra kundinformation")
        print("3. Ändra konto")
        print("4. Avsluta")

        val = input("Välj en handling (1/2/3/4): ")

        if val == "1":
            name = input("Ange kundens namn: ")
            personnummer = input("Ange personnummer: ")
            address = input("Ange adress: ")
            kundnummer = input("Ange kundnummer: ")
            konto = Bankkonto(name, personnummer, address, kundnummer)
            kunddata.append(konto)
            spara_kunddata_till_csv(kunddata)
            print("Kunden har skapats.")

        elif val == "2":
            
            # Denna meny blev lite för lång för att programmet frågar efter typ av ändringar
            # Men om vi vill ändra allt på en gång vore programmet mycket kortare
            
            personnummer = input("Ange kundens personnummer: ")
            
            # programmet tar första kund i filen som har detta personnumer i fall 
            # om flera råkade ha samma nummer
            # för att en detaljerad datakontroll inte var målet av programmet
            
            found = False
            for kund in kunddata:
                if kund.personnummer == personnummer:
                    print(f"Kundinformation för {kund.name}:")
                    print("1. Ändra namn")
                    print("2. Ändra personnummer")
                    print("3. Ändra adress")
                    print("4. Tillbaka till huvudmenyn")
                    val_kundinfo = input("Välj en handling (1/2/3/4): ")

                    if val_kundinfo == "1":
                        nytt_namn = input("Ange nytt namn: ")
                        kund.name = nytt_namn
                        print("Namnet har ändrats.")

                    elif val_kundinfo == "2":
                        nytt_personnummer = input("Ange nytt personnummer: ")
                        kund.personnummer = nytt_personnummer
                        print("Personnumret har ändrats.")

                    elif val_kundinfo == "3":
                        ny_adress = input("Ange ny adress: ")
                        kund.address = ny_adress
                        print("Adressen har ändrats.")

                    elif val_kundinfo == "4":
                        break

                    else:
                        print("Ogiltigt val. Försök igen.")

                    found = True
                    break

            if not found:
                print("Kund med detta personnummer hittades inte.")

        elif val == "3":
            # Vi kunde göra val 3 inne av val 2 för att kontot hör till kunden
            # Men då hadae valet 2 blivit ännu längre i koden, så vi separerar kund och konto
            
            personnummer = input("Ange kundens personnummer: ")
            found = False
            for kund in kunddata:
                if kund.personnummer == personnummer:
                    if isinstance(kund, Bankkonto):
                        while True:
                            print("\nVad vill du göra med kontot?")
                            print("1. Insättning")
                            print("2. Uttag")
                            print("3. Visa saldo")
                            print("4. Tillbaka till huvudmenyn")
                            val_konto = input("Välj en handling (1/2/3/4): ")

                            if val_konto == "1":
                                belopp = float(input("Ange belopp att sätta in: "))
                                kund.insattning(belopp)
                                print("Insättning genomförd.")

                            elif val_konto == "2":
                                belopp = float(input("Ange belopp att ta ut: "))
                                kund.uttag(belopp)
                                print("Uttag genomfört.")

                            elif val_konto == "3":
                                kund.visa_saldo()

                            elif val_konto == "4":
                                break

                            else:
                                print("Ogiltigt val. Försök igen.")

                        found = True
                        break

            if not found:
                print("Kund med detta personnummer hittades inte.")

        elif val == "4":
            spara_kunddata_till_csv(kunddata)
            break

        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
# Greatest Common Divisor: Eukliduv algoritmus (odcitani)

cislo1 = int(input("Zadejte prvni cislo: "))
cislo2 = int(input("Zadejte druhe cislo: "))

while cislo1 != cislo2:
    if cislo1 > cislo2:
        cislo1 -= cislo2
    else:
        cislo2 -= cislo1
print("Nejvetsi spolecny delitel je ", cislo1)

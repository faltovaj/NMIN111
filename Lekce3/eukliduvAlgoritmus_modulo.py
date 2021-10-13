#!/usr/bin/env python3
# Greatest Common Divisor: Eukliduv algoritmus (modulo)

cislo1 = int(input("Zadejte prvni cislo: "))
cislo2 = int(input("Zadejte druhe cislo: "))

while cislo1 > 0 and cislo2 > 0:
    if cislo1 > cislo2:
        cislo1 %= cislo2
    else:
        cislo2 %= cislo1

if cislo1 > 0:
    print("Nejvetsi spolecny delitel je ", cislo1)
else:
    print("Nejvetsi spolecny delitel je ", cislo2)

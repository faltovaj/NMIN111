#!/usr/bin/env python3
# Nacita prirozena cisla ze vstupu zakoncena -1, vypise jejich soucet

soucet = 0
while True:
    cislo = int(input("Zadejte cislo: "))
    if cislo==-1:
        break
    soucet += cislo
print("Soucet zadanych cisel je: ", soucet)

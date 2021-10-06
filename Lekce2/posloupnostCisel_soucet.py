#!/usr/bin/env python3
# Nacita prirozena cisla ze vstupu zakoncena -1, vypise jejich soucet

cislo = int(input("Zadejte cislo: "))

soucet = 0
while cislo!=-1:
    soucet += cislo
    cislo = int(input("Zadejte cislo: "))

print("Soucet zadanych cisel je: ", soucet)

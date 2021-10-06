#!/usr/bin/env python3
# Nacita prirozena cisla ze vstupu zakoncena -1
# Vypise prvni a druhe nejvetsi cislo

max1 = 0    # Prvni nejvetsi cislo, puvodni hodnota 0
max2 = 0    # Druhe nejvetsi cislo, puvodni hodnota 0    
while True:
    cislo = int(input("Zadejte cislo: "))
    if cislo == -1:
        break;
    if cislo >= max1:
        max2, max1 = max1, cislo
    elif cislo >= max2:
        max2 = cislo

print("Nejvetsi cislo je: ", max1)
print("Druhe nejvetsi cislo je: ", max2)



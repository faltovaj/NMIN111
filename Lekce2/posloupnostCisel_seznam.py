#!/usr/bin/env python3
# Nacita prirozena cisla ze vstupu zakoncena -1
# Zapise cisla do seznamu a vypise jejich soucet + 2. maximum

# Nacte cisla a ulozi do seznamu
seznamCisel = []
while True:
    cislo = int(input("Zadejte cislo: "))
    if cislo == -1:
        break;
    seznamCisel.append(cislo)
print("Zadali jste tato cisla: ", seznamCisel)

# Secte zadana cisla
soucet = 0
for n in seznamCisel:
    soucet += n
print("Soucet zadanych cisel je: ", soucet)

# Cisla setridi (defaultni trideni je od nejmensiho po nejvetsi)
seznamCisel.sort()
print("Cisla po trideni: ", seznamCisel)
print("Nejvetsi cislo je: ", seznamCisel[-1])
print("Druhe nejvetsi cislo je: ", seznamCisel[-2])

# Cisla setridime sestupne
seznamCisel.sort(reverse=True)
print("Cisla po reverznim trideni: ", seznamCisel)
print("Nejvetsi cislo je: ", seznamCisel[0])
print("Druhe nejvetsi cislo je: ", seznamCisel[1])

#!/usr/bin/env python3
# Vypise vsechna prvocisla do zadaneho cisla

cislo = int(input("Zadejte do jakeho cisla chcete vypisovat prvocisla: "))

kandidatNaPrvocislo = 2

while kandidatNaPrvocislo<=cislo:
   delitel = 2
   while delitel*delitel<=kandidatNaPrvocislo:
      if kandidatNaPrvocislo%delitel == 0:
         break
      delitel += 1
   else:
      print("Cislo", kandidatNaPrvocislo, "je prvocislo.")
      
   kandidatNaPrvocislo += 1

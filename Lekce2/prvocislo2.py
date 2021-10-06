#!/usr/bin/env python3
# Zjisti, zda je zadane cislo prvocislem
# 259309

cislo = int(input("Zadejte cislo: "))

delitel = 2

while delitel*delitel<=cislo:
	if cislo%delitel == 0:
		print("Cislo", cislo, "neni prvocislo, je delitelne", delitel,".")
		break
	delitel += 1
else:
        print("Cislo", cislo, "je prvocislo.")

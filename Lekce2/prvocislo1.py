#!/usr/bin/env python3
# Zjisti, zda je zadane cislo prvocislem
# 259309

cislo = int(input("Zadejte cislo: "))

delitel = 2
mamDelitele = False

while delitel<cislo:
	if cislo%delitel == 0:
		print("Cislo", cislo, "neni prvocislo, je delitelne", delitel,".")
		mamDelitele = True
		break
	delitel += 1

if not mamDelitele:
	print("Cislo", cislo, "je prvocislo.")

#!/usr/bin/env python3
# Eratosthenovo sito: algoritmus na vypsani prvocisel mensich nez N

N = int(input("Zadejte do jakeho cisla chcete vypsat prvocisla: "))
sito = [True] * (N+1)

for i in range(2,N+1):
    if sito[i]:
#       print(i)
        for j in range(2*i, (N+1), i):
            sito[j] = False

for i in range(2, len(sito)):
    if sito[i]:
        print(i)

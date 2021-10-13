#!/usr/bin/env python3
# Program vrati prvnich N Fibonacciho cisel

N = int(input("Kolik Fibonacciho cisel chcete vypsat: "))
fibCisla = [0,1]

for i in range(N-2):
    fibCisla.append(fibCisla[-1]+fibCisla[-2])
     
print(fibCisla)

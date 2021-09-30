# Hello world a jeho lehka modifikace
# Vstup: 1/ Veta, 2/ vypis ano/ne 

print("Hello world!")

sentence = input("Zadejte vetu: ")
printout = input("Chcete vetu vypsat (ano, ne)?: ")

if printout=="ano":
    print(sentence)
else:
    print("Nic jste nechteli vypsat")

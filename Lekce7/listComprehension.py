# Tabulka nasobilky
def nasobilka(n):
    return[[a*b for a in range(1, n+1)] for b in range(1, n+1)]

# Prunik dvou seznamu (predpokladam, ze se prvky v seznamech neopakuji)
def prunik(seznam1, seznam2):
    return[a for a in seznam1 if a in seznam2]

# Palindromicka slova (ctou se stejne popredu i pozadu)
def palindromickaSlova(veta):
    return [slovo for slovo in veta.split() if slovo == slovo[::-1]]

# Setrideni slov na radku podle jejich delky
def trideniSlov(radek):
    serazeneDvojice = sorted([(len(slovo), slovo) for slovo in radek.split()])
    return [prvek[1] for prvek in serazeneDvojice]

# Skalarni soucin dvou vektoru
def skalarniSoucin(vektor1, vektor2):
    if len(vektor1) != len(vektor2):
        print("Vektory nemaji stejnou delku!")
        return
    return sum([i*j for i, j in zip(vektor1, vektor2)])

# Transpozice matic
def transpozice(matice):
    return [[rada[i] for rada in matice] for i in range(len(matice[0]))]   

# Nasobeni matic
def nasobeniMatic(maticeA, maticeB):
    maticeB_T = transpozice(maticeB)
    return [[skalarniSoucin(radekA, radekB_T) for radekB_T in maticeB_T] for radekA in maticeA]

'''''
Testy reseni
'''''
print('Nasobilka')
[print(radek) for radek in nasobilka(10)]

seznam1 = [20, 10, 5, 6, 80]
seznam2 = [20, 6, 8, 38, 68, 5, 10, 560]
print(f'Prunik dvou seznamu: {prunik(seznam1, seznam2)}')

print(f'Palindromicka slova: {palindromickaSlova("anna ono male mlade")}')

print(f'Skalarni soucin: {skalarniSoucin([1,2,3], [10, 20, 30])}')

print(f'Trideni slov podle velikosti: {trideniSlov("anna ono male mlade")}')

matice1 = [[1,2,3],[4,5,6]]
matice2 = [[1,2],[3,4],[5,6]]
print(f'Nasobeni matic: {nasobeniMatic(matice1, matice2)}')

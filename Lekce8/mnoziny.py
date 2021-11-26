#!/usr/bin/env python3
# Porovnavani prvku seznamu

# fce vrati True nebo False podle toho, zda jsou dane dva seznamy stejne az na poradi prvku. Prvky se mohou opakovat
def porovnaniDvouSeznamu(seznam1, seznam2):
	# Seznam seradime, abychom mohli porovnat seznamy s prehazenymi prvky
	return sorted(seznam1)==sorted(seznam2)
	# Pokud by se prvky neopakovali, pak muzeme udelat toto:
	# return set(seznam1)==set(seznam2)

# fce vrati True nebo False podle toho, zda jsou vsechny prvky seznamu navzajem ruzne
def ruznePrvky(seznam):
	return(len(seznam)==len(set(seznam)))

seznam1 = [1, 2, 6, 10, 12, 18, 12]
seznam2 = [2, 1, 10, 12, 18, 6]
print(f"Prvni seznam: {seznam1}")
print(f"Druhy seznam: {seznam2}")
print(f"Maji stejne prvky? {porovnaniDvouSeznamu(seznam1, seznam2)}")

print(f"Ma druhy seznam navzajem ruzne prvky? {ruznePrvky(seznam2)}")
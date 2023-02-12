# SUJET 7

# Exo 1 :
def fusion(tab1,tab2):
    for number in tab2:
        tab1.append(number)
    tab1.sort()
    return tab1
    
# Appels de vérification :
print(fusion([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))

# Exo 2 :
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    """ Renvoie l'ecriture decimale du nombre donné en chiffres romains """

    if len(nombre) == 1:
        return romains[nombre]

    elif romains[nombre[0]] >=  romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]

# Appels de vérification :
print(traduire_romain("XIV"))
print(traduire_romain("CXLII"))
print(traduire_romain("MMXXIII"))
# SUJET 27

# Exo 1 :
def recherche_min(tab):
    min_val = [tab[0],0]
    for i in range(len(tab)):
        if tab[i] < min_val[0] :
            min_val = [tab[i],i]
    return min_val[1]

# Appels de vérification :
print(recherche_min([5]))
print(recherche_min([2, 4, 1]))
print(recherche_min([5, 3, 2, 2, 4]))

# Exo 2 :
def separe(tab):
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche = gauche + 1
        else :
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite = droite - 1
    return tab

# Appels de vérification :
print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
print(separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]))
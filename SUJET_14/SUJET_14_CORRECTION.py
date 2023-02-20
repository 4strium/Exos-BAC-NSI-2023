# SUJET 14

# Exo 1 :
def recherche(elt,tab):
    for i in range(len(tab)) :
        if tab[i] == elt :
            return i
    return -1           # Pas la peine de mettre de "else"

# Appels de vérification :
print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))

# Exo 2 :
def insere(a, tab):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l)-2
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l

# Appels de vérification :
print(insere(3, [1, 2, 4, 5]))
print(insere(30, [1, 2, 7, 12, 14, 25]))
print(insere(1, [2, 3, 4]))
print(insere(1, []))
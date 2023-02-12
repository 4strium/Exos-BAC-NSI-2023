# SUJET 2

# Exo 1 :
def indices_maxi(tab):
    indices_list = []
    res = []
    val_max = tab[0]
    for num in tab :
        if num > val_max :
            val_max = num
    res.append(val_max)
    for i in range(len(tab)):
        if tab[i] == val_max :
            indices_list.append(i)
    res.append(indices_list)
    return res

# Appels de vérification :
print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))

# Exo 2 :
def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

# Appels de vérification :
print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print(positif([-2]))
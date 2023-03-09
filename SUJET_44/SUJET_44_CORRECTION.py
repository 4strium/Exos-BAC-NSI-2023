# SUJET 44

# Exo 1 :
def renverse(mot):
    inverted = ''
    for char in mot :
        inverted = char + inverted 
    return inverted

# Appel de vérification :
print(renverse("informatique"))

# Exo 2 :
def crible(n):
    """
    Renvoie un tableau contenant tous les nombres premiers plus petits que N
    """
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(2, n):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2*i, n, i):
                tab[multiple] = False
    return premiers

# Appel de vérification :
assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
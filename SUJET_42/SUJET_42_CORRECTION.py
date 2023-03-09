# SUJET 42

# Exo 1 :
def tri_selection(tab):
    for j in range(len(tab)) :
        min_x = j
        for i in range(j,len(tab)) :
            if tab[i] < tab[min_x] :
                min_x = i
        tab[j], tab[min_x] = tab[min_x], tab[j]
    return tab

# Appels de vérification :
print(tri_selection([1, 52, 6, -9, 12]))

# Exo 2 :
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1,99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ",nb_mystere)
        print("Nombre d'essais: ",compteur)
    else:
        print ("Perdu ! Le nombre était ",nb_mystere)

# Appel de vérification :
plus_ou_moins()
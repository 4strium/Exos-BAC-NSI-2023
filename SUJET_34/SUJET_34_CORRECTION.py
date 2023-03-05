# SUJET 34

# Exo 1 :
def moyenne(tab):
    sum = 0
    for element in tab :
        sum += element
    if len(tab) != 0 :
        return sum/len(tab)
    else :
        # Proposer une façon de traiter le cas où le tableau passé en paramètre est vide.
        return 'Votre tableau est vide !'

# Appels de vérification :
print(moyenne([5,3,8]))
print(moyenne([1,2,3,4,5,6,7,8,9,10]))
print(moyenne([]))

# Exo 2 :
def tri(tab):
    # i est le premier indice de la zone non triée,
    # j est le dernier indice de cette zone non triée.
    # Au début, la zone non triée est le tableau complet.
    i = 0
    j = len(tab) - 1
    while i != j:
        if tab[i]== 0:
            i = i + 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1
    return tab

# Appels de vérification :
print(tri([0,1,0,1,0,1,0,1,0]))
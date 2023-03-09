# SUJET 41

# Exo 1 :
def recherche(caractere, chaine):
    occur = 0
    for char in chaine :
        if char == caractere :
            occur += 1
    return occur

# Appels de vérification :
print(recherche('e', "sciences"))
print(recherche('i',"mississippi"))
print(recherche('a',"mississippi"))

# Exo 2 :
valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre :
        return [v] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang + 1)

# Appels de vérification :
print(rendu_glouton(67, 0))
print(rendu_glouton(291, 0))
print(rendu_glouton(291,1)) # si on ne dispose pas de billets de 100
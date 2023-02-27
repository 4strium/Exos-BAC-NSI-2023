# SUJET 20

# Exo 1 :
def ajoute_dictionnaires(d1,d2):
    d = {}
    d1_keys = list(d1.keys())
    d2_keys = list(d2.keys())
    for i in d1_keys :
        if i in d2_keys :
            sum1 = d1[i] + d2[i]
            d[i] = sum1
        else :
           d[i] = d1[i]
    for j in d2_keys :
        if j in d1_keys :
            sum2 = d1[j] + d2[j]
            d[j] = sum2
        else :
           d[j] = d2[j]
    return d

# Appels de vérification :
print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))

# Exo 2 :
from random import randint

def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nbre_cases
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n = n + 1
        print(sorted(cases_vues))   # Possibilité de savoir toutes les cases déjà vues !
    return n

# Appels de vérification :
print(nbre_coups())
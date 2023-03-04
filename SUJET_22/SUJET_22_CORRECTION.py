# SUJET 22

# Exo 1 :
def liste_puissances(a,n):
    tab_pow = [a]
    for i in range(1,n):
        tab_pow.append(tab_pow[-1]*a)
    return tab_pow

def liste_puissances_borne(a,borne):
    result_list = []
    value = a
    while value < borne :
        result_list.append(value)
        value = value*a
    return result_list

# Appels de vérification :
print(liste_puissances(3, 5))
print(liste_puissances(-2, 4))
print(liste_puissances_borne(2, 16))
print(liste_puissances_borne(2, 17))
print(liste_puissances_borne(5, 5))

# Exo 2 :
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}


def est_parfait(mot):
    # mot est une chaîne de caractères (en lettres majuscules)
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    if code_concatene // code_additionne == 0 :
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

# Appels de vérification :
print(est_parfait("PAUL"))
print(est_parfait("ALAIN"))
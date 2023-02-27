# SUJET 19

# Exo 1:
def recherche(tab,n):
    i = 1
    j = 0
    while i > 0 :
        i = (len(tab)-1)//2
        if tab[i] > n :
            tab = tab[:i]
            j += i
        elif tab[i] < n :
            tab = tab[i:]
            j += i
        elif tab[i] == n :
            return i+j
    return -1

# Appels de vérification :
print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))
print(recherche([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 30, 32, 46, 49, 70], 46))

# Exo 2:
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat

# Appels de vérification :
print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))
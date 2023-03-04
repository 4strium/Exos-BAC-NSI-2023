# SUJET 29

# Exo 1 :
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def taille(a):
    if a is None:
        return 0
    else :
        return 1 + taille(a.fg) + taille(a.fd)
    
def hauteur(a):
    if a is None:
        return 0
    else:
        return 1 + max(hauteur(a.fg), hauteur(a.fd))
    
# Appels de vérification :
a = Arbre(0)
a.fg = Arbre(1)
a.fd = Arbre(2)
a.fg.fg = Arbre(3)
a.fd.fg = Arbre(4)
a.fd.fd = Arbre(5)
a.fd.fg.fd = Arbre(6)

print(taille(a))
print(hauteur(a))

# Exo 2 :
def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < nbre_elts:
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i-1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[nbre_elts] = element
    return L

print(ajoute(1, 4, [7, 8, 9]))
print(ajoute(3, 4, [7, 8, 9]))
print(ajoute(4, 4, [7, 8, 9]))
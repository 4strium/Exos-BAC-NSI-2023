# SUJET 25

# Exo 1 :
def enumere(L):
    d = {}
    for i in range(len(L)):
        if L[i] not in d :
            d[L[i]] = [i]
        else :
            d[L[i]].append(i)
    return d

# Appels de vérification :
print(enumere([1, 1, 2, 3, 2, 1]))

# Exo 2 :
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere(arbre, cle):
    """ 
        arbre est une instance de la classe Arbre qui implémente
        un arbre binaire de recherche.
    """
    if cle < arbre.v:
        if arbre.fg is not None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd is not None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

# Appels de vérification :
node_root = Arbre(5)
insere(node_root,2)
insere(node_root,7)
insere(node_root,3)
print(parcours(node_root, []))

insere(node_root,1)
insere(node_root,4)
insere(node_root,6)
insere(node_root,8)
print(parcours(node_root, []))
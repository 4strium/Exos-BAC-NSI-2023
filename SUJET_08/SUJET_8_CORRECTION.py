# SUJET 8 

# Exo 1 :
def max_dico(dico):
    max_val = list(dico.values())[0]
    max_nom = list(dico.keys())[0]
    for element in dico:
        if dico[element] > max_val :
            max_val = dico[element]
            max_nom = element   
    return (max_nom, max_val)

# Appels de vérification :
print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))

# Exo 2 :
class Pile:
    """
    Classe definissant une structure de pile.
    """
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """
        Renvoie le booleen True si la pile est vide, False sinon.
        """
        return self.contenu == []

    def empiler(self, v):
        """
        Place l'element v au sommet de la pile
        """
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'element place au sommet de la pile,
        si la pile n'est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return resultat

# Appels de vérification :
print(eval_expression([2, 3, '+', 5, '*']))
print(eval_expression([742, 56, '+', 2, '*']))
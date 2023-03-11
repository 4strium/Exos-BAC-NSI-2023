# SUJET 40

# Exo 1 :
def nombre_de_mots(phrase):
    mot = 0
    for char in phrase :
        if char == ' ' or char == '.':
            mot += 1
    return mot

# Appels de vérification :
print("\n ---- Exo 1 ---- ")
print(nombre_de_mots('Cet exercice est simple.'))
print(nombre_de_mots('Le point d exclamation est separe !'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.'))

# Exo 2 :
class Noeud:
    def __init__(self, valeur):
        '''Méthode constructeur pour la classe Noeud.
        Paramètre d'entrée : valeur (str)'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def getValeur(self):
        '''Méthode accesseur pour obtenir la valeur du noeud
        Aucun paramètre en entrée'''
        return self.valeur

    def droitExiste(self):
        '''Méthode renvoyant True si l'enfant droit existe
        Aucun paramètre en entrée'''
        return (self.droit is not None)

    def gaucheExiste(self):
        '''Méthode renvoyant True si l'enfant gauche existe
        Aucun paramètre en entrée'''
        return (self.gauche is not None)

    def inserer(self, cle):
        '''Méthode d'insertion de clé dans un arbre binaire de recherche
        Paramètre d'entrée : cle (int)'''
        if cle < self.getValeur() :
            # on insère à gauche
            if self.gaucheExiste():
                # on descend à gauche et on retente l'insertion de la clé
                self.gauche.inserer(cle)
            else:
                # on crée un fils gauche
                self.gauche = Noeud(cle)
        elif cle > self.getValeur() :
            # on insère à droite
            if self.droitExiste() :
                # on descend à droite et on retente l'insertion de la clé
                self.droit.inserer(cle)
            else:
                # on crée un fils droit
                self.droit = Noeud(cle)

# Appels de vérification :
print("\n ---- Exo 2 ---- ")
arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
print(arbre.gauche.getValeur())
print(arbre.droit.getValeur())
print(arbre.gauche.gauche.getValeur())
print(arbre.gauche.droit.getValeur())
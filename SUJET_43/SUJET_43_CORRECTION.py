# SUJET 43 

# Exo 1 :
def ecriture_binaire_entier_positif(n):
    assert n >= 0 # positif seulement
    bin = []
    if n == 0:
        return [0]
    while n != 0 :
        bin.append(n%2)
        n = n//2
    bin.reverse()
    return bin

# Appels de vérification :
print(ecriture_binaire_entier_positif(0))
print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))

# Exo 2 :
def tri_bulles(T):
    '''
    Renvoie le tableau T trié par ordre croissant
    '''
    n = len(T)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T

# Appels de vérification :
print(tri_bulles([]))
print(tri_bulles([7]))
print(tri_bulles([9, 3, 7, 2, 3, 1, 6]))
print(tri_bulles([9, 7, 4, 3]))
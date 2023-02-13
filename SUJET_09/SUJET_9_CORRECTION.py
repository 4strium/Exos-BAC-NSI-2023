# SUJET 9

# Exo 1 :
def multiplication(n1, n2):
    res = 0
    if n2 >= 0 :
        for i in range(n2):
            res += n1
        return res
    else :
        for i in range(abs(n2)):    # Valeur absolue
            res += n1
        return -res

# Appels de vérification :
print(multiplication(3,5))
print(multiplication(-4,-8))
print(multiplication(-2,6))
print(multiplication(-2,0))
print(multiplication(-9,-12))

# Exo 2 :
def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m+1, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m-1)
    else:
        return m

# Appels de vérification :
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))
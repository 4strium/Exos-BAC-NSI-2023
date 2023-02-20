# SUJET 17

# Exo 1 :
def moyenne(liste_notes):
    total_points = 0 
    total_coefficients = 0
    for couple in liste_notes:
        total_points += couple[0]*couple[1]
        total_coefficients += couple[1]
    return total_points/total_coefficients

# Appels de vérification :
print(moyenne([(15,2),(9,1),(12,3)]))

# Exo 2 :
def pascal(n):
    triangle = [[1]]
    for k in range(1,n+1):
        ligne_k = [1]
        for i in range(1,k):
            ligne_k.append(triangle[k-1][i-1]+triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle

# Appels de vérification :
print(pascal(4))
print(pascal(5))
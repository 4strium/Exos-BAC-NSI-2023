# SUJET 26

# Exo 1 :
def multiplication(n1,n2):
    res = 0
    for i in range(abs(n2)):
        res += abs(n1)
    if (n1 < 0) ^ (n2 < 0) :
        return -res
    return res

# Appels de vérification :
print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))
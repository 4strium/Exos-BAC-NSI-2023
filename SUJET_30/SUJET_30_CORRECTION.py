# SUJET 30

# Exo 1 :
def moyenne (tab):
    sum = 0
    for element in tab :
        sum += element
    return sum/len(tab)

# Appels de vérification :
print(moyenne([1.0]))
print(moyenne([1.0, 2.0, 4.0]))

# Exo 2 :
def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

# Appels de vérification :
print(binaire(83))
print(binaire(127))
print(binaire(0))
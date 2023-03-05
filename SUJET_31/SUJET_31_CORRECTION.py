# SUJET 31

# Exo 1 :
def nb_repetitions(elt,tab):
    counter = 0
    for element in tab :
        if element == elt :
            counter += 1
    return counter

# Appels de vérification :
print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']))
print(nb_repetitions(12, [1, '!', 7, 21, 36, 44]))

# Exo 2 :
def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0:
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

# Appels de vérification :
print(binaire(0))
print(binaire(77))
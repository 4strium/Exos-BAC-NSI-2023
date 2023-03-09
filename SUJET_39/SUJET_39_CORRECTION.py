# SUJET 39

# Exo 1 :
def fibonacci(n):
    lst = [1, 1]
    for i in range(n-2):
        lst.append(lst[-2]+lst[-1])
    return lst [-1]


# Appels de vérification :
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(25))
print(fibonacci(45))

# Exo 2 :
def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []

    for i in range(len(eleves)) :
        if notes[i] == note_maxi :
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi,meilleurs_eleves)

# Appels de vérification :
eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
print(pantheon(eleves_nsi, notes_nsi))
print(pantheon([],[]))
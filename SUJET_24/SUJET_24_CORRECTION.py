# SUJET 24

# Exo 1 :
def nbr_occurences(chaine):
    characters = list(chaine)
    dict_res = {}
    for element in characters :
        if element not in dict_res :
            dict_res[element] = characters.count(element)
    return dict_res

# Appels de vérification :
print(nbr_occurences("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."))

# Exo 2 :
def fusion(lst1,lst2):
    """
    La fonction fusion prend deux listes lst1, lst2 d’entiers triées par ordre croissant 
    et les fusionne en une liste triée lst12 qu’elle renvoie.
    """
    n1 = len(lst1)
    n2 = len(lst2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        if lst1[i1] < lst2[i2]:
            lst12[i] = lst1[i1]
            i1 = i1 + 1
        else:
            lst12[i] = lst2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        lst12[i] = lst1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        lst12[i] = lst2[i2]
        i2 = i2 + 1
        i = i + 1
    return lst12

# Appels de vérification :
print(fusion([1, 6, 10],[0, 7, 8, 9]))
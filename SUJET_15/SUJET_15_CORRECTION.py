# SUJET 15

# Exo 1 :
def mini(releve, date):
    val_min = releve[0]
    date_min = date[0]
    for i in range(len(releve)) :
        if releve[i] < val_min :
            val_min = releve[i]
            date_min = date[i]
    return (val_min,date_min)

# Appels de vérification :
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
print(mini(t_moy, annees))

# Exo 2 :
def inverse_chaine(chaine):
    result = str()
    for caractere in chaine:
        result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

# Appels de vérification :
print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))
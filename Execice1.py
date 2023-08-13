tableau = []
for i in range(5):
    value = int(input("les valeur du tableau : "))
    tableau.append(value)
    print (tableau)
print("le tableau final est : ",tableau)
inverse = tableau[::-1]
print("l'inverse du tableau est : ", inverse)


def inversTableau(liste):
    return liste[::-1]
tab = [1,45,85,74,48,1,0,]
result_inves = inversTableau(tab)
print('inverse = ',result_inves)
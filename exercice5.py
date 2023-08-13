taille = int(input("quelle est la taille de votre tableau : "))
votre_liste_init = [0]*taille
tableau = []
tableau_impaire = []
print('ma liste initiale est : ', votre_liste_init)
for i in range(taille):
    tableau.append(int(input("Valeur: ")))
    print(tableau)
for j in tableau:
    if j % 2 == 1:
        tableau_impaire.append(j)

print("final egale = ", tableau)
print("Les element impaire de votre liste est :", tableau_impaire)

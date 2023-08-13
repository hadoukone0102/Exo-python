votre_mot = input("Entrer un mot de votre choix: ")
alternance = ""
for i,lettre in enumerate(votre_mot):
    if i%2==0:
        alternance = alternance + lettre.upper()
    else:
        alternance = alternance + lettre.lower()

print("Mot alternant maj/min :", alternance)
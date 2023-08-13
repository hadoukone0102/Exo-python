# Lire le contenu du fichier dans une variable
with open('test.txt', 'r') as file:
    contenu = file.read()

# Remplacer les nouvelles lignes par des espaces
contenu_modifie = contenu.replace('\n', ' ')

# Afficher le contenu modifié
print(contenu_modifie)

def Factoriel(nombre):
    if nombre == 0 :    
        return 1
    else:
        return nombre * Factoriel(nombre -1)

valeur = int(input("Entrer une valeur : "))
if valeur < 0 :
    print("la factorielle d'un nombre ne peut etre inferieur 0")
else:
    facto = Factoriel(valeur)
    print("la factorielle de ", valeur , "est : ", facto)
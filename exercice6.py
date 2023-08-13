def Modification(liste):
    for i in range(len(liste)):
        if isinstance(liste[i], list):
            Modification(liste[i])
        elif liste[i] == 58:
            liste[i] = 5800

list1 = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]
Modification(list1)
print(list1)

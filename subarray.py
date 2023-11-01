def sousTableau(tableau, index1, index2):
    if index1 <= index2:
        return tableau[index1:index2-1]
    else:
        return tableau[index2:index1-1]

# Programme principal
while True:
    tableau = []
    for i in range(10):
        valeur = int(input(f"Entrez la valeur {i + 1} du tableau : "))
        tableau.append(valeur)

    index1 = int(input("Entrez le premier index : "))
    index2 = int(input("Entrez le deuxième index : "))

    resultat = sousTableau(tableau, index1, index2)
    print("Le sous-tableau est :", resultat)

    continuer = input("Voulez-vous saisir un nouveau tableau ? (Oui/Non) ")
    if continuer!= "oui":
        break

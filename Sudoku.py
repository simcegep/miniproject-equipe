

#fonction afficher la grille selon difficulté
def choisir_difficulte():
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    print("Choisissez une difficulté:")

    choix_utilisateur = int(input(""))
    if choix_utilisateur == 1:
        print(grille_facile)
        return grille_facile
    elif choix_utilisateur == 2:
        print(grille_moyen)
        return grille_moyen
    elif choix_utilisateur == 3:
        print(grille_difficile)
        return grille_difficile
    else:
        print("Choix invalide! Niveau facile est par défaut")
        print(grille_facile)
        return grille_facile

# print (choisir_difficulte())

def valide(grille, ligne, colonne, chiffre):
    """

    :param grille:
    :param ligne:
    :param colonne:
    :param chiffre:
    :return:
    """

    # vérifie la ligne
    if chiffre in grille[ligne]:
        return False

    # vérifie la colonne
    for i in range(9):
        if grille[i][colonne] == chiffre:
            return False

    # Vérifie le carré 3x3
    debut_ligne = (ligne // 3) * 3
    debut_colonne = (colonne // 3) * 3
    for i in range(3):
        for j in range(3):
            if grille[debut_ligne + i][debut_colonne + j] == chiffre:
                return False
    return True


def placement_chiffres(grille, ligne, colonne, chiffre):
   """

   :param grille:
   :param ligne:
   :param colonne:
   :param chiffre:
   :return:
   """
   if grille[ligne][colonne] != "_":
       print("La case est déjà remplie.")
       return False
   if valide(grille, ligne, colonne, chiffre):
       grille[ligne][colonne] = chiffre
       print("Le chiffre est placé avec succès! ")
   else:
       print("Le placement est invalide selon les règle du Sudoku. ")
       return False



if __name__ == '__main__':
    grille_facile = [
        [5, 3, "_", "_", 7, "_", "_", "_", "_"],
        [6, "_", "_", 1, 9, 5, "_", "_", "_"],
        ["_", 9, 8, "_", "_", "_", "_", 6, "_"],
        [8, "_", "_", "_", 6, "_", "_", "_", 3],
        [4, "_", "_", 8, "_", 3, "_", "_", 1],
        [7, "_", "_", "_", 2, "_", "_", "_", 6],
        ["_", 6, "_", "_", "_", "_", 2, 8, "_"],
        ["_", "_", "_", 4, 1, 9, "_", "_", 5],
        ["_", "_", "_", "_", 8, "_", "_", 7, 9]
    ]

    grille_facile_solution = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    grille_moyen = [
        [9, "_", "_", "_", 2, "_", "_", 7, "_"],
        ["_", 6, "_", 9, "_", "_", "_", "_", 3],
        ["_", "_", 3, "_", "_", 5, 9, "_", "_"],
        ["_", "_", 5, "_", "_", 9, 1, "_", "_"],
        ["_", 9, "_", 1, "_", 6, "_", 2, "_"],
        ["_", "_", 6, 2, "_", "_", 4, "_", "_"],
        ["_", "_", 9, 6, "_", "_", 3, "_", "_"],
        [8, "_", "_", "_", "_", 7, "_", 5, "_"],
        ["_", 3, "_", "_", 9, "_", "_", "_", 6]
    ]
    grille_moyen_solution = [
        [9, 5, 1, 3, 2, 4, 6, 7, 8],
        [4, 6, 2, 9, 7, 8, 5, 1, 3],
        [7, 8, 3, 1, 6, 5, 9, 4, 2],
        [2, 4, 5, 7, 8, 9, 1, 6, 0],
        [5, 9, 8, 1, 4, 6, 7, 2, 0],
        [3, 7, 6, 2, 5, 1, 4, 9, 0],
        [1, 2, 9, 6, 3, 0, 3, 8, 4],
        [8, 1, 4, 0, 0, 7, 2, 5, 9],
        [6, 3, 7, 8, 9, 2, 0, 0, 6]
    ]

    grille_difficile = [
        ["_", "_", 5, 3, "_", "_", "_", "_", "_"],
        [8, "_", "_", "_", "_", "_", "_", 2, "_"],
        ["_", 7, "_", "_", 1, "_", 5, "_", "_"],

        [4, "_", "_", "_", "_", 5, 3, "_", "_"],
        ["_", 1, "_", "_", 7, "_", "_", "_", 6],
        ["_", "_", 3, 2, "_", "_", "_", 8, "_"],
        ["_", 6, "_", 5, "_", "_", "_", "_", 9],
        ["_", "_", 4, "_", "_", "_", "_", 3, "_"],
        ["_", "_", "_", "_", "_", 9, 7, "_", "_"]
    ]
grille_difficile_solution = [
    [1, 4, 5, 3, 2, 7, 6, 9, 8],
    [8, 3, 9, 6, 5, 4, 1, 2, 7],
    [6, 7, 2, 9, 1, 8, 5, 4, 3],
    [4, 9, 6, 1, 8, 5, 3, 7, 2],
    [2, 1, 8, 4, 7, 3, 9, 5, 6],
    [7, 5, 3, 2, 9, 6, 8, 1, 4],
    [3, 6, 7, 5, 4, 2, 2, 8, 9],
    [9, 8, 4, 7, 6, 1, 2, 3, 5],
    [5, 2, 1, 8, 3, 9, 7, 6, 1]
]


grille = choisir_difficulte()
afficher_grille(grille)


chiffre = int(input("Quelle chiffre vouller vous rajouter ? "))
ligne = int(input("quelle est la rangé(de gauche à droite, 0 à 8) que vous voullez modifier ? "))
colonne = int(input("quelle est la colonne(de en haut à en bas, 0 à 8) que vous voullez modifier ? "))
print(afficher_grille(grille))
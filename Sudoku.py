

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
        [5, 3, "?", "?", 7, "?", "?", "?", "?"],
        [6, "?", "?", 1, 9, 5, "?", "?", "?"],
        ["?", 9, 8, "?", "?", "?", "?", 6, "?"],
        [8, "?", "?", "?", 6, "?", "?", "?", 3],
        [4, "?", "?", 8, "?", 3, "?", "?", 1],
        [7, "?", "?", "?", 2, "?", "?", "?", 6],
        ["?", 6, "?", "?", "?", "?", 2, 8, "?"],
        ["?", "?", "?", 4, 1, 9, "?", "?", 5],
        ["?", "?", "?", "?", 8, "?", "?", 7, 9]
    ]
    grille_moyen = [
        [9, "?", "?", "?", 2, "?", "?", 7, "?"],
        ["?", 6, "?", 9, "?", "?", "?", "?", 3],
        ["?", "?", 3, "?", "?", 5, 9, "?", "?"],
        ["?", "?", 5, "?", "?", 9, 1, "?", "?"],
        ["?", 9, "?", 1, "?", 6, "?", 2, "?"],
        ["?", "?", 6, 2, "?", "?", 4, "?", "?"],
        ["?", "?", 9, 6, "?", "?", 3, "?", "?"],
        [8, "?", "?", "?", "?", 7, "?", 5, "?"],
        ["?", 3, "?", "?", 9, "?", "?", "?", 6]
    ]
    grille_difficile = [
        ["?", "?", 5, 3, "?", "?", "?", "?", "?"],
        [8, "?", "?", "?", "?", "?", "?", 2, "?"],
        ["?", 7, "?", "?", 1, "?", 5, "?", "?"],

        [4, "?", "?", "?", "?", 5, 3, "?", "?"],
        ["?", 1, "?", "?", 7, "?", "?", "?", 6],
        ["?", "?", 3, 2, "?", "?", "?", 8, "?"],
        ["?", 6, "?", 5, "?", "?", "?", "?", 9],
        ["?", "?", 4, "?", "?", "?", "?", 3, "?"],
        ["?", "?", "?", "?", "?", 9, 7, "?", "?"]
    ]
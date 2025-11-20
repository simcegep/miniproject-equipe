####################################
def choisir_difficulte(): # Principalement Simon, petite modification Marc-Antoine
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
####################################
######################################
def valide(grille, ligne, colonne, chiffre): # Marc-Antoine
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
######################################
##########################################
def placement_chiffres(grille, ligne, colonne, chiffre): # Marc-An
   """
    Cette fonction prend la grille et le
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
       return True
   else:
       print("Le placement est invalide selon les règle du Sudoku. ")
       return False
   #######################################
##############################################
def indice_random(grille, grille_solution, nb_indices_utilises):  # simon
    """
indice retourné dans la grille (max 6 fois)
   donne un indice:
   cherche case vide et donne la position (i(ligne)), (j(colonne)))
    """
    Max_indices = 6

    if nb_indices_utilises >= Max_indices:
        print("vous avez utilisé tous vos indices")
        return nb_indices_utilises

    # cases vides
    cases_vides = [(i, j) for i in range(9) for j in range(9) if grille[i][j] == "_"]
    if not cases_vides:
        print("La grille est pleine, aucun indice possible.")
        return nb_indices_utilises

    i, j = random.choice(cases_vides)
    bon_chiffre = grille_solution[i][j]
    grille[i][j] = bon_chiffre
    nb_indices_utilises += 1

    print(f" Indice #{nb_indices_utilises} : La case (ligne {i}, colonne {j}) contient le chiffre {bon_chiffre}.")
    return nb_indices_utilises
####################

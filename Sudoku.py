#fonction afficher la grille selon difficulté
def choisir_difficulte(): # Principalement Simon, petite modification Marc-Antoine
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    print("Choisissez une difficulté: ")

    choix_utilisateur = int(input(""))
    if choix_utilisateur == 1:
        grille = grille_facile
        grille_solution = grille_facile_solution
        #if grille == grille_facile:
            #solution_grille = grille_facile_solution
        return grille, grille_solution

    if choix_utilisateur == 2:
        grille = grille_moyen
        grille_solution = grille_moyen_solution
        #if grille == grille_moyen:
            #solution_grille = grille_moyen_solution
        return grille, grille_solution

    if choix_utilisateur == 3:
        grille = grille_difficile
        grille_solution = grille_difficile_solution
        #if grille == grille_difficile:
            #solution_grille = grille_difficile_solution
        return grille, grille_solution

    else:
        print("Choix invalide! Niveau facile est par défaut")
        #print(grille_facile)
        grille = grille_facile
        if grille == grille_facile:
            solution_grille = grille_facile_solution
        return grille, solution_grille

# print (choisir_difficulte())

def valide(grille, ligne, colonne, chiffre): # Marc-Antoine
    """
    Vérifie si le placement d'un chiffre est valide selon les règles du sudoku
    :param grille:
    :param ligne:
    :param colonne:
    :param chiffre:
    :return:
    """

    # vérifie la ligne si le chiffre est déjà là ce placement est interdie
    for i in grille[ligne]:
        if i == chiffre:
            return False

    # vérifie la colonne si le chiffre est déjà présent si présen le placement est interdie
    for j in range(9):
        if grille[j][colonne] == chiffre:
            return False

    # Vérifie le carré 3x3 si le chiffre est déjà présent si présent le placement est interdie
    debut_ligne = (ligne // 3) * 3
    debut_colonne = (colonne // 3) * 3
    for i in range(3):
        for j in range(3):
            if grille[debut_ligne + i][debut_colonne + j] == chiffre:
                return False
    return True


def placement_chiffres(grille, ligne, colonne, chiffre): # Marc-Antoine
   """
    Cette fonction prend la grille et le chiffre choisit et son emplacement
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
       print("Le placement est invalide selon les règles du Sudoku. ")
       return False

def afficher_grille(grille): # Marc-Antoine
    """

    :param grille:
    :return:
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            val = grille[i][j]
            print(val if val != "_" else "_", end=" ")
        print()

def verifier_erreurs(grille, grille_solution):  # Gabriel

    #Vérifie si certains chiffres dans la grille ne correspondent pas à la solution.
    #Affiche les positions (ligne, colonne) des erreurs trouvées.

    """                      # TODO: donner un nombre maximale d'erreur possible exemple 0/3

    :param grille:
    :param grille_solution:
    :return:
    """

    erreurs = []
    for i in range(9):
        for j in range(9):
            if grille[i][j] != "_" and grille[i][j] != grille_solution[i][j]:
                erreurs.append((i, j))
    if erreurs:
        print("\n Erreurs détectées aux positions :")
        for e in erreurs:
            print(f" - Ligne {e[0]}, Colonne {e[1]}")
    else:
        print("\n Aucune erreur détectée pour l'instant.")


def verifier_doublons(grille):  # Gabriel

    # Vérifie s’il y a des doublons dans une ligne, une colonne ou un carré 3x3.
    #Affiche les positions des doublons trouvés.

    """

    :param grille:
    :return:
    """

    doublons = []

    # Vérifie les lignes
    for i in range(9):
        chiffres = [x for x in grille[i] if x != "_"]
        for val in set(chiffres):
            if chiffres.count(val) > 1:
                doublons.append(f"Ligne {i} (chiffre {val})")

    # Vérifie les colonnes
    for j in range(9):
        colonne = [grille[i][j] for i in range(9) if grille[i][j] != "_"]
        for val in set(colonne):
            if colonne.count(val) > 1:
                doublons.append(f"Colonne {j} (chiffre {val})")

    # Vérifie les carrés 3x3
    for bloc_ligne in range(0, 9, 3):
        for bloc_colonne in range(0, 9, 3):
            carre = []
            for i in range(3):
                for j in range(3):
                    val = grille[bloc_ligne + i][bloc_colonne + j]
                    if val != "_":
                        carre.append(val)
            for val in set(carre):
                if carre.count(val) > 1:
                    doublons.append(f"Carré 3x3 à partir de (Ligne {bloc_ligne}, Colonne {bloc_colonne}) contient deux {val}")

    if doublons:
        print("\n Doublons détectés :")
        for d in doublons:
            print(f" - {d}")
    else:
        print("\n Aucun doublon détecté pour l'instant.")




if __name__ == '__main__':  # Simon
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


    grille, grille_solution = choisir_difficulte()
    afficher_grille(grille)

    while True:
        choix = input("Voulez-vous entrer un chiffre ? (Oui/Non)(tapez 'q' pour quitter): ").lower()


        # Quitter la partie
        if choix == "q":
            print("fin de la partie.")
            if grille == grille_solution:
                print("Bravo! vous avez réussi")
            else:
                print("Vous n'avez pas terminer le Sudoku. Voici la solution.")
                afficher_grille(grille_solution)
                break

        # Demande d'indice
        if choix == "non":
            indice = input("Voulez vous un indice ? (Oui/Non): ").lower()
            if indice == "oui":
                print("L'indice va etre ici juste la fonction na pas encore été créé")
            else:
                print("D'accord, continuez !")
            continue

        elif choix == "oui":
            try:
                chiffre = int(input("Quel chiffre voulez-vous ajouter (1 à 9) ? "))
                ligne = int(input("Quelle ligne (horizontale)(0 à 8) voulez-vous modifier ? "))
                colonne = int(input("Quelle colonne (verticale)(0 à 8) voulez-vous modifier ? "))

                if chiffre < 1 or chiffre > 9:
                    print("Le chiffre doit être entre 1 et 9.")
                    continue

                placement_chiffres(grille, ligne, colonne, chiffre)  # modifier par Gabriel la boucle
                verifier_doublons(grille)
                verifier_erreurs(grille, grille_solution)
                afficher_grille(grille)

                # Vérifie si la grille est complète et correcte
                if grille == grille_solution:
                    print("Bravo! Vous avez réussi!")
                    break


            except ValueError:
                print("Erreur : veuillez entrer un nombre valide.")
            except IndexError:
                print("Erreur : les coordonnées doivent être entre 0 et 8.")
    else:
        print("Réponse invalide. Tapez 'oui', 'non' ou 'q'. ")





    '''while (grille) != solution_grille:
        chiffre = int(input("Quelle chiffre vouler vous rajouter ? "))
        ligne = int(input("quelle est la rangé(de gauche à droite, 0 à 8) que vous voulez modifier ? "))
        colonne = int(input("quelle est la colonne(de en haut à en bas, 0 à 8) que vous voulez modifier ? "))
        placement_chiffres(grille, ligne, colonne, chiffre)
        print(afficher_grille(grille))'''

import random
from dis import RETURN_CONST


# fonction afficher la grille selon difficulté
def choisir_difficulte():  # Principalement Simon, petite modification Marc-Antoine
    print("Bienvenue au jeu sudoku!")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    print("Choisissez une difficulté: ")

    choix_utilisateur = input("")
    if choix_utilisateur == "1":
        grille = grille_facile
        grille_solution = grille_facile_solution
        grille_original = [row[:] for row in grille]
        # Référence: https://docs.python.org/3/library/stdtypes.html#typesseq
        return grille, grille_solution, grille_original

    if choix_utilisateur == "2":
        grille = grille_moyen
        grille_solution = grille_moyen_solution
        grille_original = [row[:] for row in grille]
        return grille, grille_solution, grille_original

    if choix_utilisateur == "3":
        grille = grille_difficile
        grille_solution = grille_difficile_solution
        grille_original = [row[:] for row in grille]
        return grille, grille_solution, grille_original

    else:
        print("Choix invalide! Niveau facile est par défaut")
        # print(grille_facile)
        grille = grille_facile
        grille_solution = grille_facile_solution
        grille_original = [row[:]for row in grille]
        return grille, grille_solution, grille_original


def placement_chiffres(grille, ligne, colonne, chiffre, grille_solution):  # Marc-Antoine
    """
     Cette fonction tente de placer un chiffre dans la grille et vérifie si le placement provoque une erreur.
    :param grille: La actuelle du Sudoku.
    :param ligne: La ligne de la cade où placer le chiffre.
    :param colonne: La colonne de la cade où placer le chiffre.
    :param chiffre: Le chiffre à insérer dans la case.
    :return: si le placement est valide ou pas et si le placement crée une erreur
    """
    # Vérifie si la case est remplie
    if grille[ligne][colonne] != "_":
        print("La case est déjà remplie.")
        return False
    # Place le chiffre temporairement pour verifier
    grille[ligne][colonne] = chiffre

    # Vérifie les erreurs avec les fonctions : verifier_doublons et verifier_erreur
    if verifier_doublons(grille) or verifier_erreurs(grille, grille_solution):
        print(" Le placement provoque une erreur ou un doublon.")
        grille[ligne][colonne] = "_"  # annule le placement
        return False

    print(" Chiffre placé avec succès! ")
    return True

def modifier_case(grille,grille_originale, ligne, colonne, chiffre):
    """
    Cette fonction modifie la case si elle n'est pas verrouillée et si le chiffre est valide.
    :param grille: La grille qui va et qui est modifier par l'utilisateur.
    :param grille_originale: La grille qui ne sera pas modifié.
    :param ligne: L'indice de la ligne de la case à modifier.
    :param colonne: L'indice de la colonne de la case à modifier.
    :param chiffre:Le chiffre à insérer dans la grille.
    :return: Si la modification a été effectuée : True. Si la case est non modifiable ou si le chiffre est invalide: False.
    """


    if grille_originale[ligne][colonne] != "_":
        print("Impossible de modifier un chiffre de la grille de départ. ")
        return False

    if not 1 <= chiffre <= 9:
        print("Le chiffre doit être entre 1 et 9.")
        return False


    grille[ligne][colonne] = chiffre
    print(f"La case ({ligne}, {colonne}) modifiée avec : {chiffre}")
    return True


def afficher_grille(grille):  # Marc-Antoine
    """
    Cette fonction affiche la grille de manière lisible et structurée.
    :param grille: la grille choisi par le joueur.
    """

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Ligne horizontal qui sépare les blocs 3x3

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Linge vertivale qui sépare les blocs 3x3

            val = grille[i][j]
            print(val if val != "_" else "_", end=" ")
        print()


MAX_ERREURS = 3
_erreurs_commises = 0
_erreurs_positions_connues = set()

def _normalise_val(v):
    """Retourne la valeur normalisée pour comparaison (str ou int acceptable dans les grilles)."""
    return str(v) if v != "_" else "_"


def verifier_erreurs(grille, grille_solution):
    # documentation corriger par chatgpt pour eviter les fautes de francais 
    """
        Vérifie les erreurs présentes dans la grille actuelle par rapport à la grille solution.

        Cette fonction compare chaque case remplie de la grille du joueur avec la valeur
        correspondante dans la grille solution. Elle détecte toutes les positions où les       
        valeurs ne correspondent pas (en ignorant les cases encore vides, notées "_").
        Les nouvelles erreurs qui n’avaient jamais été repérées auparavant sont comptabilisées,
        tandis que les erreurs déjà connues ne sont pas recompteurs.

        :param grille:
            La grille remplie par le joueur, sous forme de liste de listes. Chaque cellule
            contient soit une valeur, soit "_" pour indiquer une case vide.

        :param grille_solution:
            La grille correcte à atteindre, sous forme de liste de listes, contenant toutes
            les valeurs finales attendues pour chaque case.

        :return:
            Retourne False s’aucune erreur n’a été trouvée au moment de l’appel.
            Retourne True si au moins une erreur est détectée dans la grille.
        """

    global _erreurs_commises, _erreurs_positions_connues

    erreurs_courantes = set()
    n = len(grille)

    # Parcours de la grille et détection des erreurs
    for i in range(n):
        for j in range(len(grille[i])):
            val = _normalise_val(grille[i][j])
            sol = _normalise_val(grille_solution[i][j])

            if val != "_" and val != sol:
                erreurs_courantes.add((i, j))

    # Aucune erreur = message + retour False
    if not erreurs_courantes:
        print("\nAucune erreur détectée pour l'instant.")
        return False

    # Calcul des nouvelles erreurs (pas déjà connues)
    nouvelles = erreurs_courantes - _erreurs_positions_connues

    # Mise à jour des compteurs
    if nouvelles:
        _erreurs_commises += len(nouvelles)
        _erreurs_positions_connues |= nouvelles

    # Affichage des erreurs actuelles
    print("\nErreurs détectées aux positions :")
    for e in sorted(erreurs_courantes):
        print(f" - Ligne {e[0]}, Colonne {e[1]}")

    # Affichage du nombre d'erreurs commises (pas de défaite)
    print(f"\nNombre d'erreurs commises : {_erreurs_commises}")

    return True




def verifier_doublons(grille):
    # documentation corriger par chatgpt pour eviter les fautes de francais 
    """
       Vérifie s’il existe des doublons dans la grille actuelle.

       La fonction inspecte successivement les lignes, les colonnes et les blocs 3x3
       afin de repérer toute valeur apparaissant plus d’une fois dans une même zone,
       en ignorant les cases vides ("_"). Dès qu’un doublon est détecté, un message
       explicite est affiché pour indiquer où il se trouve, puis la fonction stoppe
       immédiatement la recherche.

       :param grille:
           La grille du joueur, donnée sous forme de liste de listes, contenant des
           valeurs remplies ou "_" pour les cases encore vides.

       :return:
           Retourne True dès qu’un doublon est trouvé dans une ligne, une colonne ou
           un bloc 3x3.
           Retourne False si aucune duplication n’est détectée dans l’ensemble de la grille.
       """

    n = len(grille)

     # Vérification des lignes
    for i in range(n):
        vus = {}
        for j in range(len(grille[i])):
            val = _normalise_val(grille[i][j])  # aide de chatgpt pour cette partie du program pour permettre un bon fonctionnement
            if val == "_":
                continue
            if val in vus:
                print(f"Doublon dans la ligne {i} : {val} (colonnes {vus[val]} et {j})")
                return True
            vus[val] = j

    #  Vérification des colonnes
    for j in range(len(grille[0])):
        vus = {}
        for i in range(n):
            val = _normalise_val(grille[i][j])
            if val == "_":
                continue
            if val in vus:
                print(f"Doublon dans la colonne {j} : {val} (lignes {vus[val]} et {i})")
                return True
            vus[val] = i

    #  Vérification des blocs 3x3
    bloc = 3  # taille d’un bloc au Sudoku

    for bi in range(0, n, bloc):
        for bj in range(0, n, bloc):
            vus = {}
            for i in range(bi, bi + bloc):
                for j in range(bj, bj + bloc):
                    val = _normalise_val(grille[i][j])
                    if val == "_":
                        continue
                    if val in vus:
                        pi, pj = vus[val]
                        print(f"Doublon dans le bloc ({bi},{bj}) : {val} (positions ({pi},{pj}) et ({i},{j}))")
                        return True
                    vus[val] = (i, j)

    return False


def indice_random   (grille, grille_solution, nb_indices_utilises): #simon
        """
    indice retourné dans la grille (max 6 fois)
        :param grille:
        :param grille_solution:
        :param nb_indices_utilises:
        :return: grille avec indices
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

        cases_possibles = []
        for i, j in cases_vides:
            val = grille_solution[i][j]

            # Vérifie la ligne
            if any(grille[i][x] == val for x in range(9)):
                continue
            # Vérifie la colonne
            if any(grille[y][j] == val for y in range(9)):
                continue
            # Vérifie le bloc 3x3
            bi, bj = 3 * (i // 3), 3 * (j // 3)
            if any(grille[x][y] == val for x in range(bi, bi + 3) for y in range(bj, bj + 3)):
                continue

            cases_possibles.append((i, j))

        i, j = random.choice(cases_vides)
        bon_chiffre = grille_solution[i][j]
        grille[i][j] = bon_chiffre
        nb_indices_utilises += 1

        print(f" Indice #{nb_indices_utilises} : La case (ligne {i}, colonne {j}) contient le chiffre {bon_chiffre}.")
        return nb_indices_utilises


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
        ["_", "_", "_", 2, "_", "_", "_", "_", "_"],
        ["_", 8, "_", "_", 7, "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", 4, "_", "_", "_"],
        [8, "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", 6, "_", 2, "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", 2, 8],
        ["_", "_", 9, "_", "_", "_", "_", "_", "_"],
        ["_", 4, "_", "_", 5, "_", "_", "_", "_"],
        ["_", "_", "_", "_", 1, 8, "_", "_", "_"]

    ]
    grille_moyen_solution = [
        [4, 3, 5, 2, 6, 9, 7, 8, 1],
        [6, 8, 2, 5, 7, 1, 4, 9, 3],
        [1, 9, 7, 8, 3, 4, 5, 6, 2],
        [8, 2, 6, 1, 9, 5, 3, 4, 7],
        [3, 7, 4, 6, 8, 2, 9, 1, 5],
        [9, 5, 1, 7, 4, 3, 6, 2, 8],
        [5, 1, 9, 3, 2, 6, 8, 7, 4],
        [2, 4, 8, 9, 5, 7, 1, 3, 6],
        [7, 6, 3, 4, 1, 8, 2, 5, 9]

    ]

    grille_difficile = [
        [8, "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", 3, 6, "_", "_", "_", "_", "_"],
        ["_", 7, "_", "_", 9, "_", 2, "_", "_"],
        ["_", 5, "_", "_", "_", 7, "_", "_", "_"],
        ["_", "_", "_", "_", 4, 5, 7, "_", "_"],
        ["_", "_", "_", 1, "_", "_", "_", 3, "_"],
        ["_", "_", 1, "_", "_", "_", "_", 6, 8],
        ["_", "_", 8, 5, "_", "_", "_", 1, "_"],
        ["_", 9, "_", "_", "_", "_", 4, "_", "_"]
    ]

    grille_difficile_solution = [
        [8, 1, 2, 7, 5, 3, 6, 4, 9],
        [9, 4, 3, 6, 8, 2, 1, 7, 5],
        [6, 7, 5, 4, 9, 1, 2, 8, 3],
        [1, 5, 4, 2, 3, 7, 8, 9, 6],
        [3, 6, 9, 8, 4, 5, 7, 2, 1],
        [2, 8, 7, 1, 6, 9, 5, 3, 4],
        [5, 2, 1, 9, 7, 4, 3, 6, 8],
        [4, 3, 8, 5, 2, 6, 9, 1, 7],
        [7, 9, 6, 3, 1, 8, 4, 5, 2]
    ]

    grille, grille_solution, grille_originale = choisir_difficulte()
    afficher_grille(grille)
    nb_indices_utilises = 0

    while True:
        choix = input("Voulez-vous entrer un chiffre ? (Oui/Non/Change)(tapez 'Fin' pour quitter): ").lower()

        # Quitter la partie
        if choix == "fin":
            print("fin de la partie.")
            if grille == grille_solution:
                print("Bravo! Vous avez réussi")
            else:
                print("Voici la solution.")
                afficher_grille(grille_solution)
            break

        # Demande d'indice
        elif choix == "non":
            action = input("Voulez vous un indice ? (Oui/Non): ").lower()
            if action == "oui":
                nb_indices_utilises = indice_random(grille, grille_solution, nb_indices_utilises)
                afficher_grille(grille)
            else:
                print("Vous pouvez continuée.")
            continue

        elif choix == "Change":
            nouveau = int(input("Le nouveau chiffre ?"))
            ligne = int(input("Quelle ligne (horizontale)(0 à 8) voulez-vous modifier ? "))
            colonne = int(input("Quelle colonne (verticale)(0 à 8) voulez-vous modifier ? "))
            modifier_case(grille, grille_originale, ligne, colonne, nouveau)
            continue

        elif choix == "oui":
            try:
                chiffre = int(input("Quel chiffre voulez-vous ajouter (1 à 9) ? "))
                ligne = int(input("Quelle ligne (horizontale)(0 à 8) voulez-vous modifier ? "))
                colonne = int(input("Quelle colonne (verticale)(0 à 8) voulez-vous modifier ? "))

                if chiffre < 1 or chiffre > 9:
                    print("Le chiffre doit être entre 1 et 9.")
                    continue


                # Vérifie si la grille est complète et correcte
                if grille == grille_solution:
                    print("Bravo! Vous avez réussi!")
                    break

                if 1 <= chiffre <= 9:
                    if 0 <= ligne <= 8 and 0 <= colonne <= 8:
                        placement_chiffres(grille, ligne, colonne, chiffre, grille_solution)
                        afficher_grille(grille)
                        if grille == grille_solution:  # Vérifie si la grille est complète et correct
                            print("Bravo! Vous avez réussi!")
                            break
                    else:
                        print("Erreur : les coordonnées doivent entre 0 et 8. ")
                else:
                    print(" Le chiffre doit être entre 1 et 9. ")
            except ValueError:
                print("Erreur : veuillez entrer un nombre valide.")

            except IndexError:
                print("Erreur : les coordonnées doivent être entre 0 et 8.")

        else:
            print("Réponse invalide. Tapez 'oui', 'non' ou 'fin'. ")













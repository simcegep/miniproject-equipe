#pseudocode
# message ( Bienvenue au jeu de Sudoku)
# choix de diff, facile, moyen, dure
# créer grille
# faire un grille corrigée/complète pour chaque niveau de diff
# Fonctions
# afficher grille, choix difficulté, validation du chiffre( collone, ligne, chiffre),
# choix (boucle): rentrer une ligne, rentrer une collone, rentrer un chiffre, rentrer enter pour indiqué une erreur
#fonction remplacer un chiffre dans grille selon ligne/collone
    # afficher erreurs si valuer pas 1 à 9

# faire print la ligne/collone à changer si erreur
# faire print la case n'est pas vide if il entre une valeur dans une case préfait
# faire print

#changement de chiffre en cas d'erreur :
# faire liste de case qui son in touchable / faire une copie de la crille d'origine
# comparéré liste ou dictionnaire avec la grille qui a été modifier pour valider si la case peut etre modifier



# Pseudocode Marc-Antoine

# Fonction placement_chiffre
# placement_chiffres(grille, ligne, colonne, chiffre, grille_solution)

    # Si la case dans grille[ligne][colonne] n'est pas "_" alors
        # Afficher "La case est est déjà remplie."
        # Retourner Faux

    # Grille[ligne][colonne] = chiffre

    # Si verifier_doublons(grille) ou verifier_erreurs(grille, grille_solution)
        # Afficher " Le placement provoque une erreur ou un doublon"
        # Grille[ligne][colonne] = "_"
        # Retourner Faux

    # Afficher "Chiffre placéè avec succès !"
    # Retourner Vrai


# Pseudocode Marc-Antoine
# Fonction modifier_case
    # Modifier_case(grille,grille_originale, ligne, colonne, chiffre)

    # Si la case dans la grille  originale n'est pas "_"alors
        # Afficher "Impossible de modifier un chiffre de la grille de départ."
        # Retourner faux

    # Si chiffre n'est pas entre 1 et 9 alors
        # Afficher "Le chiffre doit être entre 1 et 9"
        # Retourner Faux
#
    # Grille[ligne][colonne] = chiffre
    # Afficher "La case (ligne, colonne) modifiée avec : chiffre"
    # Retourner Vrai


# Pseudocode Marc-Antoine

# Fonction afficher_grille(grille)

    # Pour chaque ligne i de 0 à 8

        # Si i est un multiple de 3 et i n'est pas = 0 alors
            # Afficher une ligne de 21 tirets

        # Pour chaque colonne j de 0 à 8

            # Si j est un multiple de 3 et j n'est pas = 0 alors
                # Afficher "|" sans retour à la ligne

            # Valeur = grille[i][j]

            # Si valeur est "_" alors
                # Afficher "_" sans retour à la ligne
            # Sinon
                # Afficher la valeur sans retour à la ligne


# Pseudocode Marc-Antoine

# Boucle du code principale

# Tant que vrai
    # Demander au joueur : "Voulez-vous entrer un chiffre ? (Oui/Non/Change)(tapez 'Fin' pour quitter): "
    # Mettre la réponse en minuscule

    # Si réponse == "fin" alors
        # Afficher "fin de la partie"
        # Si grille == grille_solution alors
            # Afficher "voici la solution"
        # Sinon
            # Afficher "voici la solution"
            # Afficher grille_solution
        # Quitter la boucle

    # Si réponse == "non" alors
        # Demander " Voulez-vous un indice ? (oui/non)
        # Si le joueur répond "oui"
            # Appeler indice_random pour ajouter un indice
            # Afficher la grille
        # Sinon
            # Afficher "vous pouvez continuer."
        # Continuer au début de la boucle

    # Si réponse == "change" alors
        # Demander la nouveau chiffre
        # Demander la ligne
        # Demander la colonne
        # Appeler modifier_case(grille, grille_originale, ligne, colonne, nouveau)
        # Continuer

    # Si réponse == "oui" alors
        # Tenter :
            # Demander le chiffre
            # Demander la ligne
            # Demander la colonne

            # Si chiffre pas entre 1 et 9 alors
                # Afficher erreur
                # Continuer

            # Si grille == grille_solution alors
                # Afficher succès
                # Quitter

            # Si ligne et colonne entre 0 et 8 alors
                # Appeler placement_chiffres(grille, ligne, colonne, chiffre, grille_solution)
                # Afficher la grille

                # Si grille == grille_solution
                    # Afficher succès
                    # Quitter

            # Sinon
                 # Afficher "coordonnées invalides"

        # Si une erreur ValueError est levée
            # Afficher "Erreur : veuillez entrer un nombre valide."
        # Si une erreur IndexError est levée
            # Afficher "Erreur : les coordonnées doivent être entre 0 et 8."

    # Sinon
        # Afficher "réponse invalide"


#PSEUDO-CODE GABRIEL

# verifier_erreurs(grille, grille_solution)

    # - Parcourir toute la grille (toutes les lignes i et colonnes j)
# - Si la case n'est pas "_" et la valeur != valeur dans grille_solution :
#     - ajouter la position (i,j) au set erreurs_courantes
# - Si erreurs_courantes est vide :
#     - afficher "Aucune erreur détectée pour l'instant."
#     - retourner False
# - Calculer nouvelles = erreurs_courantes - erreurs_positions_connues (global)
# - Si nouvelles non vide :
#     - erreurs_commises += len(nouvelles)  # incrémenter le compteur global
#     - mettre à jour erreurs_positions_connues en y ajoutant nouvelles
# - Afficher toutes les erreurs courantes (liste de positions)
# - Calculer restant = MAX_ERREURS - erreurs_commises
# - Si erreurs_commises >= MAX_ERREURS :
#     - afficher message défaite "Vous avez perdu la partie."
#     - retourner True
# - Sinon :
#     - afficher le nombre d'erreurs commises et les chances restantes
#     - retourner True    # (il y a des erreurs)

#PSEUDO-CODE GABRIEL

    # verifier_doublons(grille)
# - Pour chaque ligne i :
#     - créer dict seen vide (val -> colonne)
#     - pour chaque colonne j :
#         - if case == "_" continue
#         - if val dans seen :
#             - afficher "Doublon détecté : Ligne i contient deux fois val (colonnes seen[val] et j)."
#             - return True   # on s'arrête tout de suite
#         - else seen[val] = j
# - Pour chaque colonne j :
#     - même procédé (seen stocke ligne précédente)
#     - si doublon trouvé : afficher et return True
# - Calculer taille bloc blk = racine entière de n, si pas carré parfait alors blk = 3
# - Pour chaque bloc 3x3 (bloc_ligne, bloc_colonne) :
#     - seen = {}
#     - pour chaque case du bloc :
#         - if "_": continue
#         - if val dans seen: afficher position et return True
#         - else seen[val] = (i,j)
# - Si rien trouvé :
#     - afficher "Aucun doublon détecté pour l'instant."
#     - return False






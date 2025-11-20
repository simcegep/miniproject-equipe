#pseudocode Simon
# message ( Bienvenue au jeu de Sudoku)
# choix de diff, facile, moyen, dure
# créer grille
# faire un grille corrigée/complète pour chaque niveau de diff
# Fonctions
# afficher grille, choix difficulté, validation du chiffre( collone, ligne, chiffre),
# choix (boucle): rentrer une ligne, rentrer une collone, rentrer un chiffre, rentrer enter pour indiqué une erreur
#fonction remplacer un chiffre dans grille selon ligne/collone
    # afficher erreurs si valeur pas 1 à 9

# faire print la case n'est pas vide if il entre une valeur dans une case préfait


#changement de chiffre en cas d'erreur :
# faire liste de case qui son in touchable / faire une copie de la crille d'origine
# comparéré liste ou dictionnaire avec la grille qui a été modifier pour valider si la case peut etre modifier

# pseudo indices
# SI nb_indices_utilises >= 6 ALORS retourner nb_indices_utilises
#cases_vides <- toutes les cases (i,j) où grille[i][j] = "_"
#(i, j) <- choisir une case au hasard dans cases_vides
#grille[i][j] <- grille_solution[i][j]
#retourner nb_indices_utilises + 1


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

# verifier_erreurs(grille, grille_solution):

    # Parcourir chaque case de la grille (pour chaque ligne i, chaque colonne j) :
        # Si la case n'est pas "_" et que la valeur ne correspond pas à celle de la solution :
            # enregistrer la position (i, j) dans un ensemble erreurs_courantes.

    # Si erreurs_courantes est vide :
        # afficher "Aucune erreur détectée pour l’instant."
        # retourner False

    # Déterminer quelles erreurs viennent juste d'être commises :
       # nouvelles = erreurs_courantes - erreurs_positions_connues

    # Si de nouvelles erreurs apparaissent :
        # incrémenter erreurs_commises du nombre de nouvelles erreurs
        # ajouter ces positions dans erreurs_positions_connues

    # Afficher la liste actuelle de toutes les erreurs repérées.

    # Calculer le nombre d’essais restants :
        restant = MAX_ERREURS - erreurs_commises

    # Si le joueur a atteint ou dépassé la limite d’erreurs :
        # afficher "Vous avez perdu la partie."
        # retourner True

    # Sinon :
        # afficher combien d’erreurs ont été commises et combien il reste de tentatives
        # retourner True   (puisqu’il y a des erreurs dans la grille)


# PSEUDO-CODE GABRIEL #2

#verifier_doublons(grille):

    # Vérifier chaque ligne :
        # créer un dictionnaire vide "seen" pour suivre les valeurs déjà rencontrées
        # pour chaque case :
             # ignorer si la case contient "_"
            # si la valeur est déjà dans "seen" :
                # afficher "Doublon détecté : la ligne i contient deux fois la valeur val."
                # retourner True
            # sinon l’ajouter à seen

    # Vérifier chaque colonne :
        # même logique que pour les lignes, mais seen garde les numéros de ligne

    # Déterminer la taille standard d’un bloc :
        # blk = racine carrée entière de la taille de la grille
        # si ce n’est pas un carré parfait, utiliser blk = 3 par défaut

    # Vérifier chaque bloc (3×3 généralement) :
        # réinitialiser seen
        # parcourir toutes les cases du bloc :
            # ignorer les "_"
            # si la valeur apparaît déjà dans seen :
                # afficher la position du conflit
                # retourner True
            # sinon, enregistrer la position

    # Si aucun doublon n’a été trouvé :
        # afficher "Aucun doublon détecté pour l’instant."
        # retourner False





